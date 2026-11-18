# הרצה: research-agent, יחידה ch02, סבב 2 (M3, תיקון רשומה)

| שדה | ערך |
|---|---|
| תאריך | 2026-11-18 |
| סוכן | `research-agent` |
| הופעל על ידי | Orchestrator, בעקבות הליקוי R-ch02-11 (קטגוריה "מקורות") ב-`review_ch02_r2.md` |
| קובץ פלט | `docs/sources/chapter_02.md` (רשומה S-ch02-01, טענה 3) |

## הפרומפט המלא שנשלח

```
M3 SOURCE CORRECTION, unit ch02, research round 2 (routed from review defect R-ch02-11).

Read first: agents/research_agent.md; agents/runs/review_ch02_r2.md (defects R-ch02-10 and R-ch02-11); the record S-ch02-01 (Buolamwini & Gebru 2018, Gender Shades) in docs/sources/chapter_02.md, and its row and cross-references in docs/SOURCES.md.

Problem reported by the Reviewer: claim 3 of S-ch02-01 gives "4.4%" for dark-skinned women in Adience. According to the Reviewer, this comes from the caption of Figure 3 in the paper, which contradicts the figure's own bars and §3.5 of the same paper: there 4.4% belongs to IJB-A, and Adience is 7.4%.

TASK:
1. Verify independently against the official paper (PMLR: proceedings.mlr.press, vol. 81) — fetch the PDF/HTML and read Figure 3, its caption, and §3.5. Do not trust the Reviewer's numbers; report what the paper actually says, with locations.
2. Correct claim 3 of S-ch02-01 in docs/sources/chapter_02.md: state the verified figure per dataset with location, and document the internal inconsistency in the paper (caption vs. bars/§3.5) and which reading the book should use (or that the figure should not be used). Add an entry to the record's fetch log.
3. If docs/SOURCES.md repeats the wrong figure anywhere, correct it there too, and note the change in its section 4.2 (inconsistencies).
Write ONLY docs/sources/chapter_02.md and, if needed, docs/SOURCES.md. Never invent numbers; if you cannot reach the paper, say so and mark the figure "לא לשימוש".

FINAL MESSAGE (SHORT, ≤ 200 words): what the paper says (with locations), exactly what you changed in which file, URLs fetched (OK/FAILED).
```

## הפלט הגולמי שהסוכן החזיר (כלשונו)

```
The Reviewer was right: the "4.4% for dark-skinned women in Adience" figure comes from the caption of Figure 3, and that caption contradicts the rest of the paper. I corrected claim 3 of S-ch02-01 accordingly.

**What the paper says** (official PMLR PDF, read directly, internal page numbers):
- **Figure 3 bars (p. 6), darker female / darker male / lighter female / lighter male:** Adience 7.4 / 6.4 / 44.6 / 41.6; IJB-A 4.4 / 16.0 / 20.2 / 59.4; PPB 21.3 / 25.0 / 23.3 / 30.3.
- **Figure 3 caption (p. 6):** "Only 4.4% of subjects in Adience are darker-skinned and female in comparison to 21.3% in PPB." This is wrong.
- **§3.5 (p. 7):** "Darker females are the least represented in IJB-A (4.4%) and darker males are the least represented in Adience (6.4%)."
- **Table 3 (p. 7):** darker-skinned share is 13.8% in Adience (7.4+6.4) and 20.4% in IJB-A (4.4+16.0). Both sums match the bars.

The verified figure for dark-skinned women is 4.4% in IJB-A and 7.4% in Adience.

**Changes, in `C:\biu01\HW2\ai_book_starter\docs\sources\chapter_02.md` only:**
- **Claim 3:** now gives the figure for each dataset with locations and the §3.5 quote. It documents the caption-vs-bars/§3.5/Table 3 inconsistency and tells the writer to use 4.4% for IJB-A and 7.4% for Adience, and never "4.4% in Adience".
- **Header:** added a line noting the round-2 correction.
- **Gaps:** new item 9 on the wrong caption.
- **Fetch log:** new row 18.

`docs\SOURCES.md` does not contain the wrong figure, so I left it unchanged.

**URLs fetched:**
- https://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf: OK. The fetch tool couldn't extract text, so I read the saved PDF directly (pp. 5–7).
```

## שער האיכות של ה-Orchestrator
- `git status`: הסוכן שינה רק את `docs/sources/chapter_02.md`. ‏MD5 של `docs/SOURCES.md` לא השתנה (983878e0...). הפרקים לא נגעו.
- **תוצאה:** הנתון "4.4% ב-Adience" שגוי (כיתוב איור 3 במאמר סותר את העמודות, את סעיף 3.5 ואת טבלה 3). הנתונים המאומתים: IJB-A ‏4.4%, ‏Adience ‏7.4%. הרשומה תוקנה, והסתירה תועדה.
- **החלטה:** reviewer-agent, סבב 3 ל-ch02.
