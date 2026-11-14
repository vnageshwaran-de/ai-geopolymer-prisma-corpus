"""Redraw the graphical abstract from the released data.

Written for artifact v1.2. Usage: python3 make_graphical_abstract.py [output.png]
The four headline numbers are computed from classifier/keyword_codes.csv and physics_type_verification.csv.
"""
import csv, os, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.join(here, '..')
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, 'GraphicalAbstract.png')
load = lambda p: list(csv.DictReader(open(os.path.join(root, p), encoding='utf-8-sig')))

u = [r for r in load('classifier/keyword_codes.csv') if r['status'] == 'included' and not r['duplicate_of'].strip()]
n = len(u)
pct = lambda f: 100 * sum(1 for r in u if f(r)) / n
has = lambda r, code: code in r['trust_flags'].split(';')
family = pct(lambda r: r['T_task'] in ('prediction', 'optimization', 'multi-objective-optimization', 'inverse-design'))
xai, ext, cal = (pct(lambda r, c=c: has(r, c)) for c in ('XAI', 'ext-val', 'calibration'))
no_env = pct(lambda r: r['E_env'] == 'none-explicit')
adaptive = sum(1 for r in u if r['T_task'] == 'experiment-selection')
audit = load('physics_type_verification.csv')
verified = sum(1 for r in audit if r['audit_outcome'].startswith('Verified'))

fig = plt.figure(figsize=(1900 / 150, 840 / 150)); ax = fig.add_axes([0, 0, 1, 1]); ax.axis('off'); ax.set_xlim(0, 12.6); ax.set_ylim(0, 5.57)
ax.text(6.3, 5.13, 'Is AI making geopolymers a deployable clean technology?', ha='center', va='center', fontsize=24, fontweight='bold')
ax.text(6.3, 4.63, f'Systematic review of {n} journal studies (2013–2026) · PRISMA 2020 · reproducible keyword coding of abstracts',
        ha='center', va='center', fontsize=15, style='italic', color='#37474f')
def panel(x, y, w, h, text, fc, color='white', fs=17):
    ax.add_patch(plt.Rectangle((x, y), w, h, fc=fc, ec='none'))
    ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=fs, color=color, linespacing=1.12)
panel(0.40, 2.68, 2.75, 1.50, f'PREDICT + OPTIMIZE\n{family:.1f}% of studies', '#1a237e')
panel(3.38, 2.68, 2.75, 1.50, f'TRUST\nexplainability {xai:.0f}%\next. validation {ext:.1f}%\ncalibration {cal:.1f}%', '#b71c1c')
panel(6.36, 2.68, 2.75, 1.50, f'PHYSICS\n{verified} of {len(audit)} audited\nstudies verified', '#e65100')
panel(9.34, 2.68, 2.86, 1.50, f'ENVIRONMENT\n2 boundary-explicit LCAs\n≥{no_env:.0f}% name no\nenvironmental variable', '#f9a825', 'black', 16)
panel(0.40, 0.80, 5.73, 1.40, f'ADAPTIVE: {adaptive} studies, all simulated\nNo physical closed loop detected', '#eceff1', 'black')
panel(6.36, 0.80, 5.84, 1.40, 'ROADMAP: honest models →\nchemistry- and carbon-coupled models → closed loops\n(deployment and governance in parallel)', '#1b5e20', 'white', 15)
ax.text(6.3, 0.42, 'Open artifact: coded corpus, keyword classifier, audit tables and scripts', ha='center', va='center', fontsize=16, color='#1b5e20')
plt.savefig(out, dpi=150); plt.close()
print(f'n = {n}; prediction or optimization {family:.1f}%; explainability {xai:.0f}%; external validation {ext:.1f}%; '
      f'calibration {cal:.1f}%; no environmental term {no_env:.0f}%; verified {verified} of {len(audit)}; written to {out}')
