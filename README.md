# AI–Geopolymer PRISMA Corpus — Research Artifact (v1.2)

Open research artifact accompanying:

> Nageshwaran V., Chaggar P.K., Amritphale S.S., Darestani M. (2026). *From Property Prediction to Clean-Technology Deployment: A Systematic Review and Roadmap for Trustworthy AI in Low-Carbon Geopolymer Development.* Revised manuscript submitted to *Clean Technologies and Environmental Policy*.

This release brings the artifact into line with the revised manuscript. On 12 Nov 2026 seven further duplicate reports were found, so the analysis set is **669 unique studies** (676 before). The data, tables, figures and the manuscript files in this archive all use 669; `AMENDMENT_2026-11-12.md` records every number that changed. The release adds the deterministic keyword classifier that produces every corpus-wide share in the paper, its lexicon and its per-record output, and it updates the two audit tables. `CHANGELOG.md` lists every change since v1.1.

## Headline counts

| Quantity | Value | Where to check |
|---|---|---|
| Unique records screened | 894 | `corpus_master.csv` (774) + `corpus_fallback_only.csv` (120) |
| Core corpus at freeze (21 Aug 2026) | 729 | `extraction_master.csv` |
| Core corpus after the 12 Nov 2026 amendment | 728 | `classifier/keyword_codes.csv`, `status = included` |
| Duplicate reports | 59 | `duplicate_of` column; evidence in `duplicate_audit.csv` (52 from the 31 Aug 2026 audit, 7 added 12 Nov 2026) |
| Unique primary studies (analysis set) | 669 | included records with empty `duplicate_of` |
| Analysis set before the 12 Nov 2026 amendment | 676 | `classifier/keyword_codes_before_amendment_n676.csv` |

## Contents

| Path | Description |
|---|---|
| `classifier/keyword_classifier.py` | Deterministic keyword-heuristic classifier (case-insensitive substring matching; no language model) |
| `classifier/lexicon.json` | The lexicon the classifier matches, one term list per code |
| `classifier/keyword_codes.csv` | Per-record output for all 729 frozen records: material, task, physics, environment and trust codes, coding depth, `needs_human_verification`, `status`. **This is the coding of record.** |
| `classifier/keyword_codes_before_amendment_n676.csv` | The same output before the seven further duplicates were flagged; reproduces the 676-study numbers of earlier drafts |
| `AMENDMENT_2026-11-12.md` | The seven duplicate pairs and every number in the manuscript that changed from the 676-study to the 669-study analysis set |
| `classifier/excluded_records.csv` | The one record removed after the freeze, with its reason (classifier input) |
| `classifier/verify_shares.py` | Recomputes the counts of Tables S8 and S10 from `keyword_codes.csv` |
| `classifier/fetch_supplementary_abstracts.py`, `classifier/supplementary_abstract_dois.csv` | Retrieval script and DOIs for the 20 frozen records that are not in the Scopus export, with the abstract source for each (12 are in the analysis set: 7 abstracts from OpenAlex, 5 from the publisher page) |
| `corpus_screening.csv` | Screening ledger (pipe-delimited): per-record decision and reason code |
| `corpus_master.csv` | 774 Scopus-set records with merged screening decisions, DOI, EID, citations |
| `corpus_fallback_only.csv` | 120 unique records identified only through supplementary sources |
| `extraction_master.csv` | The frozen 729-record core corpus: bibliographic fields, the keyword codes, `status`, `duplicate_of` and `eligibility_concern` |
| `duplicate_audit.csv` | Evidence for each duplicate-report decision |
| `eligibility_flags.csv` | The six records flagged as possibly ineligible and retained (extract of `extraction_master.csv`) |
| `physics_type_verification.csv` | Physics-integration audit of 32 studies (paper Table S11) |
| `carbon_lca_audit.csv` | Carbon and LCA audit of 77 studies (paper Table S12) |
| `extraction_deep.csv`, `extraction_pilot.csv` | Full-text extraction rows (12 studies) and pilot rows (4 studies) |
| `adjudication_final.csv`, `dual_screen_report.md` | Dual-screening agreement (Cohen's kappa) and adjudication record |
| `recode/` | Blind recode worksheet for the 70-study reliability sample, completed human and procedural recodes, coder instructions, and `score_keyword_vs_human.py`, which reproduces Supplementary Tables S9 and S14 |
| `supplementary_tables/` | Machine-readable Supplementary Tables S1, S8, S9, S10, S11, S12, S13 and S14. All match the Supplementary Materials in `manuscript/` |
| `Stage2_Protocol.md`, `Stage3_Corpus_Report.md` | Review protocol with dated amendments; search log, PRISMA counts and freeze record |
| `Stage4_Taxonomy.md` | Candidate taxonomies, the selected six-axis framework, coding rules and the capability-stage rule of Figure 2 |
| `Stage6_Research_Gaps.md`, `Stage7_Roadmap.md` | Full gap chains G1–G9 and the full roadmap |
| `springerlink_sample_screen.md` | Sample screen of unharvested SpringerLink records (Supplementary Note S7) |
| `merge_corpus.py` | Corpus merge and deduplication script |
| `figures/` | `make_figures.py` (Figures 1–5), `make_figure_S1.py` (Supplementary Figure S1) and `make_graphical_abstract.py` draw the figures from the released data (matplotlib and numpy needed); the PNG files are their output and are the images used in the manuscript |
| `manuscript/` | The revised submission: manuscript (PDF, Word, LaTeX source with figures), Supplementary Materials, graphical abstract, response to the editor |
| `legacy_v1.1/` | Superseded v1.1 files kept for the record: the earlier coding (`extraction_master.csv`), audit files, manuscript tables T1–T7, scoring script and figure scripts |

## Reproducing the results

| Result | Command |
|---|---|
| Corpus-wide counts, Tables S8 and S10 (669 studies) | `python3 classifier/verify_shares.py` |
| The same counts before the amendment (676 studies) | `python3 classifier/verify_shares.py classifier/keyword_codes_before_amendment_n676.csv` |
| Supplementary Figure S1 and graphical abstract | `python3 figures/make_figure_S1.py`, `python3 figures/make_graphical_abstract.py` |
| Classifier against human recode, Tables S9 and S14 | `python3 recode/score_keyword_vs_human.py` |
| Figures 1–5 | `python3 figures/make_figures.py` |

To re-run the coding itself:

```
python3 classifier/fetch_supplementary_abstracts.py
python3 classifier/keyword_classifier.py <scopus_export.csv> extraction_master.csv out.csv classifier/supplementary_abstracts.csv classifier/excluded_records.csv
```

The Scopus export is not redistributed here because Scopus abstracts and index keywords are licensed content. It can be regenerated by running the Family A query in `Stage3_Corpus_Report.md` and exporting to CSV with the fields EID, Title, Abstract, Author Keywords and Index Keywords. Abstracts for the records outside Scopus are likewise not redistributed; the first command retrieves those that OpenAlex holds, and the rest have to be read from the publisher's page.

## Notes on reading the files

- **Coding of record.** The code columns in `extraction_master.csv` are copied from `classifier/keyword_codes.csv`. The earlier coding released in v1.1 is in `legacy_v1.1/extraction_master.csv` and is not used by the revised paper.
- **Title-only rows.** 52 rows are coded from the title alone and carry `needs_human_verification = Y`. All 52 are duplicate reports and are outside the analysis set. Every study in the analysis set is coded from title and abstract (657 from the Scopus export, 12 from a supplementary abstract source).
- **Provisional status.** Keyword codes support aggregate, directional trends only. Claims about individual studies rest on the audited subsets.
- **Scripts written for v1.2.** `verify_shares.py`, `score_keyword_vs_human.py`, `fetch_supplementary_abstracts.py` and the three figure scripts were written for this release. `verify_shares.py` and `make_figures.py` reproduce the paper's counts exactly (and the 676-study counts when run on `keyword_codes_before_amendment_n676.csv`); `score_keyword_vs_human.py` reproduces Table S9 exactly; the 13 abstracts that `fetch_supplementary_abstracts.py` retrieves from OpenAlex reproduce the released codes for those records.
- **Taxonomy scoring.** `Stage4_Taxonomy.md` reports the candidates, criteria and the selected framework. The criterion-by-criterion scoring sheet is not included.

## Provenance

- Searches: Scopus (primary index), ScienceDirect, Crossref and SpringerLink, 10 Aug 2026; corpus frozen 21 Aug 2026; one record removed and seven further duplicate reports flagged by amendment on 12 Nov 2026 (`Stage3_Corpus_Report.md` §2e).
- Screening: every record screened twice, including independently by a human co-author (Cohen's kappa 0.83 and 0.69 before resolution); disagreements adjudicated by consensus.
- Coding: keyword classifier, checked against a blind human recode of a 70-study sample (Supplementary Table S9).
- A retraction notice found during screening is excluded and flagged in the ledger.

## License and citation

Data and documentation: CC BY 4.0. Code: MIT. Please cite the paper and this archive. The DOI [10.5281/zenodo.22325910](https://doi.org/10.5281/zenodo.22325910) always resolves to the latest version; v1.1 is [10.5281/zenodo.22325994](https://doi.org/10.5281/zenodo.22325994).

Maintained at https://github.com/vnageshwaran-de/ai-geopolymer-prisma-corpus.
