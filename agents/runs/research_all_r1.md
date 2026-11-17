# הרצה: research-agent, יחידה all (איחוד), סבב 1 (M2)

| שדה | ערך |
|---|---|
| תאריך | 2026-11-17 |
| סוכן | `research-agent` |
| הופעל על ידי | Orchestrator, אחרי ששמונה הרצות המחקר (שבעה פרקים ועוד סבב 2 לפרק 7) עברו את השער |
| התחלה | 15:32:50 JST בקירוב |
| סיום | 16:02:40 JST בקירוב (משך לפי הכלי: 1,790.3 שניות) |
| שימוש | 10 קריאות לכלים, 173,328 טוקנים |
| קלט | `docs/sources/chapter_01.md` עד `chapter_07.md` |
| קובץ פלט | `docs/SOURCES.md` |

## הפרומפט המלא שנשלח

```
M2 RESEARCH, unit all (consolidation), round 1.

Read agents/research_agent.md and ALL seven per-chapter source files: docs/sources/chapter_01.md … chapter_07.md (written in earlier research runs; chapter_07 includes a round-2 addition).

Task: build docs/SOURCES.md — the consolidated source index that the Writer will use. Do NOT copy all detail; the per-chapter files remain the detailed evidence and stay unchanged. SOURCES.md must contain (Hebrew; bibliographic fields in original language):
1. Header: purpose, date 2026-11-17, and an explicit statement that each ID's full record, supported claims (with locations), examples, gaps and fetch log are in docs/sources/chapter_XX.md, which are part of the verified source base.
2. Usage rules for the Writer: only usable IDs; claims must stay within the record's access level (abstract-only → abstract-level claims; metadata-only → bibliographic/historical mention only, no content claims); items flagged "do not use" in the chapter files must not be used.
3. Per chapter: a table of ALL IDs with columns: ID | short citation (authors, year, title) | type | access level | reliability | status (שמיש / מטא-דאטה בלבד / לא לשימוש) | main topics supported. Plus a short "main gaps" list per chapter (copied faithfully from the chapter file, condensed).
4. Cross-chapter section: works that appear under more than one ID (e.g., same paper/page in different chapters) → list them as duplicates (same work), check that their bibliographic details are consistent across files and report any inconsistency; and useful cross-references (e.g., a chapter's gap covered by a source verified in another chapter — e.g., the bias-example gap in ch06 vs Gender Shades in ch02).
5. A unified bibliography draft (one entry per distinct work, alphabetical, with DOI/URL as recorded), marking which IDs map to it.
6. Summary table: per chapter — number of records, number usable, count by access level (טקסט מלא / תקציר בלבד / מטא-דאטה בלבד).

You do not need to re-fetch sources; this is a consolidation run. If you find an internal inconsistency you cannot resolve from the files, report it rather than guessing. NEVER invent anything not in the chapter files.

Write ONLY docs/SOURCES.md. Do not modify docs/sources/*.

Final message: structured report (counts per chapter, duplicates found, inconsistencies found, files written).
```

## הפלט הגולמי שהסוכן החזיר (כפי שהתקבל אצל ה-Orchestrator)

```
## דוח Research Agent: M2 Research, unit all (איחוד), סבב 1

כתבתי את `docs/SOURCES.md`, שמאחד את שבעת קבצי המקורות של הפרקים לאינדקס אחד שה-Writer קורא. לא אוחזר שום מקור מחדש, ואין בקובץ שום פרט שלא מופיע בקבצי הפרקים. בדרך נמצאו כמה אי-עקביויות קטנות, ונקודה אחת דורשת החלטה שלך (I8 למטה).

### 1. מספר רשומות לפי פרק
"שמישות" כולל רשומות בטקסט מלא וגם רשומות בתקציר בלבד. ברשומות של תקציר בלבד, הטענות מוגבלות למה שכתוב בתקציר.

| פרק | רשומות | שמישות | מטא-דאטה בלבד | לא לשימוש | טקסט מלא | תקציר בלבד | רמת גישה: מטא-דאטה |
|---|---|---|---|---|---|---|---|
| 1 | 10 | 8 | 2 | 0 | 7 | 1 | 2 |
| 2 | 14 | 12 | 2 | 0 | 9 | 3 | 2 |
| 3 | 4 | 3 | 1 | 0 | 2 | 1 | 1 |
| 4 | 8 | 8 | 0 | 0 | 7 | 1 | 0 |
| 5 | 11 | 10 | 1 | 0 | 10 | 0 | 1 |
| 6 | 13 | 10 | 3 | 0 | 7 | 3 | 3 |
| 7 | 13 | 10 | 2 | 1 | 4 | 6 | 3 |
| **סה"כ** | **73** | **61** | **11** | **1** | **46** | **15** | **12** |

- הרשומה היחידה בסטטוס "לא לשימוש" היא S-ch07-12, גרסת SSRN של Bastani. היא נשמרה רק כדי לתעד את ההבדל בין הגרסאות.
- 73 המזהים מתאימים ל-57 רשומות בביבליוגרפיה המאוחדת. גרסאות שונות של אותה עבודה רשומות כתת-פריטים, והגרסה שעדיף לצטט מסומנת.

### 2. כפילויות (אותה עבודה תחת כמה מזהים)
- **בין פרקים:** יש מקרה אחד. S-ch02-11 ו-S-ch05-08 הם אותו עמוד, Google MLCC "Overfitting", עם אותו URL. התוכן תואם, ויש רק הבדלי ניסוח בשדות המוציא לאור והסוג.
- **בתוך פרקים:**
  - Gender Shades: ‏S-ch02-01 ו-02.
  - Datasheets: ‏S-ch02-03, 04 ו-05.
  - Kaufman (גרסת הכנס וגרסת כתב העת): ‏S-ch02-06 ו-07.
  - AI100: ‏S-ch01-07 ו-08.
  - Ji et al.: ‏S-ch06-01, 02 ו-03.
  - Guo et al.: ‏S-ch06-04 ו-05.
  - Carlini et al.: ‏S-ch06-06, 07 ו-08.
  - דוח ה-Copyright Office: ‏S-ch06-11 ו-12.
  - Brynjolfsson et al.: ‏S-ch07-02 ו-03.
  - Amershi et al.: ‏S-ch07-05 ו-06.
  - AI Act: ‏S-ch07-08 ו-09.
  - Bastani et al.: ‏S-ch07-10, 11 ו-12.
  - מערך הספרות (Digits): ‏S-ch05-04 ו-05. אלה שתי עבודות שונות, אבל שתיהן מתארות אותו מערך נתונים.

### 3. אי-עקביויות שנמצאו (פירוט בסעיף 4.2 של SOURCES.md)
- **I1, Gender Shades:** מספור העמודים ב-PDF הוא "81:1–15", ובעמוד הנחיתה 77–91. קובץ הפרק כבר הכריע: לציטוט משתמשים ב-77–91.
- **I2, Ji et al.:** בגרסת arXiv v7 יש 13 מחברים, וב-Crossref יש 10. בנוסף, השם מופיע פעם כ-"Yejin Bang" ופעם כ-"Ye Jin Bang". זה הבדל בין גרסאות. לביבליוגרפיה משתמשים ב-S-ch06-03.
- **I3, Brynjolfsson:** השם מופיע פעם כ-"Lindsey R. Raymond" ופעם כ-"Lindsey Raymond". אי אפשר להכריע מהקבצים איזה נכון. המספרים בין הגרסאות שונים, וזה כבר מתועד בקובץ הפרק.
- **I4, עמוד Overfitting:** לפי פרק 5 דוגמת החלוקה 70/15/15 מופיעה בעמוד Overfitting, ולפי פרק 2 היא מופיעה בעמוד Dividing datasets (איור 9). זו לא בהכרח סתירה, ואי אפשר להכריע בלי לאחזר שוב. המלצתי: לייחס את הדוגמה ל-S-ch02-10.
- **I5, הכותרת של chapter_06:** הכותרת אומרת שרק S-ch06-09 היא ברמת מטא-דאטה בלבד. בפועל גם S-ch06-03 ו-S-ch06-07 ברמה הזו. הרשומות עצמן קובעות.
- **I6, מערך הספרות:** ב-S-ch05-04 כתוב "E. Alpaydin" ותאריך July 1998. ב-S-ch05-05 כתובים Alpaydin & Kaynak ותאריך June 30, 1998. לציטוט משתמשים ב-S-ch05-05.
- **I7, S-ch04-01:** המיקום של h=8 רשום פעם כ"עמ' 4–5" ופעם כ"עמ' 5". הבדל קטן.
- **I8, דורש החלטה שלך:** S-ch01-04 ו-S-ch07-09 הן ברמת מטא-דאטה בלבד, אבל קבצי הפרקים מאשרים בהן פריטים מסוימים:
  - ב-S-ch01-04: משפט מעמוד הספר באתר המחבר.
  - ב-S-ch07-09: תאריכי התחולה של ה-AI Act.

  זה מתנגש עם הכלל "מטא-דאטה בלבד = בלי תוכן". ההצעה השמרנית שלי: לאשר את התאריכים כמידע ביבליוגרפי, ולא להשתמש במשפט מ-S-ch01-04, אלא להסתמך על S-ch01-03.
- **I9 ו-I10:** השנה של Samuel ושל GPT-2 כבר הוכרעו בקבצי הפרקים.

### 4. הצלבות חשובות
- **X1:** הפער בפרק 6 (אין דוגמה אמפירית של הטיה) מכוסה על ידי Gender Shades, ‏S-ch02-01, בטקסט מלא. יש שתי הסתייגויות חובה:
  - הקשר לנתוני האימון הוא השערה של המחברות.
  - מדובר במסווגי תמונות, ולא במודלי שפה.
- **X2:** S-ch02-14 מכסה רק חלקית את הפער של automation bias בפרק 7. זו הגדרה ממקור לימודי, ולא ממצא אמפירי.
- **X9:** S-ch07-08 ו-09 מכסים רק חלקית את הפער של EU AI Act בפרק 6. נבדק רק סעיף 14, ולא נבדקו הוראות על פרטיות או זכויות יוצרים.
- **X5, אזהרה:** "temperature" מופיע ב-S-ch04-03 (דגימה) וב-S-ch06-04 (כיול). אלה שני שימושים שונים, ואסור לערבב ביניהם.
- יש עוד קשרים נושאיים. הרשימה המלאה (X1–X17) והפערים שאף פרק לא מכסה נמצאים בסעיף 4.3.

### 5. מה עוד יש בקובץ
- כללי שימוש ל-Writer.
- טבלה לכל פרק, עם כל המזהים ועם הפערים העיקריים.
- רשימה מרוכזת של פריטים וטענות שאסור להשתמש בהם (סעיף 3.8).
- טיוטת ביבליוגרפיה מאוחדת לפי סדר אלפביתי.
- טבלת סיכום.

### 6. קבצים
- נכתב קובץ אחד בלבד: `C:\biu01\HW2\ai_book_starter\docs\SOURCES.md`. הוא חדש, לא היה קיים קודם.
- הקבצים `docs/sources/chapter_01.md` עד `chapter_07.md` נקראו ולא שונו.
- **URLs שאוחזרו בהרצה הזו:** אין. זו הרצת איחוד.
```

## קבצים שנוצרו או שונו
- נוצר: `docs/SOURCES.md` (65,984 בתים)
- `docs/sources/*` לא שונו. ה-MD5 של chapter_02 ‏(`46ebe729`), chapter_04 ‏(`18e0a006`) ו-chapter_07 ‏(`b3624ece`) זהה לערכים שנרשמו בשערים הקודמים. לשאר ארבעת הקבצים לא נשמר MD5 לפני ההרצה, ולכן לגביהם יש רק את הדיווח של הסוכן. זו מגבלה של הבדיקה.
- `git status` (16:03:30): נוספו רק `docs/SOURCES.md` ו-`docs/sources/`, יחד עם קובצי ההרצה שה-Orchestrator כתב.

## שער האיכות של ה-Orchestrator
| בדיקה | תוצאה |
|---|---|
| קובץ קיים, עם כל ששת הסעיפים שנדרשו | ✅ (כללים, מקרא, טבלאות לפי פרק, הצלבות, ביבליוגרפיה, סיכום) |
| לפחות 2 מקורות שמישים לכל פרק | ✅ המינימום הוא 3 (פרק 3), המקסימום 12 |
| כפילויות ואי-עקביויות דווחו ולא הוסתרו | ✅ 13 קבוצות כפילויות ו-10 אי-עקביויות |
| כתיבה רק בתחום | ✅ |

## החלטת ה-Orchestrator על I8
אני מאמץ את ההצעה השמרנית:
- **S-ch07-09:** מותר להשתמש בה רק לתאריכי האימוץ והתחולה, כמידע ביבליוגרפי ורגולטורי. אסור להסתמך עליה לטענות על תוכן החוק.
- **S-ch01-04:** אין להשתמש במשפט מעמוד הספר. את הגדרת הלמידה מצטטים מ-S-ch01-03 (טקסט מלא).

ההחלטה תועבר ל-Writer בפרומפט של שלב M3. לא נדרש סבב מחקר נוסף.

**החלטה:** השער עבר. שלב המחקר (M2) הושלם.
