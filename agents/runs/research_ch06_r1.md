# הרצה: research-agent, יחידה ch06, סבב 1 (M2)

| שדה | ערך |
|---|---|
| תאריך | 2026-11-17 |
| סוכן | `research-agent` |
| הופעל על ידי | Orchestrator, אחת משבע הרצות שרצו במקביל |
| התחלה | 15:23:40 JST בקירוב |
| סיום | 15:28:38 JST בקירוב (משך לפי הכלי: 298.0 שניות) |
| שימוש | 33 קריאות לכלים, 100,374 טוקנים |
| קובץ פלט | `docs/sources/chapter_06.md` |

## הפרומפט המלא שנשלח

```
M2 RESEARCH, unit ch06, round 1.

Read first: agents/research_agent.md (UPDATED spec: record fields incl. mandatory access level, one record per URL, examples/formulas/data section, visualization ideas, fetch log, open-API fallback rules), docs/PRD.md sections 5 and 10, docs/OUTLINE.md.

Chapter 6 — "מה AI יודע — ומה לא" (~3 pages). Topics per PRD §5: hallucinations; uncertainty (and calibration); biases; privacy; copyright; responsible use. PRD requires examples WITHOUT attributing unfounded facts — so every example must be documented. Visual: case boxes.

Requirements:
- At least 2, ideally 4–6, VERIFIED reliable sources covering the subtopics; prefer academic/scientific and official institutional documents. Candidates you MAY check (verify by fetching): Ji et al. 2023 "Survey of Hallucination in Natural Language Generation" (ACM Computing Surveys / arXiv); Guo et al. 2017 "On Calibration of Modern Neural Networks" (PMLR); Carlini et al. 2021 "Extracting Training Data from Large Language Models" (USENIX Security / arXiv); Bender et al. 2021 "On the Dangers of Stochastic Parrots" (FAccT); NIST AI Risk Management Framework 1.0 (2023); U.S. Copyright Office reports on copyright and AI; a documented real-world case of hallucinated legal citations (e.g. court record Mata v. Avianca, 2023) only if verifiable from an official/court or reputable source. Choose what you can actually verify.
- Record access level honestly. For each documented case, give exactly what the source says, with location.
- Visualization ideas (marked as suggestions), e.g. case boxes.
- NEVER invent sources, DOIs, URLs, quotes, cases or numbers.

Output: write ONLY docs/sources/chapter_06.md (Hebrew; bibliographic fields in original language). IDs: S-ch06-01, ... Structure: header; records; "דוגמאות, נוסחאות ונתונים" (documented cases); "רעיונות להמחשה (הצעות)"; "פערים / לא אומת"; "יומן אחזורים".

Final message: structured report (verified sources count + access level each, all URLs OK/FAILED, gaps, files written).
```

## הפלט הגולמי שהסוכן החזיר (כפי שהתקבל אצל ה-Orchestrator)

```
פרק 6 (ch06), סבב 1, הושלם. כתבתי 13 רשומות (S-ch06-01 עד S-ch06-13, רשומה אחת לכל URL) שמכסות 7 מקורות שונים. 12 רשומות אומתו לשימוש. רשומה אחת, Bender et al., אומתה ברמת מטא-דאטה בלבד ואסור להשתמש בה לטענות תוכן. כל ששת נושאי הפרק מכוסים, אבל יש פערים (סעיף 3).

## 1. פרק 6 ומקורות מאומתים

| מזהה | מקור | רמת גישה |
|---|---|---|
| S-ch06-01 | Ji et al., Survey of Hallucination in NLG, דף arXiv | תקציר בלבד |
| S-ch06-02 | Ji et al., גרסת HTML ב-arXiv (נקראו סעיפים 2, 2.1, 3) | טקסט מלא, חלקי |
| S-ch06-03 | Ji et al., ACM Computing Surveys 55(12), 2023, DOI 10.1145/3571730 (דרך Crossref) | מטא-דאטה בלבד |
| S-ch06-04 | Guo et al. 2017, עמוד PMLR 70:1321–1330 | תקציר בלבד |
| S-ch06-05 | Guo et al. 2017, קובץ PDF של PMLR (עמ' 1321–1323) | טקסט מלא, חלקי |
| S-ch06-06 | Carlini et al., arXiv:2012.07805 | תקציר בלבד |
| S-ch06-07 | Carlini et al., עמוד USENIX Security 21 (עמ' 2633–2650) | מטא-דאטה בלבד |
| S-ch06-08 | Carlini et al., קובץ PDF של USENIX (עמ' 2633, 2640–2641) | טקסט מלא, חלקי |
| S-ch06-09 | Bender et al., FAccT '21, DOI 10.1145/3442188.3445922 (דרך Crossref) | מטא-דאטה בלבד, **לא לטענות תוכן** |
| S-ch06-10 | NIST AI 100-1 (AI RMF 1.0), ינואר 2023 (סעיף 3 כולו, עמ' 12–18) | טקסט מלא, חלקי |
| S-ch06-11 | דף הנחיתה של U.S. Copyright Office בנושא AI (שלושת חלקי הדוח ותאריכיהם) | טקסט מלא |
| S-ch06-12 | Copyright Office, Part 2: Copyrightability, ינואר 2025 (נקראו ההקדמה ועמ' 39–41, כולל הסיכום) | טקסט מלא, חלקי |
| S-ch06-13 | Mata v. Avianca, 22-cv-1461 (PKC), S.D.N.Y., החלטה על סנקציות, ECF 54, 22.6.2023 (עמ' 1–3, 32–35, 42–43 מתוך 43) | טקסט מלא, חלקי |

מה המקורות מספקים לכתיבה:
- **קופסאות מקרה מתועדות:**
  - Mata v. Avianca: ציטוטים ממסמך בית המשפט בעמ' 1, 34 ו-43.
  - שינון נתוני אימון אצל Carlini: 604 מתוך 1,800 (33.5%), ובטבלה 1 יש 46 שמות של אנשים אמיתיים ו-32 פרטי קשר.
  - ביטחון יתר של ResNet אצל Guo, איור 1.
- **נוסחאות:** כיול מושלם (משוואה 1) ו-ECE (משוואה 3), שתיהן מ-Guo.
- **הגדרות:**
  - הזיה פנימית וחיצונית (Ji, סעיף 2.1).
  - שבעת מאפייני האמינות ושלוש קטגוריות ההטיה (NIST, עמ' 12 ו-18).
  - "Prompts alone ... unlikely" (Copyright Office, עמ' 41).

## 2. כתובות שנבדקו
1. https://arxiv.org/abs/2202.03629: OK
2. https://arxiv.org/html/2202.03629: OK (נקראו 100,000 התווים הראשונים)
3. https://api.crossref.org/works/10.1145/3571730: OK
4. https://proceedings.mlr.press/v70/guo17a.html: OK
5. http://proceedings.mlr.press/v70/guo17a/guo17a.pdf: OK (הקובץ נשמר ונקרא ויזואלית)
6. https://arxiv.org/abs/2012.07805: OK
7. https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting: OK
8. https://www.usenix.org/system/files/sec21-carlini-extracting.pdf: OK
9. https://doi.org/10.1145/3442188.3445922: FAILED (הפניה 302 ל-ACM)
10. https://dl.acm.org/doi/10.1145/3442188.3445922: FAILED (403)
11. https://dl.acm.org/doi/pdf/10.1145/3442188.3445922: FAILED (403)
12. https://api.crossref.org/works/10.1145/3442188.3445922: OK
13. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf: OK
14. https://www.copyright.gov/ai/: OK
15. https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf: OK
16. https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1:2022cv01461/575368/54: FAILED (403)
17. https://storage.courtlistener.com/recap/gov.uscourts.nysd.575368/gov.uscourts.nysd.575368.54.0_1.pdf: OK

בנוסף הרצתי חיפוש רשת אחד כדי לאתר את מסמך Mata v. Avianca. תוצאות החיפוש לא שימשו כמקור.

## 3. פערים ופריטים שלא אומתו
- **Bender et al. 2021:** לא נקרא הטקסט המלא, כי ACM חוסם גישה. אין לייחס למאמר שום טענת תוכן.
- **אי-ודאות במודלי שפה גדולים:** Guo עוסק במסווגים בלבד. העברת הממצאים לצ'טבוטים מותרת רק כאנלוגיה שמסומנת ככזו.
- **אחוזי הזיה כמותיים במודלים עכשוויים:** אין מקור. לא לציין מספרים.
- **הטיות:** אין דוגמה אמפירית ספציפית, רק הגדרות מ-NIST. המסמך NIST SP 1270 לא נבדק.
- **זכויות יוצרים בנתוני אימון:** חלק 3 של דוח ה-Copyright Office לא נקרא. כל הטענות המשפטיות הן מהדין האמריקאי בלבד. דין ישראלי ו-GDPR או EU AI Act לא נבדקו.
- **מספר התקדימים המזויפים ב-Mata:** בעמודים שקראתי לא מופיע מספר כולל מפורש. בעמ' 34 נמנות שש החלטות בשמן, ולכן צריך לנסח "בין היתר שש".
- **גרסאות של Ji et al.:** ההגדרות נקראו בגרסת arXiv v7 משנת 2024. לא אומת שהנוסח זהה לגרסת כתב העת משנת 2023.
- **אנומליה ב-PDF של Carlini, עמ' 2640:** מופיעה שורה חריגה ("Somwhere says 'We extracted 16 individual's contact information...'") שסותרת את טבלה 1. סימנתי אותה בקובץ כאסורה לשימוש.

## 4. קבצים שנכתבו
- C:\biu01\HW2\ai_book_starter\docs\sources\chapter_06.md (הקובץ היחיד שנכתב; docs/SOURCES.md לא שונה)
```

## קבצים שנוצרו או שונו
- נוצר: `docs/sources/chapter_06.md` (33,155 בתים)
- `git status` (15:29:35): אין שינויים בקבצים במעקב.

## שער האיכות של ה-Orchestrator
| בדיקה | תוצאה |
|---|---|
| קובץ קיים, עם כל הסעיפים | ✅ |
| לפחות 2 מקורות מאומתים | ✅ 13 רשומות, 7 עבודות. 12 מהן ניתנות לשימוש |
| רמת גישה לכל רשומה | ✅ (13 מתוך 13) |
| כיסוי ששת הנושאים | ✅ הזיות, אי-ודאות, הטיות (הגדרות בלבד), פרטיות, זכויות יוצרים (דין אמריקאי) ושימוש אחראי |
| מקרים מתועדים ממקור ראשוני | ✅ החלטת בית המשפט ב-Mata v. Avianca, וטבלה 1 של Carlini |
| כתיבה רק בתחום | ✅ |

**הערכת איכות:** טוב מאוד, עם מקורות ראשוניים לקופסאות המקרה. הסוכן זיהה בעצמו שורה חריגה ב-PDF של Carlini ופסל אותה לשימוש, וזו התנהגות נכונה. אפשר לסגור את פער ההטיות בלי מחקר נוסף, כי Gender Shades כבר מאומת בפרק 2 (S-ch02-01), ופרק 6 יכול להפנות אליו.

**החלטה:** השער עבר.
