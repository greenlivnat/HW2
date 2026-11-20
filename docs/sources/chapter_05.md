# מקורות לפרק 5: בודקים מודלים בעזרת נתונים

- **יחידה:** ch05
- **סבב:** 1
- **תאריך אחזור לכל המקורות:** 2026-11-17
- **הוכן על ידי:** Research Agent
- **נושאי הפרק (לפי PRD סעיף 5 ו-OUTLINE):**
  - דיוק (accuracy), שיעור שגיאה, ומדדים רחבים יותר: precision, ‏recall ומטריצת בלבול.
  - למה דיוק מטעה בנתונים לא מאוזנים.
  - הכללה והתאמת יתר (overfitting) כפי שהן נראות בעקומות אימון ומבחן.
  - גרף Python מקורי מנתונים אמיתיים שמקורם מאומת, או מנתוני הדגמה מסומנים.
  - טבלה מסכמת.
  - למה אסור להסיק מגרף יותר ממה שהנתונים תומכים.
- **סיכום:** 11 רשומות, כולן מאומתות. 10 נקראו בטקסט מלא (S-ch05-01 עד S-ch05-10), ורשומה אחת אומתה במטא-דאטה בלבד (S-ch05-11).
- **עדכון M5B, סבב 1 (2026-11-18/19, ביקורת חיצונית: שגיאת הכללה מול פער הכללה):** S-ch05-10, ‏S-ch05-08 ו-S-ch05-02 אומתו מחדש עם ציטוטים מילוליים. נוספו S-ch05-12 ו-S-ch05-13 (Hardt & Recht, "Patterns, Predictions, and Actions", 2022, שני עמודים, טקסט מלא). נוסף סעיף "מה מותר ומה אסור לטעון על שגיאת הכללה". סה"כ 13 רשומות, 12 בטקסט מלא.

---

## רשומות מקורות

### S-ch05-01
- **מחברים:** scikit-learn developers
- **כותרת:** 3.4. Metrics and scoring: quantifying the quality of predictions
- **שנה / גרסה:** תיעוד scikit-learn גרסה 1.9.1 (stable). שנת פרסום לא צוינה בעמוד.
- **מוציא לאור:** scikit-learn (תיעוד רשמי)
- **קישור:** https://scikit-learn.org/stable/modules/model_evaluation.html
- **תאריך גישה:** 2026-11-17
- **סוג:** תיעוד רשמי
- **רמת גישה:** טקסט מלא. נקראו 100,000 התווים הראשונים מתוך כ-175,000, והם כוללים במלואם את סעיפי 3.4.4.2, ‏3.4.4.4, ‏3.4.4.6 ו-3.4.4.9.
- **אמינות:** גבוהה. זה התיעוד הרשמי של ספרייה מרכזית בתחום, והנוסחאות כתובות בו במפורש.
- **טענות נתמכות:**
  - **סעיף 3.4.4.2:** נוסחת accuracy היא שיעור החיזויים שתואמים לתווית האמיתית. דוגמה מהעמוד: עבור `y_true=[0,1,2,3]` ו-`y_pred=[0,2,1,3]` מתקבל דיוק של 0.5.
  - **סעיף 3.4.4.6:** הגדרת מטריצת בלבול: התא (i, j) סופר תצפיות שהן בפועל בקבוצה i וחוזו כקבוצה j. דוגמה בינארית מהעמוד: `y_true=[0,0,0,1,1,1,1,1]` ו-`y_pred=[0,1,0,1,0,1,0,1]` נותנים `tn, fp, fn, tp = (2, 1, 2, 3)`.
  - **סעיף 3.4.4.9:** הגדרה אינטואיטיבית. ‏precision היא היכולת של המסווג לא לסמן כחיובית דוגמה שלילית, ו-recall היא היכולת שלו למצוא את כל הדוגמאות החיוביות. הסעיף כולל גם נוסחאות precision, ‏recall ו-F-beta (סעיף 3.4.4.9.1).
  - **סעיף 3.4.4.4:** balanced accuracy "avoids inflated performance estimates on imbalanced datasets". לפי הסעיף, אם הדיוק הרגיל גבוה מרמת המקרה רק משום שהמסווג מנצל קבוצת מבחן לא מאוזנת, הדיוק המאוזן יורד ל-1/n_classes.
  - **הערה:** סעיף ה-accuracy עצמו אינו מזהיר במפורש מפני נתונים לא מאוזנים. את האזהרה המפורשת יש לייחס ל-S-ch05-06.

### S-ch05-02
- **מחברים:** scikit-learn developers
- **כותרת:** 3.5. Validation curves: plotting scores to evaluate models
- **שנה / גרסה:** תיעוד scikit-learn, ענף stable (1.9.1)
- **מוציא לאור:** scikit-learn (תיעוד רשמי)
- **קישור:** https://scikit-learn.org/stable/modules/learning_curve.html
- **תאריך גישה:** 2026-11-17
- **סוג:** תיעוד רשמי
- **רמת גישה:** טקסט מלא
- **אמינות:** גבוהה. זה תיעוד רשמי.
- **טענות נתמכות:**
  - **מבוא לסעיף 3.5:** הגדרת bias (השגיאה הממוצעת של אומדן על פני קבוצות אימון שונות) ו-variance (עד כמה האומדן רגיש לשינוי בקבוצת האימון).
  - **סעיף 3.5.1 (פרשנות עקומת ולידציה):** אם ציון האימון וציון הוולידציה נמוכים שניהם, יש תת-התאמה (underfitting). אם ציון האימון גבוה וציון הוולידציה נמוך, יש התאמת יתר (overfitting). ציון אימון נמוך עם ציון ולידציה גבוה "is usually not possible".
  - **סעיף 3.5.2:** הגדרת learning curve: ציוני אימון וולידציה כפונקציה של מספר דוגמאות האימון, ככלי לבדוק אם יועיל להוסיף נתונים.
  - **סעיף 3.5 (דוגמת תת-התאמה והתאמת יתר):** הדוגמה משתמשת בנתונים **סינתטיים**, דגימות רועשות של cos(1.5πx) עם פולינומים מדרגה 1, ‏4 ו-15.
  - **ציטוט מילולי, סעיף 3.5.1 (M5B, אומת מחדש ב-2026-11-19):** "If the training score and the validation score are both low, the estimator will be underfitting. If the training score is high and the validation score is low, the estimator is overfitting and otherwise it is working very well. A low training score and a high validation score is usually not possible."
  - **ציטוט מילולי, מבוא 3.5 (דוגמת הפולינומים):** "the first estimator can at best provide only a poor fit to the samples and the true function because it is too simple (high bias)". והאחרון: "approximates the training data perfectly but does not fit the true function very well, i.e. it is very sensitive to varying training data (high variance)."
  - **הערה:** הניסוח של 3.5.1 מתייחס לציון **ולידציה**, ולא לציון בדיקה. גם המילה "will be" / "is" מנוסחת כהיוריסטיקה לקריאת עקומה, ולא כהגדרה פורמלית.
  - **סעיפים 3.5.1 ו-3.5.2 (מספרים מודפסים):** בעמוד מודפסים מערכי ציונים אמיתיים מ-5-fold CV על מערך הנתונים Iris. הם מפורטים בסעיף "דוגמאות, נוסחאות ונתונים".

### S-ch05-03
- **מחברים:** scikit-learn developers
- **כותרת:** Effect of model regularization on training and test error
- **שנה / גרסה:** גלריית הדוגמאות של scikit-learn 1.9.1 (`plot_train_error_vs_test_error.py`)
- **מוציא לאור:** scikit-learn (תיעוד רשמי)
- **קישור:** https://scikit-learn.org/stable/auto_examples/model_selection/plot_train_error_vs_test_error.html
- **תאריך גישה:** 2026-11-17
- **סוג:** תיעוד רשמי (דוגמת קוד)
- **רמת גישה:** טקסט מלא
- **אמינות:** גבוהה לתיאור התופעה. כדי שהנתונים לא ייחשבו אמיתיים בטעות, חשוב לדעת שהם **סינתטיים** (`make_regression`).
- **טענות נתמכות:**
  - כשמקדם הרגולריזציה alpha שואף לאפס, המודל מנסה להתאים את נתוני האימון בשגיאה מינימלית, "However, it leads to overfitting when features are noisy". רגולריזציה חזקה מדי מובילה ל-underfitting.
  - **הגדרות הניסוי:** 150 דוגמאות אימון, ‏300 דוגמאות מבחן, ‏500 תכונות שמתוכן 50 אינפורמטיביות, מודל ElasticNet, ‏alpha בטווח `np.logspace(-5, 1, 60)`.
  - ציון R² על קבוצת המבחן ב-alpha האופטימלי הוא **0.884**, כפי שמודפס בעמוד. ערך ה-alpha האופטימלי מופיע רק במקרא הגרף.
  - **מה אסור לייחס לעמוד:** אין בו טבלת מספרים של עקומת האימון והמבחן. העקומה קיימת רק כתמונה.

### S-ch05-04
- **מחברים:** scikit-learn developers (תיאור מערך הנתונים מייחס את היצירה ל-E. Alpaydin)
- **כותרת:** 9.1. Toy datasets, סעיף 9.1.3: Optical recognition of handwritten digits dataset
- **שנה / גרסה:** תיעוד scikit-learn, ענף stable
- **מוציא לאור:** scikit-learn (תיעוד רשמי)
- **קישור:** https://scikit-learn.org/stable/datasets/toy_dataset.html
- **תאריך גישה:** 2026-11-17
- **סוג:** תיעוד רשמי (תיאור מערך נתונים)
- **רמת גישה:** טקסט מלא
- **אמינות:** גבוהה
- **טענות נתמכות:**
  - **סעיף 9.1.3:** `load_digits` מכיל 1,797 דוגמאות ו-64 תכונות (תמונה בגודל 8x8, פיקסלים שלמים בטווח 0..16), ב-10 מחלקות. אין ערכים חסרים. התאריך המצוין הוא July 1998.
  - **מקור הנתונים (מצוטט מהעמוד):** "This is a copy of the test set of the UCI ML hand-written digits datasets".
  - **סעיף 9.1.6:** מערך Breast cancer Wisconsin (diagnostic) מכיל 569 דוגמאות, בחלוקה "212 - Malignant, 357 - Benign". זה מערך לא מאוזן במידה מתונה, ואפשר להשתמש בו כדוגמה.

### S-ch05-05
- **מחברים:** E. Alpaydin, C. Kaynak
- **כותרת:** Optical Recognition of Handwritten Digits [Dataset]
- **שנה:** 1998 (נתרם ב-June 30, 1998)
- **מוציא לאור:** UCI Machine Learning Repository
- **קישור / DOI:** https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits ‏(DOI: 10.24432/C50P49)
- **תאריך גישה:** 2026-11-17
- **סוג:** מערך נתונים (מאגר מוסדי)
- **רמת גישה:** טקסט מלא (עמוד המאגר)
- **אמינות:** גבוהה. זה מאגר אוניברסיטאי מוכר, ויש לרשומה DOI.
- **טענות נתמכות:**
  - **רישיון:** "This dataset is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license."
  - המערך המלא מכיל 5,620 דוגמאות עם 64 תכונות שלמות בטווח 0–16. הגרסה שב-scikit-learn (S-ch05-04) היא עותק של קבוצת המבחן בלבד, עם 1,797 דוגמאות.
  - **ציטוט מומלץ (מהעמוד):** Alpaydin, E. & Kaynak, C. (1998). Optical Recognition of Handwritten Digits [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C50P49

### S-ch05-06
- **מחברים:** Google for Developers (Machine Learning Crash Course). לא צוינו מחברים אישיים.
- **כותרת:** Classification: Accuracy, recall, precision, and related metrics
- **שנה:** לא צוינה בעמוד (לא נמצא תאריך עדכון)
- **מוציא לאור:** Google for Developers
- **קישור:** https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall
- **תאריך גישה:** 2026-11-17
- **סוג:** תיעוד רשמי / חומר לימוד מוסדי
- **רמת גישה:** טקסט מלא
- **אמינות:** בינונית-גבוהה. זה חומר לימוד רשמי של ארגון מוביל בתחום, אבל הוא לא עבר שיפוט אקדמי ואין לו תאריך.
- **טענות נתמכות:**
  - **נוסחאות:** Accuracy = (TP+TN)/(TP+TN+FP+FN); ‏Recall (TPR) = TP/(TP+FN); ‏FPR = FP/(FP+TN); ‏Precision = TP/(TP+FP).
  - **דיוק מטעה בנתונים לא מאוזנים, עם דוגמה מספרית מהעמוד:** אם מחלקה מופיעה רק ב-1% מהמקרים, מודל שתמיד חוזה "שלילי" יקבל דיוק של 99% "despite being useless".
  - יש להעדיף מדדים אחרים על פני accuracy כשהנתונים לא מאוזנים, או כשסוג שגיאה אחד (FN או FP) יקר מהשני.

### S-ch05-07
- **מחברים:** Google for Developers (Machine Learning Crash Course)
- **כותרת:** Thresholds and the confusion matrix
- **שנה:** לא צוינה בעמוד
- **מוציא לאור:** Google for Developers
- **קישור:** https://developers.google.com/machine-learning/crash-course/classification/thresholding
- **תאריך גישה:** 2026-11-17
- **סוג:** תיעוד רשמי / חומר לימוד מוסדי
- **רמת גישה:** טקסט מלא
- **אמינות:** בינונית-גבוהה (אותו נימוק כמו ב-S-ch05-06)
- **טענות נתמכות:**
  - **מטריצת בלבול על דוגמת מסנן ספאם:**
    - TP: ספאם שנשלח לתיקיית הספאם.
    - FP: מייל לגיטימי שנשלח לספאם.
    - FN: ספאם שהגיע לתיבת הדואר הנכנס.
    - TN: מייל לגיטימי שהגיע לתיבת הדואר הנכנס.
  - סכומי השורות הם החיזויים החיוביים (TP+FP) והשליליים (FN+TN). סכומי העמודות הם החיוביים בפועל (TP+FN) והשליליים בפועל (FP+TN).

### S-ch05-08
- **מחברים:** Google for Developers (Machine Learning Crash Course)
- **כותרת:** Overfitting
- **שנה:** לא צוינה בעמוד
- **מוציא לאור:** Google for Developers
- **קישור:** https://developers.google.com/machine-learning/crash-course/overfitting/overfitting
- **תאריך גישה:** 2026-11-17
- **סוג:** תיעוד רשמי / חומר לימוד מוסדי
- **רמת גישה:** טקסט מלא
- **אמינות:** בינונית-גבוהה
- **טענות נתמכות:**
  - **הגדרה:** overfitting הוא בניית מודל ש"משנן" (memorizes) את קבוצת האימון ברמת התאמה כזו שהוא נכשל בחיזוי נכון על נתונים חדשים. מודל ש-"generalizes well" מנבא היטב על נתונים חדשים, והכללה היא "the opposite of overfitting".
  - **עקומת הכללה:** בתחילה עקומות האימון והוולידציה צמודות. אחר כך הפסד האימון ממשיך לרדת או מתייצב, בעוד שהפסד הוולידציה מתחיל לעלות. לפי כיתוב איור 15 בעמוד, דפוס כזה "strongly implies overfitting".
  - **דוגמה חזותית בעמוד:** עצים בריאים וחולים ביער (איורים 11–13). מודל מורכב מפריד היטב את נתוני האימון ונכשל על קבוצת המבחן.
  - **חלוקת נתונים לדוגמה:** 70% אימון, ‏15% ולידציה ו-15% מבחן. זו דוגמה מהעמוד ולא כלל.
  - **ציטוטים מילוליים (M5B, אומתו מחדש ב-2026-11-19):**
    - overfitting: "Overfitting means creating a model that matches (memorizes) the training set so closely that the model fails to make correct predictions on new data."
    - הכללה: "a model that generalizes well makes good predictions on new data." וגם: "Generalization is the opposite of overfitting."
    - **underfitting:** "An underfit model doesn't even make good predictions on the training data." לפי האחזור, האזור השמאלי התחתון באיור 14 (איכות נמוכה גם על נתוני האימון וגם על נתוני העולם האמיתי) מסומן "underfit models".
    - עקומת הכללה: "A graph that shows two or more loss curves is called a generalization curve."
  - **הערה:** העמוד לא משתמש במונחים "generalization error" או "generalization gap" (לפי מה שהאחזור החזיר).

### S-ch05-09
- **מחברים:** Google for Developers (Machine Learning Crash Course)
- **כותרת:** Overfitting: Interpreting loss curves
- **שנה:** לא צוינה בעמוד
- **מוציא לאור:** Google for Developers
- **קישור:** https://developers.google.com/machine-learning/crash-course/overfitting/interpreting-loss-curves
- **תאריך גישה:** 2026-11-17
- **סוג:** תיעוד רשמי / חומר לימוד מוסדי
- **רמת גישה:** טקסט מלא
- **אמינות:** בינונית-גבוהה
- **טענות נתמכות:**
  - **דפוסים של עקומות הפסד:**
    - עקומה "אידיאלית": ההפסד יורד ומתייצב.
    - תנודות לא יציבות.
    - קפיצה חדה.
    - עקומה שבה הפסד האימון מתכנס בעוד שהפסד הוולידציה "begins to rise after a certain number of training steps". העמוד מייחס את הדפוס הזה להתאמת יתר.
  - העמוד מציין שקשה לפרש עקומות הפסד לעתים קרובות. זה תומך בטענה שגרף לבדו לא תמיד מספק מסקנה חד-משמעית.

### S-ch05-10
- **מחברים:** Chiyuan Zhang, Samy Bengio, Moritz Hardt, Benjamin Recht, Oriol Vinyals
- **כותרת:** Understanding deep learning requires rethinking generalization
- **שנה:** 2017 (arXiv v1 מ-10 Nov 2016, ‏v2 מ-26 Feb 2017). לפי arXiv: "Published in ICLR 2017".
- **מוציא לאור / כנס:** ICLR 2017. הגרסה שנקראה היא arXiv:1611.03530v2.
- **קישור / DOI:** https://arxiv.org/abs/1611.03530 ‏(DOI: 10.48550/arXiv.1611.03530). טקסט מלא: https://arxiv.org/pdf/1611.03530
- **תאריך גישה:** 2026-11-17
- **סוג:** מאמר כנס (עבר שיפוט ב-ICLR)
- **רמת גישה:** טקסט מלא. נקראו עמודים 1–7 מתוך ה-PDF, כולל טבלה 1 ואיורים 1–2. הנספח (טבלה 2) לא נקרא.
- **רישיון arXiv:** arXiv non-exclusive distribution license 1.0 ‏(http://arxiv.org/licenses/nonexclusive-distrib/1.0/). זה אינו רישיון CC, ולכן מותר רק **לצטט מספרים בודדים עם ייחוס**, ולא להעתיק איורים.
- **אמינות:** גבוהה. זה מאמר מצוטט מאוד שעבר שיפוט בכנס מוביל.
- **טענות נתמכות:**
  - **סעיף 1 (עמ' 1):** "generalization error" מוגדרת כהפרש בין "training error" ל-"test error".
    - **ניסוח מילולי (M5B, אומת מחדש ב-2026-11-18 מול arXiv v2, עמ' 1, סעיף 1 Introduction, פסקה ראשונה):** "Nonetheless, some of these models exhibit remarkably small *generalization error*, i.e., difference between “training error” and “test error”."
    - גם בתקציר (עמ' 1): "successful deep artificial neural networks can exhibit a remarkably small difference between training and test performance. Conventional wisdom attributes small generalization error either to properties of the model family, or to the regularization techniques used during training."
    - **הקשר:** במאמר הזה "generalization error" היא **הפער** בין שגיאת האימון לשגיאת הבדיקה. S-ch05-12 (Hardt & Recht) מאשר שזה שימוש קיים: את הפער הם מכנים generalization gap, ומוסיפים "This quantity is sometimes also called generalization error". **השימוש האחר שהביקורת החיצונית מתארת** (שגיאת הכללה = השגיאה הצפויה על נתונים חדשים) **לא נמצא במקור מאומת בסבב הזה** (ראו פערים). לכן הדרך הבטוחה בספר היא להשתמש במונח "פער הכללה" (generalization gap) לפער, ולהציג את השגיאה על נתונים חדשים כ"סיכון" או "השגיאה על נתונים חדשים" לפי S-ch05-12.
  - **סעיף 1.1 (עמ' 2):** "Deep neural networks easily fit random labels". כשמאמנים רשת על תוויות אקראיות לגמרי היא מגיעה לשגיאת אימון 0, ושגיאת המבחן "is no better than random chance".
  - **המסר לפרק:** דיוק אימון מושלם לבדו אינו מעיד על הכללה. רק קבוצת מבחן נפרדת חושפת את הפער.
  - **סעיף 2.1 (עמ' 5):** ב-CIFAR10, כשרמת השיבוש של התוויות מתקרבת ל-1, שגיאת ההכללה מתכנסת ל-90%, "the performance of random guessing on CIFAR10".
  - **טבלה 1 (עמ' 6):** דיוק אימון ומבחן (באחוזים) של כמה מודלים על CIFAR10. ראו בסעיף "דוגמאות, נוסחאות ונתונים".
  - **איור 2 (עמ' 7):** עקומות דיוק של אימון ומבחן לאורך צעדי אימון (Inception על ImageNet ועל CIFAR10). העקומות קיימות **רק כאיור**, בלי טבלת ערכים.
  - **הערת שוליים 1 (עמ' 7):** כדי לטעון ש-early stopping משפר הכללה באופן קפדני, "we need to have another isolated test set". זה תומך ישירות בנושא "לא להסיק יותר ממה שהנתונים תומכים".

### S-ch05-11
- **מחברים:** Marina Sokolova, Guy Lapalme
- **כותרת:** A systematic analysis of performance measures for classification tasks
- **שנה:** 2009
- **כתב עת:** Information Processing & Management, 45(4), 427–437 (Elsevier)
- **קישור / DOI:** https://doi.org/10.1016/j.ipm.2009.03.002
- **תאריך גישה:** 2026-11-17. הפרטים אומתו דרך Crossref API ו-OpenAlex API.
- **סוג:** מאמר בכתב עת שפיט
- **רמת גישה:** מטא-דאטה בלבד. לפי OpenAlex המאמר סגור (closed access), ושם גם לא הופיע תקציר.
- **אמינות:** גבוהה כמקור ביבליוגרפי. התוכן לא נקרא.
- **טענות נתמכות:** לפי הכללים, מותר לייחס לו רק את מה שמשתמע מהכותרת: קיים ניתוח שיטתי של מדדי ביצוע למשימות סיווג. **אסור לייחס לו טענות ספציפיות או נוסחאות.** אפשר להזכיר אותו לכל היותר כ"קריאה נוספת".

### S-ch05-12
- **מחברים:** Moritz Hardt, Benjamin Recht
- **כותרת:** Patterns, Predictions, and Actions: A story about machine learning. פרק 6: "Generalization"
- **שנה:** 2022 (לפי עמוד הבית של הספר). בעמוד הפרק כתוב "Last updated: Mon Jun 8 11:57:41 PDT 2026".
- **מוציא לאור:** Princeton University Press (לפי עמוד הבית של האתר הרשמי של הספר)
- **קישור:** https://mlstory.org/generalization.html (עמוד הבית: https://mlstory.org/). ‏DOI או ISBN לא אומתו.
- **תאריך גישה:** 2026-11-18 (אחזור ראשון ועמוד הבית), 2026-11-19 (אחזור ציטוטים מילוליים)
- **סוג:** ספר לימוד אקדמי (גרסה מקוונת רשמית באתר המחברים)
- **רמת גישה:** טקסט מלא (סעיף "Generalization gap" בפרק 6 נקרא. שאר הפרק נקרא רק באופן חלקי)
- **רישיון:** לפי עמוד הבית, הטקסט באתר ברישיון CC BY-NC-ND 4.0. מותר לצטט ולנסח מחדש עם ייחוס. אסור לשכפל קטעים בשינוי.
- **אמינות:** גבוהה. ספר לימוד של הוצאה אוניברסיטאית, מאת חוקרים מובילים בתחום (Hardt ו-Recht הם גם מחברים שותפים של S-ch05-10).
- **טענות נתמכות (סעיף "Generalization gap"):**
  1. **סיכון (risk):** השגיאה הצפויה, R[f] = E[loss(f(X), Y)], על פני ההתפלגות כולה. "the risk R[f] captures loss on unseen example, while the empirical risk R_S[f] captures loss on seen examples."
  2. **שגיאת אימון:** "In machine learning practice, the empirical risk is often called *training error* or *training loss*,"
  3. **הגדרת פער ההכללה:** "This performance gap between seen and unseen examples is what we call *generalization gap*." ‏Definition 1: "Define the *generalization gap* of a predictor f with respect to a dataset S as" ‏Δ_gen(f) = R[f] − R_S[f].
  4. **המונח "generalization error":** "This quantity is sometimes also called *generalization error* or *excess risk*." כלומר אצל Hardt & Recht שגיאת הכללה היא **שם נוסף לפער**, ולא שם לסיכון עצמו.
  5. **הפירוק:** "Recall the following tautological, yet important identity:" ‏R[f] = R_S[f] + Δ_gen(f). השגיאה על נתונים חדשים שווה לשגיאת האימון ועוד פער ההכללה.
  6. **ציפייה כללית:** "Generally, we expect to do much better on seen examples than unseen examples."
  7. **מטרה:** "Ideally, we would like that the predictor f we find via empirical risk minimization satisfies" ‏R_S[f] ≈ R[f].
- **הערה:** בפרק הזה הפער מוגדר מול הסיכון R[f] (שגיאה צפויה על כל ההתפלגות), ולא מול שגיאת קבוצת הבדיקה. הקשר לקבוצת הבדיקה מופיע ב-S-ch05-13.

### S-ch05-13
- **מחברים:** Moritz Hardt, Benjamin Recht
- **כותרת:** Patterns, Predictions, and Actions: A story about machine learning. פרק 8: "Datasets"
- **שנה:** 2022 (לפי עמוד הבית של הספר)
- **מוציא לאור:** Princeton University Press
- **קישור:** https://mlstory.org/data.html
- **תאריך גישה:** 2026-11-19
- **סוג:** ספר לימוד אקדמי (גרסה מקוונת רשמית)
- **רמת גישה:** טקסט מלא (נקרא בשאלות ממוקדות. הסעיף "The scientific basis of machine learning benchmarks" ומשפטים על test set ו-holdout)
- **רישיון:** CC BY-NC-ND 4.0 (לפי עמוד הבית)
- **אמינות:** גבוהה
- **טענות נתמכות (סעיף "The scientific basis of machine learning benchmarks"):**
  1. **קבוצת בדיקה אומדת את הסיכון:** "the best way to test the performance of a predictor f is to collect a sufficiently large fresh dataset S" (ציטוט חלקי, ההתחלה קוצרה). ומיד אחריו: "We already learned that the empirical risk in this case is an unbiased estimate of the risk of the predictor."
  2. **חלוקה לשלוש קבוצות:** "Sometimes practitioners divide their data into multiple splits, e.g., training, validation, and test sets." וגם: "A number of variations on this theme go under the name holdout method."
  3. **קבוצת הבדיקה כ"מדגם טרי":** "In all applications of the holdout method the hope is that the test set will serve as a fresh sample" (ציטוט חלקי).
  4. **שמירת קבוצת הבדיקה:** "Ideally, the test set should be kept in a “vault,” and be brought out only at the end of the data analysis."
  5. **סכנת שימוש חוזר:** "Then the test set error of the final chosen model will underestimate the true test error, sometimes substantially." ‏(ההקשר, לפי האחזור: בחירת מודל לפי קבוצת הבדיקה.) וגם: "reuse of test data—on the face of it—invalidates the statistical guarantees of the holdout method."
- **הערה:** חלק מהציטוטים קוצרו על ידי כלי האחזור (ב-"…" או בקטיעה), ולכן הם מסומנים כחלקיים. אין להשלים אותם מהזיכרון.

---

## מה מותר ומה אסור לטעון על שגיאת הכללה (M5B)

**מותר:**
- השגיאה הצפויה של מודל על נתונים חדשים (הסיכון, risk) שונה משגיאת האימון. ההפרש ביניהן נקרא **פער הכללה** (generalization gap) (S-ch05-12, Definition 1).
- שגיאת האימון ועוד פער ההכללה שווים לשגיאה על נתונים חדשים (S-ch05-12).
- השגיאה על קבוצת בדיקה טרייה היא אומדן (בלתי מוטה) של השגיאה על נתונים חדשים (S-ch05-13).
- יש מחברים שקוראים לפער עצמו "שגיאת הכללה" (generalization error). כך עושים Zhang et al. ‏(S-ch05-10, עמ' 1), ו-Hardt & Recht מציינים שזה שם נוסף לפער (S-ch05-12).
- שימוש חוזר בקבוצת הבדיקה לבחירת מודל גורם להערכת חסר של השגיאה האמיתית (S-ch05-13; עקבי עם S-ch05-10, הערת שוליים 1).

**אסור:**
- להגדיר "שגיאת הכללה" כ"ההפרש בין שגיאת האימון לשגיאת הבדיקה" **בלי** לציין שזה שימוש של מקור מסוים ושיש מינוח מקביל (פער הכללה). הניסוח הנוכחי בשורה 46 בפרק 5 מציג אותו כמונח היחיד.
- לייחס ל-S-ch05-12 או ל-S-ch05-13 את ההגדרה "שגיאת הכללה = השגיאה הצפויה על נתונים חדשים". הם לא אומרים זאת (S-ch05-12 משתמש במונח risk לשגיאה הצפויה).
- לטעון ששגיאת הבדיקה **שווה** לשגיאת ההכללה או לסיכון. היא **אומדן** שלה (S-ch05-13).
- לטעון שקבוצת ולידציה וקבוצת בדיקה הן אותו דבר. S-ch05-02 מדבר על ולידציה, ו-S-ch05-13 מבחין בין השתיים.

---

## דוגמאות, נוסחאות ונתונים

### נוסחאות

1. **Accuracy (דיוק):**
   - הנוסחה: Accuracy = (TP+TN)/(TP+TN+FP+FN).
   - **מקורות:** S-ch05-06 (סעיף Accuracy). הצורה הכללית, שיעור ההתאמות 1/n · Σ 1(ŷᵢ = yᵢ), מופיעה ב-S-ch05-01 סעיף 3.4.4.2.
2. **Error rate (שיעור שגיאה):**
   - הנוסחה: Error rate = 1 − Accuracy = (FP+FN)/(TP+TN+FP+FN).
   - **הערה:** **אף מקור שנבדק לא מציג את הנוסחה הזו במפורש.** היא נגזרת אריתמטית מנוסחת הדיוק, וכך יש להציג אותה.
   - S-ch05-10 משתמש ב-"test error" כמשלים של דיוק המבחן: בעמ' 5, שגיאת הכללה של 90% מתאימה לניחוש אקראי בין 10 מחלקות.
3. **Precision:**
   - הנוסחה: Precision = TP/(TP+FP).
   - **מקורות:** S-ch05-06, ו-S-ch05-01 סעיף 3.4.4.9.1.
4. **Recall (TPR):**
   - הנוסחה: Recall = TP/(TP+FN).
   - **מקורות:** S-ch05-06, ו-S-ch05-01 סעיף 3.4.4.9.1.
5. **FPR:**
   - הנוסחה: FPR = FP/(FP+TN).
   - **מקור:** S-ch05-06.
6. **F-beta:**
   - הנוסחה: F_β = (1+β²)·precision·recall / (β²·precision + recall).
   - **מקור:** S-ch05-01 סעיף 3.4.4.9.1. אופציונלי לפרק.
7. **Balanced accuracy (בינארי):**
   - הנוסחה: ½·(TP/(TP+FN) + TN/(TN+FP)).
   - **מקור:** S-ch05-01 סעיף 3.4.4.4.

### דוגמאות מספריות מאומתות

- **דוגמת 99%:**
  - מחלקה נדירה (1%) ומודל שתמיד אומר "שלילי" מקבלים דיוק של 99%, למרות שהמודל חסר תועלת.
  - **מקור:** S-ch05-06.
- **דוגמת מטריצת בלבול:**
  - `y_true=[0,0,0,1,1,1,1,1]`, ‏`y_pred=[0,1,0,1,0,1,0,1]` נותנים tn=2, fp=1, fn=2, tp=3.
  - **מקור:** S-ch05-01 סעיף 3.4.4.6.
  - **חישוב נגזר (חשבון פשוט, לא מצוטט מהמקור):**
    - accuracy = 5/8 = 0.625
    - error rate = 0.375
    - precision = 3/4 = 0.75
    - recall = 3/5 = 0.6
  - זו דוגמה טובה לטבלה הקטנה בפרק.
- **פער אימון-מבחן במאמר אמיתי (S-ch05-10, טבלה 1, עמ' 6, ‏CIFAR10, באחוזים):**

  | model | # params | random crop | weight decay | train acc. | test acc. |
  |---|---|---|---|---|---|
  | Inception | 1,649,402 | yes | yes | 100.0 | 89.05 |
  | Inception | | yes | no | 100.0 | 89.31 |
  | Inception | | no | yes | 100.0 | 86.03 |
  | Inception | | no | no | 100.0 | 85.75 |
  | Inception (fitting random labels) | | no | no | 100.0 | 9.78 |
  | Inception w/o BatchNorm | 1,649,402 | no | yes | 100.0 | 83.00 |
  | Inception w/o BatchNorm | | no | no | 100.0 | 82.00 |
  | Inception w/o BatchNorm (random labels) | | no | no | 100.0 | 10.12 |
  | Alexnet | 1,387,786 | yes | yes | 99.90 | 81.22 |
  | Alexnet | | yes | no | 99.82 | 79.66 |
  | Alexnet | | no | yes | 100.0 | 77.36 |
  | Alexnet | | no | no | 100.0 | 76.07 |
  | Alexnet (random labels) | | no | no | 99.82 | 9.86 |
  | MLP 3x512 | 1,735,178 | no | yes | 100.0 | 53.35 |
  | MLP 3x512 | | no | no | 100.0 | 52.39 |
  | MLP 3x512 (random labels) | | no | no | 100.0 | 10.48 |
  | MLP 1x512 | 1,209,866 | no | yes | 99.80 | 50.39 |
  | MLP 1x512 | | no | no | 100.0 | 50.51 |
  | MLP 1x512 (random labels) | | no | no | 99.34 | 10.61 |

  המספרים הועתקו ישירות מתמונת העמוד ב-PDF (arXiv v2). לפני שימוש מומלץ שה-Reviewer יבדוק אותם שוב מול המקור.
- **מספרי Iris מתיעוד scikit-learn (S-ch05-02):**
  - **עקומת ולידציה, סעיף 3.5.1:** ‏SVC עם kernel ליניארי, ‏C ב-`np.logspace(-7, 3, 3)`, ‏5-fold.
    - train_scores:
      - [0.90, 0.94, 0.91, 0.89, 0.92]
      - [0.9, 0.92, 0.93, 0.92, 0.93]
      - [0.97, 1, 0.98, 0.97, 0.99]
    - valid_scores:
      - [0.9, 0.9, 0.9, 0.96, 0.9]
      - [0.9, 0.83, 0.96, 0.96, 0.93]
      - [1., 0.93, 1, 1, 0.9]
  - **עקומת למידה, סעיף 3.5.2:** ‏train_sizes=[50, 80, 110].
    - train_scores:
      - [0.98, 0.98, 0.98, 0.98, 0.98]
      - [0.98, 1., 0.98, 0.98, 0.98]
      - [0.98, 1., 0.98, 0.98, 0.99]
    - valid_scores:
      - [1., 0.93, 1., 1., 0.96]
      - [1., 0.96, 1., 1., 0.96]
      - [1., 0.96, 1., 1., 0.96]
  - **הערכה:** אלה רק 3 נקודות, ואין בהן דפוס של התאמת יתר. הן לא מתאימות לגרף המרכזי.

### הערכת נתונים לגרף "אימון מול מבחן לאורך אפוקים"

1. **לא נמצאה טבלה מספרית מאומתת ופתוחה של דיוק או הפסד לאורך אפוקים.**
   - ב-S-ch05-10 (איור 2) העקומות לאורך צעדי אימון קיימות רק כתמונה.
   - S-ch05-03 משתמש בנתונים סינתטיים, ומציג עקומה כתמונה בלבד ולפי alpha ולא לפי אפוקים.
   - **אין לחלץ מספרים "בעין" מאיורים ולהציג אותם כנתונים אמיתיים.**
2. **אפשרות א' (מומלצת): נתונים אמיתיים שה-Python של הפרויקט מחשב בעצמו.**
   - **הנתונים:** מערך הספרות של UCI (S-ch05-05, רישיון CC BY 4.0, ‏DOI 10.24432/C50P49), שזמין ב-scikit-learn כ-`load_digits` (S-ch05-04).
   - **מה הסקריפט עושה:** ‏`python/generate_chart.py` מאמן מודל עם seed קבוע וחלוקה קבועה של אימון ומבחן. למשל `MLPClassifier` עם `partial_fit` לאורך אפוקים, או עץ החלטה לפי עומק.
   - **מה הוא שומר:** הוא שומר את הדיוק בכל אפוק ל-CSV תחת `python/data/`.
   - **מה מאומת ומה לא:** מקור הנתונים מאומת. המספרים עצמם הם תוצר של הקוד שלנו, ולכן ניתנים לשחזור.
   - **כיתוב מתאים:** "חושב על ידי המחברת על נתוני UCI Digits". בכיתוב אין לייחס את התוצאות למקור חיצוני.
   - **הסתייגות:** לא מובטח מראש שתתקבל התאמת יתר בולטת. את התוצאה צריך לבדוק בפועל ולא להניח אותה.
3. **אפשרות ב': גרף עמודות מנתונים שפורסמו בפועל.**
   - **הנתונים:** טבלה 1 של S-ch05-10, עם דיוק אימון מול מבחן לכל מודל, כולל השורות של "random labels".
   - **היתרונות:** זה מקור אמיתי ומצוטט, והגרף ממחיש בעוצמה שדיוק אימון של 100% יכול לבוא עם דיוק מבחן של כ-10%.
   - **החיסרון:** זה **לא** גרף לאורך אפוקים.
   - **רישוי:** רישיון arXiv אינו CC. לכן מציגים מספרים עם ייחוס מלא בלבד, ולא משכפלים את האיור.
4. **אפשרות ג': נתוני הדגמה מדומים.**
   - **מתי:** אם רוצים דווקא את הצורה הקלאסית, הפסד אימון יורד והפסד מבחן יורד ואז עולה.
   - **החובה (PRD סעיף 10):** לסמן את הגרף והכיתוב במפורש כ"נתוני הדגמה מדומים", ולתאר את אופן היצירה, כולל הנוסחה וה-seed.
   - **תמיכה מושגית בצורה:** S-ch05-08 ו-S-ch05-09.
5. **ההמלצה:** אפשרות א' לגרף האפוקים, ובנוסף אפשרות ב' כטבלה המסכמת. אם אפשרות א' לא מייצרת פער ברור, עדיף להציג את מה שיצא בפועל ולא "לכוונן" עד שיופיע הדפוס הרצוי. אם בכל זאת נדרשת צורה קלאסית, יש לעבור לאפשרות ג' עם סימון מפורש.

---

## רעיונות להמחשה (הצעות)

> אלה הצעות של סוכן המחקר, לא עובדות מתועדות.

1. **גרף קווים "אימון מול מבחן":**
   - ציר X הוא אפוק, ציר Y הוא דיוק או הפסד, עם שני קווים בצבעי הפלטה (טורקיז `#2EC4B6` לאימון וסגול `#7451B8` למבחן).
   - קו אנכי מקווקו יכול לסמן "כאן מתחיל הפער", אבל **רק אם הפער אכן מופיע בנתונים**.
2. **גרף עמודות זוגיות מטבלה 1 של Zhang et al.:**
   - לכל מודל שתי עמודות, דיוק אימון ודיוק מבחן, ולצדן קבוצת עמודות של "תוויות אקראיות" שבה האימון כ-100% והמבחן כ-10%.
   - **כותרת אפשרית:** "המודל זוכר הכול, ולא מבין כלום".
3. **מטריצת בלבול מצוירת כ-2x2 (טבלת LaTeX או TikZ):**
   - על בסיס דוגמת הספאם (S-ch05-07), עם המספרים מדוגמת scikit-learn (S-ch05-01).
4. **קופסת "שאלת מחשבה":**
   - "מודל שמזהה מחלה נדירה ומקבל 99% דיוק. האם הוא טוב?" (על בסיס S-ch05-06).
5. **טבלה מסכמת של מדדים:**
   - עמודות: שם המדד, נוסחה, "שואל את השאלה...", ומתי הוא מטעה.
   - דוגמה: Accuracy שואל "כמה פעמים צדקנו?" ומטעה כשהנתונים לא מאוזנים.
6. **קופסה "מה הגרף לא אומר לנו":**
   - **סיבה 1:** חלוקה אחת ו-seed אחד אינם מוכיחים כלום על חלוקה אחרת.
   - **סיבה 2:** בחירת נקודת עצירה לפי קבוצת המבחן "מזהמת" אותה. רעיון זה מבוסס על הערת השוליים ב-S-ch05-10, עמ' 7.
   - **סיבה 3:** ביצועים על Digits אינם מעידים על מודלי שפה.
7. **דימוי יומיומי:**
   - תלמידה ששיננה את התשובות למבחן לדוגמה, לעומת תלמידה שהבינה את החומר. הדימוי מקביל לניסוי "random labels".

---

## פערים / לא אומת

1. **נוסחת error rate:** לא נמצאה כנוסחה מפורשת באף מקור שנבדק. יש להציג אותה כ"1 פחות הדיוק", כגזירה ישירה.
2. **Sokolova & Lapalme 2009 (S-ch05-11):** אומת במטא-דאטה בלבד, כי המאמר סגור ואין תקציר ב-OpenAlex. אין לייחס לו תוכן ספציפי.
3. **רישיון התוכן של Google ML Crash Course:** הטקסט שאוחזר לא כלל הצהרת רישיון ולא תאריך עדכון, ולכן הרישיון **לא אומת**. מצטטים ומנסחים מחדש בלבד, ולא מעתיקים איורים.
4. **רישיון תיעוד scikit-learn:** לא נבדק בהרצה זו, ולכן **לא אומת**. השימוש המוצע הוא ציטוט ופרפרזה בלבד. הקוד שלנו רק קורא ל-`load_digits`, והנתונים עצמם מכוסים ב-CC BY 4.0 (S-ch05-05).
5. **נתוני אפוקים אמיתיים בפורמט מספרי:** לא נמצאו במקור פתוח ומאומת. ראו את הערכת הנתונים לגרף למעלה.
6. **טבלה 2 בנספח של Zhang et al. (ImageNet):** לא נקראה. רק המספרים שמופיעים בגוף הטקסט בעמ' 5 ו-7 אומתו: 95.20% top-1 בתוויות אקראיות, ‏59.80% ללא רגולריזציה ו-72.95% עם data augmentation בלבד.
7. **"ROC/AUC":** לא נחקר בסבב הזה, ונראה מחוץ להיקף של פרק בן 3 עמודים.
8. **(M5B) אין מקור מאומת להגדרה "generalization error = השגיאה הצפויה על נתונים חדשים"**, שהביקורת החיצונית מציעה. שני המקורות שנבדקו (S-ch05-10, ‏S-ch05-12) משתמשים במונח לפער. את השגיאה הצפויה S-ch05-12 מכנה risk. אם הכותבת רוצה את המובן של הביקורת, נדרש סבב מחקר נוסף. עד אז ממליצים להשתמש במונחים "פער הכללה" ו"השגיאה על נתונים חדשים".
9. **(M5B) DOI ו-ISBN של "Patterns, Predictions, and Actions" לא אומתו.** השנה והמוציא לאור אומתו רק מעמוד הבית של האתר הרשמי, ולא דרך Crossref.
10. **(M5B) ציטוטים חלקיים ב-S-ch05-13:** כלי האחזור קיצר חלק מהמשפטים. אין להשלים אותם.

---

## יומן אחזורים

| # | URL | תוצאה | הערה |
|---|---|---|---|
| 1 | https://scikit-learn.org/stable/modules/model_evaluation.html | OK | נקראו 100K תווים מתוך כ-175K. הסעיפים הרלוונטיים נקראו במלואם. |
| 2 | https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall | OK | |
| 3 | https://developers.google.com/machine-learning/crash-course/overfitting/overfitting | OK | |
| 4 | https://arxiv.org/abs/1611.03530 | OK | מטא-דאטה ותקציר |
| 5 | https://api.crossref.org/works?query.bibliographic=A+systematic+analysis+of+performance+measures+for+classification+tasks+Sokolova+Lapalme&rows=3 | OK | אימות ביבליוגרפי של S-ch05-11 |
| 6 | https://scikit-learn.org/stable/auto_examples/model_selection/plot_validation_curve.html | FAILED | העמוד הוא הודעת הפניה (redirect) ל-plot_train_error_vs_test_error.html, ואין בו תוכן. |
| 7 | https://scikit-learn.org/stable/datasets/toy_dataset.html | OK | |
| 8 | https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits | OK | רישיון CC BY 4.0 ו-DOI אומתו |
| 9 | https://scikit-learn.org/stable/auto_examples/model_selection/plot_train_error_vs_test_error.html | OK | נתונים סינתטיים |
| 10 | https://scikit-learn.org/stable/modules/learning_curve.html | OK | |
| 11 | https://developers.google.com/machine-learning/crash-course/overfitting/interpreting-loss-curves | OK | |
| 12 | https://arxiv.org/pdf/1611.03530 | OK | האחזור הישיר החזיר PDF בינארי. הקובץ שנשמר נקרא כעמודים 1–7 (תמונות), כולל טבלה 1. |
| 13 | https://arxiv.org/abs/1611.03530v2 | OK | בדיקת רישיון: arXiv nonexclusive-distrib 1.0 |
| 14 | https://api.openalex.org/works/doi:10.1016/j.ipm.2009.03.002 | OK | מטא-דאטה בלבד. closed access, אין תקציר. |
| 15 | https://developers.google.com/machine-learning/crash-course/classification/thresholding | OK | אין הצהרת רישיון בטקסט שאוחזר |
| 16 | https://arxiv.org/pdf/1611.03530v2 | OK | M5B, 2026-11-18. הממיר לא חילץ טקסט, אבל הקובץ נשמר ועמודים 1–2 נקראו ישירות. |
| 17 | https://mlstory.org/generalization.html | OK | M5B, שני אחזורים (2026-11-18 ו-2026-11-19). האחזור השני נכשל פעם אחת בשגיאת הזדהות של הסביבה ("Login expired"), ואחרי התיקון הצליח. |
| 18 | https://mlstory.org/ | OK | M5B, 2026-11-18. כותרת, מחברים, Princeton University Press ‏2022, ‏CC BY-NC-ND 4.0 |
| 19 | https://mlstory.org/data.html | OK | M5B, 2026-11-19, שני אחזורים ממוקדים |
| 20 | https://developers.google.com/machine-learning/crash-course/overfitting/overfitting | OK | M5B, 2026-11-19, ציטוטים מילוליים (overfitting, underfit, הכללה) |
| 21 | https://scikit-learn.org/stable/modules/learning_curve.html | OK | M5B, 2026-11-19, ציטוט מילולי של סעיף 3.5.1 |
