# הרצה: reviewer-agent, יחידה ch01, סבב 1 (M3)

| שדה | ערך |
|---|---|
| תאריך | 2026-11-17 |
| סוכן | `reviewer-agent` |
| הופעל על ידי | Orchestrator |
| התחלה / סיום | 20:13 בקירוב / 20:18 בקירוב (משך לפי הכלי: 276.2 שניות) |
| שימוש | 20 קריאות לכלים, 81,024 טוקנים |
| דוח שהסוכן כתב | `agents/runs/review_ch01_r1.md` |
| קלט שנבדק | `chapters/chapter_01.txt` = `agents/runs/versions/chapter_01_r1.txt` (MD5 8624919d...) |

## הפרומפט המלא שנשלח

```
M3 REVIEW, unit ch01, round 1.

Read first: agents/reviewer_agent.md; docs/PRD.md v1.3 (sections 5 ch.1, 6 incl. the new "סגנון הכתיבה" bullets, 10, 11); docs/OUTLINE.md; docs/SOURCES.md (sections 1, 3.1, 3.8); docs/sources/chapter_01.md (full records: supported claims, access levels, gaps).

Deliverable under review: chapters/chapter_01.txt (written by writer-agent, round 1). Note: no .tex/PDF exists yet (M5), so PDF/DoD items that need a compiled book are "לא רלוונטי בשלב זה", not pass.

Check:
1. FACTS & SOURCES (highest priority): for EVERY inline citation [S-ch01-NN], verify the sentence against that record's supported claims and access level in docs/sources/chapter_01.md. Spot-check at least 3 claims against the original source online with WebFetch (e.g., the Dartmouth proposal at http://www-formal.stanford.edu/jmc/history/dartmouth/dartmouth.html, the OECD page https://oecd.ai/en/ai-principles, the AI100 "Defining AI" page, Mitchell 2006 PDF http://www.cs.cmu.edu/~tom/pubs/MachineLearning.pdf). Flag: claims beyond access level; metadata-only records (S-ch01-04, S-ch01-06) used for content; any use of the Samuel quote; the AI⊃ML⊃DL hierarchy presented as sourced fact; numbers/dates without source or context (e.g., the 85% figure must be framed as 2006); uncited substantive factual claims; invented illustrations presented as fact.
2. STRUCTURE (PRD §5 ch.1 and the user's style brief): covers definition of AI, AI vs ML vs DL, what makes a system learn, AI vs ordinary software, road map consistent with OUTLINE titles; opens with an intriguing question; ends with key insights; sets up the book's narrative thread (from the typed question to the answer); boxes and illustration marker present; source list at the end.
3. STYLE: popular science in the spirit of Carl Sagan but in an ORIGINAL voice (flag any imitation or borrowed signature phrases); rich, accessible, professional Hebrew; everyday stories/analogies; no repetition and no generic phrasing; every technical term explained at first use; correct Hebrew grammar and correct gender agreement; English terms placed sensibly for RTL.
4. LENGTH: PRD target ~2 pages; Orchestrator's brief 900–1,200 words. Count with Python (`python`, not `py`; `len(text.split())` on the body before "## מקורות לפרק"). Do not use `wc -w`.
5. ORIGINALITY: no copied sentences from sources (compare quoted/paraphrased definitions against the originals).

Output: write ONLY agents/runs/review_ch01_r1.md, in Hebrew, with:
- header (unit, round, date, what was checked, which URLs you fetched and the result);
- a defect table: ID (R-ch01-01...), location (section heading + quote snippet), category (עובדות / מקורות / מבנה / סגנון / מקוריות / עיצוב / טכני), severity (קריטי / בינוני / קל), description, suggested fix;
- a citation verification table: every citation in the chapter → record → verdict (תואם / חורג / לא תואם);
- a short style assessment (strengths and weaknesses, concrete examples);
- DoD summary (PRD §11) per item: עובר / לא עובר / לא רלוונטי בשלב זה;
- a line `SCORE: <n>/100` with a brief rubric breakdown (facts & sources 40, structure 20, style 25, length & format 15);
- LAST line exactly `VERDICT: PASS` or `VERDICT: REVISE` (REVISE if any open קריטי or בינוני defect).
Do not edit any other file.

Final message: report path, defect counts by severity and category, the score, and the verdict line.
```

## הפלט הגולמי שהסוכן החזיר

```
פרק 1 לא עבר בסבב הזה: VERDICT: REVISE, ציון 84/100. אין ליקויים קריטיים, אבל יש שני ליקויים בחומרה בינונית, ושניהם באותה פסקה, הפסקה על למידה עמוקה.

הדוח: C:\biu01\HW2\ai_book_starter\agents\runs\review_ch01_r1.md

**ספירת ליקויים: 10 בסך הכול**
- לפי חומרה: 0 קריטיים, 2 בינוניים, 8 קלים.
- לפי קטגוריה: סגנון 5 (אחד מהם בינוני), מקוריות 1 (בינוני), עובדות 1, מקורות 1, מבנה 1, עיצוב 1. אין ליקויים טכניים.

**שני הליקויים הבינוניים**
- **R-ch01-01 (מקוריות):** שלושה משפטים עוקבים הם תרגום כמעט מילולי של תקציר המאמר של LeCun, Bengio ו-Hinton מ-2015, בלי סימון ציטוט.
- **R-ch01-02 (סגנון):** באותה פסקה יש מונחים שלא מוסברים בהופעה הראשונה: backpropagation (באנגלית בלבד ובלי הסבר), ייצוגים, פרמטרים פנימיים, גנומיקה.

**הליקויים הקלים**
- **R-ch01-03:** ניסוח "מגמות המחקר" לא מדויק. ב-AI100 כתוב "factors [that] have fueled the AI revolution".
- **R-ch01-04:** תיאור משחק החיקוי של טיורינג עמום.
- **R-ch01-05:** שתי תובנות מרכזיות מנוסחות חזק יותר ממה שהמקורות שלהן אומרים.
- **R-ch01-06:** חריגה קלה באורך.
- **R-ch01-07:** יותר מדי הסתייגויות בנוסח "שלנו, לא מתוך המקור", שקוטעות את הקריאה.
- **R-ch01-08:** סיכוני כיווניות (משפט שנפתח במילה באנגלית) ובעיית התאם ב"AI יוצר".
- **R-ch01-09:** OECD לא מוצג לקורא.
- **R-ch01-10:** חזרות על המילה "דוח" ועל הפועל "התגבש", ותחושת הפליאה נחלשת באמצע הפרק.

**ניתוב:** כל הליקויים יכולים ללכת ל-writer-agent. R-ch01-05 מסווג "מקורות", אבל מתקנים אותו בניסוח בלבד, בלי צורך במקור חדש.

**מה נבדק**
- **ציטוטים:** בדקתי את כל 25 הציטוטים בגוף הפרק מול הרשומות ב-`docs/sources/chapter_01.md`. 22 תואמים ו-3 חורגים קלות. אין שימוש בפריטים האסורים מסעיף 3.8, ובפרט אין את המשפט המיוחס לסמואל.
- **רשומות מטא-דאטה בלבד:** S-ch01-04 ו-S-ch01-06 משמשות רק לאזכור ביבליוגרפי, כמותר.
- **ההיררכיה AI ⊃ ML ⊃ DL:** מוצגת במפורש כמסגרת של הספר ולא כעובדה ממקור.
- **הנתון 85%:** ממוסגר נכון כנתון מ-2006.
- **מול המקור ברשת:** אימתתי שישה מקורות בעמודים המקוריים: הצעת דרטמות', עמוד העקרונות של OECD, פוסט העדכון של OECD, שני עמודי AI100 ומאמר טיורינג. את הדוח של מיטשל כלי האחזור לא הצליח לפענח, ולכן חילצתי את הטקסט עם `pdftotext` בקריאה בלבד ובדקתי את המשפטים משם.
- **מבנה:** כל דרישות סעיפים 5 ו-6 ב-PRD קיימות, ומפת הדרך תואמת את הכותרות ב-OUTLINE.
- **אורך:** לפי `len(text.split())` על הגוף שלפני "## מקורות לפרק" יש 1,246 מילים, מעל טווח הבריף של 900–1,200.
- **Definition of Done:** רוב הסעיפים מסומנים "לא רלוונטי בשלב זה", כי עדיין אין קובצי tex או PDF.

הקובץ היחיד שכתבתי הוא הדוח, ולא נגעתי בשום קובץ אחר.

VERDICT: REVISE
```

## שער האיכות של ה-Orchestrator (20:18)
- `git status`: הקובץ החדש היחיד מהסוכן הוא `agents/runs/review_ch01_r1.md`. ‏MD5 של הפרק לא השתנה (8624919d..., זהה לעותק r1), ו-`docs/SOURCES.md` לא השתנה.
- השורה האחרונה בדוח: `VERDICT: REVISE`. נמצאה שורה `SCORE: 84/100`.
- **הערה על האורך (R-ch01-06):** הסוקר ספר 1,246 אסימונים כולל כותרות, תגיות ציטוט וסימוני קופסאות. ספירת ה-Orchestrator בלי תגיות: 1,165. הסוקר עצמו מציין 1,168 בלי סימונים. לכן החריגה שולית. ה-Writer מתבקש רק לא להאריך את הפרק.
- **ניתוב:** כל 10 הליקויים הולכים ל-writer-agent. R-ch01-05 מסווג "מקורות", אבל התיקון הוא ריכוך ניסוח בגבולות מקורות קיימים, בלי טענה חדשה. לכן אין צורך ב-research-agent (לפי כלל "ניתוב לפי מהות").
- **החלטה:** סבב תיקון 2: writer-agent, ואחריו reviewer-agent עם הדוח הקודם.
