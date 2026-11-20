# הרצת research-agent: ‏M5B, סבב 1

| שדה | ערך |
|---|---|
| סוכן | research-agent (`subagent_type=research-agent`) |
| תאריך | 2026-11-18 עד 2026-11-19 |
| יחידה | M5B: מקור ל-tanh (R-ch03-11, הערת ChatGPT) והגדרת שגיאת הכללה מול פער הכללה (הערת ChatGPT) |
| קבצים ששונו | `docs/sources/chapter_03.md`, ‏`docs/sources/chapter_05.md`, ‏`docs/SOURCES.md` |
| שימוש | 35 קריאות לכלים, 137,008 טוקנים, 308.0 שניות (המספרים של החלק שאחרי החידוש, לפי הודעת הסיום) |
| תקלה | ההרצה נעצרה בשגיאה `authentication_failed` ("Login expired"). לפי `git status` לא נכתבו קבצים. אחרי `/login` היא חודשה באותו סוכן ב-SendMessage (IR-18) |

## הפרומפט המלא שנשלח

```
פרומפט ההפעלה:
You are invoked by the Orchestrator. Your full task (in Hebrew) is in agents/runs/tasks/research_m5b_r1_prompt.txt in the project root C:\biu01\HW2\ai_book_starter. Read it and follow it exactly, including the files it names. Write only the files it allows. Finish with the output it describes.

הודעת החידוש (SendMessage, אחרי IR-18):
The Orchestrator here. Your run stopped on an authentication error (login expired); it is fixed now. No files were written yet (docs/sources/chapter_03.md, chapter_05.md and docs/SOURCES.md are unchanged). Continue from where you stopped (you were confirming the DOI of Efficient BackProp), complete both tasks in agents/runs/tasks/research_m5b_r1_prompt.txt, write only the allowed files, and finish with the output it describes.
```
קובץ המשימה: `agents/runs/tasks/research_m5b_r1_prompt.txt`.

## הפלט הגולמי

Research Agent: M5B סבב 1 הושלם. המזהים שהוקצו הם S-ch03-05 ו-S-ch05-12/13, כי אלה הבאים בתור במספור הקיים. ההנחיה הציעה את S-ch03-07 ואת S-ch05-13, אבל S-ch03-05/06 ו-S-ch05-12 לא קיימים בשום מקום במאגר (נבדק עם grep).

### 1. טבלה

| משימה | מקור | ציטוט מילולי קצר ומיקום | רמת גישה | מה מותר לטעון | מה אסור לטעון |
|---|---|---|---|---|---|
| 1א tanh | S-ch03-01 (CS231n), עודכן | פסקת Tanh: "It squashes a real-valued number to the range [-1, 1]."; "Like the sigmoid neuron, its activations saturate, but unlike the sigmoid neuron its output is zero-centered."; "Therefore, in practice the tanh non-linearity is always preferred to the sigmoid nonlinearity." בתיבת TLDR: "Try tanh, but expect it to work worse than ReLU/Maxout." ו-"Never use sigmoid." | טקסט מלא | הנוסחה 2σ(2z)−1; הטווח [-1,1]; רוויה; פלט ממורכז; "עדיף על הסיגמואיד" בייחוס לקורס, ורק לעומת הסיגמואיד (המשפט נפתח ב-"Therefore" ונובע מהמירכוז) | ש-tanh עדיפה "תמיד" באופן כללי, או שהיא ברירת המחדל (אותו עמוד ממליץ על ReLU); ש-tanh פותרת רוויה |
| 1ב tanh | S-ch03-05 (חדש): LeCun, Bottou, Orr & Müller (1998), Efficient BackProp, *Neural Networks: Tricks of the Trade*, LNCS 1524, עמ' 9–50, DOI 10.1007/3-540-49430-8_2 (אומת ב-Crossref) | סעיף 4.3 (עמ' 8 ב-PDF): "Convergence is usually faster if the average of each input variable over the training set is close to zero."; סעיף 4.4 (עמ' 10): סיגמואידים סימטריים "are preferred for the same reason that inputs should be normalized"; בתיבת Sigmoids: "Symmetric sigmoids such as hyperbolic tangent often converge faster than the standard logistic function."; עמ' 12: "the error surface can be very flat near the origin." | טקסט מלא (עותק באתר המחבר Bottou, עמודי PDF 1–2 ו-8–12) | פלט ממורכז עוזר לשכבה הבאה, ולכן tanh **לעתים קרובות** מתכנסת מהר יותר מהלוגיסטית; יש לה גם חסרונות | לייחס ל-LeCun את "always"; לתאר כ"מאמר שפיט" (זה פרק בספר ערוך, ולא אומת שעבר שיפוט פורמלי); מספרים |
| 2א | S-ch05-10 (Zhang et al.), עודכן | עמ' 1, סעיף 1: "some of these models exhibit remarkably small *generalization error*, i.e., difference between “training error” and “test error”." | טקסט מלא (arXiv v2, עמ' 1–2 נקראו מחדש) | שבמאמר הזה המונח מציין את הפער | להציג את ההגדרה הזו כמשמעות היחידה של המונח |
| 2ב | S-ch05-12 (חדש): Hardt & Recht (2022), *Patterns, Predictions, and Actions*, Princeton UP, פרק 6, mlstory.org/generalization.html | סעיף "Generalization gap": "This performance gap between seen and unseen examples is what we call *generalization gap*." ‏Definition 1: Δ_gen(f) = R[f] − R_S[f]; ‏"This quantity is sometimes also called *generalization error* or *excess risk*."; ‏"R[f] = R_S[f] + Δ_gen(f)"; ‏"the empirical risk is often called *training error*" | טקסט מלא (הסעיף); רישיון CC BY-NC-ND 4.0 | סיכון (risk) הוא השגיאה הצפויה על נתונים חדשים; פער ההכללה הוא הסיכון פחות שגיאת האימון; יש מי שמכנה את הפער "generalization error" | לייחס ל-Hardt & Recht את ההגדרה "generalization error = השגיאה הצפויה". הם אומרים את ההפך: המונח הוא כינוי נוסף לפער |
| 2ב | S-ch05-13 (חדש): Hardt & Recht, פרק 8, mlstory.org/data.html | "We already learned that the empirical risk in this case is an unbiased estimate of the risk of the predictor." (על מדגם טרי); "Ideally, the test set should be kept in a “vault,”..." | טקסט מלא (נקרא בשאלות ממוקדות; חלק מהציטוטים חלקיים) | שגיאת הבדיקה היא אומדן של השגיאה על נתונים חדשים | שהיא **שווה** לה |
| 2ג | S-ch05-08 (Google), עודכן | "Overfitting means creating a model that matches (memorizes) the training set so closely that the model fails to make correct predictions on new data."; ‏"An underfit model doesn't even make good predictions on the training data." | טקסט מלא | הגדרות מדויקות של overfitting ושל underfit | |
| 2ג | S-ch05-02 (scikit-learn), עודכן | סעיף 3.5.1: "If the training score and the validation score are both low, the estimator will be underfitting. If the training score is high and the validation score is low, the estimator is overfitting..." | טקסט מלא | היוריסטיקה לקריאת עקומה | להציג אותה כהגדרה פורמלית, או לטעון שהיא מדברת על קבוצת בדיקה (היא מדברת על ולידציה) |

**ממצא מהותי למשימה 2:** הביקורת החיצונית צודקת רק בחלקה. השימוש במונח "generalization error" לציון הפער מוכר ולגיטימי: ‏Zhang et al. משתמשים בו כך, ו-Hardt & Recht מאשרים שזה כינוי נוסף לפער. מנגד, **לא מצאתי מקור מאומת** שמגדיר "generalization error = השגיאה הצפויה על נתונים חדשים". את השגיאה הזו Hardt & Recht מכנים risk. הנקודה נרשמה כפער. הפתרון הבטוח הוא להשתמש במונח "פער הכללה".

### 2. כתובות URL שאוחזרו
- https://cs231n.github.io/neural-networks-1/ : OK (3 אחזורים)
- https://api.crossref.org/works?query.bibliographic=Efficient+BackProp+LeCun+Bottou+Orr+Muller&rows=5 : OK
- https://api.crossref.org/works/10.1007/3-540-49430-8_2 : OK
- http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf : FAILED (ECONNREFUSED)
- WebSearch "Efficient BackProp" (חיפוש, לא אחזור). המראה של צד שלישי dcmpx.remotevs.com לא שימש.
- https://leon.bottou.org/papers/lecun-98x : OK
- https://leon.bottou.org/publications/pdf/tricks-1998.pdf : OK (ה-PDF נשמר ונקרא ישירות)
- https://arxiv.org/pdf/1611.03530v2 : OK (ה-PDF נקרא ישירות, עמ' 1–2)
- https://mlstory.org/generalization.html : OK (פעמיים. ניסיון אחד נכשל בשגיאת ההזדהות "Login expired" ונוסה שוב)
- https://mlstory.org/ : OK
- https://mlstory.org/data.html : OK (פעמיים)
- https://developers.google.com/machine-learning/crash-course/overfitting/overfitting : OK
- https://scikit-learn.org/stable/modules/learning_curve.html : OK

### 3. פערים ופריטים לא מאומתים
- אין מקור מאומת להגדרה "generalization error = השגיאה הצפויה על נתונים חדשים". לשם כך נדרש סבב נוסף.
- DOI ו-ISBN של Hardt & Recht לא אומתו. השנה והמו"ל לקוחים מעמוד הבית בלבד.
- לא אומת אם פרקי *Tricks of the Trade* עברו שיפוט פורמלי. מהדורת 2012 (DOI 10.1007/978-3-642-35289-8_3) אומתה במטא-דאטה בלבד ולא נקראה. בעותק של Bottou אין מספרי עמודים מודפסים, ולכן המיקומים הם לפי סעיף ועמוד PDF.
- אין השוואה כמותית בין tanh לסיגמואיד.
- חלק מהציטוטים ב-S-ch05-13 חלקיים (קוצרו בכלי האחזור).
- ההמשך המילולי של כיתוב האיור ב-CS231n לא התקבל. לציטוט משתמשים במשפט מהפסקה.

### 4. קבצים ששונו
- `docs/sources/chapter_03.md`: עדכון S-ch03-01 (טענה 9א), רשומה חדשה S-ch03-05, הסעיף "מה מותר ומה אסור לטעון על tanh", פערים ויומן אחזורים.
- `docs/sources/chapter_05.md`: עדכון S-ch05-02, ‏S-ch05-08 ו-S-ch05-10, רשומות חדשות S-ch05-12 ו-S-ch05-13, הסעיף "מה מותר ומה אסור לטעון על שגיאת הכללה", פערים 8–10 ויומן אחזורים 16–21.
- `docs/SOURCES.md`: הערת כותרת, שורות אינדקס (חדשות ומעודכנות), פערים, סעיף 3.8 פריטים 16–17, ביבליוגרפיה 20א ו-26א, וטבלת סיכום (76 מזהים, 59 רשומות).

### 5. ניסוחים מומלצים ל-writer
**tanh (פרק 3, שורה 53):** "התוצאה היא אותו שסתום הדרגתי, אבל בטווח שבין 1- ל-1 ועם אפס באמצע, כלומר פלט ממורכז סביב אפס [S-ch03-01]. גם היא רוויה בקצוות, אבל כיוון שהפלט שלה הוא הקלט של השכבה הבאה, המירכוז הזה מאיץ לעתים קרובות את הלמידה לעומת הסיגמואיד [S-ch03-05]. לכן רשימות הקורס של סטנפורד מעדיפות אותה על הסיגמואיד, אך באותה נשימה ממליצות דווקא על ReLU, שנפגוש מיד [S-ch03-01]."

**שגיאת הכללה (פרק 5, שורה 46):** "השגיאה על דוגמאות שהוחזקו בצד היא אומדן של מה שבאמת מעניין אותנו: השגיאה הצפויה של המודל על נתונים חדשים [S-ch05-13]. להפרש בין השגיאה הזאת לשגיאת האימון קוראים פער הכללה (generalization gap) [S-ch05-12]. יש חוקרים שמכנים את הפער הזה גם שגיאת הכללה (generalization error) [S-ch05-10] [S-ch05-12]."

## שער האיכות של ה-Orchestrator
- `git status`: מחוץ לקבצים של ה-Orchestrator השתנו רק שלושת הקבצים המותרים. **עבר.**
- המזהים S-ch03-05, ‏S-ch05-12 ו-S-ch05-13 מופיעים ב-`docs/SOURCES.md` ובקובצי הפרקים. **עבר.**
- סטייה מההנחיה (מזהים 05/12/13 במקום 07/13): מוצדקת. אלה המזהים הבאים בתור. **מאושר.**
- **החלטה:** ממשיכים ל-writer (Q3). נדרש מה-writer להוסיף שורות ל"## מקורות לפרק", כי `scripts/make_bib.py` בונה מהן את `references.bib`. הפער "אין מקור להגדרה generalization error = שגיאה צפויה" מטופל בניסוח: המונח המרכזי הוא "פער הכללה", ואין טענה לא מעוגנת.
