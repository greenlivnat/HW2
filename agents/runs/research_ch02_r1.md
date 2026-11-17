# הרצה: research-agent, יחידה ch02, סבב 1 (M2)

| שדה | ערך |
|---|---|
| תאריך | 2026-11-17 |
| סוכן | `research-agent` |
| הופעל על ידי | Orchestrator, אחת משבע הרצות שרצו במקביל |
| התחלה | 15:23:40 JST בקירוב |
| סיום | 15:28:36 JST בקירוב (משך לפי הכלי: 295.9 שניות) |
| שימוש | 28 קריאות לכלים, 68,107 טוקנים |
| קובץ פלט | `docs/sources/chapter_02.md` |

## הפרומפט המלא שנשלח

```
M2 RESEARCH, unit ch02, round 1.

Read first: agents/research_agent.md (UPDATED spec: record fields incl. mandatory access level, one record per URL, examples/formulas/data section, visualization ideas, fetch log, open-API fallback rules), docs/PRD.md sections 5 and 10, docs/OUTLINE.md.

Chapter 2 — "מנתונים ללמידה" (~3 pages). Topics per PRD §5: data collection and cleaning; training, validation and test sets; labels; data bias; generalization; data leakage; a continuous example story. Key question: how do examples become statistical knowledge? Visual: data-flow diagram.

Requirements:
- At least 2, ideally 3–5, VERIFIED reliable sources; prefer academic/scientific. Candidates you MAY check (verify by fetching, do not assume content): Kaufman et al. "Leakage in data mining" (ACM TKDD 2012); Buolamwini & Gebru 2018 "Gender Shades" (PMLR, open); Gebru et al. "Datasheets for Datasets" (arXiv / CACM); scikit-learn official docs on cross-validation / train-test split and on common pitfalls (data leakage); Google Machine Learning Crash Course pages on splitting data/generalization. Choose what you can actually verify.
- Record access level honestly for each source.
- Provide usable examples (ideally real documented cases of bias or leakage, with numbers only if verified with location), and visualization ideas (marked as suggestions).
- NEVER invent sources, DOIs, URLs, quotes or numbers.

Output: write ONLY docs/sources/chapter_02.md (Hebrew; bibliographic fields in original language). IDs: S-ch02-01, ... Structure: header; records; "דוגמאות, נוסחאות ונתונים"; "רעיונות להמחשה (הצעות)"; "פערים / לא אומת"; "יומן אחזורים".

Final message: structured report (verified sources count + access level each, all URLs OK/FAILED, gaps, files written).
```

## הפלט הגולמי שהסוכן החזיר (כפי שהתקבל אצל ה-Orchestrator)

```
## Report: M2 RESEARCH, unit ch02, round 1

I wrote one file for chapter 2 ("מנתונים ללמידה"): C:\biu01\HW2\ai_book_starter\docs\sources\chapter_02.md. It has 14 verified records covering 6 distinct works, and the topics needed for the chapter are covered. The chapter needs at least 2 sources, so it passes that bar. Seven records are peer-reviewed or academic, and seven are official documentation or teaching material.

### 1. Verified sources and access level
| ID | Source | Access level |
|---|---|---|
| S-ch02-01 | Buolamwini & Gebru 2018, Gender Shades, PMLR PDF | Full text (pp. 1–10 read) |
| S-ch02-02 | Same paper, PMLR landing page (PMLR 81:77–91) | Abstract only |
| S-ch02-03 | Gebru et al., Datasheets for Datasets, arXiv abstract page | Abstract only |
| S-ch02-04 | Same paper, arXiv PDF v8 | Full text, but only pp. 1–8 read (§1–3.5) |
| S-ch02-05 | Datasheets, CACM 64(12):86–92, DOI 10.1145/3458723 (via Crossref) | Metadata only |
| S-ch02-06 | Kaufman, Rosset, Perlich, Stitelman 2012, ACM TKDD 6(4):1–21, DOI 10.1145/2382577.2382579 (Crossref, cross-checked in OpenAlex) | Abstract only |
| S-ch02-07 | Kaufman, Rosset, Perlich 2011, KDD pp. 556–563, DOI 10.1145/2020408.2020496 | Metadata only |
| S-ch02-08 | scikit-learn 1.9.1 docs, §12 Common pitfalls (data leakage) | Full text (§12.2) |
| S-ch02-09 | scikit-learn 1.9.1 docs, §3.1 Cross-validation | Full text (intro of §3.1) |
| S-ch02-10 | Google ML Crash Course, Dividing the original dataset | Full text |
| S-ch02-11 | Google ML Crash Course, Overfitting | Full text |
| S-ch02-12 | Google ML Crash Course, Labels | Full text |
| S-ch02-13 | Google ML Crash Course, Data characteristics | Full text |
| S-ch02-14 | Google ML Crash Course, Fairness: Types of bias | Full text |

**Examples in the file, each with its location:**
- **Gender Shades (real bias case):**
  - Lighter-skinned share of existing benchmarks: 79.6% (IJB-A) and 86.2% (Adience).
  - Error rates for darker-skinned women: 20.8% (Microsoft), 34.5% (Face++), 34.7% (IBM). For lighter-skinned men: 0.0%, 0.8%, 0.3%.
  - Darker-skinned women are 21.3% of the dataset but account for 61.0%–72.4% of the errors.
  - The file includes a caveat: the link to the classifiers' training data is only the authors' hypothesis (§4.4), and the companies did not disclose their training data (§4.2).
- **Leakage with numbers (scikit-learn §12.2.2):** on random data, selecting features before the train/test split gave 0.76 accuracy; selecting after the split gave 0.5. This is a synthetic demo, and the file says so.

**Other contents:**
- A k-fold average formula. It is my own notation for the source's verbal description and is marked as such.
- A suggested fictional running example story, marked as a suggestion.
- Five visualization ideas, all marked as suggestions. The data-flow diagram includes a "leakage path."

### 2. URLs fetched
1. https://proceedings.mlr.press/v81/buolamwini18a.html: OK
2. https://arxiv.org/abs/1803.09010: OK
3. https://scikit-learn.org/stable/common_pitfalls.html: OK
4. https://scikit-learn.org/stable/modules/cross_validation.html: OK
5. https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets: OK
6. https://developers.google.com/machine-learning/crash-course/overfitting/overfitting: OK
7. https://api.crossref.org/works?query.bibliographic=Leakage+in+data+mining+formulation+detection+avoidance+Kaufman&rows=3: OK
8. https://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf: OK. The fetch tool could not extract text, so I read the saved PDF directly.
9. https://dl.acm.org/doi/10.1145/2382577.2382579: FAILED (HTTP 403)
10. https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/2382577.2382579?fields=title,authors,year,venue,abstract,externalIds,openAccessPdf: FAILED (HTTP 404)
11. https://api.openalex.org/works/doi:10.1145/2382577.2382579: OK (the paper is closed access)
12. https://api.crossref.org/works/10.1145/2382577.2382579: OK
13. https://arxiv.org/pdf/1803.09010v8: OK. The PDF was read directly, pp. 1–8.
14. https://api.crossref.org/works/10.1145/3458723: OK
15. https://developers.google.com/machine-learning/crash-course/overfitting/labels: OK
16. https://developers.google.com/machine-learning/crash-course/overfitting/data-characteristics: OK
17. https://developers.google.com/machine-learning/crash-course/fairness/types-of-bias: OK

I also ran one web search. It surfaced a copy of the Kaufman paper on a university course page (cs.umb.edu). That copy is unofficial, so I did not fetch or use it, per rule 8.

### 3. Gaps and unverified items
- **Kaufman et al. body text was not read** (ACM returned 403, and no official open copy exists). Everything about it stays at abstract level, including the INFORMS 2010 and IJCNN 2011 competition cases. Those can be mentioned but not described in detail.
- **No real-world leakage case with numbers was found** (for example, in medicine). The only numeric leakage example is the synthetic scikit-learn one.
- **The LFW figures (77.5% male, 83.5% White)** appear in Gender Shades only as a citation of Han & Jain 2014. That original source was not verified.
- **Datasheets for Datasets:** p. 9 onward was not read (the Distribution and Maintenance sections and the appendix).
- **Data cleaning** has no peer-reviewed definitional source yet. It is covered only by S-ch02-13 (teaching material) and S-ch02-04 §3.4.
- **Google ML Crash Course pages** showed no last-updated date in the fetched content.
- **Gender Shades page numbers conflict:** the PDF header says "81:1–15" but the PMLR landing page says 77–91. Use 77–91 in the bibliography.

### 4. Files written
- C:\biu01\HW2\ai_book_starter\docs\sources\chapter_02.md (new; no other files changed)
```

## קבצים שנוצרו או שונו
- נוצר: `docs/sources/chapter_02.md` (34,656 בתים, MD5 `46ebe729...`)
- `git status` (15:29:27): אין שינויים בקבצים במעקב.

## שער האיכות של ה-Orchestrator
| בדיקה | תוצאה |
|---|---|
| קובץ קיים, עם כל הסעיפים | ✅ |
| לפחות 2 מקורות מאומתים | ✅ 14 רשומות, 6 עבודות שונות |
| רמת גישה לכל רשומה | ✅ (14 מתוך 14) |
| כיסוי PRD סעיף 5 | ✅ חלוקה לאימון, אימות ובדיקה, תוויות, הטיות, הכללה, זליגה וניקוי (ניקוי רק ברמת חומר לימודי) |
| כתיבה רק בתחום | ✅ |

**הערכת איכות:** חזק. יש מקרה הטיה אמיתי ומתועד היטב (Gender Shades, בטקסט מלא, עם מספרים ומיקומים), ויש דוגמת זליגה עם מספרים, שמסומנת כסינתטית. הסתייגות: מאמר הזליגה של Kaufman זמין רק ברמת התקציר.

**החלטה:** השער עבר.
