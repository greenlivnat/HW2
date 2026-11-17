# הרצה: research-agent, יחידה smoke, סבב 2

| שדה | ערך |
|---|---|
| תאריך | 2026-11-17 |
| סוכן | `research-agent` |
| הופעל על ידי | Orchestrator, אחרי ההתאוששות מהניתוק |
| התחלה | 14:48:45 JST בקירוב |
| סיום | 14:51:48 JST בקירוב (משך לפי הכלי: 183.3 שניות) |
| שימוש | 18 קריאות לכלים, 24,883 טוקנים |
| סיבת ההפעלה | ליקוי R-smoke-01 ב-`review_smoke_r1.md`: התיקון דורש מקור על המנגנון. ראו את החלטת הניתוב ב-`reviewer_smoke_r1.md` |
| קובץ פלט | `agents/runs/smoke_test/sources_smoke.md` (עדכון) |

## הפרומפט המלא שנשלח

```
SMOKE TEST, round 2 (unit: smoke). Pipeline test, NOT book production.

Orchestrator override for this test only: do NOT write to docs/SOURCES.md. You may edit ONLY agents/runs/smoke_test/sources_smoke.md.

Context: the reviewer's report agents/runs/smoke_test/review_smoke_r1.md raised defect R-smoke-01: the paragraph never explains what "back-propagation" propagates and why "backward". The current source S-smoke-01 (Rumelhart, Hinton & Williams 1986) is verified only at abstract level and does not describe the mechanism. Read the report (R-smoke-01 row) and the current sources_smoke.md.

Task: Find and VERIFY BY FETCHING one additional reliable source (ID S-smoke-02) that explains the mechanism in general terms: the error measured at the output is passed backward through the network, layer by layer (chain rule), to compute how much each weight (including weights of hidden units) contributed to the error (its gradient), and the weights are then adjusted in the direction that reduces the error. Prefer an authoritative textbook freely available online (e.g. Goodfellow, Bengio & Courville, "Deep Learning", MIT Press 2016, at deeplearningbook.org, chapter 6.5) or official university course notes. Record only what you actually saw on the fetched page, with chapter/section. If you can also fetch the full text of the 1986 paper from an official source, you may enrich S-smoke-01; otherwise leave it as is.

Do NOT research historical precedents (R-smoke-02); that defect will be fixed by wording only.

Update agents/runs/smoke_test/sources_smoke.md: keep S-smoke-01 unchanged unless enriched with verified data; add an S-smoke-02 record in the same format; append the new fetch attempts to the fetch log; update the gaps section. Add a short header line noting "סבב 2: נוסף S-smoke-02 בעקבות R-smoke-01".

Final message: your structured report (sources, every URL fetched OK/FAILED, the exact supported claims of S-smoke-02 with section, gaps, files written).
```

## הפלט הגולמי שהסוכן החזיר (כפי שהתקבל אצל ה-Orchestrator)

```
## דוח Research Agent: בדיקת עשן, סבב 2 (unit: smoke)

לפי R-smoke-01 נוסף מקור מאומת אחד, S-smoke-02: רשימות הקורס CS231n של אוניברסיטת Stanford. הספר המועדף, Goodfellow, Bengio & Courville, לא אומת, כי מהעמוד שלו לא התקבל טקסט. S-smoke-01 לא הועשר ונשאר כמו שהיה.

### 1. כיסוי
| יחידה | מקורות מאומתים |
|---|---|
| smoke | 2 (S-smoke-01 ברמת התקציר בלבד, S-smoke-02) |

**S-smoke-02:** CS231n Deep Learning for Computer Vision, רשימות הקורס "Backpropagation", https://cs231n.github.io/optimization-2/ (עיקרי), יחד עם https://cs231n.github.io/optimization-1/ (משלים). אתר הקורס https://cs231n.stanford.edu/ ("Stanford University") מקשר לרשימות תחת "Useful Notes". בעמוד הרשימות לא מופיעים מחבר ושנה, ולכן לא נרשמו. אמינות: גבוהה כהסבר מושגי, בינונית כרשומה ביבליוגרפית (חסרים מחבר ושנה).

### 2. הטענות ש-S-smoke-02 תומך בהן (ציטוטים מהעמודים שנפתחו)
1. **הגדרה** (optimization-2, Introduction): "backpropagation, which is a way of computing gradients of expressions through recursive application of chain rule."
2. **מה מחושב ולמה** (optimization-2, Introduction): "f will correspond to the loss function". הקלטים כוללים "the neural network weights". מחשבים "the gradient for the parameters" כדי "to perform a parameter update".
3. **הגרדיאנט מודד כמה כל משתנה משפיע על הפלט** (optimization-2, Simple expressions and interpretation of the gradient): "the derivative on each variable tells you the sensitivity of the whole expression on its value."
4. **כלל השרשרת** (optimization-2, Compound expressions with chain rule): "The chain rule tells us that the correct way to “chain” these gradient expressions together is through multiplication."
5. **מעבר קדימה ומעבר אחורה** (optimization-2, Intuitive understanding of backpropagation): "The forward pass computes values from inputs to output". המעבר לאחור "recursively applies the chain rule to compute the gradients", ומבצע "multiply it into every gradient it normally computes".
6. **זרימה לאחור** (אותו סעיף, וגם Summary): "The gradients can be thought of as flowing backwards through the circuit". הגרדיאנטים גם מראים "which part of the circuit should increase or decrease".
7. **שלב אחר שלב** (optimization-2, Summary): "backprop through the variables one step at a time."
8. **כיוון העדכון** (optimization-1, Computing the gradient > Numerically with finite differences, הפסקה "Update in negative gradient direction"): "we are making an update in the negative direction of the gradient", "since we wish our loss function to decrease, not increase". גודל הצעד נקרא "learning rate".

**הסתייגות שה-Writer צריך לדעת:** המקור מסביר את המנגנון בעזרת "circuit" ו-"gates", ולא בעזרת "שכבות" ו"יחידות חבויות". הניסוח "שכבה אחר שכבה, כולל המשקלים של יחידות חבויות" הוא יישום שלי של ההסבר, לא ציטוט מהמקור. את קיום היחידות החבויות ואת כוונון המשקלים שלהן מבסס S-smoke-01.

### 3. כתובות שנאחזרו בסבב הזה
| URL | תוצאה |
|---|---|
| https://www.deeplearningbook.org/contents/mlp.html | FAILED (3 ניסיונות. האחזור החזיר רק "Content truncated" בלי טקסט מהעמוד) |
| https://cs231n.github.io/optimization-2/ | OK (3 אחזורים) |
| http://neuralnetworksanddeeplearning.com/chap2.html | FAILED (שגיאת תעודת SSL) |
| https://cs231n.github.io/optimization-1/ | OK |
| https://cs231n.stanford.edu/ | OK |

### 4. פערים ופריטים שלא אומתו
- **Goodfellow et al., "Deep Learning", פרק 6.5:** לא אומת ולא נכלל.
- **Nielsen, "Neural Networks and Deep Learning", פרק 2:** לא אומת ולא נכלל.
- **מחבר ושנה של S-smoke-02:** לא מופיעים בעמוד. אין לייחס את הרשימות לאדם מסוים.
- **S-smoke-01:** לא ניסיתי שוב לאחזר את הטקסט המלא של מאמר 1986, ולכן הרשומה עדיין ברמת התקציר בלבד.
- **R-smoke-02:** לא נחקר, לפי ההוראה.

### 5. קבצים שנכתבו
- `C:\biu01\HW2\ai_book_starter\agents\runs\smoke_test\sources_smoke.md` הוא הקובץ היחיד ששיניתי. הוספתי בו את שורת הכותרת של סבב 2, את רשומת S-smoke-02, את הפערים של סבב 2 ואת רשומות האחזור של סבב 2. רשומת S-smoke-01 לא השתנתה.
- `docs/SOURCES.md` לא שונה.
```

## קבצים שנוצרו או שונו
- עודכן: `agents/runs/smoke_test/sources_smoke.md` (MD5 השתנה מ-`99ea982d...` ל-`289f6387...`)
- שאר הקבצים ב-`smoke_test/` ו-32 קובצי ה-baseline לא השתנו (נבדק עם MD5).

## שער האיכות של ה-Orchestrator
| בדיקה | תוצאה |
|---|---|
| רשומת S-smoke-02 קיימת, עם כל השדות | ✅ (מחבר ושנה מסומנים במפורש כ"לא מצוין") |
| לכל טענה יש ציטוט וסעיף | ✅ |
| רשומת S-smoke-01 נשארה כמו שהיא | ✅ (הושוותה לתוכן שהוצג בסבב 1) |
| יומן אחזורים ופערים עודכנו, כולל כישלונות | ✅ |
| `docs/SOURCES.md` לא נוצר | ✅ |
| הסוכן כתב רק בתחום שהוקצה לו | ✅ |

**החלטה:** השער עבר. ממשיכים ל-writer-agent בסבב 2, עם שלושת הליקויים.
