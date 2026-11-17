# מקורות: בדיקת עשן (smoke), סבב 1 + סבב 2

> קובץ בדיקה של צנרת הסוכנים בלבד, לא חלק מהפקת הספר. לא נכתב ל-`docs/SOURCES.md` לפי הוראת ה-Orchestrator.

> סבב 2: נוסף S-smoke-02 בעקבות R-smoke-01. רשומת S-smoke-01 לא שונתה.

## רשומה

| שדה | ערך |
|---|---|
| מזהה | S-smoke-01 |
| מחברים | David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams |
| כותרת | Learning representations by back-propagating errors |
| שנה | 1986 (אוקטובר 1986 לפי Crossref) |
| כתב עת | Nature, vol. 323, issue 6088, pp. 533–536 (מוציא לאור לפי Crossref: Springer Science and Business Media LLC) |
| DOI / קישור | 10.1038/323533a0, https://doi.org/10.1038/323533a0 |
| תאריך גישה | 2026-11-17 |
| סוג | מאמר בכתב עת שעבר שיפוט (journal-article) |
| דירוג אמינות | גבוה |
| נימוק | מאמר מקורי בכתב העת Nature. הנתונים הביבליוגרפיים זהים בארבעה מאגרים עצמאיים שנפתחו בפועל: Crossref, Semantic Scholar, OpenAlex ו-INSPIRE-HEP. |

### טענות שהמקור תומך בהן
כל הטענות לקוחות מתקציר המאמר (עמ' 533), כפי שהוצג ברשומת INSPIRE-HEP ובקטעי תוצאות החיפוש:
1. המאמר מציג שיטת למידה חדשה, back-propagation, לרשתות של יחידות דמויות-נוירון. משפט הפתיחה המצוטט: "We describe a new learning procedure, back-propagation, for networks of neurone-like units."
2. השיטה מכווננת שוב ושוב את משקלי החיבורים ברשת כדי להקטין את ההפרש בין הפלט בפועל לבין הפלט הרצוי.
3. בעקבות התאמת המשקלים, יחידות פנימיות ("חבויות"), שאינן יחידות קלט או פלט, מייצגות מאפיינים שימושיים של המשימה. לפי המחברים, היכולת ליצור מאפיינים חדשים היא מה שמבדיל את השיטה משיטות פשוטות יותר שקדמו לה, כמו perceptron-convergence procedure.

הערה: טענות 2 ו-3 הן פרפרזה של התקציר, ולא ציטוט מילולי. הטקסט המלא של המאמר לא נפתח (ראו פערים).

## רשומה (סבב 2)

| שדה | ערך |
|---|---|
| מזהה | S-smoke-02 |
| מחברים | לא מצוין בעמוד. העמוד הוא חלק מחומרי הקורס CS231n של Stanford University. עמוד הקורס מציג את המרצים Fei-Fei Li, Ehsan Adeli, Justin Johnson, Zane Durante, Tiange Xiang, אבל לא מייחס להם את כתיבת הרשימות. לכן אין לייחס את הרשימות לאדם מסוים. |
| כותרת | CS231n Deep Learning for Computer Vision: רשימות הקורס "Backpropagation" (עמוד optimization-2), ועמוד משלים "Optimization" (עמוד optimization-1) |
| שנה | לא מצוינת בעמוד (לא אומת) |
| מוציא לאור | Stanford University, קורס CS231n. עמוד הקורס https://cs231n.stanford.edu/ מקשר ל-"Useful Notes" בכתובת https://cs231n.github.io/ (אומת באחזור). |
| DOI / קישור | https://cs231n.github.io/optimization-2/ (עיקרי); https://cs231n.github.io/optimization-1/ (משלים) |
| תאריך גישה | 2026-11-17 |
| סוג | תיעוד רשמי: רשימות קורס אוניברסיטאי |
| דירוג אמינות | גבוה (להסבר מושגי). בינוני כמקור ביבליוגרפי, כי אין מחבר ושנה בעמוד. |
| נימוק | רשימות קורס רשמיות של קורס מוכר באוניברסיטת Stanford, שאליהן מקשר אתר הקורס הרשמי. הן מסבירות את המנגנון בשפה כללית ונגישה. |

### טענות שהמקור תומך בהן
כל הציטוטים נלקחו מהעמוד שנפתח בפועל, עם שם הסעיף:
1. **מה זה backpropagation** (optimization-2, סעיף Introduction): "backpropagation, which is a way of computing gradients of expressions through recursive application of chain rule."
2. **מה מחושב ולמה** (optimization-2, סעיף Introduction): ברשתות נוירונים, f היא פונקציית ה-loss ("f will correspond to the loss function"), והקלטים כוללים את משקלי הרשת ("the inputs x will consist of the training data and the neural network weights"). מחשבים את הגרדיאנט עבור הפרמטרים ("we usually only compute the gradient for the parameters") כדי לעדכן אותם ("so that we can use it to perform a parameter update").
3. **משמעות הגרדיאנט: כמה כל משתנה תורם** (optimization-2, סעיף Simple expressions and interpretation of the gradient): "the derivative on each variable tells you the sensitivity of the whole expression on its value."
4. **כלל השרשרת** (optimization-2, סעיף Compound expressions with chain rule): "The chain rule tells us that the correct way to “chain” these gradient expressions together is through multiplication."
5. **מעבר קדימה ומעבר אחורה** (optimization-2, סעיף Intuitive understanding of backpropagation): "The forward pass computes values from inputs to output". אחר כך המעבר לאחור "recursively applies the chain rule to compute the gradients". כל יחידה מחשבת גרדיאנט מקומי ("the local gradient of its output with respect to its inputs"), ובמעבר לאחור מכפילה את הגרדיאנט שמגיע אליה בגרדיאנטים המקומיים שלה ("take that gradient and multiply it into every gradient it normally computes").
6. **הגרדיאנטים "זורמים לאחור"** (optimization-2, סעיף Intuitive understanding of backpropagation): "The gradients can be thought of as flowing backwards through the circuit." בסעיף Summary: "how they flow backwards in the circuit, and how they communicate which part of the circuit should increase or decrease".
7. **שלב אחר שלב** (optimization-2, סעיף Summary): מפרקים את החישוב לשלבים, ומבצעים "backprop through the variables one step at a time."
8. **כיוון העדכון: הקטנת השגיאה** (optimization-1, סעיף Computing the gradient > Numerically with finite differences, פסקה "Update in negative gradient direction"): "we are making an update in the negative direction of the gradient" ו-"since we wish our loss function to decrease, not increase." גודל הצעד נקרא learning rate ("choosing the step size (also called the learning rate)...").

הערות פרשנות (לא עובדה מהמקור):
- הדוגמאות ב-optimization-2 מנוסחות במונחי "circuit" ו-"gates" (ביטויים מתמטיים) ולא במונחי "שכבות" ו"יחידות חבויות". הניסוח "השגיאה מועברת לאחור שכבה אחר שכבה, כולל למשקלים של יחידות חבויות" הוא יישום סביר של ההסבר לרשת נוירונים, אבל המקור לא אומר אותו במילים האלה. את קיום היחידות החבויות ואת כוונון המשקלים שלהן מבסס S-smoke-01 (תקציר).
- המקור הוא הסבר דידקטי עכשווי ולא מקור היסטורי. אין להשתמש בו לטענות על 1986.

## פערים / לא אומת
- **הטקסט המלא של המאמר לא נפתח.** עמוד המאמר ב-nature.com הפנה (303) לעמוד הזדהות. לכן הטענות מבוססות על התקציר בלבד, ואין הפניות לסעיפים או לעמודים מעבר לעמ' 533.
- **התקציר המלא לא אומת מילה במילה.** Crossref, Semantic Scholar ו-OpenAlex לא כוללים תקציר. INSPIRE-HEP החזיר ציטוט של משפט הפתיחה בלבד ותקציר של שאר התוכן.
- עמודי PubMed (מאמר אחר שנבדק כחלופה: LeCun, Bengio, Hinton, "Deep learning", 2015) ו-NASA ADS לא נפתחו. Crossref עבור DOI 10.1038/nature14539 החזיר HTTP 429. **המאמר הזה לא אומת** ואינו נכלל.
- עותקים לא רשמיים של קובץ ה-PDF שהופיעו בתוצאות החיפוש (gwern.net, baulab.info, academia.edu) לא נפתחו ולא שימשו כמקור.
- **סבב 2: S-smoke-01 לא הועשר.** בסבב הזה לא נעשה ניסיון נוסף לאחזר את הטקסט המלא של מאמר 1986 ממקור רשמי, ולכן הרשומה נשארה ברמת התקציר.
- **סבב 2: ספר הלימוד Goodfellow, Bengio & Courville, "Deep Learning" (פרק 6.5) לא אומת.** האחזור של https://www.deeplearningbook.org/contents/mlp.html החזיר רק placeholder של "Content truncated", בלי טקסט מהעמוד (שלושה ניסיונות). לכן הספר לא נכלל כמקור, ואין לצטט ממנו.
- **סבב 2: "Neural Networks and Deep Learning" של Michael Nielsen (פרק 2) לא אומת.** האחזור נכשל בשגיאת תעודת SSL.
- **סבב 2: מחבר ושנה של S-smoke-02 לא אומתו.** הם לא מופיעים בעמוד הרשימות, ולכן אין לייחס את הרשימות לאדם מסוים.
- **סבב 2: הניסוח "שכבה אחר שכבה" ו"משקלים של יחידות חבויות"** לא מופיע מילולית ב-S-smoke-02 (ראו הערות פרשנות ברשומה). זהו יישום של ההסבר הכללי, ולא ציטוט.
- R-smoke-02 (תקדימים היסטוריים) לא נחקר, לפי הוראת ה-Orchestrator.

## יומן אחזורים
| URL | תוצאה |
|---|---|
| https://www.nature.com/articles/323533a0 | FAILED (הפניית 303 לעמוד הזדהות) |
| https://pubmed.ncbi.nlm.nih.gov/26017442/ | FAILED (שגיאת cookies) |
| https://api.crossref.org/works/10.1038/nature14539 | FAILED (HTTP 429) |
| https://api.crossref.org/works/10.1038/323533a0 | OK |
| https://api.semanticscholar.org/graph/v1/paper/DOI:10.1038/323533a0?fields=title,authors,year,venue,abstract,externalIds | OK (ללא תקציר) |
| https://api.openalex.org/works/doi:10.1038/323533a0 | OK (ללא תקציר) |
| https://ui.adsabs.harvard.edu/abs/1986Natur.323..533R/abstract | FAILED (HTTP 405) |
| https://inspirehep.net/api/literature/2171919 | OK |
| WebSearch: "Learning representations by back-propagating errors" abstract | OK (חיפוש, לא אחזור עמוד) |
| **סבב 2** | |
| https://www.deeplearningbook.org/contents/mlp.html | FAILED (האחזור החזיר placeholder של "Content truncated" בלי טקסט; 3 ניסיונות) |
| https://cs231n.github.io/optimization-2/ | OK (3 אחזורים) |
| http://neuralnetworksanddeeplearning.com/chap2.html | FAILED (שגיאת תעודת SSL) |
| https://cs231n.github.io/optimization-1/ | OK |
| https://cs231n.stanford.edu/ | OK (אימות שיוך מוסדי וקישור לרשימות) |
