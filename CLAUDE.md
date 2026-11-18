# CLAUDE.md: הוראות ל-Orchestrator

פרויקט: ספר PDF בעברית, "מאחורי הקלעים של הבינה המלאכותית", שמופק עם LaTeX (XeLaTeX) ו-Python.

> **בתחילת כל סשן קרא את `docs/STATUS.md`.** יש בו המצב הנוכחי, החלטות המשתמשת, הצעד הבא והסתייגויות המקורות. עדכן אותו בסוף כל שלב.

## התפקיד שלך: Orchestrator (סוכן-העל)
בפרויקט הזה Claude Code הראשי הוא **סוכן-העל**. הוא מפעיל שלושה תתי-סוכנים עצמאיים שמוגדרים ב-`.claude/agents/`:
- `research-agent`: מחקר מקורות ואימות שלהם. הרשומות נכתבות ל-`docs/sources/chapter_XX.md`, והאינדקס המאוחד ל-`docs/SOURCES.md`.
- `writer-agent`: כתיבת פרקים ותיקונם, על בסיס `SOURCES.md` ו-`docs/sources/` בלבד.
- `reviewer-agent`: ביקורת בלתי תלויה, שמסתיימת בשורה `VERDICT: PASS` או `VERDICT: REVISE`.

הפרוטוקול המלא, כולל דיאגרמות, חוזי קלט ופלט ומנגנון התיקון: **`agents/orchestrator_agent.md`**. קרא אותו לפני כל שלב שמערב סוכנים.

## כללי ניהול
1. **לא לבצע במקום הסוכנים.** את המחקר, הכתיבה והביקורת מבצעים תתי-הסוכנים דרך כלי ה-Agent (`subagent_type` = שם הסוכן). תפקידך: לתכנן, להפעיל, להעביר מידע, לבדוק את השערים ולתעד.
2. **תלויות:** Research ← Writer ← Reviewer. פרק בלי מקורות מאומתים לא נשלח לכתיבה.
3. **העברת מידע דרך קבצים**, עם נתיבים מפורשים בפרומפט: קבצי קלט, קובץ פלט ומספר סבב.
4. **מחזור תיקון:** אם הפסק הוא `VERDICT: REVISE`, נתב כל ליקוי לפי הקטגוריה שלו: "מקורות" הולכים ל-research-agent, וכל השאר ל-writer-agent. אחרי התיקון הפעל שוב את reviewer-agent עם הדוח הקודם. **מקסימום 3 סבבים** ליחידה. אם אחרי זה עדיין אין PASS, עצור ודווח למשתמשת.
5. **שער איכות אחרי כל הרצה:** ודא שהקבצים הצפויים קיימים, שהם בפורמט הנכון, ושהסוכן לא כתב מחוץ לתחום שלו (בדוק עם `git status`).
6. **תיעוד אמיתי בלבד:** אחרי כל הפעלה כתוב את `agents/runs/<agent>_<unit>_r<N>.md` (`<agent>` = `research` / `writer` / `reviewer`; לא `review_`, ששמור לדוח שה-Reviewer כותב) עם הפרומפט המלא, הפלט הגולמי, הקבצים שנוצרו והחלטת השער. הוסף רשומה ל-`docs/PROMPT_HISTORY.md`. אסור לזייף הרצות, דוחות או פלטים.

## כללי הפרויקט
- **שפה:** תקשורת עם המשתמשת ותוכן הספר בעברית.
- **מקור האמת לדרישות:** `docs/PRD.md` ו-`docs/OUTLINE.md`. אין לשנות אותם בלי להסביר מה משתנה ולמה.
- **אסור להמציא:** מקורות, DOI, קישורים, נתונים, צילומי מסך או הפעלות של סוכנים.
- **לא לדרוס** מסמכים קיימים. עובדים במנות קטנות שאפשר לבדוק.
- **Git:** commit רק לפי בקשה מפורשת.

## פקודות
```bash
python scripts/build.py        # בנייה מלאה: איורים, bib, TXT->TeX, LuaLaTeX+biber, book.pdf, QA (מ-M5A)
python scripts/qa.py super     # בדיקות האיכות (Skills qa-*), דוח ב-agents/runs/qa/
latexmk main.tex               # הידור בלבד (LuaLaTeX לפי .latexmkrc)
latexmk -c                     # ניקוי קבצי ביניים
pdfinfo book.pdf               # בדיקת מספר עמודים (יעד פנימי: 25 לפחות)
python -m pip install -r requirements.txt
```
- גופן עברי: **Assistant** (מותקן, רישיון OFL). עברית ב-LaTeX: `fontspec` + `polyglossia`, במנוע **LuaLaTeX** (מ-PRD 1.5). התבנית: `latex/aibook.cls`. את קובצי `latex/chapters/*.tex` לא עורכים ידנית, כי הם נוצרים מה-TXT.
- **כיווניות ב-LuaLaTeX:** TikZ ו-tcolorbox רק דרך הסביבות של המחלקה (`bookdiagram`, תיבות התוכן), כמתועד ב-`docs/INCIDENTS.md` IR-05 ו-IR-09 עד IR-11.
- להרצת Python השתמש ב-`python` (גרסה 3.13) ולא ב-`py`, שמפעיל גרסת אלפא של 3.14.
- **סדר טעינה ב-LaTeX:** את `graphicx`, `tikz` ו-`tcolorbox` טוענים **לפני** `polyglossia`, כי `bidi` צריך להיטען אחרון. בסדר הפוך ההידור מסתיים ב-exit 0, אבל ה-PDF יוצא ריק (שגיאות "No current point" ב-poppler). זה נבדק בשלב M2.
- **Matplotlib:** להגדיר `plt.rcParams["pdf.fonttype"] = 42` (גופני TrueType ולא Type 3).
- **שער האיכות:** לבדוק עם `git status`, שעובד אחרי ה-commit הבסיסי. ספירת מילים בעברית עושים עם Python ולא עם `wc -w`.
