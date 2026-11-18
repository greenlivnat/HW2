"""Writer revision task. Usage: python mkfix.py <n> <round> <orchestrator_notes>"""
import sys
n, r, notes = sys.argv[1], int(sys.argv[2]), sys.argv[3]
nn = f"0{n}"; u = f"ch{nn}"
T = f"""M3 REVISION, unit {u}, round {r}.

Read first: agents/writer_agent.md; docs/STYLE_GUIDE.md (binding); the review report agents/runs/review_{u}_r{r-1}.md; your original task file agents/runs/tasks/writer_{u}_r1_prompt.txt (ALL its chapter-specific source rules remain binding); the current chapters/chapter_{nn}.txt (a frozen copy of the reviewed version is agents/runs/versions/chapter_{nn}_r{r-1}.txt — do not touch it); docs/SOURCES.md and docs/sources/chapter_{nn}.md for every source check.

TASK: revise chapters/chapter_{nn}.txt to fix EVERY defect in the report (critical, medium AND minor). Write ONLY that file.

Orchestrator notes (routing and constraints): {notes}

Rules: cite only IDs in SOURCES.md, within access level; no new factual claim without an existing record — if a fix would need a new source, do not write the claim and say so; keep the dough story, voice, boxes (STYLE_GUIDE §4) and illustration lines; stay inside the STYLE_GUIDE §7 length band (the Orchestrator counts with Python — you cannot, so when adding text, also say where you cut).

FINAL MESSAGE (SHORT, ≤ 250 words): table defect ID → what was changed (or why not) for EVERY defect; source ID changes; rough word count change (+/−).
"""
open(f"agents/runs/tasks/writer_{u}_r{r}_prompt.txt", "w", encoding="utf-8").write(T)
print("ok", u, r)
