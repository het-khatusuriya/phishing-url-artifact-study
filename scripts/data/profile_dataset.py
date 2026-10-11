"""Profile an untrusted URL dataset file (CSV/TXT/JSON). Run with: python -I scripts/data/profile_dataset.py <path> [--url-col URL] [--label-col LABEL] [--date-cols a,b] [--comment #] [--no-header] [--sep ,] [--json-list LABEL]
Prints: row count, columns, label distribution, scheme distribution, www share, IP-host share, duplicate URLs, min/max of date columns.
"""
import argparse, csv, json, re, sys, hashlib, io, os
from collections import Counter
from urllib.parse import urlsplit
csv.field_size_limit(10**9)
IP_RE = re.compile(r'^\d{1,3}(\.\d{1,3}){3}$')

def sha256(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()

def host_of(u):
    u = u.strip()
    if '://' not in u:
        scheme = 'none'; rest = u
    else:
        scheme, rest = u.split('://', 1); scheme = scheme.lower()
    host = rest.split('/', 1)[0].split('?', 1)[0].split('#', 1)[0]
    if '@' in host: host = host.rsplit('@', 1)[1]
    host = host.split(':', 1)[0].lower()
    return scheme, host

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('path'); ap.add_argument('--url-col', default='url'); ap.add_argument('--label-col', default=None)
    ap.add_argument('--date-cols', default=''); ap.add_argument('--comment', default=None); ap.add_argument('--no-header', action='store_true')
    ap.add_argument('--sep', default=','); ap.add_argument('--json-list', default=None, help='file is a JSON list of URLs; value = label to assign')
    ap.add_argument('--names', default=None, help='comma-separated column names for headerless files')
    a = ap.parse_args()
    print('file:', a.path); print('size_bytes:', os.path.getsize(a.path)); print('sha256:', sha256(a.path))
    rows = []
    if a.json_list is not None:
        with open(a.path, encoding='utf-8', errors='replace') as f:
            data = json.load(f)
        cols = ['url', 'label']; rows = [{'url': u, 'label': a.json_list} for u in data]
    else:
        with open(a.path, encoding='utf-8-sig', errors='replace', newline='') as f:
            lines = (l for l in f if not (a.comment and l.startswith(a.comment)))
            if a.no_header:
                names = a.names.split(',') if a.names else None
                rd = csv.reader(lines, delimiter=a.sep)
                first = next(rd, None)
                if first is None: print('empty'); return
                if names is None: names = [f'c{i}' for i in range(len(first))]
                cols = names; rows.append(dict(zip(names, first)))
                for r in rd: rows.append(dict(zip(names, r)))
            else:
                rd = csv.DictReader(lines, delimiter=a.sep)
                cols = rd.fieldnames; rows = list(rd)
    print('rows:', len(rows)); print('columns:', cols)
    uc = a.url_col if a.url_col in cols else cols[0]
    print('url_column_used:', uc)
    if a.label_col and a.label_col in cols:
        print('label_distribution:', dict(Counter(r.get(a.label_col) for r in rows).most_common(20)))
    sch = Counter(); www = 0; ip = 0; urls = []
    for r in rows:
        u = (r.get(uc) or '')
        urls.append(u); s, h = host_of(u); sch[s] += 1
        if h.startswith('www.'): www += 1
        if IP_RE.match(h): ip += 1
    n = max(len(rows), 1)
    print('scheme_distribution:', dict(sch.most_common(10)))
    print('share_www_hosts: %.4f' % (www / n)); print('share_ip_hosts: %.4f' % (ip / n))
    print('duplicate_urls:', len(urls) - len(set(urls)))
    for dc in [c for c in a.date_cols.split(',') if c]:
        if dc in cols:
            vals = sorted(v for v in (r.get(dc) or '' for r in rows) if v)
            print(f'date_col {dc}: min={vals[0] if vals else None} max={vals[-1] if vals else None}')
    print('sample_rows:', [dict(list(r.items())[:6]) for r in rows[:3]])
if __name__ == '__main__':
    main()
