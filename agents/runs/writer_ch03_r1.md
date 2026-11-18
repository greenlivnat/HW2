# הרצה: writer-agent, יחידה ch03, סבב 1 (M3)

| שדה | ערך |
|---|---|
| תאריך | 2026-11-17 |
| סוכן | `writer-agent` |
| הופעל על ידי | Orchestrator (במקביל לפרקים 2–7) |
| שער האיכות | 21:29 |
| שימוש | 18 קריאות לכלים, 76,617 טוקנים, 219.6 שניות |
| קובץ פלט | `chapters/chapter_03.txt` (עותק: `agents/runs/versions/chapter_03_r1.txt`) |

## הפרומפט המלא שנשלח
ההפעלה (Agent tool) הפנתה לקובץ המשימה. התוכן המלא שלו מופיע כאן.

```
M3 WRITING, unit ch03, round 1. Your complete task specification (prepared by the Orchestrator) is in the file agents/runs/tasks/writer_ch03_r1_prompt.txt. Read it first and follow it exactly ...
```

### תוכן קובץ המשימה `agents/runs/tasks/writer_ch03_r1_prompt.txt`
```
M3 WRITING, unit ch03, round 1.

Read first (in order):
1. agents/writer_agent.md (role spec).
2. docs/STYLE_GUIDE.md — BINDING: literary voice, scientific-integrity rules, the dough-story arc (§3, row for chapter 3), the five content boxes and their markers (§4), illustration/formula/table/placeholder markers (§5), palette (§6), length (§7).
3. docs/PRD.md v1.4 §4, §5 (chapter 3), §6, §10; docs/OUTLINE.md.
4. chapters/chapter_01.txt — APPROVED by the user; it defines the voice and the story's starting point. Read it for continuity; do NOT repeat its content, analogies or examples (matryoshka, recipe vs. cook, mixing console are taken).
5. docs/SOURCES.md (§1, §3.3, §3.8, §4) and the full records in docs/sources/chapter_03.md. Cross-chapter records may be used only where SOURCES.md §4 explicitly links them to this chapter.

TASK: write chapter 3, "הרשת הנוירונית מבפנים", into chapters/chapter_03.txt (overwrite the skeleton). Write ONLY that file; no .tex.

Content (PRD §5): the artificial neuron; weights and bias; layers; activation functions; the formula z = \sum_{i=1}^{n} w_i x_i + b with an explanation of every component; the limits of the brain analogy.

Story (STYLE_GUIDE §3): the reader's question has become numbers; inside the machine there is no 'dough', only weights. Use a small numeric neuron example tied (playfully) to the scene — numbers marked 'מספרים להמחשה בלבד'. Close pointing to chapter 4: how a whole language model turns these numbers into an answer.

Boxes: 2–4 boxes chosen to fit the topic, using the exact markers in STYLE_GUIDE §4. Suggested for this chapter: במעבדה (the formula z and a worked numeric example marked as illustration); מושג שכדאי להכיר (activation function); מיתוס מול מציאות (the network is a brain). No two boxes of the same type in a row; each box adds something the body doesn't say.

Visual: at least one original visualization to be generated in code in M4, as an [איור 3.N: ...] line in the exact STYLE_GUIDE §5 format (type, content, palette colours, data source). Required/suggested: REQUIRED: [נוסחה] z = \sum_{i=1}^{n} w_i x_i + b [/נוסחה] followed by an explanation of each symbol; then a = f(z) as a separate didactic step. Visual: a TikZ schematic of one neuron (inputs x1..xn, weights on arrows, summation node with b, activation f, output a) plus a small strip showing 2–3 layers; palette per STYLE_GUIDE §6.

Length: 1,400–1,800 clean words of body text (excluding the source list). You cannot run Python; the Orchestrator will count. Stay inside the band — do not overshoot.

CHAPTER-SPECIFIC SOURCE RULES (binding; from docs/STATUS.md §4 and SOURCES.md gaps):
- The split notation z then a = f(z) is a didactic convention — no source separates them explicitly; present it as the book's notation.
- Rosenblatt (S-ch03-03) and McCulloch & Pitts (S-ch03-04): historical mention ONLY (name, year, title). Do not describe the perceptron's structure from S-ch03-03 nor attribute content such as 'threshold neuron' to McCulloch & Pitts.
- Do not claim Nair & Hinton 'invented' ReLU.
- Goodfellow et al. is not verified — do not cite.
- Biological numbers (86 billion neurons, 10^14–10^15 synapses) come from course notes, not a primary source; if used, attribute exactly to the record and phrase as an approximate estimate.
- The '6x speed-up' figure may be attributed only to CS231n, not to Krizhevsky et al.
- Chapter 1 already introduced backpropagation ('התפשטות לאחור') and parameters as mixing-console knobs ('weights and biases' promised for chapter 3); you may deepen, not repeat.

GENERAL RULES: cite only IDs that exist in docs/SOURCES.md, right after the claim, within each record's access level and listed supported claims; metadata-only records → bibliographic/historical mention only; no item from SOURCES.md §3.8; every number/date has an ID and its context (population, task, year); invented examples clearly framed as illustrations ("דמיינו", "לדוגמה", "מספרים להמחשה בלבד"); no facts about baking chemistry (the dough story is about the reader's experience with the system). If a claim needs a missing source, don't write it — list it under "Needs research".

Structure: first line "פרק 3 — הרשת הנוירונית מבפנים"; the opening question on its own line; "## " section headings; the boxes; the illustration line(s); "## תובנות מרכזיות" (4–6 bullets); "## מקורות לפרק" (cited IDs with short bibliographic info copied from SOURCES.md §5).

FINAL MESSAGE (SHORT, ≤ 300 words): file + rough word count; source IDs used (one line each, main claim); boxes used (type + title); illustration line(s) as written; Needs research; one line on how the dough story advances.
```

## הפלט הגולמי שהסוכן החזיר (כלשונו)

```
I wrote chapter 3 to C:\biu01\HW2\ai_book_starter\chapters\chapter_03.txt, replacing the skeleton. I didn't touch any other file. By rough estimate the body is about 1,600–1,700 words, not counting the source list. I couldn't count it exactly, so please check it with your Python count. The two illustration lines add to the total; if it comes in over 1,800, the easiest thing to trim is the "גרסה דולפת" (Leaky ReLU) sentence.

**Source IDs used**
- S-ch03-01 (CS231n): the neuron model; weights are learned; the formula; activation functions; ReLU's 6x speed-up versus tanh, attributed only to CS231n; ReLU units "dying"; Leaky ReLU at about 0.01; logistic regression; layers and fully connected layers; the 26 and 41 parameter counts; the biological numbers, phrased as "an estimate quoted in the course notes"; the four limits of the brain analogy.
- S-ch03-02 (Nair & Hinton 2010): the definition max(0, x); the abstract claim that relative intensities are preserved; how the gradient is handled; the paper points to earlier work. I do not say they invented ReLU.
- S-ch03-03 (Rosenblatt 1958): name, year and title only.
- S-ch03-04 (McCulloch & Pitts 1943): name, year and title only.
- S-ch01-05 (cross-chapter link X14): backpropagation turns the knobs; each layer builds its description on the previous layer's.

**Boxes**
- במעבדה: "נוירון צעצוע בערב של הקוראת". Numbers marked "מספרים להמחשה בלבד": z = 0.85, so the neuron fires; then z = −0.55, so a = 0.
- מושג שכדאי להכיר: "פונקציית הפעלה". Adds the firing-rate interpretation and the ReLU gradient, which the body doesn't cover.
- מיתוס מול מציאות: "the network is a brain", answered with the four gaps.

**Illustration lines** (full text is in the file)
- [איור 3.1: נוירון אחד ורשת קטנה | סוג: תרשים TikZ | …] One neuron (x, w, Σ with b, z, f, a) plus a 3→4→2 strip labelled 26 parameters. Data source: the book's own framework, with structure per S-ch03-01.
- [איור 3.2: שלוש פונקציות הפעלה | סוג: גרף Matplotlib | …] Sigmoid, tanh and ReLU computed from the formulas; no empirical data.

The formulas appear in this order: z = \sum_{i=1}^{n} w_i x_i + b, then an explanation of each symbol, then a = f(z), which the text presents as the book's own notation.

**Needs research**
- There is no source for why non-linearity is necessary (stacked linear layers collapsing into one), so I left that claim out.
- There is no primary neuroscience source for the 86 billion neurons and 10^14–10^15 synapses.
- There is no source for which activation function is most common today, so the chapter makes no such claim.

**Dough story:** her question has turned into numbers. Inside the machine there is no "dough", only weights, and none of the numbers is "yeast". The chapter ends with words starting to appear and points to chapter 4.
```

## שער האיכות של ה-Orchestrator (21:29)
פלט סקריפט השער:
```
file=chapters/chapter_03.txt md5=0273dca8
words_clean=1315 raw=1605
first_line='פרק 3 — הרשת הנוירונית מבפנים'
ids_all=['S-ch01-05', 'S-ch03-01', 'S-ch03-02', 'S-ch03-03', 'S-ch03-04'] missing_in_SOURCES=[]
cited_in_body_not_in_list=[] listed_not_cited=[]
boxes(open,close)= {'במעבדה': (1, 1), 'מושג שכדאי להכיר': (1, 1), 'מיתוס מול מציאות': (1, 1)} unbalanced= [] old_markers= []
illustrations=2 pending_M4=0 insights_section=True
latin_sentence_starts(candidates)=['McCulloch'] percents=[]
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
?? agents/runs/versions/chapter_05_r1.txt
?? agents/runs/versions/chapter_07_r1.txt
?? agents/runs/writer_ch05_r1.md
?? agents/runs/writer_ch07_r1.md
```
