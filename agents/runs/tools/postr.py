"""After a reviewer run: gate + run log. Usage: python postr.py <n> <round> <usage_text> <decision_text>
Requires scratchpad raw_reviewer_ch0N_rR.txt."""
import sys, os, subprocess, hashlib, datetime, re
SP = os.path.dirname(os.path.abspath(__file__)) + "/"
n, r, usage, decision = sys.argv[1:5]
nn = f"0{n}"; u = f"ch{nn}"
rep = f"agents/runs/review_{u}_r{r}.md"
chap = f"chapters/chapter_{nn}.txt"; ver = f"agents/runs/versions/chapter_{nn}_r{r}.txt"
md5 = lambda p: hashlib.md5(open(p, 'rb').read()).hexdigest()[:8]
ok_same = md5(chap) == md5(ver)
lines = open(rep, encoding='utf-8').read().rstrip().splitlines()
last = lines[-1].strip()
score = [l for l in lines if l.startswith('SCORE')]
st = subprocess.run(["git", "status", "--short"], capture_output=True, text=True, encoding="utf-8").stdout
task = f"agents/runs/tasks/reviewer_{u}_r{r}_prompt.txt"
now = datetime.datetime.now().strftime("%H:%M")
raw = open(SP + f"raw_reviewer_{u}_r{r}.txt", encoding="utf-8").read()
log = f"""# הרצה: reviewer-agent, יחידה {u}, סבב {r} (M3)

| שדה | ערך |
|---|---|
| תאריך | 2026-11-17 |
| סוכן | `reviewer-agent` |
| הופעל על ידי | Orchestrator |
| שימוש | {usage} |
| דוח שהסוכן כתב | `{rep}` |
| קלט שנבדק | `{ver}` (MD5 {md5(ver)}) |

## הפרומפט המלא שנשלח
ההפעלה הפנתה לקובץ המשימה `{task}`. זה התוכן המלא שלו:

```
{open(task, encoding='utf-8').read().rstrip()}
```

## הפלט הגולמי שהסוכן החזיר (כלשונו)

```
{raw.rstrip()}
```

## שער האיכות של ה-Orchestrator ({now})
- הפרק {'לא השתנה בזמן הביקורת (MD5 זהה לעותק)' if ok_same else '**השתנה**: MD5 שונה מהעותק. לבדיקה'}.
- השורה האחרונה בדוח: `{last}`. {score[0] if score else 'לא נמצאה שורת SCORE'}.
- `git status --short` (יש סוכנים אחרים שרצים במקביל):
```
{st.rstrip()}
```
- **החלטה:** {decision}
"""
open(f"agents/runs/reviewer_{u}_r{r}.md", "w", encoding="utf-8").write(log)
print(u, r, 'same' if ok_same else 'CHANGED', last, score)
