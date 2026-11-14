"""Redraw Figures 1-5 of the revised manuscript from the released data.

Written for artifact v1.2. Usage:
    python3 make_figures.py [output_directory] [keyword_codes.csv]

Figures 2 and 3 are computed from classifier/keyword_codes.csv (669 unique included studies) and
Figure 4 from carbon_lca_audit.csv. Figures 1 and 5 are diagrams; the script checks the PRISMA
arithmetic of Figure 1 before drawing it. The counts are asserted against expected values, so the
script stops if the data change unexpectedly.

To redraw the figures for the 676-study analysis set (before seven further duplicate reports
were flagged on 12 Nov 2026), pass classifier/keyword_codes_before_amendment_n676.csv as the second
argument. The images in manuscript/5_LaTeX_source/ are the output of this script.
"""
import csv, os, sys
from collections import Counter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.join(here, '..')
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, 'out')
codes_path = sys.argv[2] if len(sys.argv) > 2 else os.path.join(root, 'classifier', 'keyword_codes.csv')
os.makedirs(out, exist_ok=True)
load = lambda p: list(csv.DictReader(open(os.path.join(root, p), encoding='utf-8-sig')))

codes = list(csv.DictReader(open(codes_path, encoding='utf-8-sig')))
included = [r for r in codes if r['status'] == 'included']
u = [r for r in included if not r['duplicate_of'].strip()]
n = len(u)
dups = len(included) - n
EXPECTED = {   # n: (stage counts, cohort sizes, explainability % by cohort)
    669: ([342, 51, 236, 9, 23, 5, 3, 0], [23, 51, 122, 129, 175, 169], [17, 14, 32, 40, 43, 51]),
    676: ([345, 52, 239, 9, 23, 5, 3, 0], [23, 52, 122, 130, 178, 171], [17, 13, 32, 40, 44, 50]),
}
assert (len(codes), len(included)) == (729, 728) and (n, dups) in ((669, 59), (676, 52)), (n, dups)
flags = lambda r: set(r['trust_flags'].split(';'))
year = lambda r: min(int(r['year']), 2026)          # one in-press item dated 2027 is shown with 2026


# ---------- Figure 1: PRISMA flow ----------
assert 774 + 320 + 100 + 20 == 1214 and 1214 - 320 == 894
assert 3 + 4 + 15 + 14 + 31 + 3 == 70 and 894 - 70 == 824 and 824 - 58 == 766
assert 6 + 28 + 3 == 37 and 12 + 37 == 49 and 766 - 49 == 717 and 717 + 12 == 729 and 729 - 1 == 728 and 728 - dups == n
fig = plt.figure(figsize=(8.335, 10.21)); ax = fig.add_axes([0.01, 0.01, 0.98, 0.98]); ax.axis('off'); ax.set_xlim(0, 10); ax.set_ylim(1.7, 15.1)
def box(x, y, w, h, text, fc, ec, fs=9.5):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.05', fc=fc, ec=ec, lw=1.8))
    ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=fs)
def arrow(x1, y1, x2, y2):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='-|>', mutation_scale=16, lw=1.6, color='#37474f'))
box(0.3, 13.4, 4.6, 1.5, 'Records identified n = 1,214\nScopus Family A n=774 · ScienceDirect n=320\nCrossref n=100 · SpringerLink n=20\n(per-source counts post internal dedup)', '#e8f5e9', '#2e7d32')
box(5.6, 13.6, 4.1, 1.1, 'IEEE Xplore n=13\n(all conference papers\n→ excluded at source, EC4)', '#f5f5f5', '#9e9e9e', 9)
arrow(2.6, 13.35, 2.6, 12.85)
box(0.3, 11.7, 4.6, 1.1, 'Duplicate records removed\nbefore screening n = 320\n(supplementary records matched to Scopus)', '#fff3e0', '#ef6c00')
arrow(2.6, 11.65, 2.6, 11.15)
box(0.3, 9.9, 4.6, 1.2, 'Unique records screened n = 894\nprimary screen by the first author; each record\nalso screened by a co-author (κ = 0.83, 0.69)', '#e3f2fd', '#1565c0')
box(5.6, 10.0, 4.1, 2.1, 'Removed at title–abstract n = 70\nduplicates found in screening: 3\nEC1 preprint/non-journal: 4 · EC2 out of scope: 15\nEC4 conference: 14 · EC5 non-construction: 31\nEC7 venue quality: 3', '#ffebee', '#c62828', 8.5)
box(5.6, 8.5, 4.1, 1.1, 'Routed to Context Corpus n = 58\n(reviews and adjacent evidence;\nnot in synthesis counts)', '#f5f5f5', '#616161', 9)
arrow(4.95, 10.7, 5.55, 10.9); arrow(4.95, 10.2, 5.55, 9.3)
arrow(2.6, 9.85, 2.6, 9.35)
box(0.3, 8.2, 4.6, 1.1, 'Candidate primary records n = 766\n(894 − 70 − 58)', '#f3e5f5', '#6a1b9a')
arrow(1.6, 8.15, 1.6, 7.35)
box(0.3, 6.2, 2.6, 1.1, 'Included directly at\ntitle–abstract n = 717', '#e8f5e9', '#2e7d32')
arrow(4.95, 8.5, 5.55, 7.4)
box(5.6, 5.9, 4.1, 1.5, 'Assessed at full text or full abstract n = 49\nincluded 12 · excluded 37\n(EC2: 6 · EC3: 28 · EC7: 3)', '#fff3e0', '#ef6c00', 9)
arrow(1.6, 6.15, 1.6, 5.45)
arrow(5.55, 6.2, 4.95, 5.2)
ax.text(5.35, 5.45, '12', fontsize=9, ha='center', color='#37474f')
box(0.3, 4.3, 4.6, 1.1, 'Records included at freeze n = 729\n(717 + 12; 21 Aug 2026)', '#e8f5e9', '#2e7d32', 10.5)
box(5.6, 3.5, 4.1, 1.5, f'After freeze: 1 review moved to the\nContext Corpus (now 59) → 728 records;\n{dups} duplicate reports flagged', '#fff3e0', '#ef6c00', 9)
arrow(4.95, 4.6, 5.55, 4.35); arrow(2.6, 4.25, 2.6, 3.75)
box(0.3, 2.2, 4.6, 1.5, f'CORE CORPUS\nn = {n} unique primary studies\n(728 records)', '#e8f5e9', '#1b5e20', 12)
plt.savefig(os.path.join(out, 'Fig1.png'), dpi=200); plt.close()


# ---------- Figure 2: studies per year by capability stage ----------
def stage(r):
    """Highest stage whose vocabulary the record carries."""
    if r['T_task'] == 'experiment-selection': return 7
    if r['T_task'] == 'inverse-design': return 6
    if r['P_physics'] == 'III+flag': return 5
    if flags(r) & {'UQ', 'calibration'}: return 4
    if 'XAI' in flags(r): return 3
    if r['T_task'] in ('optimization', 'multi-objective-optimization'): return 2
    return 1
by_stage = Counter(stage(r) for r in u)
assert [by_stage[i] for i in range(1, 9)] == EXPECTED[n][0], by_stage
names = ['1. ML prediction', '2. Optimization (single- or multi-objective)', '3. Explainable AI', '4. Uncertainty-aware',
         '5. Physics-informed (flagged)', '6. Inverse design', '7. Adaptive (simulated)', '8. Autonomous']
years = list(range(2013, 2027))
grid = np.zeros((8, len(years)))
for r in u:
    grid[stage(r) - 1, years.index(year(r))] += 1
colors = plt.cm.viridis(np.linspace(0.05, 0.95, 8))
fig, ax = plt.subplots(figsize=(13, 7))
bottom = np.zeros(len(years))
for i in range(8):
    ax.bar(years, grid[i], bottom=bottom, color=colors[i], width=0.75, label=f'{names[i]} (n = {by_stage[i + 1]})')
    bottom += grid[i]
ax.set_xticks(years); ax.set_xlim(2012.4, 2026.6)
ax.set_xlabel('Publication year', fontsize=14); ax.set_ylabel(f'Unique studies (n = {n})', fontsize=14)
ax.legend(loc='upper left', fontsize=11)
ax.spines[['top', 'right']].set_visible(False)
plt.tight_layout(); plt.savefig(os.path.join(out, 'Fig2.png'), dpi=200); plt.close()


# ---------- Figure 3: trust practices by publication cohort ----------
cohorts = [('2013–2019', 2013, 2019), ('2020–2021', 2020, 2021), ('2022–2023', 2022, 2023),
           ('2024', 2024, 2024), ('2025', 2025, 2025), ('2026', 2026, 2026)]
practices = [('Explainability', 'XAI'), ('External validation', 'ext-val'), ('Uncertainty', 'UQ'),
             ('Out-of-distribution', 'OOD'), ('Calibration', 'calibration'), ('Stated repository', 'repro-signal')]
size = [sum(lo <= year(r) <= hi for r in u) for _, lo, hi in cohorts]
assert size == EXPECTED[n][1], size
share = np.array([[100 * sum(code in flags(r) and lo <= year(r) <= hi for r in u) / size[j]
                   for j, (_, lo, hi) in enumerate(cohorts)] for _, code in practices])
assert [round(v) for v in share[0]] == EXPECTED[n][2], share[0]
fig, ax = plt.subplots(figsize=(12, 5.8))
im = ax.imshow(share, cmap='YlOrRd', vmin=0, vmax=55, aspect='auto')
ax.set_xticks(range(len(cohorts))); ax.set_xticklabels([f'{c[0]}\n(n={s})' for c, s in zip(cohorts, size)], fontsize=11)
ax.set_yticks(range(len(practices))); ax.set_yticklabels([p[0] for p in practices], fontsize=12)
for i in range(share.shape[0]):
    for j in range(share.shape[1]):
        ax.text(j, i, f'{share[i, j]:.0f}', ha='center', va='center', fontsize=12, color='white' if share[i, j] > 27 else 'black')
fig.colorbar(im, ax=ax, label='% of cohort')
plt.tight_layout(); plt.savefig(os.path.join(out, 'Fig3.png'), dpi=200); plt.close()


# ---------- Figure 4: primary environmental treatment in the audited studies ----------
audit = load('carbon_lca_audit.csv')
treat = Counter(r['primary_treatment'] for r in audit)
order = [('rhetoric-only', 'Environmental framing without quantification', '#b71c1c'),
         ('emission-factors-quantified', 'Emission factors (quantified, no LCA)', '#e65100'),
         ('carbon-as-objective', 'Carbon inside optimization objective (primary treatment)', '#f9a825'),
         ('LCA-performed', 'LCA performed (boundaries not ISO-explicit)', '#558b2f'),
         ('ISO/boundary-LCA', 'ISO 14040/44 boundary-explicit LCA', '#1b5e20')]
assert len(audit) == 77 and [treat[k] for k, _, _ in order] == [20, 22, 20, 13, 2], treat
assert sum(r['carbon_in_optimization'] == 'Y' for r in audit) == 25
fig, ax = plt.subplots(figsize=(11, 5.06))
for i, (key, label, color) in enumerate(order):
    ax.barh(i, treat[key], color=color, height=0.62)
    ax.text(treat[key] + 0.5, i, f'{label}: {treat[key]}/77 ({100 * treat[key] / 77:.0f}%)', va='center', fontsize=11)
ax.set_yticks([]); ax.set_xlim(0, 62); ax.set_xlabel('Studies (of the 77 audited)', fontsize=12)
ax.spines[['top', 'right', 'left']].set_visible(False)
plt.tight_layout(); plt.savefig(os.path.join(out, 'Fig4.png'), dpi=200); plt.close()


# ---------- Figure 5: roadmap ----------
tiers = [('Immediate (0-2 y): make existing models honest', '#1565c0',
          ['I1 Shared benchmark', 'I2 Calibration by\ndefault', 'I3 Applicability-domain\nreporting', 'I4 Shared\nterminology', 'I5 Time-split\nvalidation']),
         ('Emerging (2-5 y): couple models to chemistry and carbon', '#558b2f',
          ['E1 Physics-\nconstrained design', 'E2 ML–LCA with\nfactor uncertainty', 'E3 Interlaboratory\nround-robin', 'E4 Early-age\nupdating', 'E5 Augmentation test']),
         ('Frontier (5-10 y): close the loop', '#ad1457',
          ['F1 First self-driving\nlaboratory', 'F2 Digital-twin\npilot', 'F3 Language-model\nsupport tools', 'F4 Transferable\nmodels']),
         ('Parallel throughout: deployment and governance', '#ef6c00',
          ['D1 Performance-based\nacceptance', 'D2 Digital material\npassports', 'D3 Demonstration\nsequence'])]
fig = plt.figure(figsize=(13.2, 7.04)); ax = fig.add_axes([0.02, 0.02, 0.96, 0.96]); ax.axis('off'); ax.set_xlim(0, 10); ax.set_ylim(0, 9.2)
for row, (title, color, items) in enumerate(tiers):
    top = 8.6 - 2.2 * row
    ax.text(0.1, top, title, fontsize=14, fontweight='bold', color=color, va='bottom')
    width = (9.8 - 0.1 * (len(items) - 1)) / len(items)
    for k, item in enumerate(items):
        x = 0.1 + k * (width + 0.1)
        ax.add_patch(plt.Rectangle((x, top - 1.45), width, 1.25, fc='white', ec=color, lw=2.5))
        ax.text(x + width / 2, top - 0.82, item, ha='center', va='center', fontsize=12)
plt.savefig(os.path.join(out, 'Fig5.png'), dpi=200); plt.close()

print(f'Figures 1-5 written to {out}')
