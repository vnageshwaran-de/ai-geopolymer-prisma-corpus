# Changelog

## v1.2.1 — 2026-11-14

DOI and address corrections only; no data, code or results changed.
- From v1.2 the archive is published from the repository `ai-geopolymer-prisma-corpus`, under a new Zenodo record: all versions 10.5281/zenodo.24222980, v1.2 10.5281/zenodo.24222981. Versions 1.0 and 1.1 remain under the earlier record 10.5281/zenodo.22325910.
- The manuscript (data availability statement), the Supplementary Materials, `README.md` and `CITATION.cff` now cite 10.5281/zenodo.24222980. In v1.2 they still cited the earlier record.

## v1.2 — 2026-11-12

Aligned with the revised manuscript, including the amendment of 12 Nov 2026 (seven further duplicate reports; analysis set 676 → 669).

Added
- `classifier/`: `keyword_classifier.py`, `lexicon.json`, `keyword_codes.csv` (per-record keyword codes for all 729 frozen records), `excluded_records.csv`, `verify_shares.py`, `fetch_supplementary_abstracts.py`, `supplementary_abstract_dois.csv`.
- `recode/score_keyword_vs_human.py`: reproduces Supplementary Table S9.
- `figures/`: scripts and output for Figures 1–5, Supplementary Figure S1 and the graphical abstract, drawn from the released data.
- `Stage4_Taxonomy.md`.
- `supplementary_tables/`: Supplementary Tables S1, S8, S9, S10, S11, S12 and S13 as CSV.
- `eligibility_flags.csv`: the six records flagged as possibly ineligible, extracted from `extraction_master.csv`.
- `CITATION.cff`, `.zenodo.json`, `LICENSE`, `MANIFEST_SHA256.txt`.

Changed
- **Analysis set 676 → 669.** Seven supplementary-source records (SD76, SD106, SD130, SD205, SD236, SD264, SD288) share a DOI, journal and year with Scopus records already in the corpus and are now flagged in `duplicate_of`. `duplicate_audit.csv` has three verdicts corrected from DISTINCT to DUPLICATE and four rows added (59 duplicates in all). `keyword_codes.csv`, `extraction_master.csv`, Tables S1, S8 and S10 and Figures 1–3 are regenerated. The manuscript, Supplementary Materials, graphical abstract and response letter in `manuscript/` are updated to match. `AMENDMENT_2026-11-12.md` lists every number that changed; `classifier/keyword_codes_before_amendment_n676.csv` keeps the earlier output. `Stage3_Corpus_Report.md` gains amendment §2e.
- Core corpus: 729 records at freeze, 728 after one bibliometric review (record SD292, 10.1016/j.marenvres.2026.108214) was moved to the context corpus on 12 Nov 2026. Analysis set before the duplicate amendment: 676 unique studies.
- `extraction_master.csv`: the code columns now hold the keyword-classifier codes, with `coding_depth`, `classification_method`, `needs_human_verification` and `status` added. Bibliographic fields, `duplicate_of` and `eligibility_concern` are unchanged. The v1.1 file is in `legacy_v1.1/`.
- `physics_type_verification.csv`: now the 32-study audit of Table S11 (v1.1 had 28 rows). Columns are now `doi, year, venue, title, flag, audit_outcome, note`.
- `carbon_lca_audit.csv`: now the 77-study audit of Table S12 (v1.1 had 76 rows); three rows recoded and one study added, as described in the table note. Columns are now `doi, year, venue, title, primary_treatment, quantified, carbon_in_optimization`.
- `manuscript/`: replaced with the revised submission (four tables, five figures), including the response to the editor. Data availability now cites an all-versions DOI (corrected in v1.2.1 to 10.5281/zenodo.24222980). In the Supplementary Materials a leftover table from the earlier coding (headed n = 677) was removed from Table S9, and the pointer for Table S4 was reworded.
- `README.md`: rewritten; author list updated.

Revision after pre-submission review (13 Nov 2026)
- Manuscript text revised in response to a review report: the capability-stage rule of Figure 2 is stated in Section 4; Figure 1 is redrawn with the direct-inclusion and full-text branches shown separately and without the "LLM-assisted" label (the primary screen was done by hand); the denominators of the screening agreement statistics are explained; search and audit limitations are stated more fully; nine references are added (one audited study that was described but not cited, a further systematic review, two reporting guidelines, an open dataset and four standards); capitalisation in reference titles is restored.
- New Supplementary Table S14 (sensitivity and specificity of the classifier against the human recode), produced by `recode/score_keyword_vs_human.py`.
- Figure 2 has a tick for every year; Figure 5 labels I1 "Shared benchmark".

Moved to `legacy_v1.1/`
- v1.1 versions of `extraction_master.csv` and the two audit files, manuscript tables T1–T7, `score_recode.py` and the figure scripts.

Removed
- v1.1 figures F1–F8 and the v1.1 manuscript files. They remain available in the v1.1 archive (10.5281/zenodo.22325994).

Unchanged from v1.1
- `corpus_screening.csv`, `corpus_master.csv`, `corpus_fallback_only.csv`, `extraction_deep.csv`, `extraction_pilot.csv`, `adjudication_final.csv`, `duplicate_audit.csv`, `dual_screen_report.md`, `springerlink_sample_screen.md`, the `Stage*.md` reports, `merge_corpus.py`, the worksheets and instructions in `recode/`.

## v1.1 — 2026-09-05
Zenodo 10.5281/zenodo.22325994.

## v1.0
Zenodo 10.5281/zenodo.22325911.
