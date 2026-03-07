#!/usr/bin/env python

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from typing import Any, Dict, List

from multi_source_ingest import (
    build_source_queries,
    fetch_biorxiv_collection,
    fetch_europe_pmc_papers,
    fetch_pubmed_papers,
    get_source_settings,
    load_config,
    log,
    merge_paper_records,
    paper_matches_queries,
    save_json,
)


SCRIPT_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))


def run_date_token() -> str:
    token = str(os.getenv("DPR_RUN_DATE") or "").strip()
    if token:
        return token
    return datetime.now(timezone.utc).strftime("%Y%m%d")


def archive_raw_dir(token: str) -> str:
    return os.path.join(ROOT_DIR, "archive", token, "raw")


def load_json_list(path: str) -> List[Dict[str, Any]]:
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f) or []
        return data if isinstance(data, list) else []
    except Exception as exc:
        log(f"[WARN] 读取失败: {path} | {exc}")
        return []


def fetch_arxiv_via_existing_step(python: str, extra_args: List[str], token: str) -> List[Dict[str, Any]]:
    raw_dir = archive_raw_dir(token)
    arxiv_raw = os.path.join(raw_dir, f"arxiv_only_papers_{token}.json")
    cmd = [python, os.path.join(SCRIPT_DIR, "1.1.fetch_paper_arxiv.py"), "--output", arxiv_raw, *extra_args]
    log(f"[INFO] Step1/arXiv -> {' '.join(cmd)}")
    subprocess.run(cmd, check=True)
    return load_json_list(arxiv_raw)


def source_enabled(name: str, settings: Dict[str, Any]) -> bool:
    enabled = settings.get("enabled_sources") or []
    return name in enabled


def write_manifest(raw_dir: str, token: str, payload: Dict[str, Any]) -> None:
    path = os.path.join(raw_dir, f"multi_source_manifest_{token}.json")
    save_json(payload, path)


def filter_records_by_queries(
    source_name: str,
    records: List[Dict[str, Any]],
    queries: List[str],
    raw_dir: str,
    token: str,
) -> List[Dict[str, Any]]:
    if not queries:
        return records
    filtered = [paper for paper in records if paper_matches_queries(paper, queries)]
    save_json(filtered, os.path.join(raw_dir, f"{source_name}_filtered_papers_{token}.json"))
    log(f"[INFO] {source_name} query-filtered: kept {len(filtered)}/{len(records)}")
    return filtered


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch papers from multiple sources and merge/deduplicate.")
    parser.add_argument("--days", type=int, default=None, help="lookback days")
    parser.add_argument("--ignore-seen", action="store_true")
    parser.add_argument("--disable-supabase-read", action="store_true")
    args = parser.parse_args()

    token = run_date_token()
    raw_dir = archive_raw_dir(token)
    os.makedirs(raw_dir, exist_ok=True)

    config = load_config()
    settings = get_source_settings(config)
    days = int(args.days or ((config.get("arxiv_paper_setting") or {}).get("days_window") or 1))
    per_query_limit = int(settings.get("per_query_limit") or 40)
    query_limit = int(settings.get("query_limit") or 12)
    source_queries = build_source_queries(config, query_limit)
    log(f"[INFO] multi-source queries={len(source_queries)}")

    python = sys.executable
    extra_args: List[str] = []
    if args.days is not None:
        extra_args.extend(["--days", str(args.days)])
    if args.ignore_seen:
        extra_args.append("--ignore-seen")
    if args.disable_supabase_read:
        extra_args.append("--disable-supabase-read")

    all_records: List[Dict[str, Any]] = []
    per_source_counts: Dict[str, int] = {}
    per_source_filtered_counts: Dict[str, int] = {}

    if source_enabled("arxiv", settings):
        arxiv_items = fetch_arxiv_via_existing_step(python, extra_args, token)
        per_source_counts["arxiv"] = len(arxiv_items)
        arxiv_items = filter_records_by_queries("arxiv", arxiv_items, source_queries, raw_dir, token)
        per_source_filtered_counts["arxiv"] = len(arxiv_items)
        all_records.extend(arxiv_items)
    else:
        per_source_counts["arxiv"] = 0
        per_source_filtered_counts["arxiv"] = 0

    if source_queries and source_enabled("europe_pmc", settings):
        try:
            epmc = fetch_europe_pmc_papers(source_queries, per_query_limit=per_query_limit, days=days)
            epmc = [p for p in epmc if paper_matches_queries(p, source_queries)]
            per_source_counts["europe_pmc"] = len(epmc)
            per_source_filtered_counts["europe_pmc"] = len(epmc)
            save_json(epmc, os.path.join(raw_dir, f"europe_pmc_papers_{token}.json"))
            all_records.extend(epmc)
        except Exception as exc:
            per_source_counts["europe_pmc"] = 0
            per_source_filtered_counts["europe_pmc"] = 0
            log(f"[WARN] Europe PMC fetch failed: {exc}")
    else:
        per_source_counts.setdefault("europe_pmc", 0)
        per_source_filtered_counts.setdefault("europe_pmc", 0)

    if source_queries and source_enabled("pubmed", settings):
        try:
            pubmed = fetch_pubmed_papers(source_queries, per_query_limit=per_query_limit, days=days)
            pubmed = [p for p in pubmed if paper_matches_queries(p, source_queries)]
            per_source_counts["pubmed"] = len(pubmed)
            per_source_filtered_counts["pubmed"] = len(pubmed)
            save_json(pubmed, os.path.join(raw_dir, f"pubmed_papers_{token}.json"))
            all_records.extend(pubmed)
        except Exception as exc:
            per_source_counts["pubmed"] = 0
            per_source_filtered_counts["pubmed"] = 0
            log(f"[WARN] PubMed fetch failed: {exc}")
    else:
        per_source_counts.setdefault("pubmed", 0)
        per_source_filtered_counts.setdefault("pubmed", 0)

    for source_name, day_key in (("biorxiv", "biorxiv_days"), ("medrxiv", "medrxiv_days")):
        if not source_enabled(source_name, settings):
            per_source_counts[source_name] = 0
            per_source_filtered_counts[source_name] = 0
            continue
        try:
            items = fetch_biorxiv_collection(source_name, days=int(settings.get(day_key) or days))
            items = [p for p in items if paper_matches_queries(p, source_queries)]
            per_source_counts[source_name] = len(items)
            per_source_filtered_counts[source_name] = len(items)
            save_json(items, os.path.join(raw_dir, f"{source_name}_papers_{token}.json"))
            all_records.extend(items)
        except Exception as exc:
            per_source_counts[source_name] = 0
            per_source_filtered_counts[source_name] = 0
            log(f"[WARN] {source_name} fetch failed: {exc}")

    merged = merge_paper_records(all_records)
    merged_path = os.path.join(raw_dir, f"arxiv_papers_{token}.json")
    save_json(merged, merged_path)
    write_manifest(
        raw_dir,
        token,
        {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "date_token": token,
            "queries": source_queries,
            "source_counts": per_source_counts,
            "source_filtered_counts": per_source_filtered_counts,
            "merged_count": len(merged),
            "sources_enabled": settings.get("enabled_sources") or [],
        },
    )
    log(f"[OK] merged multi-source raw saved: {merged_path} | count={len(merged)}")


if __name__ == "__main__":
    main()
