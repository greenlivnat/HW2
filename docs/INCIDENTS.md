# חקר אירועים (Incident Reports)

> כל רשומה מבחינה בין **עובדות** (נבדקו מול קובץ, פלט, לוג או `git`) לבין **השערות** (הסבר סביר שלא הוכח). המקורות לעובדות של IR-01 עד IR-03 ו-IR-06: ‏`docs/PROMPT_HISTORY.md` וקובצי `agents/runs/`. נכתב ב-2026-11-18 (M4/M5A).

| מזהה | שלב | תקלה | מניעה (שיטתית) |
|---|---|---|---|
| IR-01 | M1 | PDF ריק אחרי הידור "מוצלח" | כלל סדר טעינה ב-CLS, ובדיקת טקסט ב-PDF ב-qa-BiDi |
| IR-02 | Smoke Test | ניתוק API לפני כתיבת קובץ הרצה | נקודת התאוששות ב-STATUS §0 |
| IR-03 | M3 | HTTP 429 באמצע הרצת writer | סוכן אחד בכל רגע; חידוש בהודעה לאותו סוכן |
| IR-04 | M4 | ניתוק API אחרי יצירת האיורים | נקודת התאוששות אחרי כל חבילה |
| IR-05 | M5A | תיבות, תרשימים ופסי כותרת זזו אל מחוץ לעמוד | כלל כיווניות ב-CLS, ובדיקה ב-qa-BiDi |
| IR-06 | M3 | נתון שגוי במקור (4.4% ב-Adience) | אימות מול טבלאות הנתונים, לא מול כיתובים |
| IR-07 | M3 | טבלה 5.2 הופיעה לפני 5.1 | qa-table בודק סדר מספור; ‏`\ref` אוטומטי בממיר |
| IR-08 | M5A | תווים חסרים בגופן (₁ ‏₂ ‏σ ‏←) | מיפוי במתמטיקה ב-`esc()`; ‏qa-typeset נכשל על "Missing character" |
| IR-09 | M5A | תיבה שנשברת בין עמודים איבדה מסגרת | תיבות לא נשברות (CLS 1.1.0); qa-BiDi |
| IR-10 | M5A | ליגטורת fi הפוכה במונחים לועזיים בתוך עברית | `Ligatures=NoCommon` בגופנים העבריים; qa-BiDi |
| IR-11 | M5A | תיבת "מילות מפתח" מחוץ לשוליים | סביבה `keywordsbox` ב-CLS; qa-BiDi אוסר tcolorbox גולמי |
| IR-12 | M4 | עובדה שגויה בקובץ העובדות של ה-Orchestrator | עובדות על הניסוי נגזרות מה-CSV בסקריפט |
| IR-13 | M5A | טקסט חורג מהשוליים (17.9pt): נתיב קובץ ארוך בנספח | נתיבים ב-`\nolinkurl` בממיר; `\sloppy` בביבליוגרפיה (הוחלף ב-M5B, ראו IR-17); qa-typeset |
| IR-14 | M4 (התגלה ב-M5B) | עברית הפוכה בגרפי Matplotlib (איורים 4.1, 5.1) | `he()` לא הופכת; qa-img בודק את כיוון העברית בפועל |
| IR-15 | M5A (התגלה ב-M5B) | תיבת תובנות לבדה בעמוד כמעט ריק | `scripts/layout.py` ו-`\chapterlayout` (סידור צפוף בשתי רמות); התיבה נשארת unbreakable; qa-BiDi |
| IR-16 | M3 (התגלה ב-M5B) | סימוני LaTeX גולמיים בטקסט (`x_i`, `\sum`) בפרק 3 | סימון `$...$` בממיר; qa-typeset נכשל על TeX גולמי ב-PDF |
| IR-17 | M5A (התגלה ב-M5B) | כתובות URL "מרווחות" בביבליוגרפיה, מספור עמודים שונה מה-PDF, תווית "נספח" ברשימת המקורות | CLS 1.2.0; qa-typeset בודק מספור ומטא-דאטה |
| IR-18 | M5B | פקיעת התחברות באמצע הרצת research-agent | בדיקת git status וחידוש אותו סוכן; נקודות התאוששות |
| IR-19 | M5B | בנייה שנתקעה ב-LuaLaTeX (לא שוחזרה) | מגבלת זמן לכל שלב ב-build.py |

## IR-01: ‏PDF ריק אחרי הידור "מוצלח" (M1)
- **עובדות:** בבדיקת הסביבה ב-M1 טעינת `polyglossia` לפני `tikz` ו-`tcolorbox` הסתיימה ב-exit 0, אבל ה-PDF יצא ריק, ו-poppler דיווח "No current point". אחרי שינוי סדר הטעינה הדף הומר לתמונה ונבדק חזותית (PROMPT_HISTORY, רשומה 003).
- **מדוע לא התגלה מיד:** קוד היציאה של המהדר היה 0, והבדיקה הייתה מבוססת עליו.
- **השערה:** ‏`bidi` (שנטענת דרך polyglossia ב-XeLaTeX) מגדירה מחדש פקודות גרפיות, ולכן היא צריכה להיטען אחרונה.
- **מניעה:** ב-`latex/aibook.cls` חבילות הגרפיקה נטענות לפני polyglossia, עם הערה שמפנה לכלל. ‏qa-BiDi נכשל אם אין טקסט עברי שניתן לחלץ מה-PDF, כך שקוד יציאה 0 כבר לא מספיק.

## IR-02: ניתוק API ב-Smoke Test
- **עובדות:** החיבור התנתק אחרי שדוח הביקורת של סבב 1 התקבל, ולפני שנכתב `reviewer_smoke_r1.md`. ההתאוששות: רשימת קבצים ו-MD5 מול baseline, וקובץ ההרצה החסר נכתב עם הערה שנכתב אחרי הניתוק. אף סוכן לא הופעל מחדש (PROMPT_HISTORY, רשומה 004).
- **השערה:** תקלה בצד השירות.
- **מניעה:** התיעוד נכתב מיד אחרי כל הפעלה. מ-M4 יש גם טבלת נקודת התאוששות ב-STATUS §0.

## IR-03: ‏HTTP 429 באמצע הרצת writer ‏(M3, ‏ch03 סבב 2)
- **עובדות:** ההרצה נקטעה במגבלת קצב, וחודשה אחרי האיפוס בהודעת SendMessage לאותו סוכן (`agents/runs/writer_ch03_r2.md`).
- **השערה:** עומס של כמה סוכנים במקביל באותו חלון זמן.
- **מניעה:** לפי בקשת המשתמשת ב-M4/M5A, סוכן אחד בכל רגע ומודל חסכוני ככל שמתאים.

## IR-04: ניתוק API באמצע M4 (2026-11-18)
- **עובדות:** הסשן נקטע אחרי שנוצרו `python/experiment_config.json`, ‏`generate_chart.py`, ‏`make_figures.py`, קובצי ה-CSV וה-JSON ושישה קובצי איור, ולפני שתוקנו שני ליקויים שזוהו בבדיקה חזותית:
  - במקרא של איור 4.1 הופיעה מסגרת זהב שנלקחה מהעמודה המודגשת.
  - בתווית של איור 5.1 שולבו מחרוזת עברית הפוכה ומחרוזת LTR, והסדר יצא שגוי.
- **ההתאוששות:** `git status` ורשימת הקבצים הראו שכל התוצרים קיימים, ושלא היה commit. הניסוי **לא** הורץ מחדש. הורץ רק `make_figures.py`, שקורא את ה-CSV הקיים. שני האיורים נבדקו חזותית ותוקנו.
- **השערה:** ניתוק בצד השירות. אין ראיה לסיבה.
- **מדוע לא נמנע:** לא נשמרה נקודת התאוששות אחרי P1–P2.
- **מניעה:** טבלת STATUS §0 מתעדכנת בסוף כל חבילה. ב-`he()` כל שורת תווית מעובדת כמחרוזת שלמה.

## IR-05: תיבות, תרשימים ופסי כותרת זזו אל מחוץ לעמוד (M5A)
- **עובדות:**
  - במעבר ל-LuaLaTeX, ב-`tcolorbox` שבתוך פסקה RTL המסגרת זזה ימינה אל מחוץ לשוליים (בדיקה ב-scratchpad).
  - בהידור הראשון של הספר: פסי הפתיחה של הפרקים לא נראו (רק הטקסט הלבן); בתרשימים 2.1 ו-4.2 הטקסט יצא מחוץ למסגרות; לשוניות הכותרת של התיבות בלטו מחוץ לתיבה; וכותרת הכריכה חסרה.
  - שלושה ניסויים מבודדים הראו:
    - (א) TikZ בהקשר RTL: צומת בלי `text width` מוזז מהמסגרת שלו, והתמונה כולה ממוקמת לא נכון.
    - (ב) עטיפה LTR עם `\pardir TRT` בתוך צומת: צומת עם `text width` מוזז.
    - (ג) `\hbox dir TLT` סביב התמונה, ו-`\textdir TRT` בלבד בצמתים: הכול במקום.
  - התיקון הוטמע ב-CLS: הסגנון `he`, הסביבה `bookdiagram`, וכן הכותרת, הכותרת העליונה, הכותרת התחתונה והכריכה. גם את הלשוניות של כותרות התיבות החליף פס כותרת רגיל.
- **מדוע לא התגלה קודם:** בבדיקת M1 נבדק רק XeLaTeX עם תרשים בן 3 צמתים, בלי צמתים ברוחב קבוע ובלי `remember picture`.
- **השערה:** ב-LuaTeX, קופסה (hbox או vbox) שהכיוון שלה שונה מכיוון התוכן שלה ממוקמת לפי כיוון הקופסה ולא לפי כיוון התוכן. זה מתאים לכל התצפיות, אבל לא נבדק בקוד המקור של LuaTeX.
- **מניעה:** ‏qa-BiDi נכשל אם איור TikZ לא עטוף ב-`bookdiagram`, או אם יש `\pardir` בצומת. ‏qa-super כולל בדיקה חזותית של עמודים מייצגים.

## IR-06: נתון שגוי במקור (M3)
- **עובדות:** הנתון "4.4% ב-Adience" נלקח מכיתוב איור במאמר Gender Shades, והכיתוב סותר את העמודות, את סעיף 3.5 ואת טבלה 3. ‏research-agent תיקן את רשומה S-ch02-01 (IJB-A ‏4.4%, ‏Adience ‏7.4%), והנתון הוסר מהפרק (`agents/runs/research_ch02_r2.md`).
- **מדוע לא התגלה ב-M2:** האימות היה מול הטקסט הנגיש, והכיתוב נראה סמכותי.
- **מניעה:** מספר שמגיע מכיתוב של איור נבדק מול טבלה או גוף הטקסט באותו מקור (כלל ל-Research ול-Detector).

## IR-07: טבלה 5.2 הופיעה לפני 5.1 (M3)
- **עובדות:** בפרק 5 טבלה 5.2 מופיעה בקובץ לפני טבלה 5.1 (נרשם ב-STATUS כמשימה פתוחה).
- **השערה:** הטבלאות מוספרו לפי סדר התכנון ולא לפי סדר ההופעה.
- **מניעה:** ‏qa-table נכשל כשהמספרים אינם עולים לפי סדר ההופעה. ב-PDF המספור נקבע אוטומטית ב-LaTeX, והממיר הופך "טבלה X.Y" שבגוף הטקסט ל-`\ref`. התיקון ב-TXT מוקצה ל-Fixer.

## IR-08: תווים חסרים בגופן (M5A)
- **עובדות:** בהידור הראשון דווח "Missing character" לתווים ₁ ‏₂ ‏₃ ‏σ ו-←, שאינם בגופן Assistant.
- **מניעה:** הפונקציה `esc()` ב-`scripts/txt2tex.py` ממפה אותם למתמטיקה ($x_1$, ‏$\sigma$, ‏$\leftarrow$). ‏qa-typeset נכשל על כל "Missing character", כך שתו חדש ייתפס לפני ההגשה.

## IR-09 עד IR-11: שלושה ליקויי תבנית שהבדיקות האוטומטיות לא תפסו (M5A)
- **עובדות:** ‏Detector r1 (`agents/runs/review_m5a_r1.md`) מצא אותם בבדיקה חזותית, כש-qa-super עמד על 78 PASS ו-0 FAIL.
  - (09) תיבת "תובנות מרכזיות" שנשברה בין עמודים איבדה את המסגרת.
  - (10) ‏"artificial" הוצג כ-"artfiicial". ה-Orchestrator אימת את זה בקובץ בדיקה מבודד, ו-`Ligatures=NoCommon` תיקן.
  - (11) ב-`main.tex` נוצרה תיבת מילות המפתח ב-tcolorbox ישיר, בלי העטיפה של IR-05.
- **מדוע לא התגלו:** בדיקות ה-QA היו טקסטואליות. ‏`pdftotext` מאחד ליגטורות ולכן לא חושף היפוך, ואף בדיקה לא כיסתה שבירת תיבות או שימוש ישיר ב-tcolorbox.
- **השערה (09):** אותו מנגנון של IR-05. החלק השני של תיבה שבורה נבנה מחוץ לעטיפת ה-LTR. לא נבדק לעומק.
- **מניעה:**
  - CLS 1.1.0: תיבות לא נשברות, ‏`Ligatures=NoCommon`, ‏`keywordsbox`.
  - שלוש בדיקות חדשות ב-qa-BiDi: גופנים עבריים בלי ליגטורות, אין `egin{tcolorbox}` מחוץ למחלקה, תיבות `unbreakable`.
  - הלקח: qa-super הוא תנאי הכרחי ולא מספיק, והבדיקה החזותית של Detector נשארת חובה.

## IR-12: עובדה שגויה בקובץ העובדות (M4)
- **עובדות:** ב-`agents/runs/tasks/m4_facts.md` ה-Orchestrator כתב "דיוק הבדיקה לא יורד בשום שלב". ב-CSV, בתקופה 37 יש ירידה מ-0.9733 ל-0.9711. ה-writer העתיק את הטענה, ו-Detector מצא אותה (D-m5a-04).
- **מקור השגיאה:** סיכום "בעין" של הגרף, במקום חישוב מהנתונים.
- **מניעה:** הקובץ תוקן. טענות על צורת עקומה (מונוטוניות, פער מרבי, נקודת התייצבות) מחושבות בסקריפט מתוך ה-CSV, ולא נכתבות ביד.

## IR-13: טקסט חורג מהשוליים (M5A)
- **עובדות:** אחרי סבב Fixer, ‏qa-typeset נכשל: Overfull של 17.9pt בנספח, שנגרם מנתיב קובץ ארוך בהפניה [agents/runs/...] שלא ניתן לשבור. נוסף על כך היה Overfull של 4.1pt בביבליוגרפיה (כתובת URL ארוכה).
- **מדוע לא התגלה קודם:** הנתיב הארוך נוסף לפסקה רק בקיצור של Fixer, ששינה את שבירת השורות.
- **מניעה:** הממיר עוטף נתיבים ב-`\nolinkurl`, שמאפשר שבירה אחרי "/". בביבליוגרפיה נוסף `\sloppy`. ‏qa-typeset ממשיך להיכשל על כל חריגה מעל 5pt.

## IR-14: עברית הפוכה בגרפים (M4, התגלה בביקורת החיצונית ב-M5B)
- **עובדות:** בגרסה v0.9 (עמודים 23 ו-29) התוויות בעברית באיורים 4.1 ו-5.1 הופיעו הפוכות ("ראשה לכ"). הפונקציה `he()` ב-`python/make_figures.py` הפכה ידנית את סדר האותיות, מתוך הנחה ש-Matplotlib אינו תומך בכיווניות. בבדיקה מבודדת (2026-11-18) ‏Matplotlib 3.11.2 הציג מחרוזת עברית רגילה בסדר הנכון, ואת המחרוזת שהופכה ידנית הוא הציג הפוכה.
- **מדוע לא התגלה:** ‏`pdftotext` אינו מחלץ את העברית מקובצי ה-PDF של Matplotlib, ולכן בדיקות ה-QA הטקסטואליות לא ראו אותה. גם "תיקון המקרא והתווית אחרי הניתוק" (IR-04) נשען על אותה הנחה שגויה, ונבדק רק ברזולוציה נמוכה.
- **מניעה:** ‏`he()` מחזירה את הטקסט כמו שהוא. ב-qa-img נוספה בדיקה התנהגותית: מציירים "ש" ואחריה נקודות, ובודקים באיזה צד של התמונה האות נוחתת. כך יודעים אם Matplotlib מסדר מימין לשמאל, ואם זה עקבי עם `he()`.

## IR-15: תיבת "תובנות מרכזיות" בעמוד כמעט ריק (M5A, התגלה ב-M5B)
- **עובדות:** בגרסה v0.9 ארבעה עמודים (11, 20, 25, 38) הכילו רק את תיבת התובנות שבסוף הפרק. הסיבה: אחרי IR-09 כל התיבות הוגדרו `unbreakable`, ותיבה שלא נכנסה בתחתית העמוד עברה בשלמותה לעמוד הבא.
- **ניסיון 1, נכשל:** הגדרנו את התיבה `breakable`. בבדיקה החזותית (עמודים 11–12) התיבה השבורה איבדה את המסגרת, ופס הכותרת זז אל מחוץ לשוליים. זה אישור נוסף ל-IR-09 תחת LuaLaTeX, ולכן השינוי בוטל.
- **ניסיון 2, נכשל בגלל באג:** סידור צפוף לפרקים שנרשמו ב-`latex/layout_tight.tex` לא השפיע על העימוד. הסיבה: `\in@` לא הרחיב את הארגומנט השני שלו, ולכן הבדיקה תמיד נכשלה. האבחון נעשה עם `\typeout` ביומן, והתיקון היה `\edef` לפני הקריאה.
- **הפתרון:** `scripts/layout.py` רץ בתוך `build.py`, ואחרי כל הידור מאתר פרק שהעמוד האחרון שלו מכיל פחות מ-14 שורות. רמה 1 מצמצמת את הרווח בין הפסקאות ואת המרווח בין השורות, ומקטינה את הגופן בתיבת התובנות. פרק שעדיין לא נכנס עובר לרמה 2. ברשימה הסופית: פרקים 1, 3 ו-4, ופרק 3 גם ברמה 2. אחרי התיקון אין עמוד כזה, ובדיקת ה-Detector קבעה שהריווח קריא. הקובץ שנוצר נשמר ב-git, כך ש-`latexmk` לבדו מפיק את אותו ספר.
- **מניעה:** התיבות נשארות unbreakable, ו-qa-BiDi נכשל על כל תיבה שמוגדרת `breakable`.

## IR-16: סימוני LaTeX גולמיים בטקסט (M3, התגלה ב-M5B)
- **עובדות:** בגרסה v0.9 (עמוד 17) הופיעו בטקסט "x_i", ‏"w_i" ו-"\sum_{i=1}^{n}" כמחרוזות. הממיר `scripts/txt2tex.py` מבריח כל `_` ו-`\`, ולא היה סימון למתמטיקה בתוך שורה.
- **מניעה:** הממיר מכיר את הסימון `$...$` ומעביר אותו ל-LaTeX כמו שהוא. ‏qa-typeset נכשל אם הטקסט של ה-PDF מכיל סימוני TeX (`\cmd`, ‏`_{`, ‏`^{`, ‏`x_i`). בבדיקה הראשונה הוא אכן נכשל על עמודים 18–19, לפני תיקון הטקסט.

## IR-17: עימוד הביבליוגרפיה ומספור העמודים (M5A, התגלה ב-M5B)
- **עובדות:** ‏(א) ה-`\sloppy` מ-IR-13 מתח את הרווחים בתוך כתובות ה-URL ("https : / / www"). ‏(ב) עמודי הפתיחה מוספרו בנפרד, כך שבעמוד 29 של ה-PDF הודפס המספר 22. ‏(ג) פתיחת רשימת המקורות נשאה את התווית "נספח", כי מצב הנספח לא אופס. ‏(ד) ב-PDF לא היה שדה מחבר.
- **מניעה (CLS 1.2.0):** ביבליוגרפיה מיושרת לימין בלי מתיחה, ‏URL נשבר אחרי כל תו, ורשומה לא נחצית בין עמודים. מספור ערבי רציף מהכריכה (עמוד 1), ‏`\backmatter` מאפס את מצב הנספח, ו-`\bookauthors` קובע את `pdfauthor`. ‏qa-typeset בודק שכל מספר מודפס שווה למספר העמוד ב-PDF, ושיש שדה מחבר.

## IR-18: פקיעת התחברות באמצע הרצת research-agent ‏(M5B, ‏2026-11-19)
- **עובדות:** ‏research-agent (משימה `agents/runs/tasks/research_m5b_r1_prompt.txt`) נעצר בשגיאה `authentication_failed` ("Login expired") בזמן שאימת DOI. המשתמשת התחברה מחדש (`/login`).
- **בדיקת מצב:** ‏`git status` הראה ש-`docs/sources/chapter_03.md`, ‏`chapter_05.md` ו-`docs/SOURCES.md` לא שונו. לא נכתב פלט חלקי.
- **התאוששות:** אותו סוכן חודש ב-SendMessage עם הקשר מלא (כמו ב-IR-03). לא הופעל סוכן חדש, ולא חזרנו על עבודה.
- **מניעה:** נקודת התאוששות ב-STATUS §00 לפני כל חבילה, ובדיקת `git status` לפני חידוש.

## IR-19: תהליכים שנתקעו (M5B, ‏2026-11-19 עד 2026-11-20)
- **עובדות:** שלוש היתקעויות בשלושה כלים שונים, שאף אחת מהן לא חזרה בהרצה החוזרת:
  - (1) הבנייה הראשונה אחרי ה-writer לא הסתיימה תוך 600 שניות. ‏`main.log` נעצר בעמוד 24.
  - (2) שלב הגרפים (`make_figures.py`, בדרך כלל 2–3 שניות) נעצר אחרי 300 שניות במגבלת הזמן החדשה. כשהורץ לבדו הוא הסתיים תוך 2.5 שניות.
  - (3) קריאה ל-`pdftotext` נשארה פתוחה כתהליך תלוי, ונסגרה ידנית (`taskkill`).
  - בכל המקרים בנייה או קריאה חוזרת, בלי שום שינוי בקבצים, הצליחה.
- **השערה (לא הוכחה):** בעיה ברמת המערכת, למשל סריקת קבצים, ולא באג בכלי מסוים. ההשערה הקודמת, לולאה בתיבה ניתנת לשבירה, נחלשה אחרי (2) ו-(3).
- **מניעה:** מגבלת זמן בכל שלב של `build.py` (‏300 שניות), בכל קריאה לכלי חיצוני ב-`qa.py` (‏240 שניות) וב-`layout.py` (‏60 שניות). תקלה כזו נכשלת עכשיו במפורש במקום להיתקע.


## IR-20 ? Windows execution helper failed before command startup

PowerShell, cmd.exe and Node failed even for working-directory and Git reads. The execution helper reported `helper_unknown_error: setup refresh had errors`. Retrying in both shells and restarting Windows plus updating Codex did not restore the managed execution path. Launching Codex in Windows unelevated sandbox mode restored five read-only diagnostics. This establishes recovery of process startup. MiKTeX execution and restricted paths require their own verification. The specific cause of the original helper failure was not established.

## IR-21 ? Quantitative and causal claims escaped structural checks

CR-01 through CR-03 resulted from loss of units or scope when translating results and mechanisms into prose. Source-key checks could validate the presence of citations but could not compare the claim to its primary passage. The committee now requires result-unit, population, comparator and mask-index checks against the original study. See [the evidence table](CODEX_REVIEW.md).

## IR-22 ? Mixed-direction question punctuation

The automatic Latin detector wrapped letters without the adjacent question mark in the Turing example. The resulting punctuation traveled with the RTL context. The preventive check is an explicit full-phrase LTR span, checked both in generated TeX and the rendered PDF.

## IR-23 ? Experiment summary validated only partially

The legacy code QA compared row count and final test score. The strengthened test compares ordered epochs, final and best row data, and derived gaps. Reruns now report a failed process or missing artifact explicitly. Byte equality can still depend on numerical package versions. Chart freshness remains a separate check.


### IR-20 follow-up ? environment recovery and residual build limits

Liat reported recovering basic execution in the unelevated sandbox, correcting Python PATH, creating the HW2 virtual environment, setting PYTHONUTF8, installing Python dependencies, updating MiKTeX, prioritizing MiKTeX-New, installing Strawberry Perl and passing Latexmk/Biber version probes. Codex verified Python imports and executable resolution, reproduced the experiment, and exercised the real build. Latexmk advanced to LuaLaTeX, but format initialization still failed with access denied. A direct run with bounded timeout and workspace-local caches hit registry setup permissions. Git staging independently failed on index.lock creation while no pre-existing lock was visible.


### Final management decision

The updated tool versions and Python environment made dependency imports, chart generation and byte-identical experiment reproduction possible. LuaLaTeX format initialization still failed with access denied. Liat chose to retain the original consistent PDF and sources and archive the proposals. This limits publication risk and avoids further work on the local TeX setup. The Git restriction also persisted in the documentation phase: staging could not create index.lock, fetch could not open FETCH_HEAD, and the shell's GitHub connection failed at its configured proxy. No stale index lock was present. The exact registry permission cause beyond the observed denials was not established.
