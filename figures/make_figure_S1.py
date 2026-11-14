"""Redraw Supplementary Figure S1 (the six-axis coding framework and its two views).

Written for artifact v1.2. Usage: python3 make_figure_S1.py [output.png]
The record and study counts are read from classifier/keyword_codes.csv.
"""
import csv, os, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

here = os.path.dirname(os.path.abspath(__file__))
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, 'FigS1.png')
rows = list(csv.DictReader(open(os.path.join(here, '..', 'classifier', 'keyword_codes.csv'), encoding='utf-8-sig')))
included = [r for r in rows if r['status'] == 'included']
unique = [r for r in included if not r['duplicate_of'].strip()]

fig = plt.figure(figsize=(9.5, 4.51)); ax = fig.add_axes([0.01, 0.01, 0.98, 0.98]); ax.axis('off'); ax.set_xlim(0, 12); ax.set_ylim(0, 5.7)
def box(x, y, w, h, text, ec, fc='white', fs=9.5, lw=2):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.03', fc=fc, ec=ec, lw=lw))
    ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=fs)
def arrow(x1, y1, x2, y2):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='-|>', mutation_scale=12, lw=1.4, color='#37474f'))
axes = [('M  Material system', '#8d6e63'), ('T  AI task', '#1976d2'), ('R  Trust practices', '#7b1fa2'),
        ('P  Physics integration (Types I–V)', '#689f38'), ('E  Environmental function', '#f57c00'),
        ('D  Deployment maturity\n(audited subsets only)', '#c2185b')]
for i, (label, color) in enumerate(axes):
    y = 4.85 - 0.88 * i
    box(0.2, y, 4.1, 0.62, label, color)
    arrow(4.33, y + 0.31, 5.33, 2.85)
box(5.35, 2.0, 2.6, 1.7, f'One coding of\n{len(included)} records\n({len(unique)} unique studies),\nreleased', '#37474f', '#eceff1', 9.5)
for label, y in [('Capability stages\nover time (Fig. 2)', 4.1), ('Six-axis profiles and audits\n(Tables 2, S10–S12)', 1.6)]:
    box(8.6, y - 0.5, 3.2, 1.0, label, '#2e7d32', '#e8f5e9')
    arrow(7.98, 2.85, 8.57, y)
plt.savefig(out, dpi=200); plt.close()
print(f'{len(included)} records, {len(unique)} unique studies; written to {out}')
