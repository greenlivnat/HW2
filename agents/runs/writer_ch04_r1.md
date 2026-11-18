# הרצה: writer-agent, יחידה ch04, סבב 1 (M3)

| שדה | ערך |
|---|---|
| תאריך | 2026-11-17 |
| סוכן | `writer-agent` |
| הופעל על ידי | Orchestrator (במקביל לפרקים 2–7) |
| שער האיכות | 21:30 |
| שימוש | 22 קריאות לכלים, 85,007 טוקנים, 236.3 שניות |
| קובץ פלט | `chapters/chapter_04.txt` (עותק: `agents/runs/versions/chapter_04_r1.txt`) |

## הפרומפט המלא שנשלח
ההפעלה (Agent tool) הפנתה לקובץ המשימה. התוכן המלא שלו מופיע כאן.

```
M3 WRITING, unit ch04, round 1. Your complete task specification (prepared by the Orchestrator) is in the file agents/runs/tasks/writer_ch04_r1_prompt.txt. Read it first and follow it exactly ...
```

### תוכן קובץ המשימה `agents/runs/tasks/writer_ch04_r1_prompt.txt`
```
M3 WRITING, unit ch04, round 1.

Read first (in order):
1. agents/writer_agent.md (role spec).
2. docs/STYLE_GUIDE.md — BINDING: literary voice, scientific-integrity rules, the dough-story arc (§3, row for chapter 4), the five content boxes and their markers (§4), illustration/formula/table/placeholder markers (§5), palette (§6), length (§7).
3. docs/PRD.md v1.4 §4, §5 (chapter 4), §6, §10; docs/OUTLINE.md.
4. chapters/chapter_01.txt — APPROVED by the user; it defines the voice and the story's starting point. Read it for continuity; do NOT repeat its content, analogies or examples (matryoshka, recipe vs. cook, mixing console are taken).
5. docs/SOURCES.md (§1, §3.4, §3.8, §4) and the full records in docs/sources/chapter_04.md. Cross-chapter records may be used only where SOURCES.md §4 explicitly links them to this chapter.

TASK: write chapter 4, "כיצד מודל שפה מייצר תשובה", into chapters/chapter_04.txt (overwrite the skeleton). Write ONLY that file; no .tex.

Content (PRD §5): tokens; numeric representations (embeddings); attention; predicting the next token; choosing from probabilities (sampling, temperature); the 9-block process diagram with a loop and a discussion of how simplified it is.

Story (STYLE_GUIDE §3): the answer is built word by word; slow the scene down until each chosen token is visible on the reader's screen (her question: 'למה הבצק שלי לא תופח, ומה אפשר לעשות עכשיו?'). Any example token split or probabilities shown are 'להמחשה בלבד'. Close pointing to chapter 5: how do we know whether such an answer is any good?

Boxes: 2–4 boxes chosen to fit the topic, using the exact markers in STYLE_GUIDE §4. Suggested for this chapter: מאחורי הקלעים (the loop: token after token); מושג שכדאי להכיר (token); רגע של מחשבה. No two boxes of the same type in a row; each box adds something the body doesn't say.

Visual: at least one original visualization to be generated in code in M4, as an [איור 4.N: ...] line in the exact STYLE_GUIDE §5 format (type, content, palette colours, data source). Required/suggested: REQUIRED: the 9-block TikZ diagram exactly as in docs/OUTLINE.md: שאלת משתמש → קבלת הטקסט → פירוק לטוקנים → ייצוג מספרי → עיבוד קשב → חישוב ציוני טוקנים → המרה להסתברויות → בחירת טוקן → הרכבת תשובה, with a loop arrow from 'בחירת טוקן' back to 'פירוק לטוקנים/ייצוג מספרי'. Optionally a second small bar-chart idea of illustrative next-token probabilities (clearly marked as illustrative, not model output).

Length: 1,400–1,800 clean words of body text (excluding the source list). You cannot run Python; the Orchestrator will count. Stay inside the band — do not overshoot.

CHAPTER-SPECIFIC SOURCE RULES (binding; from docs/STATUS.md §4 and SOURCES.md gaps):
- Block 2 is 'קבלת הטקסט', NOT 'ניקוי קלט' (S-ch04-04: GPT-2 avoids lossy preprocessing such as lower-casing).
- Do NOT describe commercial chatbot layers (system prompts, RLHF, safety filters) — no source.
- No Hebrew tokenization numbers; no sizes of current models beyond GPT-2/GPT-3 as recorded.
- Do not present Vaswani et al. Figure 1 as a description of a chatbot. Conference venues of GPT-3 / Vaswani not verified — don't state them.
- temperature/top_k/top_p: cover only from S-ch04-03. 'temperature' here means sampling; note it is not the calibration sense used later in chapter 6.
- State explicitly that the diagram is explanatory and simplified, not a full architecture.

GENERAL RULES: cite only IDs that exist in docs/SOURCES.md, right after the claim, within each record's access level and listed supported claims; metadata-only records → bibliographic/historical mention only; no item from SOURCES.md §3.8; every number/date has an ID and its context (population, task, year); invented examples clearly framed as illustrations ("דמיינו", "לדוגמה", "מספרים להמחשה בלבד"); no facts about baking chemistry (the dough story is about the reader's experience with the system). If a claim needs a missing source, don't write it — list it under "Needs research".

Structure: first line "פרק 4 — כיצד מודל שפה מייצר תשובה"; the opening question on its own line; "## " section headings; the boxes; the illustration line(s); "## תובנות מרכזיות" (4–6 bullets); "## מקורות לפרק" (cited IDs with short bibliographic info copied from SOURCES.md §5).

FINAL MESSAGE (SHORT, ≤ 300 words): file + rough word count; source IDs used (one line each, main claim); boxes used (type + title); illustration line(s) as written; Needs research; one line on how the dough story advances.
```

## הפלט הגולמי שהסוכן החזיר (כלשונו)

```
I wrote chapter 4 in C:\biu01\HW2\ai_book_starter\chapters\chapter_04.txt, replacing the skeleton. No other file was touched and there is no .tex. My rough estimate is 1,700–1,780 body words, but I could not run Python, so please count it. If it comes out over 1,800, the illustration lines and the "תשעה צעדים" section are the easiest places to cut.

**Source IDs used**
- S-ch04-01: attention (query, key, value, weighted sum); 8 heads; masking; learned embeddings with d_model=512 (2017); linear layer plus softmax giving next-token probabilities; the generator writes one token at a time and feeds it back in; the original was an encoder-decoder for translation with 6 stacked layers; positional encoding and other omitted parts.
- S-ch04-02: language as an open problem, with vocabularies of 30k–50k (2016); the BPE algorithm; "lower" split into low + er.
- S-ch04-03: the next-token breakdown of text probability; how much the decoding strategy changes quality; flat vs. peaked distributions ("hot"); the beam search failure modes; pure sampling producing gibberish; top-k, top-p and temperature.
- S-ch04-04: GPT-2 skips lossy preprocessing (the basis for block 2, קבלת הטקסט); byte-level BPE with 256 base symbols; context window of 1,024 tokens; 1.5B parameters; built on the Transformer with changes.
- S-ch04-05: words once treated as atomic units; word vectors; King − Man + Woman ≈ Queen, which the paper takes from earlier work.
- S-ch04-06: word vs. character vs. subword tokenization; vocabulary sizes of 40,478 for the first GPT and 50,257 for GPT-2, including the end-of-text token.
- S-ch04-07: what a decoding strategy is; greedy is the Hugging Face default and repeats itself in long text; beam search; sampling; the code loop.
- S-ch04-08: GPT-3 is autoregressive with 175B parameters (abstract level only).

**Boxes**
- [מושג שכדאי להכיר: טוקן (token)]
- [מאחורי הקלעים: הלולאה, טוקן אחר טוקן]
- [רגע של מחשבה]: the same question asked twice; does a lower temperature mean a more correct answer?

**Illustrations**
I numbered them in the order they appear, so the bar chart is 4.1 and the required 9-block diagram is 4.2.
- [איור 4.1: אותם ציונים, שתי טמפרטורות | סוג: גרף Matplotlib (עמודות) | …made-up scores, t=1 vs t=0.5, softmax with temperature from S-ch04-03 eq. 4; caption "נתוני הדגמה, לא פלט של מודל" …]
- [איור 4.2: מהשאלה אל התשובה, בתשעה צעדים | סוג: תרשים TikZ | the 9 blocks exactly as in OUTLINE, with a loop arrow from "בחירת טוקן" back to "פירוק לטוקנים"/"ייצוג מספרי"; caption "תרשים הסברתי ומפושט, לא ארכיטקטורה מלאה" …]

**Binding rules I followed**
- The body says plainly that the diagram is a simplified explanation, not a full architecture.
- Commercial chatbot layers get one sentence: the book does not deal with them.
- There are no Hebrew tokenization figures. The split of "תופח" is marked להמחשה בלבד.
- The temperature section points to the different meaning of the word in chapter 6.
- Venues are not given for Vaswani et al. or GPT-3.

**Needs research**
- Contextual embeddings: that attention makes word vectors depend on context comes from the researcher's note, not a listed supported claim. The chapter only says attention "mixes in" information from neighbouring words. This is backed by the weighted-sum claim in S-ch04-01.

**Dough story**
The scene is slowed down to the moment between "יש" and "כמה" in an example answer (labelled as an example, not real output), and each token is followed until it reaches the screen. The chapter ends with the fluent answer on screen and the reader's next question: how do we know it is good? That leads into chapter 5.
```

## שער האיכות של ה-Orchestrator (21:30)
פלט סקריפט השער:
```
file=chapters/chapter_04.txt md5=25b56d35
words_clean=1510 raw=1776
first_line='פרק 4 — כיצד מודל שפה מייצר תשובה'
ids_all=['S-ch04-01', 'S-ch04-02', 'S-ch04-03', 'S-ch04-04', 'S-ch04-05', 'S-ch04-06', 'S-ch04-07', 'S-ch04-08'] missing_in_SOURCES=[]
cited_in_body_not_in_list=[] listed_not_cited=[]
boxes(open,close)= {'מאחורי הקלעים': (1, 1), 'רגע של מחשבה': (1, 1), 'מושג שכדאי להכיר': (1, 1)} unbalanced= [] old_markers= []
illustrations=2 pending_M4=0 insights_section=True
latin_sentence_starts(candidates)=['GPT-'] percents=[]
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
?? agents/runs/tasks/reviewer_ch05_r1_prompt.txt
?? agents/runs/versions/chapter_03_r1.txt
?? agents/runs/versions/chapter_05_r1.txt
?? agents/runs/versions/chapter_06_r1.txt
?? agents/runs/versions/chapter_07_r1.txt
?? agents/runs/writer_ch03_r1.md
?? agents/runs/writer_ch05_r1.md
?? agents/runs/writer_ch06_r1.md
?? agents/runs/writer_ch07_r1.md
```
