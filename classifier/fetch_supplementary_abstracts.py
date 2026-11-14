"""Retrieve abstracts for the records that are not in the Scopus export.

Written for artifact v1.2. Usage:
    python3 fetch_supplementary_abstracts.py [supplementary_abstract_dois.csv] [supplementary_abstracts.csv]

For each DOI in supplementary_abstract_dois.csv the script asks OpenAlex (https://openalex.org) for the
work and rebuilds the abstract from its inverted index. The output file has the columns
id, doi, source, abstract and is the optional fourth argument of keyword_classifier.py.

Where OpenAlex holds no abstract the row is written with an empty abstract and source
'not in OpenAlex'. Those abstracts have to be read from the publisher's article page and pasted
into the output file by hand; the classifier codes any record without an abstract from its title alone.

OpenAlex limits anonymous use. Set OPENALEX_API_KEY (free key) or OPENALEX_MAILTO to avoid being throttled.
Abstracts are not redistributed in this archive.
"""
import csv, json, os, sys, time, urllib.parse, urllib.request

here = os.path.dirname(os.path.abspath(__file__))
src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, 'supplementary_abstract_dois.csv')
out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(here, 'supplementary_abstracts.csv')

def openalex(doi):
    params = {'select': 'id,doi,abstract_inverted_index'}
    if os.environ.get('OPENALEX_API_KEY'):
        params['api_key'] = os.environ['OPENALEX_API_KEY']
    if os.environ.get('OPENALEX_MAILTO'):
        params['mailto'] = os.environ['OPENALEX_MAILTO']
    url = 'https://api.openalex.org/works/https://doi.org/' + urllib.parse.quote(doi, safe='/') + '?' + urllib.parse.urlencode(params)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'geopolymer-review-artifact'}), timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return {}
            if e.code == 429 and attempt == 2:
                sys.exit('OpenAlex rate limit reached. Set OPENALEX_API_KEY and run again.')
        except Exception:
            pass
        time.sleep(2 * (attempt + 1))
    return {}

def abstract_text(work):
    index = work.get('abstract_inverted_index') or {}
    return ' '.join(word for _, word in sorted((pos, word) for word, positions in index.items() for pos in positions))

rows = []
with open(src, encoding='utf-8-sig') as f:
    for r in csv.DictReader(f):
        text = abstract_text(openalex(r['doi'])) if r['doi'].strip() else ''
        rows.append({'id': r['id'], 'doi': r['doi'], 'source': 'OpenAlex' if len(text) > 100 else 'not in OpenAlex',
                     'abstract': text if len(text) > 100 else ''})
        print(r['id'], r['doi'], rows[-1]['source'], len(text))
        time.sleep(0.2)
with open(out, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['id', 'doi', 'source', 'abstract'])
    w.writeheader(); w.writerows(rows)
print(f'{sum(r["source"] == "OpenAlex" for r in rows)} of {len(rows)} abstracts retrieved; written to {out}')
