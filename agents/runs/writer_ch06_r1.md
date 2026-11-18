# הרצה: writer-agent, יחידה ch06, סבב 1 (M3)

| שדה | ערך |
|---|---|
| תאריך | 2026-11-17 |
| סוכן | `writer-agent` |
| הופעל על ידי | Orchestrator (במקביל לפרקים 2–7) |
| שער האיכות | 21:29 |
| שימוש | 20 קריאות לכלים, 89,435 טוקנים, 231.5 שניות |
| קובץ פלט | `chapters/chapter_06.txt` (עותק: `agents/runs/versions/chapter_06_r1.txt`) |

## הפרומפט המלא שנשלח
ההפעלה (Agent tool) הפנתה לקובץ המשימה. התוכן המלא שלו מופיע כאן.

```
M3 WRITING, unit ch06, round 1. Your complete task specification (prepared by the Orchestrator) is in the file agents/runs/tasks/writer_ch06_r1_prompt.txt. Read it first and follow it exactly ...
```

### תוכן קובץ המשימה `agents/runs/tasks/writer_ch06_r1_prompt.txt`
```
M3 WRITING, unit ch06, round 1.

Read first (in order):
1. agents/writer_agent.md (role spec).
2. docs/STYLE_GUIDE.md — BINDING: literary voice, scientific-integrity rules, the dough-story arc (§3, row for chapter 6), the five content boxes and their markers (§4), illustration/formula/table/placeholder markers (§5), palette (§6), length (§7).
3. docs/PRD.md v1.4 §4, §5 (chapter 6), §6, §10; docs/OUTLINE.md.
4. chapters/chapter_01.txt — APPROVED by the user; it defines the voice and the story's starting point. Read it for continuity; do NOT repeat its content, analogies or examples (matryoshka, recipe vs. cook, mixing console are taken).
5. docs/SOURCES.md (§1, §3.6, §3.8, §4) and the full records in docs/sources/chapter_06.md. Cross-chapter records may be used only where SOURCES.md §4 explicitly links them to this chapter.

TASK: write chapter 6, "מה AI יודע — ומה לא", into chapters/chapter_06.txt (overwrite the skeleton). Write ONLY that file; no .tex.

Content (PRD §5): hallucinations, uncertainty, bias, privacy, copyright, responsible use; examples without attributing unsupported facts.

Story (STYLE_GUIDE §3): part of the answer on the reader's screen sounds confident but may not be correct (do not invent what the answer said about baking — describe it generically, e.g., 'a confident sentence she cannot verify'); and what happens to what she typed? Close pointing to chapter 7: the human who checks.

Boxes: 2–4 boxes chosen to fit the topic, using the exact markers in STYLE_GUIDE §4. Suggested for this chapter: מיתוס מול מציאות (the system 'knows' facts); מאחורי הקלעים (memorization and extraction of training data); רגע של מחשבה (privacy). No two boxes of the same type in a row; each box adds something the body doesn't say.

Visual: at least one original visualization to be generated in code in M4, as an [איור 6.N: ...] line in the exact STYLE_GUIDE §5 format (type, content, palette colours, data source). Required/suggested: at least one: e.g., a TikZ 'case cards' panel (2–3 cards: a legal case with fabricated citations, a memorization/extraction finding, a bias audit) or a conceptual diagram 'where errors come from' (data → training → generation → user). No invented rates or numbers.

Length: 1,400–1,800 clean words of body text (excluding the source list). You cannot run Python; the Orchestrator will count. Stay inside the band — do not overshoot.

CHAPTER-SPECIFIC SOURCE RULES (binding; from docs/STATUS.md §4 and SOURCES.md gaps):
- No hallucination rates or any quantitative frequency of errors.
- Mata v. Avianca: write 'בין היתר שש החלטות' (that the court listed by name); no total number of fabricated cases.
- Bias example: refer to Gender Shades (S-ch02-01) per cross-reference X1, with the two caveats recorded in the sources files.
- Carlini et al.: the anomalous line on p. 2640 ('Somwhere says...') is forbidden.
- Bender et al. (S-ch06-09): metadata only — no content claims.
- Copyright Office report: do not state Part 3's conclusions.
- LLM calibration is NOT established by the sources; Guo et al. only as a marked analogy (calibration of classifiers). If you mention 'temperature' in the calibration sense, note it differs from sampling temperature in chapter 4.
- All legal claims are US-based; do not generalize to Israeli/EU law (see X9).
- Ji et al. definitions read in arXiv v7 — say 'according to the survey' without asserting identity with the journal version.

GENERAL RULES: cite only IDs that exist in docs/SOURCES.md, right after the claim, within each record's access level and listed supported claims; metadata-only records → bibliographic/historical mention only; no item from SOURCES.md §3.8; every number/date has an ID and its context (population, task, year); invented examples clearly framed as illustrations ("דמיינו", "לדוגמה", "מספרים להמחשה בלבד"); no facts about baking chemistry (the dough story is about the reader's experience with the system). If a claim needs a missing source, don't write it — list it under "Needs research".

Structure: first line "פרק 6 — מה AI יודע — ומה לא"; the opening question on its own line; "## " section headings; the boxes; the illustration line(s); "## תובנות מרכזיות" (4–6 bullets); "## מקורות לפרק" (cited IDs with short bibliographic info copied from SOURCES.md §5).

FINAL MESSAGE (SHORT, ≤ 300 words): file + rough word count; source IDs used (one line each, main claim); boxes used (type + title); illustration line(s) as written; Needs research; one line on how the dough story advances.
```

## הפלט הגולמי שהסוכן החזיר (כלשונו)

```
I wrote chapter 6 to C:\biu01\HW2\ai_book_starter\chapters\chapter_06.txt, replacing the skeleton. It's about 1,650–1,750 body words by my rough estimate, which could be near the 1,800 ceiling, so please run the Python count. No other file was touched.

**Source IDs used:**
- S-ch06-01: according to the survey abstract, text generators tend to hallucinate, which hurts performance and user trust.
- S-ch06-02: the definition of hallucination, the intrinsic vs extrinsic split, and the causes (data, training/decoding). Read in v7 and attributed as "according to the survey".
- S-ch06-04: modern networks are poorly calibrated; temperature scaling (noted as not the sampling temperature of ch4).
- S-ch06-05: the calibration definition (100 predictions at 0.8, about 80 correct), LeNet vs ResNet, "cannot claim causality". Labelled as an analogy only, with no claim about LLMs.
- S-ch06-06: extraction of training data from GPT-2; larger models are more vulnerable.
- S-ch06-08: 604 of 1,800 (33.5%; best variant 67%), Table 1 (46 named people, 32 contact items), the public-data caveat. The forbidden line on p. 2640 is not used.
- S-ch06-10 (NIST): three bias categories, privacy, copyright in training data, seven trustworthiness traits, human involvement.
- S-ch06-11: the three parts of the Copyright Office report and their dates. No Part 3 conclusions are stated.
- S-ch06-12: Part 2 conclusion ("prompts alone" are unlikely to be enough), no legislative change recommended. Flagged as US law only.
- S-ch06-13 (Mata v. Avianca): "בין היתר שש החלטות", the timeline, $5,000, the "gatekeeping role", the screenshots.
- S-ch02-01 (Gender Shades, via X1): 20.8–34.7% vs 0.0–0.8% error rates, with both caveats (the cause is a hypothesis; these are image classifiers, not LLMs).

S-ch06-09 (Bender et al.) is not used.

**Boxes:**
- מיתוס מול מציאות: the system "knows" facts, and asking it whether it is right counts as checking.
- מאחורי הקלעים: איך תופסים מודל שמשנן
- רגע של מחשבה: privacy.

**Illustration:** one line, [איור 6.1: שלושה תיקים על השולחן]. It is a TikZ panel of three case cards (Mata, Carlini, Gender Shades), each with the fields "מה קרה / מה המקור אומר / מה לומדים", using the full palette. The data sources are S-ch06-13, S-ch06-08 and S-ch02-01, and no number on the cards is outside them.

**Needs research:**
1. What chat services do with what users type (retention, use for training). The text says only that it depends on the service and its terms.
2. Calibration of LLMs.
3. Israeli and EU privacy and copyright law.

**Dough story:** the reader stops at one confident sentence she cannot verify and wonders where her typed words went. The chapter closes with her keeping the answer without accepting it, looking for evidence outside the chat window, which leads into chapter 7.
```

## שער האיכות של ה-Orchestrator (21:29)
פלט סקריפט השער:
```
file=chapters/chapter_06.txt md5=2fe2de89
words_clean=1464 raw=1690
first_line='פרק 6 — מה AI יודע — ומה לא'
ids_all=['S-ch02-01', 'S-ch06-01', 'S-ch06-02', 'S-ch06-04', 'S-ch06-05', 'S-ch06-06', 'S-ch06-08', 'S-ch06-10', 'S-ch06-11', 'S-ch06-12', 'S-ch06-13'] missing_in_SOURCES=[]
cited_in_body_not_in_list=[] listed_not_cited=[]
boxes(open,close)= {'מאחורי הקלעים': (1, 1), 'רגע של מחשבה': (1, 1), 'מיתוס מול מציאות': (1, 1)} unbalanced= [] old_markers= []
illustrations=1 pending_M4=0 insights_section=True
latin_sentence_starts(candidates)=['Avianca', 'GPT-', 'NIST', 'NIST', 'NIST', 'NIST', 'Avianca', 'S-ch'] percents=['20.8%', '34.7%', '0.0%', '0.8%', '33.5%', '67%']
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
?? agents/runs/versions/chapter_07_r1.txt
?? agents/runs/writer_ch03_r1.md
?? agents/runs/writer_ch05_r1.md
?? agents/runs/writer_ch07_r1.md
```
