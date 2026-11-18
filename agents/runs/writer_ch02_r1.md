# הרצה: writer-agent, יחידה ch02, סבב 1 (M3)

| שדה | ערך |
|---|---|
| תאריך | 2026-11-17 |
| סוכן | `writer-agent` |
| הופעל על ידי | Orchestrator (במקביל לפרקים 2–7) |
| שער האיכות | 21:30 |
| שימוש | 19 קריאות לכלים, 98,004 טוקנים, 272.4 שניות |
| קובץ פלט | `chapters/chapter_02.txt` (עותק: `agents/runs/versions/chapter_02_r1.txt`) |

## הפרומפט המלא שנשלח
ההפעלה (Agent tool) הפנתה לקובץ המשימה. התוכן המלא שלו מופיע כאן.

```
M3 WRITING, unit ch02, round 1. Your complete task specification (prepared by the Orchestrator) is in the file agents/runs/tasks/writer_ch02_r1_prompt.txt. Read it first and follow it exactly ...
```

### תוכן קובץ המשימה `agents/runs/tasks/writer_ch02_r1_prompt.txt`
```
M3 WRITING, unit ch02, round 1.

Read first (in order):
1. agents/writer_agent.md (role spec).
2. docs/STYLE_GUIDE.md — BINDING: literary voice, scientific-integrity rules, the dough-story arc (§3, row for chapter 2), the five content boxes and their markers (§4), illustration/formula/table/placeholder markers (§5), palette (§6), length (§7).
3. docs/PRD.md v1.4 §4, §5 (chapter 2), §6, §10; docs/OUTLINE.md.
4. chapters/chapter_01.txt — APPROVED by the user; it defines the voice and the story's starting point. Read it for continuity; do NOT repeat its content, analogies or examples (matryoshka, recipe vs. cook, mixing console are taken).
5. docs/SOURCES.md (§1, §3.2, §3.8, §4) and the full records in docs/sources/chapter_02.md. Cross-chapter records may be used only where SOURCES.md §4 explicitly links them to this chapter.

TASK: write chapter 2, "מנתונים ללמידה", into chapters/chapter_02.txt (overwrite the skeleton). Write ONLY that file; no .tex.

Content (PRD §5): collecting and cleaning data; training, validation and test sets; labels; bias in data; generalization; data leakage; one continuous example story.

Story (STYLE_GUIDE §3): time 'rewinds': long before the reader typed her question, the system had already learned from many examples. The reader recalls how she herself learned to bake from experience (illustration only). Close by pointing to chapter 3: how do those examples turn into numbers inside the machine?

Boxes: 2–4 boxes chosen to fit the topic, using the exact markers in STYLE_GUIDE §4. Suggested for this chapter: מאחורי הקלעים (the train/validation/test split); מיתוס מול מציאות (more data does not automatically mean less bias); רגע של מחשבה. No two boxes of the same type in a row; each box adds something the body doesn't say.

Visual: at least one original visualization to be generated in code in M4, as an [איור 2.N: ...] line in the exact STYLE_GUIDE §5 format (type, content, palette colours, data source). Required/suggested: a data-flow diagram (TikZ): raw examples → labeling → cleaning → split into train / validation / test → training → evaluation, with the test set visibly 'locked' until the end; palette per STYLE_GUIDE §6.

Length: 1,400–1,800 clean words of body text (excluding the source list). You cannot run Python; the Orchestrator will count. Stay inside the band — do not overshoot.

CHAPTER-SPECIFIC SOURCE RULES (binding; from docs/STATUS.md §4 and SOURCES.md gaps):
- Do not describe details of the leakage cases in the INFORMS 2010 / IJCNN 2011 competitions (abstract-level mention only, if at all). Kaufman et al. at abstract level only.
- The leakage example in S-ch02-08 is synthetic — say so if used. No real leakage case with numbers.
- LFW demographic figures (77.5% / 83.5%) are a secondary citation — do NOT use.
- Datasheets: only pages actually read. No academic definition of 'data cleaning' was found — describe it plainly without attributing a definition.
- Gender Shades (S-ch02-01) is this chapter's main bias source; keep to its record's claims and caveats.
- Google MLCC pages have no update dates; cite them without dates.

GENERAL RULES: cite only IDs that exist in docs/SOURCES.md, right after the claim, within each record's access level and listed supported claims; metadata-only records → bibliographic/historical mention only; no item from SOURCES.md §3.8; every number/date has an ID and its context (population, task, year); invented examples clearly framed as illustrations ("דמיינו", "לדוגמה", "מספרים להמחשה בלבד"); no facts about baking chemistry (the dough story is about the reader's experience with the system). If a claim needs a missing source, don't write it — list it under "Needs research".

Structure: first line "פרק 2 — מנתונים ללמידה"; the opening question on its own line; "## " section headings; the boxes; the illustration line(s); "## תובנות מרכזיות" (4–6 bullets); "## מקורות לפרק" (cited IDs with short bibliographic info copied from SOURCES.md §5).

FINAL MESSAGE (SHORT, ≤ 300 words): file + rough word count; source IDs used (one line each, main claim); boxes used (type + title); illustration line(s) as written; Needs research; one line on how the dough story advances.
```

## הפלט הגולמי שהסוכן החזיר (כלשונו)

```
I wrote chapter 2 into C:\biu01\HW2\ai_book_starter\chapters\chapter_02.txt, replacing the skeleton. My rough hand estimate is about 1,650–1,750 clean words, which should be inside the 1,400–1,800 band. I could not run a count, so it needs your Python check. No other file was touched and there is no .tex.

**Sources used:**
- S-ch02-01: Gender Shades. Benchmarks 79.6% / 86.2% light-skinned; PPB of 1,270 people; labeling process and the binary-gender caveat; error rates 20.8–34.7% vs 0.0–0.8%; 21.3% of PPB vs 61.0–72.4% of errors. The training-data cause is stated as the authors' hypothesis, and the companies did not disclose their training data.
- S-ch02-03: no standard way to document datasets; the datasheet proposal.
- S-ch02-04: datasets shape model behaviour and deployment mismatch; models may reproduce or amplify bias; datasheet questions on collection, composition and processing.
- S-ch02-06: abstract level only. Leakage as a major mistake, and learn-predict separation. The competitions are not mentioned at all.
- S-ch02-08: definition of leakage; the 0.76 vs 0.5 demo, marked as synthetic; split before preprocessing; never fit on test data.
- S-ch02-09: train/validation/test roles; tuning on the test set leaks; cost of a three-way split; k-fold; a perfect score from repeating labels.
- S-ch02-10: the three-way split; 70/15/15 as an example only; the test set wears out; no duplicates in the test set and it must be representative.
- S-ch02-11: overfitting, generalization and its conditions.
- S-ch02-12: human raters and disagreement; proxy labels.
- S-ch02-13: unreliable data types; the noise can never be fully removed.
- S-ch02-14: selection and historical bias.

**Boxes:**
- מאחורי הקלעים: "שלוש ערימות, אחת נעולה"
- מיתוס מול מציאות: more data does not remove bias
- רגע של מחשבה: which datasheet question you would want answered first for the reader's system

**Illustration:** [איור 2.1: מסלול הדוגמאות, מהאיסוף ועד הבדיקה | סוג: תרשים TikZ | תוכן: זרימה מימין לשמאל: דוגמאות גולמיות ← תיוג ← ניקוי ← חלוקה לאימון, אימות ובדיקה ← אימון ← כיוונון מול האימות ← בדיקה סופית חד-פעמית. קבוצת הבדיקה מאחורי "חומה" עם מנעול, ויוצא ממנה חץ אחד בלבד, בסוף. חץ מקווקו "זליגה" חוצה את החומה ומסמן את הדרך האסורה | צבעים: תיבות וחצים Turquoise ‏#00C9C8, טקסט, קבוצת הבדיקה והחומה Midnight Blue ‏#101B35, מנעול Gold ‏#E4B65C, חץ הזליגה Violet ‏#7956D8, רקע Paper White ‏#F5F7FA | מקור הנתונים: מסגרת הספר, על בסיס S-ch02-08, ‏S-ch02-09 ו-S-ch02-10 (תרשים מושגי, בלי נתונים)]

**Needs research:** Nothing is missing from the text. I deliberately left out:
- A real leakage case with numbers.
- Any claim about what data the reader's actual chat system was trained on.
- A formal definition of data cleaning; cleaning is described in plain words with no attributed definition.

**Dough story:** time rewinds to before the question. The reader remembers learning to bake from many tries, all in one kitchen. A made-up team builds a "risen / not risen" photo classifier and runs into cleaning, labeling, leakage and the "notebook written in one kitchen" bias. The chapter returns to the waiting screen and points to chapter 3: how examples become numbers.
```

## שער האיכות של ה-Orchestrator (21:30)
פלט סקריפט השער:
```
file=chapters/chapter_02.txt md5=957ee2f9
words_clean=1535 raw=1708
first_line='פרק 2 — מנתונים ללמידה'
ids_all=['S-ch02-01', 'S-ch02-03', 'S-ch02-04', 'S-ch02-06', 'S-ch02-08', 'S-ch02-09', 'S-ch02-10', 'S-ch02-11', 'S-ch02-12', 'S-ch02-13', 'S-ch02-14'] missing_in_SOURCES=[]
cited_in_body_not_in_list=[] listed_not_cited=[]
boxes(open,close)= {'מאחורי הקלעים': (1, 1), 'רגע של מחשבה': (1, 1), 'מיתוס מול מציאות': (1, 1)} unbalanced= [] old_markers= []
illustrations=1 pending_M4=0 insights_section=True
latin_sentence_starts(candidates)=[] percents=['70%', '15%', '79.6%', '86.2%', '20.8%', '34.7%', '0.0%', '0.8%', '21.3%', '61.0%', '72.4%']
explicitly programmed present: False
```
`git status --short` בזמן השער (ייתכן ששינויים בפרקים אחרים שייכים לסוכנים שרצים במקביל):
```
 M chapters/chapter_02.txt
 M chapters/chapter_03.txt
 M chapters/chapter_04.txt
 M chapters/chapter_05.txt
 M chapters/chapter_06.txt
 M chapters/chapter_07.txt
?? agents/runs/tasks/reviewer_ch03_r1_prompt.txt
?? agents/runs/tasks/reviewer_ch04_r1_prompt.txt
?? agents/runs/tasks/reviewer_ch05_r1_prompt.txt
?? agents/runs/tasks/reviewer_ch06_r1_prompt.txt
?? agents/runs/tasks/reviewer_ch07_r1_prompt.txt
?? agents/runs/versions/chapter_03_r1.txt
?? agents/runs/versions/chapter_04_r1.txt
?? agents/runs/versions/chapter_05_r1.txt
?? agents/runs/versions/chapter_06_r1.txt
?? agents/runs/versions/chapter_07_r1.txt
?? agents/runs/writer_ch03_r1.md
?? agents/runs/writer_ch04_r1.md
?? agents/runs/writer_ch05_r1.md
?? agents/runs/writer_ch06_r1.md
?? agents/runs/writer_ch07_r1.md
```
