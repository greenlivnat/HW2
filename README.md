<div dir="rtl">

# מאחורי הקלעים של הבינה המלאכותית
### מהנתון הראשון ועד לתשובה שעל המסך

**מחברות:** ליאת קפהזידר ולבנת בנסון · **קוד קבוצה:** LIATLVNT · **מטלה:** 02

ספר מדע פופולרי בעברית (PDF, ‏43 עמודים) על הדרך שעוברת שאלה שהוקלדה לצ'טבוט, עד שעל המסך מופיעה תשובה. הספר נכתב, נבדק והודר במערכת של סוכני בינה מלאכותית (Claude Code), בהנחיית המחברות ובפיקוחן. כל שלב בתהליך מתועד בריפו הזה.

<p align="center">
  <img src="screenshots/01_cover.png" width="23%" alt="כריכה">
  <img src="screenshots/03_chapter_opener.png" width="23%" alt="פתיחת פרק 1">
  <img src="screenshots/05_temperature_chart.png" width="23%" alt="פרק 4: גרף הטמפרטורה">
  <img src="screenshots/06_experiment_chart.png" width="23%" alt="פרק 5: תוצאות הניסוי">
</p>

> ✅ **הפרויקט הושלם: גרסה v1.0 (2026-11-20).** הספר אושר להגשה אחרי ביקורת חיצונית סופית של v0.95 ב-ChatGPT.

| | |
|---|---|
| 📕 הספר | [`book.pdf`](book.pdf) (גרסה נוכחית), גרסאות קודמות ב-[`releases/`](releases/) |
| 🧭 סטטוס | [`docs/STATUS.md`](docs/STATUS.md) |
| 📜 שינויים | [`CHANGELOG.md`](CHANGELOG.md) |
| 🧯 תקלות | [`docs/INCIDENTS.md`](docs/INCIDENTS.md) (IR-01 עד IR-19) |
| 📦 תיעוד חיצוני | [`docs/external/ai_book_documentation/`](docs/external/ai_book_documentation/) (ChatGPT, תהליך וגרסאות קודמות) |

---

## 1. חזון הספר
הספר עוקב אחרי חוט עלילתי אחד: קוראת ששואלת מכונה למה הבצק שלה לא תפח. משם הוא יורד שכבה אחר שכבה: מה זו בינה מלאכותית (פרק 1), איך מכונה לומדת מנתונים (2), מה קורה בתוך רשת נוירונית (3), איך מודל שפה מייצר תשובה טוקן אחר טוקן (4), איך בודקים מודל (5), מה המכונה לא יודעת (6), ומה תפקידו של האדם (7). הנספח, "כך נוצר הספר שאתם קוראים", מספר איך הספר עצמו נבנה.

עקרונות המסמך המחייב (`docs/PRD.md`):
- **כל טענה עם מקור מאומת.** אין מקורות, נתונים או צילומי מסך מומצאים.
- **ניסוי אמיתי.** הגרף בפרק 5 מחושב בניסוי של הספר, ולא מנתונים מדומים.
- **כל המחשה נוצרת מקוד.** ‏Matplotlib ו-TikZ, בלי תמונות חיצוניות.
- **סגנון מדע פופולרי בקול מקורי:** פתיחה בשאלה, סיום בתובנות, וחמש תיבות תוכן קבועות.

## 2. ארכיטקטורת הסוכנים
חמישה סוכנים בארכיטקטורת כוכב. סוכן-העל מתאם, והסוכנים לא מדברים זה עם זה ישירות. כל המידע עובר דרך קבצים, כך שלכל שלב נשאר תיעוד.

```mermaid
flowchart TB
    U([המחברות]) -->|בקשה, אישור| O[Orchestrator<br/>סוכן-העל]
    O -->|משימה בקובץ| R[research-agent<br/>מחקר ואימות מקורות]
    O -->|משימה בקובץ| W[writer-agent<br/>כתיבה ותיקון פרקים]
    O -->|משימה בקובץ| V[reviewer-agent<br/>ביקורת · Detector]
    O -->|דוח ליקויים| F[fixer-agent<br/>תיקון מינימלי]
    R -->|docs/SOURCES.md| W
    W -->|chapters/*.txt| V
    V -->|VERDICT: PASS / REVISE| O
    V -.->|ליקוי שיטתי| O
    O -->|CLS · ממיר · סקריפטים| B[(build.py → book.pdf)]
    B -->|qa-super: 8 Skills| V
```

| סוכן | תפקיד | כותב רק ל- |
|---|---|---|
| **Orchestrator** | מתכנן, מפעיל, בודק שערים (`git status`, ספירות, מזהים), מתעד. אינו כותב תוכן במקום הסוכנים | `docs/STATUS.md`, ‏`agents/runs/*` |
| **research-agent** | מאתר מקורות ומאמת אותם (DOI, רמת גישה, ציטוט ומיקום) | `docs/sources/`, ‏`docs/SOURCES.md` |
| **writer-agent** | כותב ומתקן פרקים על בסיס מקורות מאומתים בלבד | `chapters/*.txt` |
| **reviewer-agent** | ביקורת בלתי תלויה עם ציון ופסק. במצב **Detector** מאתר ליקויים ב-PDF המהודר | `agents/runs/review_*.md` |
| **fixer-agent** | מתקן במינימום שינוי לפי דוח. ליקוי שיטתי מוסלם לסוכן-העל ומתוקן בכלי, לא בטקסט | `chapters/*.txt` |

**כללים:** סוכן אחד בכל רגע; עד 3 סבבי תיקון ליחידה; כל דוח ביקורת מסתיים ב-`VERDICT: PASS` או `VERDICT: REVISE`; כל הפעלה מתועדת ב-`agents/runs/<agent>_<unit>_r<N>.md` (הפרומפט המלא והפלט הגולמי). הפרוטוקול: [`agents/orchestrator_agent.md`](agents/orchestrator_agent.md).

**Skills** (`.claude/skills/`, ‏13): חמישה נהלי סוכנים (`agent-*`) ושמונה בדיקות איכות (`qa-*`). הבדיקות הן קוד דטרמיניסטי (`scripts/qa.py`), שבודק כיווניות, טבלאות, קוד וניסוי, איורים, עימוד, תשתית וגרסת התבנית. `qa-super` מריץ את כולן.

## 3. תהליך הפיתוח
```mermaid
flowchart LR
    M1[M1<br/>הקמה, PRD,<br/>Smoke Test] --> M2[M2<br/>מחקר מקורות] --> M3[M3<br/>7 פרקים + נספח<br/>Writer ⇄ Reviewer] --> M4[M4<br/>ניסוי UCI Digits<br/>ואיורים] --> M5A[M5A<br/>CLS · LuaLaTeX<br/>Detector ⇄ Fixer] --> X{{ביקורת חיצונית<br/>ChatGPT}} --> M5B[M5B + M6<br/>תיקונים · README] --> M7[M7<br/>הגשה]
```

| שלב | מה נעשה | ראיות |
|---|---|---|
| M1 | PRD, ארכיטקטורת סוכנים, ‏Smoke Test (‏80 ← 92) | `agents/runs/smoke_test/` |
| M2 | 73 רשומות מקור, 61 שמישות; כל פרק עם 3 מקורות שמישים לפחות | `docs/SOURCES.md` |
| M3 | Writer ← Reviewer לכל פרק, commit לכל פרק שעבר | `agents/runs/m3_summary.md` |
| M4 | ניסוי מוגדר מראש, ‏3 גרפי Matplotlib ו-7 תרשימי TikZ | `python/`, ‏`latex/figures/` |
| M5A | תבנית `aibook.cls`, ממיר TXT ל-TeX, ‏IEEE, ‏Detector ‏84 ← Fixer ← ‏96 | `agents/runs/review_m5a_r2.md` |
| ביקורת חיצונית | ChatGPT מצא ליקויי עימוד ודיוקים מדעיים שהביקורת הפנימית פספסה | `prompts/12_m5b_m6_external_review.txt` |
| M5B + M6 | תיקונים בכלים, מקורות חדשים, נספח מורחב, Detector, ‏README | `agents/runs/*_m5b_*` |

### גרף השיפור: ציוני הביקורת הפנימית
<img src="assets/charts/figA_2_scores.png" width="70%" alt="ציונים ראשוניים מול סופיים">

> אלה **ציוני ביקורת פנימית של reviewer-agent**, בסבב הראשון ובסבב האחרון של כל יחידה. הם אינם ציון של מרצה או של בודק אנושי. הנתונים: [`python/data/review_scores.csv`](python/data/review_scores.csv).

## 4. תוצאות הניסוי (פרק 5)
מסווג MLP קטן (שכבה נסתרת אחת של 32 נוירונים) על **UCI Optical Recognition of Handwritten Digits**. מקור הנתונים: Alpaydin & Kaynak, 1998, ברישיון CC BY 4.0. העותק הוא `load_digits` של scikit-learn: ‏1,797 תמונות של 8×8 פיקסלים. כל ההגדרות נקבעו **לפני ההרצה** ב-[`python/experiment_config.json`](python/experiment_config.json): ‏seed ‏42, חלוקה של 75% אימון ו-25% בדיקה עם ריבוד, ‏40 תקופות. לניסוי אין קבוצת אימות. קבוצת הבדיקה נמדדת לדיווח בלבד.

| מדד | ערך |
|---|---|
| דוגמאות אימון / בדיקה | 1,347 / 450 |
| דיוק אימון בסוף (תקופה 40) | 0.998 |
| דיוק בדיקה בסוף (תקופה 40) | 0.976 |
| פער הכללה מוערך בסוף | 2.2 נקודות אחוז |
| הפער המרבי | 3.8 נקודות, בתקופה 8 (0.920 מול 0.882) |

<img src="screenshots/06_experiment_chart.png" width="45%" alt="דיוק אימון מול דיוק בדיקה">

שחזור: `python python/generate_chart.py` כותב את `python/data/digits_accuracy.csv`. הבדיקה `python scripts/qa.py code --rerun` מריצה את הניסוי מחדש ומשווה את התוצאה לקובץ השמור.

## 5. מבנה הפרויקט
```
ai_book_starter/
├── book.pdf                 # הספר (נוצר ב-build.py)
├── main.tex                 # מסמך-העל: כריכה, קרדיטים, תוכן, פרקים, ביבליוגרפיה
├── references.bib           # נוצר מ-chapters/*.txt (IEEE)
├── chapters/*.txt           # מקור האמת לתוכן (כותבים ומתקנים כאן)
├── latex/
│   ├── aibook.cls           # התבנית (v1.2.0, עם CHANGELOG פנימי)
│   ├── chapters/*.tex       # נוצרים מה-TXT, לא עורכים ידנית
│   ├── figures/*.tex        # תרשימי TikZ
│   └── layout_tight.tex     # נוצר ב-scripts/layout.py
├── python/                  # הניסוי, הגרפים והנתונים (data/)
├── assets/charts/           # גרפי Matplotlib (PDF + PNG)
├── scripts/                 # build, txt2tex, make_bib, qa, layout, screenshots
├── docs/                    # PRD, OUTLINE, STATUS, SOURCES, INCIDENTS, PROMPT_HISTORY, TODO, PLAN
├── agents/                  # הגדרות הסוכנים, runs/ (כל הרצה), tasks/ (משימות)
├── .claude/agents, skills/  # הגדרות תתי-הסוכנים ו-13 Skills
├── prompts/                 # הפרומפטים של המשתמשות, לפי הסדר
├── releases/                # גרסאות PDF משמעותיות
└── screenshots/             # צילומי מסך מתוך הספר
```

## 6. התקנה והידור
**דרישות:** Python 3.13, ‏TeX Live או MiKTeX עם LuaLaTeX, ‏biber ו-latexmk, ‏poppler-utils (`pdftotext`, ‏`pdfinfo`, ‏`pdftoppm`), והגופן **Assistant** (רישיון OFL).

```bash
python -m pip install -r requirements.txt
python scripts/build.py                 # גרפים → bib → TXT→TeX → LuaLaTeX+biber → book.pdf → QA
python scripts/build.py --experiment    # כולל הרצה מחדש של הניסוי
python scripts/qa.py super              # כל בדיקות האיכות → agents/runs/qa/qa_report.md
python scripts/screenshots.py           # צילומי מסך מעודכנים מתוך book.pdf
latexmk main.tex                        # הידור בלבד (LuaLaTeX, לפי .latexmkrc)
```
ב-Windows מריצים `python`, ולא `py`.

## 7. צילומי מסך
| | | |
|---|---|---|
| <img src="screenshots/02_toc.png" alt="תוכן עניינים"> | <img src="screenshots/04_neuron_math.png" alt="נוסחת הנוירון"> | <img src="screenshots/07_appendix_scores.png" alt="נספח: ציוני הביקורת"> |
| תוכן עניינים, עם מספור זהה ל-PDF | פרק 3: הנוסחה והסימון המתמטי | הנספח: איור נ.2 |

## 8. התפתחות הגרסאות
| תגית | commit | מה | PDF |
|---|---|---|---|
| v0.1 | `32317ba` | הקמה (M1) ומחקר מקורות (M2) | |
| v0.2 | `57f249d` | השלמת הכתיבה (M3): 7 פרקים ונספח | |
| v0.9 | `d5b7b50` | ספר מלא לפני הביקורת החיצונית (46 עמ') | [`releases/book_v0.9.pdf`](releases/book_v0.9.pdf) |
| v0.95 | `498ec46` | אחרי תיקוני הביקורת החיצונית (43 עמ') | [`releases/book_v0.95.pdf`](releases/book_v0.95.pdf) |
| **v1.0** | `283bd03` ואחריו commit הסיום | **גרסת ההגשה הסופית**. הספר זהה ל-v0.95, ונוספו התיעוד החיצוני ואישור הביקורת החיצונית הסופית | [`releases/book_v1.0.pdf`](releases/book_v1.0.pdf) |

פירוט: [`CHANGELOG.md`](CHANGELOG.md).

## 9. ניהול משאבים וטוקנים
- **עד סוף M5A:** תועדו 51 הפעלות של תתי-סוכנים, ולשלוש מהן לא נרשם מספר טוקנים. סך הכול **3,511,855 טוקנים**:

  | סוכן | הפעלות | טוקנים |
  |---|---:|---:|
  | writer | 20 | 1,277,930 |
  | reviewer | 19 | 1,408,658 |
  | research | 11 | 722,285 |
  | fixer | 1 | 102,982 |
- **M5B:** research ‏137,008 (החלק שאחרי החידוש), ‏writer ‏137,161, ‏Detector: ראו `agents/runs/reviewer_m5b_r1.md`.
- **אמצעי חיסכון:**
  - סוכן אחד בכל רגע (אחרי HTTP 429, ‏IR-03).
  - קובצי משימה ועובדות במקום הדבקת הקשר ארוך.
  - בדיקות איכות בקוד במקום קריאה של מודל.
  - סבב Detector/Fixer אחד לכל הספר.
  - איחוד משימות של אותו סוכן להרצה אחת.
  - הניסוי רץ פעם אחת, ונבדק לשחזור רק בסוף.
- **נקודות התאוששות:** טבלת חבילות ב-`docs/STATUS.md` §0. אחרי ניתוק בודקים את `git status` וממשיכים מהחבילה הראשונה שלא הושלמה.

## 10. תקלות, פתרונות ולקחים
`docs/INCIDENTS.md` כולל 19 רשומות. כל רשומה מפרידה בין עובדות להשערות, ומסתיימת במניעה שיטתית. מבחר:

| # | תקלה | פתרון שיטתי |
|---|---|---|
| IR-01 | PDF ריק אחרי הידור "מוצלח" | סדר טעינה ב-CLS (tikz ו-tcolorbox לפני polyglossia) |
| IR-03, ‏04, ‏18 | ניתוק API, ‏HTTP 429, פקיעת התחברות | נקודות התאוששות; חידוש אותו סוכן; סוכן אחד בכל רגע |
| IR-05, ‏09 | תיבות ותרשימים זזו מחוץ לעמוד; תיבה שבורה איבדה מסגרת | מסגרת LTR מפורשת ב-CLS; תיבות לא נשברות |
| IR-12 | עובדה שגויה בקובץ העובדות של סוכן-העל | מספרים על הניסוי מחושבים מה-CSV ולא נכתבים ביד |
| IR-14 | עברית הפוכה בגרפים | ‏Matplotlib 3.11 מסדר עברית בעצמו; בדיקה התנהגותית ב-qa-img |
| IR-15 | תיבת תובנות לבדה בעמוד כמעט ריק | `scripts/layout.py` מסדר פרקים צפוף יותר באופן אוטומטי |
| IR-16 | ‏`x_i` ו-`\sum` כטקסט גולמי | סימון `$...$` בממיר; ‏qa-typeset נכשל על TeX גולמי |
| IR-19 | בנייה שנתקעה (לא שוחזרה) | מגבלת זמן לכל שלב ב-build.py |

**לקחים:**
1. **בדיקה אוטומטית היא תנאי הכרחי ולא מספיק.** ‏qa-super עבר נקי, וליקויים חזותיים נמצאו רק בבדיקה בעין, אצל Detector ואצל ChatGPT. כל ליקוי כזה הפך לבדיקה חדשה.
2. **ליקוי שחוזר מתקנים בכלי ולא בטקסט.** תיקון אחד בתבנית או בממיר תיקן את כל הפרקים בבת אחת.
3. **עין מבחוץ.** מודל אחר, שלא השתתף בכתיבה, מצא את מה שהביקורת הפנימית (‏96, ‏PASS) לא מצאה.
4. **התאוששות מתחילה במה שקיים בפועל** (`git status`, קבצים), ולא במה שזוכרים שנעשה.
5. **ציון פנימי הוא כלי בקרה ולא אישור איכות.** ההחלטה על הגשה נשארת אצל המחברות.

### בקרת איכות בגרסה v0.95
- **qa-super:** ‏**92 PASS · 0 WARN · 0 FAIL** (`agents/runs/qa/qa_report.md`). כולל את השחזור של הניסוי, שיצא זהה בית אחר בית.
- **שחזור הספר:** אחרי ניקוי מלא של קובצי הביניים, `build.py` הפיק ספר בן 43 עמודים עם טקסט זהה (השוואת hash של `pdftotext`).
- **Detector:** ‏93, ‏REVISE. שני הליקויים הבינוניים (D-m5b-01, ‏D-m5b-02) תוקנו, ואחריהם האימות האוטומטי עבר.

### ליקויים ידועים (קלים, אינם חוסמים הגשה)
| מזהה | ליקוי | סיבה |
|---|---|---|
| D-m5b-03 | נוסחאות ארוכות בתיבת המעבדה בפרק 3 נשברות בין שורות בפסקה מימין לשמאל | התיקון דורש שינוי בשבירת השורות של מתמטיקה בתוך RTL בממיר |
| D-m5b-06 | ברשומה [60] בביבליוגרפיה כתובת ה-URL נשברת אחרי "https:", ויש מילים בעברית בתוך רשומות באנגלית | נתוני ה-bib ושבירת URL. התיקון שיטתי (make_bib, ‏CLS) |

## 11. התוצר הסופי מול תיעוד הגרסאות הקודמות
| | מה זה | איפה |
|---|---|---|
| ✅ **התוצר הסופי (v1.0, ‏43 עמ')** | הספר, קוד המקור שלו, הגרפים והתרשימים, וצילומי המסך שבסעיף 7. הספר זהה ל-v0.95 | [`book.pdf`](book.pdf), ‏[`releases/book_v1.0.pdf`](releases/book_v1.0.pdf), ‏[`screenshots/`](screenshots/) |
| 🕘 גרסה קודמת (v0.9, ‏46 עמ') | הספר לפני הביקורת החיצונית | [`releases/book_v0.9.pdf`](releases/book_v0.9.pdf) |
| 🕘 תיעוד תהליך (חיצוני) | חבילת ChatGPT: ביקורת על v0.9, יומן ליווי, צילומי טרמינל מהעבודה, ועמודי טיוטה של v0.9 | [`docs/external/ai_book_documentation/`](docs/external/ai_book_documentation/) |
| 🕘 תיעוד תהליך (פנימי) | כל הרצה של כל סוכן, דוחות ביקורת ו-QA | [`agents/runs/`](agents/runs/), ‏[`docs/PROMPT_HISTORY.md`](docs/PROMPT_HISTORY.md) |

### גרפים ותרשימים של התוצר הסופי
- **גרפי Matplotlib** (נוצרים מקוד, ב-[`python/make_figures.py`](python/make_figures.py)):
  - [פונקציות הפעלה (3.1)](assets/charts/fig3_1_activations.png)
  - [טמפרטורה (4.1)](assets/charts/fig4_1_temperature.png)
  - [ניסוי UCI Digits (5.1)](assets/charts/fig5_1_accuracy.png)
  - [ציוני הביקורת הפנימית (נ.2)](assets/charts/figA_2_scores.png)
- **תרשימי TikZ** (קוד מקור ב-[`latex/figures/`](latex/figures/), מוצגים בספר): עיגולים מקוננים (1.1), מסלול הדוגמאות (2.1), רשת נוירונים (3.2), מודל שפה ב-9 בלוקים (4.2), גבולות הידע (6.1), האדם במעגל (7.1), ארכיטקטורת הסוכנים (נ.1).
- **צילומי מסך נבחרים מהספר:**
  - [כריכה](screenshots/01_cover.png)
  - [תוכן עניינים](screenshots/02_toc.png)
  - [פתיחת פרק](screenshots/03_chapter_opener.png)
  - [נוסחה](screenshots/04_neuron_math.png)
  - [טמפרטורה](screenshots/05_temperature_chart.png)
  - [ניסוי](screenshots/06_experiment_chart.png)
  - [נספח](screenshots/07_appendix_scores.png)

## 12. חבילת התיעוד החיצונית (ChatGPT)
המחברות ליוו את העבודה בשיחה עם ChatGPT, והתיעוד ממנה שולב כמו שהוא, בלי עריכה, בתיקייה [`docs/external/ai_book_documentation/`](docs/external/ai_book_documentation/). **החבילה מתעדת את התהליך ואת הגרסאות הקודמות.** היא אינה בדיקה עצמאית של התוצר הסופי. לפי ההערה שלה עצמה, ה-PDF בן 43 העמודים לא נבדק בה.

| תיקייה | תוכן | גרסה |
|---|---|---|
| [`README.md`](docs/external/ai_book_documentation/README.md) | תיאור החבילה וסייגיה | |
| [`external_review/EXTERNAL_REVIEW.md`](docs/external/ai_book_documentation/external_review/EXTERNAL_REVIEW.md) | **הביקורת החיצונית** שהובילה ל-M5B | v0.9 (46 עמ') |
| [`pdf_draft_pages/`](docs/external/ai_book_documentation/pdf_draft_pages/) | 9 עמודים מ-v0.9 שעליהם נכתבה הביקורת (לפני התיקונים) | v0.9 |
| [`screenshots/`](docs/external/ai_book_documentation/screenshots/) | 16 צילומי טרמינל אמיתיים: הסביבה, ההקמה, ה-Smoke Test, ‏M2, ניתוק ה-API ב-M4 ופקיעת ההתחברות ב-M5B | M1–M5B |
| [`notes/`](docs/external/ai_book_documentation/notes/) | יומן התקדמות, אינדקס פרומפטים, תוכנית M3, וסיכום v0.95 | M1–v0.95 |
| [`visuals/`](docs/external/ai_book_documentation/visuals/) | תרשימי סוכנים, גרפי מחקר וציונים (עם קוד Python), ופלטה מוצעת | M1–v0.95 |

**הבהרות:**
- הגרפים בחבילה מבוססים על דיווחי Claude Code. ‏`overfitting_demo` מבוסס על **נתונים סינתטיים להמחשה**, והוא אינו תוצאת הניסוי של הספר. תוצאות הניסוי נמצאות בסעיף 4.
- הציונים בחבילה הם ציוני ביקורת פנימית של הסוכנים, לא ציוני הגשה.
- לפני השילוב נבדקו כל הקבצים, כולל כל 16 צילומי המסך והמטא-דאטה של התמונות. לא נמצא מידע אישי רגיש: אין תעודות זהות, כתובות מייל, שמות משתמש, מפתחות או סיסמאות. מופיעים רק נתיב הפרויקט וגרסאות הכלים.
- קובץ הדיווח הרשמי למרצה נפרד מהריפו ואינו כלול בו.

## 13. רישיונות וקרדיטים
- **נתונים:** UCI Optical Recognition of Handwritten Digits (Alpaydin & Kaynak, 1998), ‏CC BY 4.0.
- **גופן:** Assistant, ‏SIL Open Font License.
- **מקורות:** רשימה מלאה בסגנון IEEE בסוף הספר, ואינדקס עם רמת הגישה של כל מקור ב-`docs/SOURCES.md`.
- **הפקה:** Claude Code (Anthropic) בהנחיית המחברות.

</div>



## Independent Codex Quality Review and Collaborative Engineering

**The original v1.0 book remains unchanged. Proposed publication corrections are preserved separately as independent review evidence and have not been incorporated into a newly compiled PDF.**

The independent Codex review followed the original Claude Code development workflow. Academic, publication and technical reviewers identified findings. The Fixer prepared targeted changes, and an independent Detector checked their scientific scope, LTR markup and all 64 chapter citation keys. The review addresses the Turing question's punctuation, ReLU and causal attention, the limits of the image-level experiment split, and the units and scope of two Chapter 7 studies.

The experiment CSV reproduced byte for byte. The review workflow recorded 16 experiment checks, 5 focused regressions and 17 independent image checks. Aggregate QA had 75 passes and one failure for missing compiled output. The Detector confirmed Figure 5.1 values. Matplotlib separately reported an Assistant font fallback. The original figures remain in the publication.

Liat performed the initial Git Pull, created the personal branch and recovered the Python and TeX tooling. She chose to preserve the consistent, published v1.0 artifact and defer uncompiled corrections. The review documents the failed format initialization, preventive QA proposals and the separation between the original and follow-up work.

[Original book](book.pdf) | [Baseline page 8](screenshots/03_chapter_opener.png) | [Review and QA evidence](docs/CODEX_REVIEW.md) | [Proposed patch and recovery instructions](docs/review-evidence/README.md) | [PRD](docs/PRD.md) | [Incidents](docs/INCIDENTS.md) | [Codex Skills](agents/codex/skills/README.md) | [Prompt history](docs/PROMPT_HISTORY.md) | [Collaboration](COLLABORATION.md) | [PR description](docs/PULL_REQUEST.md)
