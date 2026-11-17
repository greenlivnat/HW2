# הרצה: writer-agent, יחידה ch01, סבב 2 (M3, תיקון)

| שדה | ערך |
|---|---|
| תאריך | 2026-11-17 |
| סוכן | `writer-agent` |
| הופעל על ידי | Orchestrator, בעקבות `review_ch01_r1.md` (REVISE, ‏84/100) |
| התחלה / סיום | 20:19 בקירוב / 20:24 בקירוב (משך לפי הכלי: 353.5 שניות) |
| שימוש | 5 קריאות לכלים, 86,388 טוקנים |
| קובץ פלט | `chapters/chapter_01.txt` (עותק הגרסה: `agents/runs/versions/chapter_01_r2.txt`) |

## הפרומפט המלא שנשלח

```
M3 REVISION, unit ch01, round 2.

Read first: agents/writer_agent.md; the review report agents/runs/review_ch01_r1.md (verdict REVISE, score 84/100); the current chapter chapters/chapter_01.txt (your round-1 text; a frozen copy is at agents/runs/versions/chapter_01_r1.txt — do not touch the copy); docs/SOURCES.md and docs/sources/chapter_01.md for every source check. PRD v1.3 §6 style rules still apply.

TASK: revise chapters/chapter_01.txt to fix ALL 10 defects in the report (R-ch01-01 … R-ch01-10). Write ONLY chapters/chapter_01.txt.

Priorities:
- R-ch01-01 (medium, originality): rewrite the deep-learning passage in your own words and structure. Do not translate the LeCun et al. abstract sentence by sentence. Keep the claims at abstract level [S-ch01-05].
- R-ch01-02 (medium, style): explain every term in that passage at first use, in plain Hebrew with an everyday image: backpropagation (give a Hebrew name, e.g. "התפשטות לאחור", English in parentheses, and one sentence of intuition that stays within S-ch01-05 / S-ch01-08), representations, internal parameters. If a term (e.g. genomics) is not needed, drop it rather than explain it.
- R-ch01-05: soften the two insights so they say no more than their sources. If part of an insight is the book's own framing, don't attach a citation to that part.
- R-ch01-07: reduce the "שלנו, לא מתוך המקור" disclaimers. Use one clear, graceful framing where it matters (the scene is an illustration; the hierarchy is the book's framing). Integrity rules still hold: an invented example must still read clearly as an illustration, and the hierarchy must still not appear as a sourced fact.
- R-ch01-08: no Hebrew sentence may start with a Latin-script word; fix the agreement in "AI יוצר".
- R-ch01-10: reduce the repetition of "דוח" and of "התגבש". Strengthen the sense of wonder and the wide view in the middle of the chapter, in your own original voice (no Sagan imitation), without adding unsourced facts.
- R-ch01-03, 04, 06, 09: as suggested in the report. On length: the Orchestrator's Python count of real words (excluding tags and markers) for round 1 was 1,165. Keep the body at or below roughly the current length, and do not grow it.

All source rules from round 1 remain binding: cite only IDs in SOURCES.md, within each record's access level; S-ch01-04 and S-ch01-06 bibliographic only; no Samuel quote; no Turing 10^9 number; any new factual claim needs an existing record, otherwise list it under "Needs research" and do not write it.

FINAL MESSAGE:
1. A table: defect ID → what was changed (or why not), for EVERY defect R-ch01-01 … R-ch01-10.
2. Source IDs used (note any change from round 1).
3. Needs research (if any).
4. Approximate body word count.
```

## הפלט הגולמי שהסוכן החזיר

```
## הדוח של סוכן הכתיבה: M3, יחידה ch01, סבב 2

תיקנתי את כל עשרת הליקויים בקובץ אחד בלבד: C:\biu01\HW2\ai_book_starter\chapters\chapter_01.txt. לא נגעתי בעותק המוקפא `agents/runs/versions/chapter_01_r1.txt` ולא בקבצים אחרים.

**ספירת מילים:** לגוף הפרק יש כ-1,170 מילים, בלי כותרות, סימוני קופסאות וכיתוב האיור, ובלי תגי ציטוט. את הספירה עשיתי ביד, פסקה אחר פסקה, כי לא היה לי כלי להריץ Python, ולכן היא משוערת. בסבב 1 הייתה 1,165 מילים, כך שהאורך כמעט לא השתנה. כדאי לאמת בספירת ה-Python של השער. אם יוצא יותר מ-1,165 וצריך לקצר עוד, הכי פשוט להוריד את פסקת הפליאה על המעטפות (כ-47 מילים) או את אחד התבליטים בתובנות.

### 1. טבלת ליקויים

| ליקוי | מה שונה |
|---|---|
| R-ch01-01 | כתבתי את קטע הלמידה העמוקה מחדש בסדר ובתחביר משלי. יש בו שתי פסקאות, ובכל אחת שאלה מנחה: "ומה פירוש 'עמוקה'?" ואחריה "ומה קובע את התיאור שכל שכבה מפיקה?". הרעיון בשפה פשוטה: כל שכבה בונה את התיאור שלה לנתונים מתוך התיאור של השכבה שלפניה, וכך נוצרות כמה רמות של הפשטה. אחר כך באה אנלוגיית הילד שלומד לקרוא, ואחריה האלגוריתם ותחומי השיפור כרשימה קצרה. הטענות נשארו ברמת התקציר [S-ch01-05]. |
| R-ch01-02 | **התפשטות לאחור:** המונח מופיע לראשונה כ"התפשטות לאחור (backpropagation)" בשיטת האימון ש-AI100 מתאר [S-ch01-08]. ההסבר: האלגוריתם שמסמן למכונה איך לשנות את הכפתורים בכל שכבה [S-ch01-05], עם דימוי של טכנאי במערבל קול. **ייצוג:** "לתיאור כזה קוראים ייצוג (representation)". **פרמטרים:** "מספרים פנימיים... שאפשר לדמות לכפתורים במערבל קול", עם הפניה למשקולות בפרק 3. **רמת השיא:** "התוצאות הטובות ביותר שהושגו עד אז". **גנומיקה:** הושמטה. |
| R-ch01-03 | "מומחי AI100 מונים כמה גורמים שהזינו את מהפכת הבינה המלאכותית, ובראשם הבשלתה של למידת המכונה [S-ch01-08]". |
| R-ch01-04 | "...ומנסה לקבוע מי מבין שני משתתפים סמויים הוא הגבר ומי האישה. ואז הוא שואל מה יקרה אם מכונה תתפוס את מקומו של אחד מהם [S-ch01-02]". את המילים "רק לפי תשובות כתובות" שהציע הדוח לא הוספתי, כי הן לא מופיעות ברשומה. |
| R-ch01-05 | **תבליט 3:** "לפי ההגדרה של מיטשל, מערכת למדה אם הביצועים שלה במשימה, לפי מדד מוגדר, משתפרים באופן אמין בעקבות ניסיון [S-ch01-03]". **תבליט 4:** הציטוט [S-ch01-05] מחובר רק ל"שכבה על גבי שכבה של ייצוגים". המשפט "במטריושקה של הספר... ולא שם נרדף" מנוסח כמסגרת של הספר, בלי ציטוט. |
| R-ch01-06 | **מה התקצר:** פסקת הסיום של הפתיחה, תיאור מיצירת העדכון של OECD, וההסתייגויות. **מה הושמט:** משפט סמואל ותבליט "הכתבים המייסדים" (כפול לתוכן שבגוף הפרק). אלה פיצו על ההסברים שנוספו, ולכן האורך נשאר בערך כמו בסבב 1. |
| R-ch01-07 | **סצנת הבצק:** נפתחת ב"דמיינו שעת ערב מאוחרת" ומסתיימת ב"לתמונה הזאת נחזור לאורך הספר". **ההיררכיה:** מסגור אחד, "הספר הזה מציע תמונה משלו: בובת מטריושקה", בלי ציטוט. **כיתוב האיור:** "המפה מסכמת את המסגרת של הספר". **קופסת "מושג חשוב":** רק "לדוגמה". **הוסרו:** "לשם המחשה", "אנלוגיה שלנו" ו"שלנו, לא מתוך המקור". |
| R-ch01-08 | **משפט בלועזית:** אין משפט שנפתח במילה לועזית; "התפשטות לאחור" באה לפני המונח האנגלי. **דרטמות':** "ונתנו לנושא את השם artificial intelligence, כלומר בינה מלאכותית". **התאם:** "מערכות של בינה מלאכותית יוצרת (generative AI)". **מעבר לדוח:** בקופסה השורות T:/P:/E: נפתחו באות לטינית, ולכן שיניתי אותן ל"המשימה (T):", "המדד (P):" ו"הניסיון (E):". |
| R-ch01-09 | "הארגון לשיתוף פעולה ולפיתוח כלכלי (OECD), ארגון בין-ממשלתי, בחר...". הניסוח נשען על סוג המקור ברשומה S-ch01-09. |
| R-ch01-10 | **"דוח":** לא מופיע עוד בגוף הפרק. במקומו "פאנל המומחים", "הפאנל", "מומחי AI100", "הפאנל של סטנפורד", "חיבור" ו"לדבריו". **"התגבש":** נשאר רק אצל הטבח. במטריושקה הוא הוחלף ב"נבנית", ובתובנה 2 ב"מתכנת את עצמו". **פליאה:** נוספה פסקה אחרי נתון ה-85%: "עצרו רגע מול המספר הזה. על כל מעטפה כזאת כתב מישהו בכתב ידו... מיומנות שקשה להסביר במילים נלמדה בלי הסבר." הפסקה לא מוסיפה עובדות מעבר ל-S-ch01-03. |

### 2. מזהי מקורות
- **בשימוש:** S-ch01-01, 02, 03, 04, 05, 07, 08, 09, 10.
- **שינוי מסבב 1:** S-ch01-06 (סמואל) לא מצוטט עוד, כי המשפט הושמט כדי לשמור על האורך, ולכן הסרתי אותו גם מרשימת "מקורות לפרק".
- **רמות גישה:** S-ch01-04 נשאר ביבליוגרפי בלבד. S-ch01-05 נשאר ברמת התקציר. אין ציטוט של סמואל ואין את המספר 10^9 של טיורינג.

### 3. נדרש מחקר
אין. לא נוספה טענה עובדתית בלי רשומה קיימת.
```

## שער האיכות של ה-Orchestrator (20:24)
- `git status` ו-MD5: הסוכן שינה רק את `chapters/chapter_01.txt` (MD5 חדש 7ade0b33...). העותק `chapter_01_r1.txt`, ‏`review_ch01_r1.md`, ‏`docs/SOURCES.md` ו-`docs/sources/chapter_01.md` לא השתנו.
- מזהים: S-ch01-01 עד 05 ו-07 עד 10. כולם קיימים ב-`SOURCES.md`. ‏S-ch01-06 הוסר.
- בדיקה של משפטים שנפתחים במילה לועזית: נמצאה התאמה אחת, "Nilsson", והיא חיובית שגויה (אחרי "Nils J."). אין משפט כזה.
- **ממצא:** ספירת Python של מילים נקיות (בלי תגיות וסימונים): **1,247**, לעומת 1,165 בסבב 1. בספירה הגולמית, כמו זו של הסוקר: 1,328. הפרק התארך למרות ההנחיה, והספירה הידנית של ה-Writer (1,170) לא הייתה מדויקת. ה-Orchestrator לא קובע את החומרה של הממצא, אלא מעביר אותו ל-Reviewer.
- **תקלת תיעוד:** סקריפט ה-bash הראשון שכתב את הקובץ הזה נכשל בשגיאת ציטוט (`unexpected EOF`), ולא נכתב אז שום קובץ. הקובץ נכתב מחדש מאותם תכנים. הפרומפט ל-Reviewer, סבב 2, נשלח כרגיל.
- **החלטה:** השער עבר, עם הממצא. הצעד הבא: reviewer-agent, סבב 2.
