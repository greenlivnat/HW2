"""After a writer run: gate + snapshot + run log. Usage: python postw.py <n> <round> [usage_text]
Requires scratchpad raw_writer_ch0N_rR.txt and agents/runs/tasks/writer_ch0N_rR_prompt.txt (or scratchpad prompt)."""
import sys, os, subprocess, shutil, datetime
SP = os.path.dirname(os.path.abspath(__file__)) + "/"
n, r = sys.argv[1], sys.argv[2]
usage = sys.argv[3] if len(sys.argv) > 3 else "לא נמסר בעת כתיבת הקובץ"
nn = f"0{n}"; u = f"ch{nn}"
chap = f"chapters/chapter_{nn}.txt"
g = subprocess.run([sys.executable, SP + "gate.py", chap], capture_output=True, text=True, encoding="utf-8", env={**os.environ, "PYTHONIOENCODING": "utf-8"}).stdout
st = subprocess.run(["git", "status", "--short"], capture_output=True, text=True, encoding="utf-8").stdout
os.makedirs("agents/runs/versions", exist_ok=True)
shutil.copy(chap, f"agents/runs/versions/chapter_{nn}_r{r}.txt")
task = f"agents/runs/tasks/writer_{u}_r{r}_prompt.txt"
inv = f"M3 {'WRITING' if r == '1' else 'REVISION'}, unit {u}, round {r}. Your complete task specification (prepared by the Orchestrator) is in the file {task}. Read it first and follow it exactly ..."
now = datetime.datetime.now().strftime("%H:%M")
raw = open(SP + f"raw_writer_{u}_r{r}.txt", encoding="utf-8").read()
taskt = open(task, encoding="utf-8").read()
log = f"""# הרצה: writer-agent, יחידה {u}, סבב {r} (M3)

| שדה | ערך |
|---|---|
| תאריך | 2026-11-17 |
| סוכן | `writer-agent` |
| הופעל על ידי | Orchestrator{' (במקביל לפרקים 2–7)' if r == '1' else ''} |
| שער האיכות | {now} |
| שימוש | {usage} |
| קובץ פלט | `{chap}` (עותק: `agents/runs/versions/chapter_{nn}_r{r}.txt`) |

## הפרומפט המלא שנשלח
ההפעלה (Agent tool) הפנתה לקובץ המשימה. התוכן המלא שלו מופיע כאן.

```
{inv}
```

### תוכן קובץ המשימה `{task}`
```
{taskt.rstrip()}
```

## הפלט הגולמי שהסוכן החזיר (כלשונו)

```
{raw.rstrip()}
```

## שער האיכות של ה-Orchestrator ({now})
פלט סקריפט השער:
```
{g.rstrip()}
```
`git status --short` בזמן השער (ייתכן ששינויים בפרקים אחרים שייכים לסוכנים שרצים במקביל):
```
{st.rstrip()}
```
"""
open(f"agents/runs/writer_{u}_r{r}.md", "w", encoding="utf-8").write(log)
print(g)
