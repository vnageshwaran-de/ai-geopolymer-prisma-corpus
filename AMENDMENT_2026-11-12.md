# Amendment of 12 November 2026: analysis set 676 → 669

On 12 Nov 2026, while the artifact was being prepared for v1.2, DOIs were resolved through Crossref for the supplementary-source records that had none in the ledger. Seven supplementary-source records in the analysis set were found to be duplicate reports of Scopus records already in the corpus. Each pair shares a DOI, journal and year; the supplementary record carries a shortened title, the same failure mode as the 52 duplicates found in the 31 Aug 2026 audit. Three of the seven had been marked DISTINCT in that audit.

| Duplicate record | Kept record (Scopus) | DOI |
|---|---|---|
| SD76 | 2-s2.0-105021266320 | 10.1016/j.asej.2025.103854 |
| SD106 | 2-s2.0-105007925869 | 10.1016/j.nxmate.2025.100812 |
| SD130 | 2-s2.0-105019264834 | 10.1016/j.hybadv.2025.100569 |
| SD205 | 2-s2.0-85105259171 | 10.1016/j.asej.2021.03.018 |
| SD236 | 2-s2.0-105040692013 | 10.1016/j.nxmate.2026.102389 |
| SD264 | 2-s2.0-85184073306 | 10.1680/jmacr.23.00144 |
| SD288 | 2-s2.0-105004811499 | 10.1016/j.jobe.2025.112879 |

Everything in this archive uses the amended analysis set (**669 unique studies; 59 duplicate reports**): the data files, the supplementary tables, the figures and the manuscript files in `manuscript/`. This file records every number that changed from earlier drafts of the revised manuscript, which reported 676. No headline share moved by more than 0.2 percentage points and no conclusion changed.

`classifier/keyword_codes_before_amendment_n676.csv` reproduces the earlier numbers; `classifier/keyword_codes.csv` reproduces the current ones.

## 1. Counts that changed everywhere

| Quantity | Before | After |
|---|---|---|
| Unique primary studies (analysis set) | 676 | 669 |
| Duplicate reports | 52 | 59 |
| Records included (Core Corpus) | 728 | 728 (unchanged) |

"676" appears in the abstract, Sections 1.3, 2.1, 2.6.4, 2.7 and 9, Table 1, the captions of Figure 2 and Tables 2 and 3, the Data availability statement and the graphical abstract.

## 2. Main text, by section

| Where | Before | After |
|---|---|---|
| 2.1 Protocol | duplicate audit "found 52 pairs", "giving 676 unique primary studies" | 59 pairs (52 in the audit of 31 Aug 2026 and 7 on 12 Nov 2026); 669 |
| 2.5 Coverage | "a further 52 were Scopus records under abbreviated titles, so Scopus already held 372 of the 440 (85%)" | a further 59; 379 of the 440 (86%) |
| 2.6.4 Who performed the coding | "Scopus export for 657 of the 676 unique studies. For the remaining 19" | 657 of the 669; remaining 12 |
| 2.6.4 Who performed the coding | "(OpenAlex; 13 studies) ... (6 studies)" | "(OpenAlex; 7 studies) ... (5 studies)". Re-checked against OpenAlex on 13 Nov 2026: it holds abstracts for 13 of the original 19 and for 7 of the remaining 12 |
| 2.6.4 Reliability | "random sample of 70 studies (about 10% of the corpus)" | Unchanged, but one sampled record (SD236) is now a duplicate report; it remains among the 67 compared |
| 2.6.4 Further checks | excluding the six flagged records "changes no headline proportion by more than 0.3 percentage points" | Still true (largest change 0.2 points at n = 663) |
| 5.1 Growth | "38 in 2021 ... 130 in 2024, 178 in 2025 and 171 in the first part of 2026" | 37 in 2021; 129 in 2024; 175 in 2025; 169 in 2026 |
| 5.1 Growth | since January 2024: "70.9% [95% CI 67.3–74.2]" | 70.7% [67.1–74.0] ("71%" in the abstract and Section 1.2 is unchanged) |
| 5.1 Materials | fly-ash/slag blends 23.7%; slag 15.7%; stabilized soils 6.2%; biomass ashes 4.1% | 23.8%; 15.5%; 6.3%; 4.2% |
| 5.1 Materials | fly-ash 23.2%; mixed or other 28.6%; metakaolin 6.1%; recycled aggregate 3.6%; one-part 2.8%; tailings 1.2%; red mud 1.2% | Unchanged |
| 5.1 Tasks | design vocabulary "16.3% [13.7–19.2]"; mix-design optimization 10.5%; multi-objective 5.0% | 16.1% [13.5–19.1]; 10.3%; 5.1% |
| 5.1 Tasks | 94.5% [92.5–96.0]; 78.3%; 3.6%; 1.5%; 0.4%; 0.7% | Unchanged |
| 5.1 Targets | durability terms "in 23.7% of abstracts" | 23.9% |
| 5.2 Trust | external validation "4.7% [3.4–6.6]" | 4.6% [3.3–6.5] |
| 5.2 Trust | no trust-practice term "57.7% [53.9–61.4]" | 57.8% [54.1–61.5] |
| 5.2 Trust | explainability 39.3% [35.7–43.1]; uncertainty 1.8% [1.0–3.1]; out-of-distribution 1.3% [0.7–2.5]; calibration 0.6% [0.2–1.5] | Unchanged |
| 5.3 Physics | Type I "80.5% [77.3–83.3]"; Type II "16.0% [13.4–18.9]"; sum "96.4% [94.8–97.6]" | 80.3% [77.1–83.1]; 16.1% [13.5–19.1]; 96.4% [94.7–97.6] |
| 5.3 Physics | 24 flagged studies (3.6%); audit of 32 | Unchanged |
| 5.4 Environment | no environmental term "41.0% [37.3–44.7]"; carbon terms 26.0% | 40.8% [37.1–44.6]; 26.2% |
| 5.4 Environment | "Of the 178 studies whose abstracts use carbon or life-cycle vocabulary" | 177 |
| 5.4 Environment | LCA terms 2.7%; 0.3% [0.1–1.1] of the corpus; all counts within the 77 audited | Unchanged |
| 8 Limitations | "for 19 studies the abstract came from an open index or the publisher page" | 12 |

## 3. Tables and figures

| Item | Change |
|---|---|
| Table 2 (trust practices) | Header "% of 669". Explainability 263, 39.3. External validation 31, 4.6. None signalled 387, 57.8. Other rows unchanged |
| Table 3 (gaps) | G7 "Signalled in 4.6%". G4 "At least 41%" is unchanged (40.8%) |
| Figure 1 | "59 duplicate reports flagged"; "n = 669 unique primary studies". `figures/Fig1.png` |
| Figure 2 | n = 669. Stage counts 342 / 51 / 236 / 9 / 23 / 5 / 3 / 0 (were 345 / 52 / 239 / 9 / 23 / 5 / 3 / 0). `figures/Fig2.png` |
| Figure 3 | Cohort sizes 23 / 51 / 122 / 129 / 175 / 169. Explainability 17 / 14 / 32 / 40 / 43 / 51%. External validation 0 / 4 / 1 / 5 / 5 / 8%. Other rows unchanged. `figures/Fig3.png` |
| Figures 4 and 5 | Unchanged |
| Graphical abstract | "676 journal studies" → 669; "ext. validation 4.7%" → 4.6% |
| Supplementary Figure S1 | "(676 unique studies)" → 669 |

## 4. Supplementary Materials

| Item | Change |
|---|---|
| Table S1 | Duplicate reports 52 → 59; unique primary studies 676 → 669; identity check "728 − 59 = 669". File: `supplementary_tables/S1_prisma_reconciliation.csv` |
| Table S8 | Denominator 669; all rows recomputed. File: `supplementary_tables/S8_wilson_intervals.csv` |
| Table S9, design note | "70 unique studies (10.3% of the corpus)" → "70 studies (about 10% of the corpus)", with a sentence noting that one sampled record (SD236) was later identified as a duplicate report. Agreement figures are unchanged |
| Table S9, residual screening error | "(n = 670) ... prediction-or-optimization 94.5% to 94.6%; no trust-practice term 57.7% to 57.5%; no environmental term 41.0% to 41.0%" → n = 663; 94.5% to 94.6%; 57.8% to 57.6%; 40.8% to 40.9% |
| Table S10 | n = 669. Rows that change: fly-ash 120 / 23 / 8 / 0 / 0 / 4 / 0, total 155; FA-slag 117 / 21 / 10 / 2 / 1 / 7 / 1, total 159; slag 79 / 10 / 4 / 2 / 3 / 6 / 0, total 104; mixed/other 158 / 11 / 10 / 1 / 5 / 4 / 2, total 191. File: `supplementary_tables/S10_material_by_task.csv` |
| Table S12, note | "76 of the 77 are among the 178 studies" → 177 |
| Tables S11, S13 | Unchanged |

## 5. Other changes made to the manuscript files at the same time

| Item | Change |
|---|---|
| Data availability statement; Supplementary Materials, first paragraph | Zenodo DOI changed from the v1.1 record (10.5281/zenodo.22325994) to the all-versions DOI of the current archive (10.5281/zenodo.24222980) |
| Supplementary Materials, Table S9 | A second table headed "n = 677 / n = 671 (eligible)", left over from the earlier coding and contradicted by the text beside it, was removed |
| Supplementary Materials, pointers | Table S4 pointer reworded to "taxonomy candidates, selection and coding rules"; `stage3/springerlink_sample_screen.md` corrected to `springerlink_sample_screen.md` |
| Response to the Editor | 676 → 669 and external validation 4.7% → 4.6% in the authors' replies; a sentence on the seven further duplicates added under Corrections; "the 76 environmentally audited studies" corrected to 77 to match the manuscript. The editor's quoted comment is left as written |
