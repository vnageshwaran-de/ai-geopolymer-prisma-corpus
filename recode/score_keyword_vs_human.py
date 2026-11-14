"""Agreement between the keyword classifier and the blind human recode (Supplementary Tables S9 and S14).

Written for artifact v1.2. Usage, from any directory:
    python3 score_keyword_vs_human.py [keyword_codes.csv] [recode_worksheet_human_completed.csv] [--write-s14]

The 70-study sample is joined on record id. Rows the human coder left uncoded because she judged the
record ineligible (3 of 70) are dropped, leaving n = 67. For each axis the script prints percentage
agreement and Cohen's kappa. Kappa is not informative when a category is very rare.

Comparisons
  Task, full label   classifier T_task against the human primary task label
  Task family        prediction, optimization, multi-objective optimization or inverse design, against any other task
  Physics type       I / II / III-and-above (classifier 'III+flag' counts as III-and-above)
  Environmental      'none-explicit' against any environmental label
  Trust flags        classifier flag present against human Y/N
"""
import csv, os, sys
from collections import Counter

here = os.path.dirname(os.path.abspath(__file__))
args = [x for x in sys.argv[1:] if not x.startswith('--')]
kc_path = args[0] if len(args) > 0 else os.path.join(here, '..', 'classifier', 'keyword_codes.csv')
hum_path = args[1] if len(args) > 1 else os.path.join(here, 'recode_worksheet_human_completed.csv')
load = lambda p: list(csv.DictReader(open(p, encoding='utf-8-sig')))

kc = {r['id']: r for r in load(kc_path)}
sample = load(hum_path)
hum = [h for h in sample if h['T_primary_task'].strip()]
print(f'sample {len(sample)}; judged ineligible by the human coder {len(sample) - len(hum)}; compared n = {len(hum)}')

def agreement(pairs):
    n = len(pairs)
    po = sum(a == b for a, b in pairs) / n
    ca, cb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    pe = sum(ca[c] * cb.get(c, 0) for c in ca) / n ** 2
    return po, ((po - pe) / (1 - pe) if pe < 1 else None)

FAMILY = ('prediction', 'optimization', 'multi-objective-optimization', 'inverse-design')
DESIGN = FAMILY[1:]
p3 = lambda p: p.strip() if p.strip() in ('I', 'II') else 'III+'
FLAGS = [('Explainability flag', 'XAI', 'SC_explainability_YN'), ('Uncertainty flag', 'UQ', 'SC_uncertainty_YN'),
         ('Calibration flag', 'calibration', 'SC_calibration_YN'),
         ('External-validation flag', 'ext-val', 'SC_external_validation_YN'),
         ('Out-of-distribution flag', 'OOD', 'SC_OOD_or_transfer_YN'),
         ('Repository flag', 'repro-signal', 'SC_reproducibility_YN')]

task, fam, phys, env = [], [], [], []
flags = {name: [] for name, _, _ in FLAGS}
for h in hum:
    k = kc[h['record_id']]
    ht = h['T_primary_task'].strip()
    task.append((k['T_task'], ht))
    fam.append((k['T_task'] in FAMILY, ht in FAMILY))
    phys.append((p3(k['P_physics'].replace('III+flag', 'III+')), p3(h['P_physics_type_I_to_V'])))
    env.append((k['E_env'] == 'none-explicit', 'none-explicit' in h['E_env_function']))
    kt = set(k['trust_flags'].split(';'))
    for name, code, col in FLAGS:
        flags[name].append((code in kt, h[col].strip().upper() == 'Y'))

rows = [('Task, full label', task), ('Task family (prediction-or-optimization vs other)', fam),
        ('Physics type (I / II / III and above)', phys), ('Environmental: none vs any', env)] + list(flags.items())
print(f'\n{"Axis / flag":52s} agreement   kappa')
for name, pairs in rows:
    po, kp = agreement(pairs)
    print(f'{name:52s} {100 * po:6.1f}%   {"  n/a" if kp is None else f"{kp:5.2f}"}')

x = flags['Explainability flag']
print(f'\nNo environmental label: classifier {sum(a for a, _ in env)}, human {sum(b for _, b in env)} of {len(env)}')
print(f'Explainability: classifier {sum(a for a, _ in x)}, human {sum(b for _, b in x)} of {len(x)}')
print(f'Design work: classifier {sum(a in DESIGN for a, _ in task)}, human {sum(b in DESIGN for _, b in task)}, '
      f'both {sum(a in DESIGN and b in DESIGN for a, b in task)}')

# ---------- Supplementary Table S14: sensitivity and specificity against the human recode ----------
import math

def wilson(k, n, z=1.959964):
    p = k / n; d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d; h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return 100 * max(0, c - h), 100 * min(1, c + h)

corpus = [r for r in kc.values() if r['status'] == 'included' and not r['duplicate_of'].strip()]
S14 = [('Prediction or optimization family', fam, lambda r: r['T_task'] in FAMILY),
       ('Design vocabulary', [(a in DESIGN, b in DESIGN) for a, b in task], lambda r: r['T_task'] in DESIGN),
       ('Explainability', flags['Explainability flag'], lambda r: 'XAI' in r['trust_flags'].split(';')),
       ('Uncertainty quantification', flags['Uncertainty flag'], lambda r: 'UQ' in r['trust_flags'].split(';')),
       ('External validation', flags['External-validation flag'], lambda r: 'ext-val' in r['trust_flags'].split(';')),
       ('No environmental variable', env, lambda r: r['E_env'] == 'none-explicit')]
header = ['Quantity', 'Classifier, corpus (%)', 'Classifier, sample (k/67)', 'Human, sample (k/67)', 'Both (k)',
          'Sensitivity', 'Specificity', 'Human-coded share, % [95% CI]']
table = [header]
for name, pairs, f in S14:
    n = len(pairs)
    tp = sum(a and b for a, b in pairs); fp = sum(a and not b for a, b in pairs)
    fn = sum(b and not a for a, b in pairs); tn = n - tp - fp - fn
    lo, hi = wilson(tp + fn, n)
    table.append([name, f'{100 * sum(1 for r in corpus if f(r)) / len(corpus):.1f}', f'{tp + fp}/{n}', f'{tp + fn}/{n}', str(tp),
                  f'{tp / (tp + fn):.2f}' if tp + fn else 'n/a', f'{tn / (tn + fp):.2f}' if tn + fp else 'n/a',
                  f'{100 * (tp + fn) / n:.1f} [{lo:.1f}–{hi:.1f}]'])
print('\nTable S14: classifier against the human coder (human coding taken as reference)')
for row in table:
    print(f'{row[0]:36s}' + ''.join(f'{c:>24s}' for c in row[1:]))
if '--write-s14' in sys.argv:
    out = os.path.join(here, '..', 'supplementary_tables', 'S14_classifier_sensitivity_specificity.csv')
    with open(out, 'w', newline='', encoding='utf-8') as fh:
        csv.writer(fh).writerows(table)
    print('written to', out)
