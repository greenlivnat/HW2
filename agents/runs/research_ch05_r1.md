# הרצה: research-agent, יחידה ch05, סבב 1 (M2)

| שדה | ערך |
|---|---|
| תאריך | 2026-11-17 |
| סוכן | `research-agent` |
| הופעל על ידי | Orchestrator, אחת משבע הרצות שרצו במקביל |
| התחלה | 15:23:40 JST בקירוב |
| סיום | 15:27:52 JST בקירוב (משך לפי הכלי: 252.5 שניות) |
| שימוש | 24 קריאות לכלים, 57,042 טוקנים |
| קובץ פלט | `docs/sources/chapter_05.md` |

## הפרומפט המלא שנשלח

```
M2 RESEARCH, unit ch05, round 1.

Read first: agents/research_agent.md (UPDATED spec: record fields incl. mandatory access level, one record per URL, examples/formulas/data section, visualization ideas, fetch log, open-API fallback rules), docs/PRD.md sections 5 and 10, docs/OUTLINE.md (note the proposed chart: train vs test performance over training epochs, plus a table).

Chapter 5 — "בודקים מודלים בעזרת נתונים" (~3 pages). Topics per PRD §5: accuracy vs. error rate vs. broader evaluation (e.g. precision/recall, confusion matrix, why accuracy misleads on imbalanced data); generalization and overfitting as seen in train vs test curves; an original Python chart from REAL data whose origin is verified, OR simulated data explicitly marked as demo; a summary table; why one cannot conclude more from a chart than the data supports.

Requirements:
- At least 2, ideally 3–5, VERIFIED reliable sources; prefer academic/scientific/official documentation. Candidates you MAY check (verify by fetching): scikit-learn official docs (model evaluation: accuracy, precision, recall, confusion matrix; learning/validation curves); Google ML Crash Course pages on classification metrics and overfitting; Sokolova & Lapalme 2009 "A systematic analysis of performance measures for classification tasks"; Zhang et al. 2017 "Understanding deep learning requires rethinking generalization" (arXiv/ICLR). Choose what you can actually verify.
- IMPORTANT for the chart: look for a REAL, openly licensed, verifiable dataset or published numeric table that could support a train-vs-test chart (e.g. a scikit-learn documentation example with published numbers, or a paper table). Report exactly what numbers exist and where, and the license. If none is verifiable, say so plainly and recommend clearly labeled demo data — do not fabricate numbers.
- Capture formulas (accuracy, error rate, precision, recall) with source location.
- Visualization ideas (marked as suggestions).
- NEVER invent sources, DOIs, URLs, quotes or numbers.

Output: write ONLY docs/sources/chapter_05.md (Hebrew; bibliographic fields in original language). IDs: S-ch05-01, ... Structure: header; records; "דוגמאות, נוסחאות ונתונים" (incl. chart-data assessment); "רעיונות להמחשה (הצעות)"; "פערים / לא אומת"; "יומן אחזורים".

Final message: structured report (verified sources count + access level each, all URLs OK/FAILED, gaps, chart-data recommendation, files written).
```

## הפלט הגולמי שהסוכן החזיר (כפי שהתקבל אצל ה-Orchestrator)

```
## Research report: ch05, round 1

Chapter 5 now has 11 verified sources. 10 were read in full text and one was checked from its bibliographic details only. I found no open, verifiable table of train vs test numbers per epoch, so I recommend generating the chart from a real public dataset with our own script.

### 1. Sources for Chapter 5

| ID | Source | Access level |
|---|---|---|
| S-ch05-01 | scikit-learn, "3.4 Metrics and scoring" (v1.9.1). Covers accuracy, confusion matrix, precision/recall/F-beta, balanced accuracy | Full text (first 100K of ~175K chars; the relevant sections were read in full) |
| S-ch05-02 | scikit-learn, "3.5 Validation curves". Bias/variance, how to read under/overfitting, Iris numbers printed on the page | Full text |
| S-ch05-03 | scikit-learn example, "Effect of model regularization on training and test error". Uses **synthetic** data; test R² = 0.884 | Full text |
| S-ch05-04 | scikit-learn, "Toy datasets" §9.1.3 (Digits: 1,797 samples, 64 features, 10 classes) and §9.1.6 (Breast cancer: 212 malignant / 357 benign) | Full text |
| S-ch05-05 | Alpaydin & Kaynak (1998), Optical Recognition of Handwritten Digits, UCI repository, DOI 10.24432/C50P49. **License: CC BY 4.0 (checked on the page)** | Full text (repository page) |
| S-ch05-06 | Google ML Crash Course, "Accuracy, recall, precision…". Formulas plus the "99% accuracy yet useless" example on imbalanced data | Full text |
| S-ch05-07 | Google ML Crash Course, "Thresholds and the confusion matrix" (spam example) | Full text |
| S-ch05-08 | Google ML Crash Course, "Overfitting". Definitions of overfitting and generalization; Figure 15 caption says the pattern "strongly implies overfitting" | Full text |
| S-ch05-09 | Google ML Crash Course, "Interpreting loss curves" | Full text |
| S-ch05-10 | Zhang, Bengio, Hardt, Recht & Vinyals, "Understanding deep learning requires rethinking generalization", ICLR 2017, arXiv:1611.03530v2, DOI 10.48550/arXiv.1611.03530 | Full text (pages 1–7; appendix not read) |
| S-ch05-11 | Sokolova & Lapalme (2009), Information Processing & Management 45(4):427–437, DOI 10.1016/j.ipm.2009.03.002 | Bibliographic details only (via Crossref and OpenAlex; paywalled, no abstract available) |

The formulas for accuracy, precision, recall, FPR, F-beta and balanced accuracy are recorded with their source sections. The file also has a worked confusion-matrix example from S-ch05-01 §3.4.4.6: tn=2, fp=1, fn=2, tp=3.

### 2. URLs fetched
1. https://scikit-learn.org/stable/modules/model_evaluation.html: OK
2. https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall: OK
3. https://developers.google.com/machine-learning/crash-course/overfitting/overfitting: OK
4. https://arxiv.org/abs/1611.03530: OK
5. https://api.crossref.org/works?query.bibliographic=A+systematic+analysis+of+performance+measures+for+classification+tasks+Sokolova+Lapalme&rows=3: OK
6. https://scikit-learn.org/stable/auto_examples/model_selection/plot_validation_curve.html: FAILED (the page only redirects to the example in #9)
7. https://scikit-learn.org/stable/datasets/toy_dataset.html: OK
8. https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits: OK
9. https://scikit-learn.org/stable/auto_examples/model_selection/plot_train_error_vs_test_error.html: OK
10. https://scikit-learn.org/stable/modules/learning_curve.html: OK
11. https://developers.google.com/machine-learning/crash-course/overfitting/interpreting-loss-curves: OK
12. https://arxiv.org/pdf/1611.03530: OK (I read the saved PDF pages as images, including Table 1)
13. https://arxiv.org/abs/1611.03530v2: OK (license check: arXiv non-exclusive distribution 1.0, not a Creative Commons license)
14. https://api.openalex.org/works/doi:10.1016/j.ipm.2009.03.002: OK (details only; paywalled)
15. https://developers.google.com/machine-learning/crash-course/classification/thresholding: OK

### 3. Gaps and unverified items
- **Error rate formula:** no source states it explicitly. The chapter should present it as "1 minus accuracy", derived directly from the accuracy formula.
- **Sokolova & Lapalme (S-ch05-11):** only the bibliographic details are confirmed. It must not be cited for any specific claim; at most it can appear as further reading.
- **Licenses not confirmed:** I found no license statement for the Google ML Crash Course pages, and I did not check scikit-learn's documentation license. Both should be paraphrased and cited, not copied, and their figures should not be reproduced.
- **Zhang et al. appendix (Table 2, ImageNet):** not read. Only the ImageNet figures quoted in the body text on pp. 5 and 7 are verified.
- **Per-epoch numbers:** none exist in a verified, open numeric form. The per-epoch curves in Zhang et al. (Figure 2) and in S-ch05-03 are images only, and nobody should estimate numbers by eye from them.
- **ROC/AUC:** not researched.
- **Accuracy section of S-ch05-01:** it does not itself warn about imbalanced data. Attribute that warning to S-ch05-06; S-ch05-01 §3.4.4.4 (balanced accuracy) only implies it.

### 4. Chart data recommendation
- **Option A (recommended for the epoch chart):** use real data with a confirmed origin and compute the curve ourselves. The UCI Digits dataset (CC BY 4.0, DOI 10.24432/C50P49) is available in scikit-learn as `load_digits`. A script would train with a fixed seed and a fixed train/test split, record train and test accuracy for each epoch to a CSV under `python/data/`, and the chart caption would say it was computed by the author.
  - A clear overfitting gap is not guaranteed. The chart should show whatever actually comes out, without tuning settings until the hoped-for shape appears.
- **Option B (summary table or bar chart):** use Zhang et al. Table 1 (p. 6), which gives real published CIFAR10 train and test accuracy. Train accuracy is 100 or close to it everywhere. Test accuracy is 50–89% with true labels and about 10% with random labels (for example, Inception: 100.0 train vs 9.78 test). The full table is transcribed in the file.
  - This is not a per-epoch chart.
  - Because the arXiv license is not Creative Commons, cite the numbers with attribution only and do not reproduce the figure.
  - I transcribed the numbers from page images, so the Reviewer should re-check them against the PDF.
- **Option C (only if the classic curve shape is required):** use simulated data. Per PRD §10, the chart and caption must be labeled explicitly as demo data, with a description of how it was generated.

### 5. Files written
- C:\biu01\HW2\ai_book_starter\docs\sources\chapter_05.md (new file)

I did not modify any other file. The fetched PDF was saved automatically by the fetch tool to C:\Users\baroy\.claude\projects\C--biu01-HW2-ai-book-starter\b0a8136a-c716-4290-aef0-3d0bd081ec50\tool-results\webfetch-1794921927172-m2t4sm.pdf, which is outside the repo.
```

## קבצים שנוצרו או שונו
- נוצר: `docs/sources/chapter_05.md` (31,930 בתים)
- `git status` (15:28:43): הופיעו רק `docs/sources/` וקובץ ההרצה של ch03 שה-Orchestrator כתב. אין שינויים בקבצים במעקב.

## שער האיכות של ה-Orchestrator
| בדיקה | תוצאה |
|---|---|
| קובץ קיים, עם כל הסעיפים | ✅ |
| לפחות 2 מקורות מאומתים | ✅ 11 מקורות: 10 בטקסט מלא, 1 במטא-דאטה בלבד |
| רמת גישה לכל רשומה | ✅ (11 רשומות, 11 שדות של רמת גישה) |
| נוסחאות | ✅ accuracy, ‏precision, ‏recall, ‏FPR, ‏F-beta. שיעור השגיאה הוא נגזרת שמסומנת במפורש |
| הערכת נתונים לגרף | ✅ שלוש אפשרויות, והמלצה מנומקת |
| כתיבה רק בתחום | ✅ |

**הערכת איכות:** הכיסוי טוב מאוד, ומרבית המקורות זמינים בטקסט מלא. החלק החשוב לשלב M4 הוא אפשרות A: נתוני Digits אמיתיים (CC BY 4.0) והרצה משלנו. היא עומדת בדרישת PRD סעיף 5 (נתונים אמיתיים שמקורם מאומת), ואין בה צורך לנחש מספרים. המספרים מטבלה 1 של Zhang et al. הועתקו מתמונת עמוד, ולכן Reviewer צריך לבדוק אותם שוב.

**החלטה:** השער עבר.
