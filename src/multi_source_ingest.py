#!/usr/bin/env python

from __future__ import annotations

import json
import os
import re
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Iterable, List

import requests

try:
    from subscription_plan import build_pipeline_inputs
except ModuleNotFoundError:  # pragma: no cover
    from src.subscription_plan import build_pipeline_inputs


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CONFIG_FILE = os.path.join(ROOT_DIR, "config.yaml")

DEFAULT_SOURCE_SETTINGS = {
    "query_limit": 12,
    "per_query_limit": 40,
    "biorxiv_days": 2,
    "medrxiv_days": 2,
    "enabled_sources": ["arxiv", "europe_pmc", "pubmed", "biorxiv", "medrxiv"],
}

DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:a-z0-9]+", re.IGNORECASE)
RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}


def log(message: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {message}", flush=True)


def get_with_retry(
    session: requests.Session,
    url: str,
    *,
    params: Dict[str, Any] | None = None,
    timeout: int = 45,
    label: str = "http",
    max_attempts: int = 4,
) -> requests.Response:
    last_error: Exception | None = None
    for attempt in range(1, max_attempts + 1):
        try:
            resp = session.get(url, params=params, timeout=timeout)
            if resp.status_code in RETRYABLE_STATUS_CODES:
                raise requests.HTTPError(
                    f"{resp.status_code} {resp.reason}",
                    response=resp,
                )
            resp.raise_for_status()
            return resp
        except requests.RequestException as exc:
            last_error = exc
            status_code = getattr(getattr(exc, "response", None), "status_code", None)
            if attempt >= max_attempts or (status_code is not None and status_code not in RETRYABLE_STATUS_CODES):
                break
            sleep_seconds = min(2 ** (attempt - 1), 8)
            log(f"[WARN] {label} retry {attempt}/{max_attempts} after status={status_code or 'network'} sleep={sleep_seconds}s")
            time.sleep(sleep_seconds)
    assert last_error is not None
    raise last_error


def load_config() -> Dict[str, Any]:
    if not os.path.exists(CONFIG_FILE):
        return {}
    try:
        import yaml  # type: ignore
    except Exception:
        return {}
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def get_source_settings(config: Dict[str, Any]) -> Dict[str, Any]:
    raw = (config or {}).get("paper_sources") or {}
    if not isinstance(raw, dict):
        raw = {}
    settings = dict(DEFAULT_SOURCE_SETTINGS)
    settings.update({k: v for k, v in raw.items() if v is not None})
    enabled = settings.get("enabled_sources")
    if not isinstance(enabled, list) or not enabled:
        settings["enabled_sources"] = list(DEFAULT_SOURCE_SETTINGS["enabled_sources"])
    return settings


def ensure_list(value: Any) -> List[str]:
    if isinstance(value, list):
        return [str(v).strip() for v in value if str(v).strip()]
    if value is None:
        return []
    text = str(value).strip()
    return [text] if text else []


def normalize_title_key(title: str) -> str:
    text = str(title or "").strip().lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff ]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def normalize_doi(value: Any) -> str:
    text = str(value or "").strip().lower()
    if not text:
        return ""
    m = DOI_RE.search(text)
    return m.group(0).lower() if m else ""


def paper_year(value: Any) -> str:
    text = str(value or "").strip()
    m = re.search(r"\b(19|20)\d{2}\b", text)
    return m.group(0) if m else ""


def normalize_authors(raw: Any) -> List[str]:
    if not isinstance(raw, list):
        return []
    out: List[str] = []
    seen: set[str] = set()
    for item in raw:
        text = str(item or "").strip()
        if not text:
            continue
        key = text.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(text)
    return out


def choose_primary_link(paper: Dict[str, Any]) -> str:
    for key in ("pdf_url", "link", "doi_url", "pubmed_url", "url"):
        value = str(paper.get(key) or "").strip()
        if value:
            return value
    return ""


def canonical_key(paper: Dict[str, Any]) -> str:
    doi = normalize_doi(paper.get("doi"))
    if doi:
        return f"doi:{doi}"
    arxiv_id = str((paper.get("external_ids") or {}).get("arxiv") or paper.get("id") or "").strip().lower()
    if arxiv_id and paper.get("source") == "arxiv":
        return f"arxiv:{arxiv_id}"
    title_key = normalize_title_key(paper.get("title") or "")
    year = paper_year(paper.get("published") or "")
    if title_key:
        return f"title:{title_key}|{year}"
    return f"fallback:{paper.get('source')}:{paper.get('id')}"


def merge_text_fields(old: str, new: str) -> str:
    old_text = str(old or "").strip()
    new_text = str(new or "").strip()
    if len(new_text) > len(old_text):
        return new_text
    return old_text


def merge_paper_records(records: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    merged: Dict[str, Dict[str, Any]] = {}
    priority = {"arxiv": 5, "pubmed": 4, "europe_pmc": 3, "biorxiv": 2, "medrxiv": 1}

    for paper in records:
        if not isinstance(paper, dict):
            continue
        title = str(paper.get("title") or "").strip()
        if not title:
            continue
        key = canonical_key(paper)
        source = str(paper.get("source") or "").strip() or "unknown"
        source_id = str(paper.get("id") or "").strip()
        item = merged.get(key)
        if item is None:
            copied = dict(paper)
            copied["authors"] = normalize_authors(copied.get("authors"))
            copied["sources"] = [source]
            copied["source_ids"] = {source: source_id} if source_id else {}
            copied["external_ids"] = dict(copied.get("external_ids") or {})
            copied["canonical_key"] = key
            copied["link"] = choose_primary_link(copied)
            merged[key] = copied
            continue

        old_source = str(item.get("source") or "").strip()
        if priority.get(source, 0) > priority.get(old_source, 0):
            item["source"] = source
            if source_id:
                item["id"] = source_id

        item["title"] = merge_text_fields(item.get("title"), paper.get("title"))
        item["abstract"] = merge_text_fields(item.get("abstract"), paper.get("abstract"))
        item["published"] = merge_text_fields(item.get("published"), paper.get("published"))
        item["updated_at"] = merge_text_fields(item.get("updated_at"), paper.get("updated_at"))
        item["primary_category"] = merge_text_fields(item.get("primary_category"), paper.get("primary_category"))

        categories = ensure_list(item.get("categories")) + ensure_list(paper.get("categories"))
        item["categories"] = sorted({c for c in categories if c})

        authors = normalize_authors(item.get("authors")) + normalize_authors(paper.get("authors"))
        item["authors"] = normalize_authors(authors)

        doi = normalize_doi(item.get("doi")) or normalize_doi(paper.get("doi"))
        if doi:
            item["doi"] = doi

        ext = dict(item.get("external_ids") or {})
        ext.update({k: v for k, v in dict(paper.get("external_ids") or {}).items() if v})
        item["external_ids"] = ext

        srcs = ensure_list(item.get("sources")) + [source]
        item["sources"] = sorted({s for s in srcs if s})
        src_ids = dict(item.get("source_ids") or {})
        if source_id:
            src_ids[source] = source_id
        item["source_ids"] = src_ids

        if not str(item.get("link") or "").strip():
            item["link"] = choose_primary_link(paper)
        elif "arxiv.org" not in str(item.get("link") or "") and "arxiv.org" in choose_primary_link(paper):
            item["link"] = choose_primary_link(paper)

    output = list(merged.values())
    output.sort(key=lambda x: str(x.get("published") or ""), reverse=True)
    return output


def _dedupe_phrases(values: Iterable[str], limit: int) -> List[str]:
    seen: set[str] = set()
    out: List[str] = []
    for value in values:
        text = str(value or "").strip()
        if not text:
            continue
        key = text.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(text)
        if len(out) >= limit:
            break
    return out


def build_source_queries(config: Dict[str, Any], limit: int) -> List[str]:
    plan = build_pipeline_inputs(config or {})
    phrases: List[str] = []
    for item in plan.get("context_keywords") or []:
        text = str(item.get("keyword") or "").strip()
        if text:
            phrases.append(text)
    for item in plan.get("context_queries") or []:
        text = str(item.get("query") or "").strip()
        if text and len(text.split()) <= 8:
            phrases.append(text)
    return _dedupe_phrases(phrases, limit)


def paper_matches_queries(paper: Dict[str, Any], queries: List[str]) -> bool:
    blob = " ".join(
        [
            str(paper.get("title") or ""),
            str(paper.get("abstract") or ""),
            " ".join(ensure_list(paper.get("categories"))),
        ]
    ).lower()
    if not blob.strip():
        return False
    for query in queries:
        normalized_query = re.sub(r"\s+", " ", str(query or "").strip().lower())
        if normalized_query and normalized_query in blob:
            return True
        terms = [t for t in re.split(r"\W+", normalized_query) if len(t) >= 4]
        if not terms:
            continue
        hits = sum(1 for t in terms if t in blob)
        required_hits = 2 if len(terms) >= 2 else 1
        if hits >= required_hits:
            return True
    return False


def get_ncbi_api_settings() -> Dict[str, str]:
    api_key = str(os.getenv("NCBI_API_KEY") or os.getenv("PUBMED_API_KEY") or "").strip()
    email = str(os.getenv("NCBI_EMAIL") or os.getenv("PUBMED_EMAIL") or "").strip()
    tool = str(os.getenv("NCBI_TOOL") or "daily-paper-reader").strip()
    out: Dict[str, str] = {}
    if api_key:
        out["api_key"] = api_key
    if email:
        out["email"] = email
    if tool:
        out["tool"] = tool
    return out


def request_pubmed_with_fallback(
    session: requests.Session,
    url: str,
    *,
    params: Dict[str, Any],
    timeout: int,
    label: str,
) -> requests.Response:
    variants: List[Dict[str, Any]] = [dict(params)]
    if "email" in params or "tool" in params:
        trimmed = dict(params)
        trimmed.pop("email", None)
        trimmed.pop("tool", None)
        variants.append(trimmed)
    if "api_key" in params:
        anonymous = dict(variants[-1])
        anonymous.pop("api_key", None)
        variants.append(anonymous)

    last_error: Exception | None = None
    for idx, variant in enumerate(variants, start=1):
        try:
            if idx > 1:
                removed = sorted(set(params.keys()) - set(variant.keys()))
                log(f"[WARN] {label} fallback {idx}/{len(variants)} remove={','.join(removed) or 'none'}")
            return get_with_retry(
                session,
                url,
                params=variant,
                timeout=timeout,
                label=label,
            )
        except requests.HTTPError as exc:
            last_error = exc
            status_code = getattr(getattr(exc, "response", None), "status_code", None)
            if status_code != 400 or idx >= len(variants):
                break
            continue
        except requests.RequestException as exc:
            last_error = exc
            break
    assert last_error is not None
    raise last_error


def _to_iso_day(value: Any) -> str:
    text = str(value or "").strip()
    if not text:
        return ""
    m = re.match(r"^(\d{4})[-/](\d{2})[-/](\d{2})", text)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    return text[:10]


def _parse_dt(value: Any) -> datetime | None:
    text = str(value or "").strip()
    if not text:
        return None
    for candidate in (text, text.replace("Z", "+00:00")):
        try:
            dt = datetime.fromisoformat(candidate)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(timezone.utc)
        except Exception:
            pass
    try:
        return datetime.strptime(text[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)
    except Exception:
        return None


def extract_europe_pmc_link(item: Dict[str, Any], pmid: str) -> str:
    if pmid:
        return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
    full_text = item.get("fullTextUrlList") or {}
    if isinstance(full_text, dict):
        entries = full_text.get("fullTextUrl") or []
        if isinstance(entries, list):
            for entry in entries:
                if not isinstance(entry, dict):
                    continue
                url = str(entry.get("url") or "").strip()
                if url:
                    return url
    direct = str(item.get("fullTextUrl") or "").strip()
    if direct:
        return direct
    doi = normalize_doi(item.get("doi"))
    if doi:
        return f"https://doi.org/{doi}"
    return ""


def fetch_europe_pmc_papers(queries: List[str], per_query_limit: int = 40, days: int = 2) -> List[Dict[str, Any]]:
    results: List[Dict[str, Any]] = []
    session = requests.Session()
    threshold = datetime.now(timezone.utc) - timedelta(days=max(days, 1) + 1)

    for phrase in queries:
        page = 1
        fetched = 0
        while fetched < per_query_limit:
            page_size = min(25, per_query_limit - fetched)
            params = {
                "query": phrase,
                "format": "json",
                "resultType": "core",
                "pageSize": page_size,
                "page": page,
            }
            resp = get_with_retry(
                session,
                "https://www.ebi.ac.uk/europepmc/webservices/rest/search",
                params=params,
                timeout=45,
                label="EuropePMC search",
            )
            payload = resp.json() or {}
            items = (((payload.get("resultList") or {}).get("result")) or [])
            if not items:
                break
            for item in items:
                published = _to_iso_day(item.get("firstPublicationDate") or item.get("pubYear"))
                dt = _parse_dt(published)
                if dt and dt < threshold:
                    continue
                doi = normalize_doi(item.get("doi"))
                pmid = str(item.get("pmid") or "").strip()
                link = extract_europe_pmc_link(item, pmid)
                results.append(
                    {
                        "id": pmid or doi or str(item.get("id") or ""),
                        "source": "europe_pmc",
                        "title": str(item.get("title") or "").strip(),
                        "abstract": str(item.get("abstractText") or "").strip(),
                        "authors": [str(item.get("authorString") or "").strip()] if str(item.get("authorString") or "").strip() else [],
                        "primary_category": str(item.get("journalTitle") or "").strip(),
                        "categories": [str(item.get("pubType") or "").strip()] if str(item.get("pubType") or "").strip() else [],
                        "published": published,
                        "updated_at": _to_iso_day(item.get("firstIndexDate") or published),
                        "link": link,
                        "doi": doi,
                        "external_ids": {"pmid": pmid, "pmcid": str(item.get("pmcid") or "").strip()},
                    }
                )
            fetched += len(items)
            page += 1
            if len(items) < page_size:
                break
    return results


def fetch_pubmed_papers(queries: List[str], per_query_limit: int = 40, days: int = 2) -> List[Dict[str, Any]]:
    session = requests.Session()
    results: List[Dict[str, Any]] = []
    id_seen: set[str] = set()
    ncbi_params = get_ncbi_api_settings()

    for phrase in queries:
        params = {
            "db": "pubmed",
            "term": phrase,
            "retmode": "json",
            "retmax": min(per_query_limit, 100),
            "reldate": max(days, 1),
            "datetype": "pdat",
        }
        params.update(ncbi_params)
        resp = request_pubmed_with_fallback(
            session,
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
            params=params,
            timeout=45,
            label="PubMed esearch",
        )
        payload = resp.json() or {}
        ids = (((payload.get("esearchresult") or {}).get("idlist")) or [])
        ids = [str(i).strip() for i in ids if str(i).strip()]
        ids = [i for i in ids if i not in id_seen][:per_query_limit]
        if not ids:
            continue
        id_seen.update(ids)
        fetch_resp = request_pubmed_with_fallback(
            session,
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi",
            params={"db": "pubmed", "id": ",".join(ids), "retmode": "xml", **ncbi_params},
            timeout=60,
            label="PubMed efetch",
        )
        root = ET.fromstring(fetch_resp.text)
        for article in root.findall(".//PubmedArticle"):
            pmid = "".join(article.findtext(".//PMID", default="")).strip()
            article_title = "".join(article.findtext(".//ArticleTitle", default="")).strip()
            abstract_parts = []
            for node in article.findall(".//Abstract/AbstractText"):
                label = str(node.attrib.get("Label") or "").strip()
                text = "".join(node.itertext()).strip()
                if not text:
                    continue
                abstract_parts.append(f"{label}: {text}" if label else text)
            authors = []
            for author in article.findall(".//Author"):
                fore = "".join(author.findtext("ForeName", default="")).strip()
                last = "".join(author.findtext("LastName", default="")).strip()
                collective = "".join(author.findtext("CollectiveName", default="")).strip()
                name = " ".join(p for p in [fore, last] if p).strip() or collective
                if name:
                    authors.append(name)
            year = (
                article.findtext(".//PubDate/Year")
                or article.findtext(".//ArticleDate/Year")
                or ""
            )
            month = article.findtext(".//PubDate/Month") or "01"
            day = article.findtext(".//PubDate/Day") or "01"
            month_map = {
                "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
                "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12",
            }
            month = month_map.get(month, month.zfill(2) if month.isdigit() else "01")
            day = day.zfill(2) if day.isdigit() else "01"
            published = f"{year}-{month}-{day}" if year else ""
            doi = ""
            for aid in article.findall(".//ArticleId"):
                if str(aid.attrib.get("IdType") or "").lower() == "doi":
                    doi = normalize_doi("".join(aid.itertext()))
                    break
            results.append(
                {
                    "id": pmid,
                    "source": "pubmed",
                    "title": article_title,
                    "abstract": " ".join(abstract_parts).strip(),
                    "authors": authors,
                    "primary_category": "PubMed",
                    "categories": ["pubmed"],
                    "published": published,
                    "updated_at": published,
                    "link": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else "",
                    "doi": doi,
                    "external_ids": {"pmid": pmid},
                }
            )
    return results


def fetch_biorxiv_collection(server: str, days: int = 2) -> List[Dict[str, Any]]:
    session = requests.Session()
    cursor = 0
    results: List[Dict[str, Any]] = []
    window = f"{max(days, 1)}d"
    while True:
        url = f"https://api.biorxiv.org/details/{server}/{window}/{cursor}/json"
        resp = get_with_retry(
            session,
            url,
            timeout=60,
            label=f"{server} details",
        )
        payload = resp.json() or {}
        collection = payload.get("collection") or []
        if not collection:
            break
        for item in collection:
            doi = normalize_doi(item.get("doi"))
            version = str(item.get("version") or "").strip()
            results.append(
                {
                    "id": doi or f"{server}:{version}:{item.get('title')}",
                    "source": server,
                    "title": str(item.get("title") or "").strip(),
                    "abstract": str(item.get("abstract") or "").strip(),
                    "authors": [a.strip() for a in str(item.get("authors") or "").split(";") if a.strip()],
                    "primary_category": str(item.get("category") or "").strip(),
                    "categories": [str(item.get("category") or "").strip()] if str(item.get("category") or "").strip() else [],
                    "published": _to_iso_day(item.get("date")),
                    "updated_at": _to_iso_day(item.get("date")),
                    "link": str(item.get("jatsxml") or item.get("rel_link") or "").strip(),
                    "doi": doi,
                    "external_ids": {"doi": doi},
                }
            )
        messages = payload.get("messages") or []
        total = 0
        if messages and isinstance(messages, list):
            try:
                total = int((messages[0] or {}).get("total") or 0)
            except Exception:
                total = 0
        cursor += len(collection)
        if len(collection) < 100 or (total and cursor >= total):
            break
    return results


def save_json(data: Any, path: str) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
