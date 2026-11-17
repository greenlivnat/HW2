# הרצה: writer-agent, יחידה ch01, סבב 1 (M3)

| שדה | ערך |
|---|---|
| תאריך | 2026-11-17 |
| סוכן | `writer-agent` |
| הופעל על ידי | Orchestrator |
| התחלה / סיום | 20:05 בקירוב / 20:12 בקירוב (משך לפי הכלי: 364.6 שניות) |
| שימוש | 41 קריאות לכלים, 125,280 טוקנים |
| קובץ פלט | `chapters/chapter_01.txt` (עותק הגרסה: `agents/runs/versions/chapter_01_r1.txt`) |

## הפרומפט המלא שנשלח

```
M3 WRITING, unit ch01, round 1.

Read first (in this order):
1. agents/writer_agent.md (your role spec).
2. docs/PRD.md — version 1.3. Sections 4, 5 (chapter 1), 6 (NOTE the new "סגנון הכתיבה" sub-bullets added in v1.3) and 10. docs/OUTLINE.md.
3. docs/SOURCES.md (sections 1, 3.1, 3.8, 4) and the full detailed records in docs/sources/chapter_01.md. You may also use records from other chapters' files only if a cross-reference in SOURCES.md section 4.3 explicitly points chapter 1 to them.

TASK: write chapter 1, "מהי בינה מלאכותית?", into chapters/chapter_01.txt (overwrite the current skeleton placeholder in that file). Write ONLY that file. Do not create a .tex file in this round.

Content (PRD §5): definition(s) of AI; the difference between AI, machine learning and deep learning; what makes a system "learn"; key question from OUTLINE: how does AI differ from ordinary software (rules written by a programmer vs. behavior learned from examples); a road map of the book.

Length: PRD target is ~2 printed pages, but the user wants a rich narrative chapter. Aim for 900–1,200 Hebrew words of body text (excluding the source list).

STYLE (decided by the user — binding):
- Popular science inspired by the SPIRIT of Carl Sagan's books (wonder, curiosity, the wide view, respect for the reader), but in an ORIGINAL literary voice. Do not imitate, quote or paraphrase his sentences, signature phrases or structures (e.g., no "billions and billions", no "pale blue dot"/"cosmos" style borrowings). Do not mention Sagan.
- Rich, accessible, captivating and professional Hebrew.
- Stories, analogies and examples from everyday life.
- OPEN with an intriguing question.
- Narrative thread across the whole book: a journey behind the scenes of AI, from the moment the reader types a question until the answer appears on the screen. Chapter 1 sets up this frame (the reader — "הקוראת", per OUTLINE — types a question) and ends with a road map that hands off to chapter 2 (data and learning). Road map must match OUTLINE chapter titles 2–7 and the appendix.
- Weave in scientific facts and academic sources.
- CLOSE with a short section of key insights ("תובנות מרכזיות"), 4–6 crisp items, not a repetition of earlier sentences.
- No repetitiveness, no generic phrasing (avoid clichés like "בעולם המשתנה של היום", "מהפכה טכנולוגית", "לא סוד ש...").
- Explain every technical term at first use (Hebrew term + English in parentheses where helpful).

TEXT CONVENTIONS for the .txt file:
- First line: chapter title; then the opening question.
- Section headings as lines starting with "## ".
- Include exactly one or two boxes marked as:
  [מושג חשוב: <title>] ... [/מושג חשוב]
  [שאלת מחשבה] ... [/שאלת מחשבה]
- Mark the planned visual (OUTLINE: concept map) with a single line: [איור: מפת מושגים — <one-line description>]. Do NOT claim a source for the visual's hierarchy.
- Inline citations as [S-ch01-NN] right after the supported claim (same format as the smoke test).
- End the file with a "## מקורות לפרק" list of the IDs you cited, each with short bibliographic info copied from SOURCES.md section 5.

SOURCE RULES (binding; Orchestrator decision I8 and STATUS §4):
- Cite only IDs that exist in docs/SOURCES.md, and keep each claim within that record's access level and the supported claims listed in docs/sources/chapter_01.md.
- S-ch01-04 (Mitchell 1997) and S-ch01-06 (Samuel 1959) are metadata-only: at most a historical/bibliographic mention (name, title, year). No content claims. Do NOT use the sentence from Mitchell's book web page. Do NOT use the famous quote attributed to Samuel ("without being explicitly programmed") in any form, not even paraphrased as his words.
- The learning definition (task T, performance P, experience E) comes from S-ch01-03 (Mitchell 2006).
- The hierarchy AI ⊃ ML ⊃ DL has NO explicit source: present it as the book's own summary/framing ("נסכם זאת כך..."), not as an attributed fact.
- S-ch01-05 (LeCun et al. 2015) is abstract-only: stay at the abstract's level of detail.
- Turing's prediction: if you use it, respect gap 7 in the sources (the "10^9" reading is unverified against the PDF — prefer not to cite that number).
- OECD updated definition date: write "2023–2024" or cite S-ch01-09 without an exact approval date.
- Any number or date must carry its source ID. Any illustrative example you invent (e.g., a spam filter story, a made-up dialogue) must be clearly framed as an illustration, not as a factual report, and must not include invented statistics.
- If a claim you want needs a source that is missing, DO NOT write it; list it under "Needs research".

FINAL MESSAGE to the Orchestrator:
1. File written and Hebrew word count (state how you counted).
2. Source IDs used, each with the claim(s) it supports.
3. "Needs research": claims you wanted but lacked a source for.
4. Style choices: the opening question, the narrative frame, and the analogies you used.
```

## הפלט הגולמי שהסוכן החזיר

```
Writer Agent report: M3, unit ch01, round 1

**1. File written**
- C:\biu01\HW2\ai_book_starter\chapters\chapter_01.txt. The skeleton placeholder is replaced. No other file was touched and no .tex file was created.
- Word count: about 1,190 words of body text (from the title to the end of "תובנות מרכזיות", without the source list). I had no shell access, so I could not run Python. I counted whitespace-separated tokens with the Grep tool (`\S+`, -o, using offset to find the token index of the "## מקורות לפרק" heading). That gave 1,245 tokens. I then took off about 52 non-word tokens: 26 citation tags, 8 "##" markers, 6 bullet dashes, 3 em-dashes and 9 box or illustration markers. Please recheck with Python at the quality gate. The result is close to the 1,200 ceiling.
- Structure:
  - First line is the title, then the opening question.
  - 8 "## " sections, including "מפת הדרך" and "תובנות מרכזיות" (6 items).
  - One [מושג חשוב: ...] box and one [שאלת מחשבה] box.
  - One [איור: מפת מושגים — ...] line. It is explicitly marked as the book's own framing, with no source claimed for the hierarchy.
  - Closes with "## מקורות לפרק" (10 IDs, bibliographic info from SOURCES.md §5).

**2. Source IDs used and the claims they support**
- **S-ch01-01:**
  - Proposal dated 31 Aug 1955.
  - McCarthy, Minsky, Rochester and Shannon proposed a 2-month, 10-person study in summer 1956 under the name "artificial intelligence".
  - The conjecture that every aspect of learning and intelligence can in principle be described precisely enough for a machine to simulate it.
  - "Self-Improvement" is among the seven aspects. Also used in insight 5.
- **S-ch01-02:**
  - 1950, "Can machines think?".
  - The imitation game: the interrogator sits in a separate room, and a participant is later replaced by a machine.
  - The child-machine: like a notebook from a stationer's, little mechanism and many blank sheets.
  - Also used in insight 5. Turing's prediction is not used at all: no "10^9", no 70%, no 50 years.
- **S-ch01-03:**
  - The T/P/E learning definition (in the box).
  - Manual programming vs. getting computers to "program themselves" from experience plus some initial structure.
  - Speech recognition and computer vision: trained systems are more accurate than hand-written programs.
  - The 85% handwritten-mail figure, explicitly framed as "as of 2006".
  - ML as an outgrowth of computer science and statistics.
  - Also used in insights 2 and 3.
- **S-ch01-04 (metadata only):** bibliographic mention only, "Mitchell, author of the textbook Machine Learning (1997)". No content, and the web-page sentence is not used.
- **S-ch01-05 (abstract level):**
  - Multiple processing layers learn representations at multiple levels of abstraction.
  - Backpropagation indicates how to change the internal parameters each layer uses.
  - Dramatic improvements in speech recognition, visual object recognition and genomics.
  - Also used in insight 4.
- **S-ch01-06 (metadata only):** in 1959 the phrase "Machine Learning" appeared in the title of a paper by A. L. Samuel on checkers. No content, and the "without being explicitly programmed" quote is not used in any form.
- **S-ch01-07:**
  - Nilsson's definition (via AI100, 2016).
  - No precise, universally accepted definition.
  - The "AI effect".
  - The calculator example and intelligence as a continuum (in the thought box).
  - Also used in insights 1 and 6.
- **S-ch01-08:**
  - The maturing of ML is foremost among the research trends.
  - DL is a form of artificial neural networks trained with backpropagation.
- **S-ch01-09:** the full OECD "AI system" definition, paraphrased in Hebrew. No approval date is given. Also used in insight 1.
- **S-ch01-10:** "content" was added in the update, dated "2023–2024", to cover generative AI.

**3. Needs research**
- The AI ⊃ ML ⊃ DL hierarchy still has no explicit source (gap 3 / X14). In the text it is presented as the book's own framing: "נסכם... זו המסגרת של הספר הזה, ולא ציטוט ממקור מסוים".
- First names Alan, John, Marvin, Nathaniel, Claude and Arthur do not appear in the records, which give initials only. I used surnames only (and "A. L. Samuel"). If full names are wanted, the research agent needs to confirm them.
- I wanted to say that the Turing test idea and early AI work spanned the 1950s–60s more broadly, and to give a modern example of everyday AI such as recommendation systems. There are no records for either, so both were left out.
- Insight 4 ("DL is not a synonym for AI") cites S-ch01-05 for the layers part. The "not a synonym" part is the book's framing. The reviewer may want that citation moved or removed.

**4. Style choices**
- **Opening question:** "מי כתב את התשובה שמופיעה עכשיו על המסך, אם שום אדם לא ראה את השאלה?"
- **Narrative frame:**
  - Late evening, the reader's ("הקוראת") dough has not risen, and she types "למה הבצק שלי לא תופח, ומה אפשר לעשות עכשיו?". The scene is explicitly labeled as an illustration that will recur through the book.
  - The OECD definition is read back onto her scene: input is the question, output is content, and "מסיקה" sits in the middle.
  - The road map lists ch. 2–7 and the appendix by their exact OUTLINE titles. It hands off to ch. 2 with "המסע מתחיל... בערימות הדוגמאות שמהן המערכת למדה".
- **Analogies, each marked as ours:**
  - Recipe vs. a cook who learned by tasting (the section title "מתכון מול טעימה").
  - Trying to write rules for a handwritten "7".
  - A spam filter as the T/P/E illustration in the concept box, labeled "שלנו, לא מתוך המקור", with no statistics.
  - Matryoshka dolls for AI/ML/DL.
  - A beginning reader going from strokes to letters, words and sentence, for levels of abstraction.
  - In the thought box: calculator and keyboard autocomplete, plus a question about where the line will be in a decade.
- **Constraints kept:**
  - No Sagan mention, imitation or signature phrases.
  - None of the clichés listed in the brief.
  - Each technical term is explained at first use, with the English in parentheses: machine learning, deep learning, generative AI, artificial neural networks, backpropagation, AI effect, T/P/E.
```

## שער האיכות של ה-Orchestrator (20:12)
- `git status`: הסוכן שינה רק את `chapters/chapter_01.txt`. (`docs/PRD.md`, ‏`docs/STATUS.md` ו-`prompts/08_...` שונו על ידי ה-Orchestrator לפני ההרצה.)
- MD5 של `docs/SOURCES.md` ו-`docs/sources/chapter_01.md` זהה לפני ההרצה ואחריה (983878e0... / bc3370b2...).
- ספירת מילים ב-Python (גוף הפרק, בלי תגיות ובלי רשימת המקורות): **1,165**. בטווח היעד 900–1,200.
- מזהים מצוטטים: S-ch01-01 עד S-ch01-10. כולם קיימים ב-`docs/SOURCES.md`.
- המשפט המיוחס ל-Samuel ("explicitly programmed") לא מופיע.
- **החלטה:** השער עבר. הצעד הבא: reviewer-agent, סבב 1.
