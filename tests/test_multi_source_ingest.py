import unittest

from src.multi_source_ingest import canonical_key, merge_paper_records, normalize_doi


class MultiSourceIngestTest(unittest.TestCase):
    def test_normalize_doi(self):
        self.assertEqual(
            normalize_doi("https://doi.org/10.1101/2026.03.01.123456"),
            "10.1101/2026.03.01.123456",
        )

    def test_canonical_key_prefers_doi(self):
        paper = {"title": "Test", "doi": "10.1000/xyz-1", "published": "2026-03-07"}
        self.assertEqual(canonical_key(paper), "doi:10.1000/xyz-1")

    def test_merge_paper_records_merges_cross_source_duplicates(self):
        records = [
            {
                "id": "arxiv-1",
                "source": "arxiv",
                "title": "Foundation Models for Pathogen Detection",
                "abstract": "short",
                "authors": ["Alice"],
                "published": "2026-03-07",
                "link": "https://arxiv.org/abs/1234.5678",
                "doi": "10.1000/abc",
                "external_ids": {"arxiv": "1234.5678"},
            },
            {
                "id": "pmid-1",
                "source": "pubmed",
                "title": "Foundation Models for Pathogen Detection",
                "abstract": "longer abstract for the same paper",
                "authors": ["Alice", "Bob"],
                "published": "2026-03-07",
                "link": "https://pubmed.ncbi.nlm.nih.gov/1/",
                "doi": "10.1000/abc",
                "external_ids": {"pmid": "1"},
            },
        ]

        merged = merge_paper_records(records)
        self.assertEqual(len(merged), 1)
        item = merged[0]
        self.assertEqual(item["doi"], "10.1000/abc")
        self.assertIn("arxiv", item["sources"])
        self.assertIn("pubmed", item["sources"])
        self.assertEqual(item["source"], "arxiv")
        self.assertIn("longer abstract", item["abstract"])


if __name__ == "__main__":
    unittest.main()
