"""Orchestrator quality gate for a chapter TXT file. Usage: python gate.py chapters/chapter_02.txt"""
import re, sys, hashlib
path = sys.argv[1]
t = open(path, encoding='utf-8').read()
body = t.split('## מקורות לפרק')[0]
raw = len(body.split())
clean = re.sub(r'\[/?[^\]]*\]', '', body)
clean = re.sub(r'^##\s*', '', clean, flags=re.M)
words = len([x for x in clean.split() if re.search(r'\w', x)])
src = open('docs/SOURCES.md', encoding='utf-8').read()
ids = sorted(set(re.findall(r'S-ch\d\d-\d\d', t)))
missing = [i for i in ids if i not in src]
body_ids = sorted(set(re.findall(r'S-ch\d\d-\d\d', body)))
list_ids = sorted(set(re.findall(r'S-ch\d\d-\d\d', t[len(body):])))
boxes = ['מאחורי הקלעים', 'רגע של מחשבה', 'במעבדה', 'מושג שכדאי להכיר', 'מיתוס מול מציאות']
box_counts = {}
for b in boxes:
    o = len(re.findall(r'\[' + b + r'(?::[^\]]*)?\]', t)); c = t.count('[/' + b + ']')
    box_counts[b] = (o, c)
old_boxes = [b for b in ['מושג חשוב', 'שאלת מחשבה'] if '[' + b in t]
illus = re.findall(r'\[איור [^\]]*\]', t)
pending = re.findall(r'\[ממתין ל-M4[^\]]*\]', t)
lines = t.splitlines()
first = lines[0] if lines else ''
latin = []
for para in body.split('\n'):
    for m in re.finditer(r'(?:^|(?<=[.!?:])\s+)([A-Za-z][A-Za-z\-]+)', para.strip()):
        latin.append(m.group(1))
pct = re.findall(r'\d+(?:[.,]\d+)?\s*%', body)
print(f'file={path} md5={hashlib.md5(t.encode()).hexdigest()[:8]}')
print(f'words_clean={words} raw={raw}')
print(f'first_line={first[:60]!r}')
print(f'ids_all={ids} missing_in_SOURCES={missing}')
print(f'cited_in_body_not_in_list={[i for i in body_ids if i not in list_ids]} listed_not_cited={[i for i in list_ids if i not in body_ids]}')
print('boxes(open,close)=', {k: v for k, v in box_counts.items() if v != (0, 0)}, 'unbalanced=', [k for k, v in box_counts.items() if v[0] != v[1]], 'old_markers=', old_boxes)
print(f'illustrations={len(illus)} pending_M4={len(pending)} insights_section={"## תובנות מרכזיות" in t}')
print(f'latin_sentence_starts(candidates)={latin} percents={pct}')
print('explicitly programmed present:', 'explicitly programmed' in t.lower())
