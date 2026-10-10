# Information Warfare Intelligence Investigation

A reproducible, evidence-led investigation framework for the fictional AsteriaGrid scenario. This repository is structured to support the assignment outputs: a technical report, evidence inventory, source verification, timeline, propagation analysis, media review, intelligence assessment, and defensive response.

> **Dataset status:** The GitHub repository was empty when this project was prepared. No assignment dataset was available locally. Accordingly, this repository does **not** invent posts, claims, dates, media findings, metrics, or citations. It contains a polished report framework, evidence templates, and analysis tooling that can be populated when the instructor-provided dataset is added.

## Quick start

1. Copy the supplied files into `data/raw/` without editing them. Keep original filenames: `social_media_posts.csv`, `source_register.csv`, `media_register.csv`, `README.txt`; add `source_documents/` and `media_evidence/`.
2. Create an environment and install `requirements.txt` (Python 3.10+).
3. Run `python scripts/analyze_dataset.py --input-dir data/raw --output-dir outputs`.
4. Review the generated chronology and metrics; investigate and cite each finding before filling `report/technical_report.md` and the templates in `templates/`.
5. Render Markdown to PDF/Word using your preferred editor if required. Verify the final report is 10–15 pages excluding cover, references, and appendices.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
python scripts/analyze_dataset.py --input-dir data/raw --output-dir outputs
```

The script accepts common column-name variants, but inspect its detected schema and the dataset README before relying on any output. It builds a directed repost/reply/quote relationship graph from parent IDs, reports in-degree, betweenness, and PageRank at post level, and exports edge/node tables and a Graphviz DOT visualization. Metrics describe the supplied graph, not real-world influence or coordination.

## Repository map

- `report/technical_report.md` — structured report draft with explicit data-dependent placeholders.
- `scripts/analyze_dataset.py` — reproducible CSV parsing, timeline and network analysis.
- `templates/` — evidence, claims, media, and source-verification registers.
- `data/raw/` — place the original assignment data here (not included).
- `outputs/` — generated tables and graph files (not committed by default).
- `docs/analysis_protocol.md` — collection, verification, confidence, and reproducibility protocol.

## Integrity, safety, and scope

This is a fictional analytical simulation. Do not contact accounts or organizations, access systems, attempt exploitation, or treat synthetic data as evidence about real entities. Preserve supplied originals; distinguish observation from inference; cite external sources; declare AI assistance according to course policy. Complete the analysis and prose individually, and do not submit unverified placeholders as findings.

## Reproducibility

Record Python/package versions, execution date, dataset filenames, SHA-256 hashes, and any manual exclusions in the appendix. Generated CSVs are derived working products, not replacements for source data. See `docs/analysis_protocol.md`.
