"""Recompute the corpus-wide counts of Supplementary Tables S8 and S10 from keyword_codes.csv.

Added in artifact v1.2 as a convenience check; it is not part of the coding pipeline.
Usage: python3 verify_shares.py [keyword_codes.csv]
Analysis set = records with status 'included' and an empty duplicate_of field (n = 669).
Run it on keyword_codes_before_amendment_n676.csv to obtain the counts before the 12 Nov 2026 duplicate amendment.
"""
import csv, os, sys
from collections import Counter

path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'keyword_codes.csv')
rows = list(csv.DictReader(open(path, encoding='utf-8-sig')))
inc = [r for r in rows if r['status'] == 'included']
u = [r for r in inc if not r['duplicate_of'].strip()]
n = len(u)
print(f'records in file {len(rows)}; included {len(inc)}; unique studies {n}')

task = lambda r: r['T_task']
trust = lambda r: set(r['trust_flags'].split(';'))
env = lambda r: set(r['E_env'].split(';'))
DESIGN = ('optimization', 'multi-objective-optimization', 'inverse-design')
checks = [
    ('Prediction only (task label)', lambda r: task(r) == 'prediction'),
    ('Design vocabulary', lambda r: task(r) in DESIGN),
    ('Prediction or optimization family', lambda r: task(r) == 'prediction' or task(r) in DESIGN),
    ('Multi-objective optimization', lambda r: task(r) == 'multi-objective-optimization'),
    ('Inverse design', lambda r: task(r) == 'inverse-design'),
    ('Experiment selection', lambda r: task(r) == 'experiment-selection'),
    ('No trust-practice term', lambda r: 'none-detected' in trust(r)),
    ('Explainability', lambda r: 'XAI' in trust(r)),
    ('External validation', lambda r: 'ext-val' in trust(r)),
    ('Uncertainty quantification', lambda r: 'UQ' in trust(r)),
    ('Out-of-distribution or transfer', lambda r: 'OOD' in trust(r)),
    ('Calibration', lambda r: 'calibration' in trust(r)),
    ('Named code repository', lambda r: 'repro-signal' in trust(r)),
    ('Physics Type I', lambda r: r['P_physics'] == 'I'),
    ('Physics Type II', lambda r: r['P_physics'] == 'II'),
    ('Physics vocabulary flagged (Type III or above)', lambda r: r['P_physics'] == 'III+flag'),
    ('No environmental term', lambda r: 'none-explicit' in env(r)),
    ('Carbon term', lambda r: 'carbon' in env(r)),
    ('Life-cycle assessment term', lambda r: 'LCA' in env(r)),
    ('Carbon or LCA term', lambda r: bool(env(r) & {'carbon', 'LCA'})),
    ('Durability term', lambda r: 'durability' in env(r)),
    ('Published since Jan 2024', lambda r: int(r['year']) >= 2024),
]
print('\nTable S8 counts')
for name, f in checks:
    k = sum(1 for r in u if f(r))
    print(f'  {name:48s} {k:4d}/{n}  {100 * k / n:5.1f}%')

print('\nTable S10: material system by primary task (material axis is multi-label)')
tasks = ['prediction', 'optimization', 'multi-objective-optimization', 'inverse-design', 'classification',
         'microstructure/image-analysis', 'experiment-selection']
ct = Counter((m, task(r)) for r in u for m in r['M_material'].split(';'))
for m in ['fly-ash', 'FA-slag', 'slag', 'metakaolin/clay', 'red-mud', 'tailings', 'biomass-ash', 'recycled-aggregate',
          'one-part', 'stabilized-soil', 'mixed/other-AAM']:
    v = [ct[(m, t)] for t in tasks]
    print(f'  {m:20s}', *[f'{x:4d}' for x in v], f'| {sum(v):4d}')
