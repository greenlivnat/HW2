# הרצה: writer-agent, יחידה ch05, סבב 1 (M3)

| שדה | ערך |
|---|---|
| תאריך | 2026-11-17 |
| סוכן | `writer-agent` |
| הופעל על ידי | Orchestrator (במקביל לפרקים 2–7) |
| שער האיכות | 21:28 |
| שימוש | 13 קריאות לכלים, 85,953 טוקנים, 172.7 שניות |
| קובץ פלט | `chapters/chapter_05.txt` (עותק: `agents/runs/versions/chapter_05_r1.txt`) |

## הפרומפט המלא שנשלח
ההפעלה (Agent tool) הפנתה לקובץ המשימה. התוכן המלא שלו מופיע כאן.

```
M3 WRITING, unit ch05, round 1. Your complete task specification (prepared by the Orchestrator) is in the file agents/runs/tasks/writer_ch05_r1_prompt.txt. Read it first and follow it exactly ...
```

### תוכן קובץ המשימה `agents/runs/tasks/writer_ch05_r1_prompt.txt`
```
M3 WRITING, unit ch05, round 1.

Read first (in order):
1. agents/writer_agent.md (role spec).
2. docs/STYLE_GUIDE.md — BINDING: literary voice, scientific-integrity rules, the dough-story arc (§3, row for chapter 5), the five content boxes and their markers (§4), illustration/formula/table/placeholder markers (§5), palette (§6), length (§7).
3. docs/PRD.md v1.4 §4, §5 (chapter 5), §6, §10; docs/OUTLINE.md.
4. chapters/chapter_01.txt — APPROVED by the user; it defines the voice and the story's starting point. Read it for continuity; do NOT repeat its content, analogies or examples (matryoshka, recipe vs. cook, mixing console are taken).
5. docs/SOURCES.md (§1, §3.5, §3.8, §4) and the full records in docs/sources/chapter_05.md. Cross-chapter records may be used only where SOURCES.md §4 explicitly links them to this chapter.

TASK: write chapter 5, "בודקים מודלים בעזרת נתונים", into chapters/chapter_05.txt (overwrite the skeleton). Write ONLY that file; no .tex.

Content (PRD §5): the difference between accuracy, error rate and evaluating results; training vs. test performance; a summary table; why one must not conclude from a chart more than the data supports; the book's own experiment on UCI Digits.

Story (STYLE_GUIDE §3): the reader asks: how do we know the answer is good? We test on data the system has not seen. Link back to chapter 1's handwritten digits (85% of US handwritten mail sorted automatically, as of 2006, S-ch01-03 — only if SOURCES.md links it; otherwise refer to 'as described in chapter 1' without re-citing) — now the book runs its own small experiment on handwritten digits. Close pointing to chapter 6: even a well-tested system has limits.

Boxes: 2–4 boxes chosen to fit the topic, using the exact markers in STYLE_GUIDE §4. Suggested for this chapter: במעבדה (the UCI Digits experiment: method now, results in M4); מושג שכדאי להכיר (accuracy and error rate); מיתוס מול מציאות (high training accuracy = a good model). No two boxes of the same type in a row; each box adds something the body doesn't say.

Visual: at least one original visualization to be generated in code in M4, as an [איור 5.N: ...] line in the exact STYLE_GUIDE §5 format (type, content, palette colours, data source). Required/suggested: REQUIRED: [איור 5.1 ...] a Matplotlib line chart of train vs. test accuracy per epoch from python/data/*.csv produced by python/generate_chart.py (Turquoise = train, Violet = test, Gold for a highlighted point), caption saying the numbers were computed in the book's experiment. Plus [טבלה 5.1 ...] with columns epoch | train accuracy | test accuracy — values filled in M4.

Length: 1,400–1,800 clean words of body text (excluding the source list). You cannot run Python; the Orchestrator will count. Stay inside the band — do not overshoot.

CHAPTER-SPECIFIC SOURCE RULES (binding; from docs/STATUS.md §4 and SOURCES.md gaps):
- NO EXPERIMENT RESULTS EXIST YET. Do not write any accuracy number, any curve shape, or claim that overfitting does/doesn't appear. Use placeholders exactly: [ממתין ל-M4: ...] for results, the chart, the table values and the numeric interpretation. Write the surrounding interpretation conditionally (what it would mean if train and test diverge, and what if they don't).
- Describe the planned method per PRD §5: UCI Optical Recognition of Handwritten Digits (Alpaydin & Kaynak 1998, DOI 10.24432/C50P49, CC BY 4.0), 1,797 examples, 64 features, 10 classes, loaded via sklearn.datasets.load_digits (S-ch05-04, S-ch05-05); fixed seed, fixed train/test split, accuracy per epoch, saved to CSV; no tuning toward a desired shape (state this honesty rule to the reader).
- Error rate has no source formula: present it as derived, 'שיעור השגיאה = 1 פחות הדיוק'.
- Sokolova & Lapalme (S-ch05-11) metadata only — at most 'further reading'.
- Never extract numbers 'by eye' from figures in sources; do not reproduce figures from Zhang et al. ROC/AUC not researched — don't cover.
- Google MLCC / scikit-learn pages: paraphrase, don't copy.

GENERAL RULES: cite only IDs that exist in docs/SOURCES.md, right after the claim, within each record's access level and listed supported claims; metadata-only records → bibliographic/historical mention only; no item from SOURCES.md §3.8; every number/date has an ID and its context (population, task, year); invented examples clearly framed as illustrations ("דמיינו", "לדוגמה", "מספרים להמחשה בלבד"); no facts about baking chemistry (the dough story is about the reader's experience with the system). If a claim needs a missing source, don't write it — list it under "Needs research".

Structure: first line "פרק 5 — בודקים מודלים בעזרת נתונים"; the opening question on its own line; "## " section headings; the boxes; the illustration line(s); "## תובנות מרכזיות" (4–6 bullets); "## מקורות לפרק" (cited IDs with short bibliographic info copied from SOURCES.md §5).

FINAL MESSAGE (SHORT, ≤ 300 words): file + rough word count; source IDs used (one line each, main claim); boxes used (type + title); illustration line(s) as written; Needs research; one line on how the dough story advances.
```

## הפלט הגולמי שהסוכן החזיר (כלשונו)

```
Chapter 5 (round 1) is written in C:\biu01\HW2\ai_book_starter\chapters\chapter_05.txt. It replaces the skeleton, and I touched no other file. I estimate about 1,500 clean words of body text, but I couldn't count with Python, so please check it against the 1,400–1,800 band. There are no experiment numbers, curve shapes or overfitting claims. Every result is a `[ממתין ל-M4: ...]` placeholder, and the reading of the graph is written conditionally.

**Source IDs used**
- S-ch05-01: definition of accuracy, and the 4-example case that gives 0.5.
- S-ch05-02: how to read train vs. test scores (underfitting and overfitting).
- S-ch05-04: load_digits has 1,797 examples, 8×8 = 64 features, values 0–16, 10 classes, and is a copy of the UCI test set.
- S-ch05-05: the UCI dataset itself (Alpaydin & Kaynak, 1998), CC BY 4.0, 5,620 examples.
- S-ch05-06: the accuracy formula, the 99% trap with a 1% class, and when to prefer other measures.
- S-ch05-07: the four outcomes of a spam filter (TP/FP/FN/TN).
- S-ch05-08: definitions of overfitting and generalization, and the loss-curve pattern.
- S-ch05-09: loss curves are often hard to interpret.
- S-ch05-10: random labels give 100.0% train vs. 9.78% test (Inception, CIFAR10, Table 1), and claims about early stopping need a separate test set.
- S-ch05-11: "further reading" only, no content claims.

**Boxes**
- מושג שכדאי להכיר: "דיוק ושיעור שגיאה". It links to the spam filter in chapter 1, includes a `[נוסחה]`, and gives error rate as 1 minus accuracy, presented as derived.
- מיתוס מול מציאות: high training accuracy means a good model.
- במעבדה: "איך נבנה הניסוי". It also states the honesty rule (no tuning toward a desired shape).

**Illustration and table lines**
- `[איור 5.1: דיוק אימון מול דיוק בדיקה לאורך תקופות האימון | סוג: גרף Matplotlib (גרף קווים) | ... | צבעים: אימון Turquoise #00C9C8, בדיקה Violet #7956D8, נקודה מודגשת Gold #E4B65C ... | מקור הנתונים: ניסוי M4, python/data/<קובץ>.csv ...]`
- `[טבלה 5.1 ...]` has the columns תקופה | דיוק אימון | דיוק בדיקה, with a placeholder for the values.

**Deviations from the task spec**
- I didn't repeat the 85% figure or cite S-ch01-03, because SOURCES.md §4 doesn't link it to chapter 5. The text just says "בפרק 1 פגשנו...".
- In one placeholder (model type, split ratio, seed, number of epochs) I pointed to python/generate_chart.py instead of a CSV, because those settings won't be in the CSV.

**Needs research**
- There is no source defining an epoch. It is explained in one plain sentence.
- The point that a single split or seed only describes that split is the book's own reasoning, not a sourced claim.

**Dough story:** the reader moves from reading the answer to asking how it was checked. The book then runs its own handwritten-digit experiment, and the chapter ends by pointing to chapter 6: even a well-tested system makes mistakes.
```

## שער האיכות של ה-Orchestrator (21:28)
פלט סקריפט השער:
```
file=chapters/chapter_05.txt md5=504009c4
words_clean=1187 raw=1401
first_line='פרק 5 — בודקים מודלים בעזרת נתונים'
ids_all=['S-ch05-01', 'S-ch05-02', 'S-ch05-04', 'S-ch05-05', 'S-ch05-06', 'S-ch05-07', 'S-ch05-08', 'S-ch05-09', 'S-ch05-10', 'S-ch05-11'] missing_in_SOURCES=[]
cited_in_body_not_in_list=[] listed_not_cited=[]
boxes(open,close)= {'במעבדה': (1, 1), 'מושג שכדאי להכיר': (1, 1), 'מיתוס מול מציאות': (1, 1)} unbalanced= [] old_markers= []
illustrations=1 pending_M4=4 insights_section=True
latin_sentence_starts(candidates)=['Optical'] percents=['99%', '100.0%', '9.78%', '99%']
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
?? agents/runs/versions/chapter_05_r1.txt
?? agents/runs/writer_ch05_r1.md
```
