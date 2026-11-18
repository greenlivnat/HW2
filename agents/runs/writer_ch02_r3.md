# הרצה: writer-agent, יחידה ch02, סבב 3 (M3)

| שדה | ערך |
|---|---|
| תאריך | 2026-11-17 |
| סוכן | `writer-agent` |
| הופעל על ידי | Orchestrator |
| שער האיכות | 12:31 |
| שימוש | לא נמסר בעת כתיבת הקובץ |
| קובץ פלט | `chapters/chapter_02.txt` (עותק: `agents/runs/versions/chapter_02_r3.txt`) |

## הפרומפט המלא שנשלח
ההפעלה (Agent tool) הפנתה לקובץ המשימה. התוכן המלא שלו מופיע כאן.

```
M3 REVISION, unit ch02, round 3. Your complete task specification (prepared by the Orchestrator) is in the file agents/runs/tasks/writer_ch02_r3_prompt.txt. Read it first and follow it exactly ...
```

### תוכן קובץ המשימה `agents/runs/tasks/writer_ch02_r3_prompt.txt`
```
M3 REVISION, unit ch02, round 3.

Read first: agents/writer_agent.md; docs/STYLE_GUIDE.md (binding); the review report agents/runs/review_ch02_r2.md; your original task file agents/runs/tasks/writer_ch02_r1_prompt.txt (ALL its chapter-specific source rules remain binding); the current chapters/chapter_02.txt (a frozen copy of the reviewed version is agents/runs/versions/chapter_02_r2.txt — do not touch it); docs/SOURCES.md and docs/sources/chapter_02.md for every source check.

TASK: revise chapters/chapter_02.txt to fix EVERY defect in the report (critical, medium AND minor). Write ONLY that file.

Orchestrator notes (routing and constraints): FINAL allowed round. R-ch02-10 (medium): REMOVE the '4.4% ב-Adience' figure and do not use any Adience/IJB-A dark-skinned-women percentage (it is being corrected in the record by the research agent in parallel). If you keep the composition point, use only figures already verified in S-ch02-01 and accepted by the reviewer (e.g., PPB 53.6%/46.4% vs. 86.2% lighter-skinned in Adience — check the record), or drop the comparison. Also fix the implication: PPB is a TEST benchmark; its composition revealed the gap, it did not fix bias. R-ch02-09 closes with this fix. Do not touch docs/. Keep 1,400–1,800.

Rules: cite only IDs in SOURCES.md, within access level; no new factual claim without an existing record — if a fix would need a new source, do not write the claim and say so; keep the dough story, voice, boxes (STYLE_GUIDE §4) and illustration lines; stay inside the STYLE_GUIDE §7 length band (the Orchestrator counts with Python — you cannot, so when adding text, also say where you cut).

FINAL MESSAGE (SHORT, ≤ 250 words): table defect ID → what was changed (or why not) for EVERY defect; source ID changes; rough word count change (+/−).
```

## הפלט הגולמי שהסוכן החזיר (כלשונו)

```
I revised C:\biu01\HW2\ai_book_starter\chapters\chapter_02.txt (round 3), and that is the only file I wrote. The fix is one sentence in the myth-vs-reality box (around line 71). I did not change the dough story, the voice, the three boxes, the figure 2.1 line, the key-takeaways section or the sources list.

| Defect | What changed |
|---|---|
| R-ch02-10 (medium) | I removed "21.3% ב-PPB לעומת 4.4% בלבד ב-Adience" and did not use any dark-skinned-women percentage for Adience or IJB-A. The new sentence uses only the PPB split already in the S-ch02-01 record (claim 3): "ב-Gender Shades, מה שחשף את הפער היה הרכב ולא גודל: מאגר הבדיקה PPB בנוי כמעט מאוזן, 53.6% בהירי עור ו-46.4% כהי עור [S-ch02-01]. הוא לא תיקן אף מסווג, אבל רק בעזרתו אפשר היה לראות היכן הם נכשלים." The box now names PPB as a test benchmark that exposed the gap and says it did not fix bias. I left out the Adience 86.2% comparison because the chapter body already gives it. |
| R-ch02-09 (minor, partial) | Closed by the same fix. The box adds something new (the PPB split and that a test set reveals but does not fix bias) and no longer repeats the body. The sentence implying PPB fixed bias is gone. |
| R-ch02-11 (minor, sources) | Not mine to fix: it goes to the research agent. I did not touch `docs/`, and the chapter no longer depends on the wrong figure. |

- **Source IDs:** no changes. The box still cites only S-ch02-01, S-ch02-14 and S-ch02-10, and no new factual claim was added.
- **Word count:** about +20 words (my estimate, since I can't count with Python). That puts the body near 1,580, inside 1,400–1,800, and the myth box near 103 words, inside 40–120. Nothing was cut because no cut was needed.
- **Needs research:** none.
```

## שער האיכות של ה-Orchestrator (12:31)
פלט סקריפט השער:
```
file=chapters/chapter_02.txt md5=2d4c7614
words_clean=1579 raw=1752
first_line='פרק 2 — מנתונים ללמידה'
ids_all=['S-ch02-01', 'S-ch02-03', 'S-ch02-04', 'S-ch02-06', 'S-ch02-08', 'S-ch02-09', 'S-ch02-10', 'S-ch02-11', 'S-ch02-12', 'S-ch02-13', 'S-ch02-14'] missing_in_SOURCES=[]
cited_in_body_not_in_list=[] listed_not_cited=[]
boxes(open,close)= {'מאחורי הקלעים': (1, 1), 'רגע של מחשבה': (1, 1), 'מיתוס מול מציאות': (1, 1)} unbalanced= [] old_markers= []
illustrations=1 pending_M4=0 insights_section=True
latin_sentence_starts(candidates)=[] percents=['70%', '15%', '79.6%', '86.2%', '20.8%', '34.7%', '0.0%', '0.8%', '21.3%', '61.0%', '72.4%', '53.6%', '46.4%']
explicitly programmed present: False
```
`git status --short` בזמן השער (ייתכן ששינויים בפרקים אחרים שייכים לסוכנים שרצים במקביל):
```
 M chapters/chapter_02.txt
 M chapters/chapter_06.txt
 M docs/STATUS.md
?? agents/runs/review_ch02_r1.md
?? agents/runs/review_ch02_r2.md
?? agents/runs/review_ch06_r1.md
?? agents/runs/reviewer_ch02_r1.md
?? agents/runs/reviewer_ch02_r2.md
?? agents/runs/reviewer_ch06_r1.md
?? agents/runs/tasks/research_ch02_r2_prompt.txt
?? agents/runs/tasks/reviewer_ch02_r1_prompt.txt
?? agents/runs/tasks/reviewer_ch02_r2_prompt.txt
?? agents/runs/tasks/reviewer_ch06_r1_prompt.txt
?? agents/runs/tasks/reviewer_ch06_r2_prompt.txt
?? agents/runs/tasks/writer_ch02_r2_prompt.txt
?? agents/runs/tasks/writer_ch02_r3_prompt.txt
?? agents/runs/tasks/writer_ch06_r2_prompt.txt
?? agents/runs/tools/
?? agents/runs/versions/chapter_02_r1.txt
?? agents/runs/versions/chapter_02_r2.txt
?? agents/runs/versions/chapter_06_r1.txt
?? agents/runs/versions/chapter_06_r2.txt
?? agents/runs/writer_ch02_r1.md
?? agents/runs/writer_ch02_r2.md
?? agents/runs/writer_ch06_r1.md
?? agents/runs/writer_ch06_r2.md
```
