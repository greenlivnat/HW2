# מקורות: פרק 3, "הרשת הנוירונית מבפנים" (סבב 1)

> יחידה: ch03. סבב מחקר: 1. תאריך: 2026-11-17.
> נושאים לפי PRD סעיף 5: נוירון מלאכותי; משקולות והטיה; שכבות; פונקציות הפעלה; הנוסחה `z = \sum_{i=1}^{n} w_i x_i + b` ופרשנות לכל רכיב; מגבלות האנלוגיה למוח.
> שאלת מפתח: איך מספרים מתחברים לחיזוי?
> סיכום: 4 מקורות מאומתים. שניים בטקסט מלא (S-ch03-01, S-ch03-02), אחד ברמת תקציר (S-ch03-03), אחד ברמת מטא-דאטה בלבד (S-ch03-04).

---

## רשומה S-ch03-01

| שדה | ערך |
|---|---|
| מזהה | S-ch03-01 |
| מחברים | לא מצוין בעמוד. העמוד הוא חלק מרשימות הקורס CS231n של Stanford University (שיוך מוסדי אומת ב-Smoke Test דרך https://cs231n.stanford.edu/, שמקשר ל-cs231n.github.io). אין לייחס את הרשימות לאדם מסוים. |
| כותרת | CS231n Deep Learning for Computer Vision: רשימות הקורס "Neural Networks Part 1: Setting up the Architecture" (עמוד neural-networks-1) |
| שנה | לא מצוינת בעמוד (לא אומת) |
| מוציא לאור | Stanford University, קורס CS231n |
| DOI / קישור | https://cs231n.github.io/neural-networks-1/ |
| תאריך גישה | 2026-11-17 |
| סוג | תיעוד רשמי: רשימות קורס אוניברסיטאי |
| רמת גישה | טקסט מלא |
| דירוג אמינות | גבוה (להסבר מושגי). בינוני כמקור ביבליוגרפי, כי אין מחבר ושנה בעמוד. |
| נימוק | רשימות רשמיות של קורס מוכר באוניברסיטת Stanford. העמוד מכסה כמעט את כל נושאי הפרק: מודל הנוירון, משקלים והטיה, פונקציות הפעלה, שכבות, ומגבלות האנלוגיה הביולוגית. |

### טענות שהמקור תומך בהן
הציטוטים נלקחו מהעמוד שנפתח בפועל (שני אחזורים). שמות הסעיפים לפי כותרות העמוד.

1. **הנוירון המלאכותי: מכפלה במשקלים, הוספת הטיה, ואי-ליניאריות** (סעיף Modeling one neuron): "each neuron performs a dot product with the input and its weights, adds the bias and applies the non-linearity".
2. **הנוסחה בעמוד** (סעיף Modeling one neuron > Single neuron as a linear classifier): הנוירון מחשב σ(Σᵢ wᵢxᵢ + b), כאשר σ היא פונקציית סיגמואיד. בתת-סעיף Biological motivation and connections פונקציית ההפעלה מסומנת באופן כללי באות f.
3. **משמעות המשקלים** (סעיף Biological motivation and connections): "the synaptic strengths (the weights w) are learnable and control the strength of influence". כלומר המשקלים נלמדים, וקובעים כמה השפעה יש לכל קלט.
4. **ההשראה הביולוגית** (סעיף Biological motivation and connections): "The basic computational unit of the brain is a neuron." וגם: "Each neuron receives input signals from its dendrites and produces output signals along its (single) axon."
5. **נתונים ביולוגיים** (סעיף Biological motivation and connections): "Approximately 86 billion neurons can be found in the human nervous system" ו-"they are connected with approximately 10^14 - 10^15 synapses". (נתון שמצוטט ברשימות הקורס, ולא במקור נוירו-מדעי ראשוני.)
6. **פונקציית ההפעלה כקצב ירי** (סעיף Biological motivation and connections, פרפרזה): העמוד ממדל את קצב הירי (firing rate) של הנוירון באמצעות פונקציית ההפעלה f, בהנחת "rate code": רק תדירות הקוצים נושאת מידע, והתזמון המדויק שלהם לא.
7. **מגבלות האנלוגיה למוח** (סעיף Biological motivation and connections): "It's important to stress that this model of a biological neuron is very coarse". העמוד מונה ארבע סיבות (פרפרזה, פרט לציטוט אחד):
   - יש סוגים רבים של נוירונים, ולכל אחד תכונות שונות.
   - "The dendrites in biological neurons perform complex nonlinear computations."
   - סינפסה אינה משקל יחיד, אלא מערכת דינמית לא-ליניארית מורכבת.
   - במערכות רבות לתזמון המדויק של הקוצים יש חשיבות, ולכן קירוב ה-rate code עלול לא להתקיים.
   ועוד אזהרה: "be prepared to hear groaning sounds from anyone with some neuroscience background if you draw analogies". בנוסף, תוכן העניינים מציין "Quick intro without brain analogies", כלומר אפשר להסביר רשתות נוירונים בלי אנלוגיה למוח.
8. **נוירון יחיד כמסווג ליניארי** (סעיף Single neuron as a linear classifier, פרפרזה): אם מפרשים את σ(Σᵢ wᵢxᵢ + b) כהסתברות של אחת משתי מחלקות ומוסיפים cross-entropy loss, מתקבל מסווג בינארי (Binary Softmax, הנקרא גם logistic regression). זה מה שמחבר בין "מספרים" ל"חיזוי".
9. **פונקציות הפעלה נפוצות** (סעיף Commonly used activation functions):
   - Sigmoid: ‏σ(x) = 1 / (1 + e^(−x)). "Sigmoids saturate and kill gradients." הפלט שלה גם לא ממורכז סביב אפס. לפי העמוד היא "has recently fallen out of favor and it is rarely ever used."
   - Tanh: ‏tanh(x) = 2σ(2x) − 1. "the tanh non-linearity is always preferred to the sigmoid nonlinearity."
   - ReLU: ‏f(x) = max(0, x). "It was found to greatly accelerate (e.g. a factor of 6 in Krizhevsky et al.) the convergence". בכיתוב האיור: "indicating the 6x improvement in convergence with the ReLU unit compared to the tanh unit."
   - חיסרון של ReLU: "the ReLU units can irreversibly die during training".
   - Leaky ReLU: ‏f(x) = 𝟙(x < 0)(αx) + 𝟙(x ≥ 0)(x), כאשר α קבוע קטן (בערך 0.01).
10. **שכבות** (סעיף Neural Network architectures > Layer-wise organization): "Neural Networks are modeled as collections of neurons that are connected in an acyclic graph." בשכבה מחוברת במלואה (fully-connected): "neurons between two adjacent layers are fully pairwise connected, but neurons within a single layer share no connections." כשאומרים רשת בת N שכבות לא סופרים את שכבת הקלט: "Notice that when we say N-layer neural network, we do not count the input layer." לשכבת הפלט בדרך כלל אין פונקציית הפעלה (פרפרזה).
11. **ספירת פרמטרים בדוגמת האיור** (סעיף Layer-wise organization):
   - רשת שמאלית: שלושה קלטים, שכבה חבויה של 4 נוירונים ושכבת פלט של 2 נוירונים. "4 + 2 = 6 neurons", ‏20 משקלים ו-6 הטיות, סך הכול "26 learnable parameters".
   - רשת ימנית: שלושה קלטים, שתי שכבות חבויות של 4 נוירונים כל אחת ופלט אחד. "4 + 4 + 1 = 9 neurons", ‏32 משקלים ו-9 הטיות, סך הכול "41 learnable parameters".

הערות פרשנות (לא עובדה מהמקור):
- הצורה `z = \sum_{i=1}^{n} w_i x_i + b` שב-PRD זהה לביטוי שבתוך σ(·) בעמוד, עם אינדקס מפורש עד n. ההפרדה בין z (הסכום המשוקלל) לבין הפעלת הפונקציה עליו היא סימון דידקטי. העמוד עצמו כותב את הכול בביטוי אחד.
- נתון ההאצה פי 6 מיוחס בעמוד ל-Krizhevsky et al. המאמר המקורי של Krizhevsky לא נפתח בסבב הזה. אם מצטטים את המספר, יש לייחס אותו לרשימות CS231n שמדווחות עליו.

---

## רשומה S-ch03-02

| שדה | ערך |
|---|---|
| מזהה | S-ch03-02 |
| מחברים | Vinod Nair, Geoffrey E. Hinton (Department of Computer Science, University of Toronto) |
| כותרת | Rectified Linear Units Improve Restricted Boltzmann Machines |
| שנה | 2010 |
| מוציא לאור | Proceedings of the 27th International Conference on Machine Learning (ICML), Haifa, Israel, 2010 (כפי שמודפס בהערת השוליים בעמ' 1) |
| DOI / קישור | https://www.cs.toronto.edu/~hinton/absps/reluICML.pdf (עותק באתר של המחבר Hinton באוניברסיטת טורונטו). DOI לא אומת. |
| תאריך גישה | 2026-11-17 |
| סוג | מאמר בכנס שעבר שיפוט |
| רמת גישה | טקסט מלא (נקראו עמודים 1–3 מתוך קובץ ה-PDF) |
| דירוג אמינות | גבוה |
| נימוק | מאמר בכנס ICML, עותק רשמי באתר המחבר באוניברסיטה. נחשב למאמר מרכזי בהפצת ReLU. |

### טענות שהמקור תומך בהן
1. **הגדרת ReLU** (סעיף 4, Empirical Evaluation, עמ' 3): היחידות הדטרמיניסטיות מממשות את הפונקציה "y = max(0, x)". לצורך backpropagation הגרדיאנט נלקח כ-0 כאשר x ≤ 0 וכ-1 כאשר x > 0, ומתעלמים מאי-הרציפות ב-x = 0.
2. **השוואה ליחידות בינאריות** (Abstract, עמ' 1, ציטוט): "Compared with binary units, these units learn features that are better for object recognition on the NORB dataset and face verification on the Labeled Faces in the Wild dataset."
3. **שימור מידע לאורך שכבות** (Abstract, עמ' 1, ציטוט): "Unlike binary units, rectified linear units preserve information about relative intensities as information travels through multiple layers of feature detectors."
4. **נוסחה עם משקלים והטיה** (סעיף 1.1, משוואה 2, עמ' 1): היחידה החבויה מקבלת ערך 1 בהסתברות p(h_j = 1) = 1 / (1 + exp(−b_j − Σ_{i∈vis} v_i w_ij)), כאשר b_j היא ההטיה של j ו-v_i הוא מצב הקלט i. זו פונקציית סיגמואיד על סכום משוקלל ועוד הטיה.
5. **הקלט ליחידה** (סעיף 2, משוואה 7, עמ' 2): ‏x = v·wᵀ + b, כלומר מכפלה של וקטור הקלט בווקטור המשקלים ועוד הטיה.
6. **"מודלים של נוירונים אמיתיים"** (סעיף 2, עמ' 2, ציטוט): "A small modification to binomial units makes them far more interesting as models of real neurons and also more useful for practical applications."
7. **הקשר לעבודה קודמת** (סעיף 2, עמ' 3, פרפרזה): ‏Jarrett et al. ‏(2009) בחנו אי-ליניאריות מסוג max(0, x) ברשתות קונבולוציה ומצאו שהן משפרות ביצועים מבחינתיים.

הערות פרשנות:
- ההקשר של המאמר הוא Restricted Boltzmann Machines, נושא טכני שחורג מרמת הספר. מומלץ להשתמש בו רק לביסוס ההגדרה max(0, x) ולעובדה היסטורית שהשימוש ב-ReLU קודם במאמר הזה. אין לטעון שהמאמר "המציא" את ReLU: המאמר עצמו מפנה לעבודות קודמות (Jarrett et al., 2009; Hahnloser et al., 2003).

---

## רשומה S-ch03-03

| שדה | ערך |
|---|---|
| מזהה | S-ch03-03 |
| מחברים | F. Rosenblatt (Frank Rosenblatt לפי OpenAlex) |
| כותרת | The perceptron: A probabilistic model for information storage and organization in the brain. |
| שנה | 1958 (נובמבר 1958 לפי OpenAlex) |
| כתב עת | Psychological Review, vol. 65, issue 6, pp. 386–408. מוציא לאור: American Psychological Association (APA) |
| DOI / קישור | 10.1037/h0042519, https://doi.org/10.1037/h0042519 |
| תאריך גישה | 2026-11-17 |
| סוג | מאמר בכתב עת שעבר שיפוט |
| רמת גישה | תקציר בלבד (התקציר הופיע ב-OpenAlex, וכלי האחזור החזיר סיכום שלו ולא נוסח מילולי מלא) |
| דירוג אמינות | גבוה (למטא-דאטה ולעובדה ההיסטורית) |
| נימוק | הפרטים הביבליוגרפיים זהים בשלושה מאגרים שנפתחו: Crossref, ‏OpenAlex, ‏Semantic Scholar. |

### טענות שהמקור תומך בהן
1. **עובדה ביבליוגרפית/היסטורית:** ב-1958 פרסם Rosenblatt ב-Psychological Review מאמר בשם "The perceptron", שמציג את עצמו כ"מודל הסתברותי לאחסון וארגון מידע במוח" (לפי הכותרת).
2. **לפי התקציר (פרפרזה ברמת התקציר בלבד):** המאמר עוסק בשאלה איך מידע נאגר במוח ואיך מידע שנאגר משפיע על זיהוי והתנהגות. הוא מתאר עבודה ב-Cornell Aeronautical Laboratory במימון Office of Naval Research.

הערה: אין להסיק מהרשומה הזו פרטים על מבנה הפרספטרון, נוסחאות או תוצאות. גוף המאמר לא נפתח.

---

## רשומה S-ch03-04

| שדה | ערך |
|---|---|
| מזהה | S-ch03-04 |
| מחברים | Warren S. McCulloch, Walter Pitts |
| כותרת | A logical calculus of the ideas immanent in nervous activity |
| שנה | 1943 |
| כתב עת | The Bulletin of Mathematical Biophysics, vol. 5, issue 4, pp. 115–133. מוציא לאור לפי Crossref: Springer Science and Business Media LLC |
| DOI / קישור | 10.1007/BF02478259, https://doi.org/10.1007/BF02478259 |
| תאריך גישה | 2026-11-17 |
| סוג | מאמר בכתב עת שעבר שיפוט |
| רמת גישה | מטא-דאטה בלבד |
| דירוג אמינות | גבוה (לפרטים הביבליוגרפיים בלבד) |
| נימוק | הפרטים זהים ב-Crossref וב-OpenAlex. התקציר לא זמין (null ב-OpenAlex, ‏404 ב-Semantic Scholar, ועמוד Springer הפנה לעמוד הזדהות). |

### טענות שהמקור תומך בהן
1. **עובדה ביבליוגרפית/היסטורית בלבד:** ב-1943 פרסמו McCulloch ו-Pitts מאמר בשם "A logical calculus of the ideas immanent in nervous activity" בכתב העת The Bulletin of Mathematical Biophysics.

הערה: אין לייחס למאמר תוכן מסוים (למשל "נוירון סף בינארי") על סמך הרשומה הזו. התוכן לא אומת.

---

## דוגמאות, נוסחאות ונתונים

| # | פריט | מקור ומיקום |
|---|---|---|
| 1 | הנוירון: σ(Σᵢ wᵢxᵢ + b). מכפלה של הקלטים במשקלים, הוספת הטיה, ואז פונקציית הפעלה. | S-ch03-01, סעיפים Modeling one neuron ו-Single neuron as a linear classifier |
| 2 | צורת ה-PRD: `z = \sum_{i=1}^{n} w_i x_i + b`, ואחריה a = f(z). זה סימון שקול לפריט 1 (פרשנות, ראו הערות ב-S-ch03-01). | S-ch03-01 (מבנה); הסימון z הוא דידקטי |
| 3 | הקלט ליחידה בכתיב וקטורי: x = v·wᵀ + b | S-ch03-02, סעיף 2, משוואה 7, עמ' 2 |
| 4 | סיגמואיד על סכום משוקלל ועוד הטיה: p(h_j = 1) = 1 / (1 + exp(−b_j − Σᵢ v_i w_ij)) | S-ch03-02, סעיף 1.1, משוואה 2, עמ' 1 |
| 5 | Sigmoid: ‏σ(x) = 1 / (1 + e^(−x)) | S-ch03-01, Commonly used activation functions |
| 6 | Tanh: ‏tanh(x) = 2σ(2x) − 1 | S-ch03-01, Commonly used activation functions |
| 7 | ReLU: ‏f(x) = max(0, x). גרדיאנט 0 עבור x ≤ 0 ו-1 עבור x > 0. | S-ch03-01, Commonly used activation functions; S-ch03-02, סעיף 4, עמ' 3 |
| 8 | Leaky ReLU עם α ≈ 0.01 | S-ch03-01, Commonly used activation functions |
| 9 | האצה של פי 6 בהתכנסות עם ReLU לעומת tanh (מדווח בשם Krizhevsky et al.) | S-ch03-01, Commonly used activation functions (כולל כיתוב האיור) |
| 10 | כ-86 מיליארד נוירונים במערכת העצבים של האדם, כ-10^14 עד 10^15 סינפסות | S-ch03-01, Biological motivation and connections |
| 11 | ספירת פרמטרים: רשת 3→4→2 עם 6 נוירונים, 20 משקלים ו-6 הטיות, סך הכול 26 פרמטרים. רשת 3→4→4→1 עם 9 נוירונים, 32 משקלים ו-9 הטיות, סך הכול 41 פרמטרים. | S-ch03-01, Layer-wise organization |
| 12 | ארבע מגבלות של האנלוגיה הביולוגית (סוגי נוירונים, דנדריטים לא-ליניאריים, סינפסה כמערכת דינמית, תזמון קוצים) | S-ch03-01, Biological motivation and connections |

**דוגמה מספרית לשימוש הכותב:** אפשר לבנות דוגמה מספרית מומצאת (למשל שלושה קלטים, שלושה משקלים והטיה, וחישוב z ואז ReLU או סיגמואיד). דוגמה כזו לא לקוחה ממקור, ולכן לפי PRD סעיף 10 יש לסמן אותה בטקסט כ"דוגמה להמחשה" ולא להציג אותה כנתון.

## רעיונות להמחשה (הצעות)
> אלה הצעות של סוכן המחקר, ולא עובדות מהמקורות.

1. **סכמה של נוירון יחיד:** שלושה חיצים של קלטים x₁, x₂, x₃, עם משקל w_i על כל חץ. הם נכנסים לעיגול Σ, נוסף אליהם b, ומשם ממשיכים לקופסה f ולפלט. מתחת לסכמה מופיעה הנוסחה `z = \sum_{i=1}^{n} w_i x_i + b`, עם חיצי הסבר: "קלט", "משקל = חשיבות", "הטיה = סף/הזזה", "סכום".
2. **שלושה גרפים קטנים זה לצד זה:** sigmoid, ‏tanh, ‏ReLU, על טווח x בין 5- ל-5. אפשר לייצר אותם ב-Python/matplotlib מהנוסחאות בפריטים 5–7, ואין בהם נתונים אמפיריים.
3. **סכמת שכבות 3→4→2** כמו בדוגמה של CS231n (פריט 11), עם תיבת הסבר שסופרת משקלים והטיות (20 + 6 = 26). את האיור יש לצייר מחדש (TikZ), ולא להעתיק את האיור מהעמוד.
4. **טבלת השוואה "נוירון ביולוגי מול נוירון מלאכותי"**: דנדריטים מול קלטים, סינפסה מול משקל, קצב ירי מול פונקציית הפעלה, ועמודה של "מה האנלוגיה מפספסת" לפי ארבע המגבלות בפריט 12.
5. **ציר זמן זעיר (אופציונלי):** 1943 McCulloch & Pitts, ‏1958 Rosenblatt, ‏2010 Nair & Hinton (ReLU). מציגים רק שנים ושמות מאמרים, בלי לתאר את תוכן מאמרי 1943 ו-1958, שלא אומת.

## פערים / לא אומת
- **Goodfellow, Bengio & Courville, "Deep Learning" לא אומת.** האחזור של https://www.deeplearningbook.org/contents/intro.html החזיר רק placeholder של "Content truncated" (כמו ב-Smoke Test). אין לצטט את הספר.
- **תוכן המאמר של McCulloch & Pitts (1943) לא אומת.** יש רק מטא-דאטה. Springer הפנה לעמוד הזדהות, ‏Semantic Scholar החזיר 404, ו-OpenAlex לא כולל תקציר. אין לייחס למאמר מודל נוירון סף או תוכן אחר.
- **תוכן המאמר של Rosenblatt (1958) לא אומת מעבר לתקציר**, ואת התקציר עצמו קיבלתי כסיכום ולא כנוסח מילולי. אין לתאר את מבנה הפרספטרון על בסיס S-ch03-03.
- **המאמר של Krizhevsky et al. לא נפתח.** נתון "פי 6" מבוסס רק על הדיווח ב-S-ch03-01.
- **הנתונים הביולוגיים (86 מיליארד נוירונים, 10^14 עד 10^15 סינפסות)** מגיעים מרשימות קורס, ולא ממקור נוירו-מדעי ראשוני. אם הכותב רוצה להדגיש אותם, מומלץ להשתמש בניסוח "לפי רשימות הקורס CS231n", או לבקש סבב מחקר נוסף למקור ראשוני.
- **אין מקור שמשתמש בסימון z בנפרד** (z = Σ wᵢxᵢ + b ואז a = f(z)) בצורה המדויקת שב-PRD. המקורות כותבים את הביטוי בתוך הפונקציה. ההפרדה היא סימון דידקטי שקול.
- **מחבר ושנה של S-ch03-01 לא אומתו.**
- **DOI או עמוד PMLR של S-ch03-02 לא אומתו.** המקור נלקח מאתר המחבר.

## יומן אחזורים
| URL | תוצאה |
|---|---|
| https://cs231n.github.io/neural-networks-1/ | OK (2 אחזורים) |
| https://api.crossref.org/works/10.1037/h0042519 | OK (ללא תקציר) |
| https://api.crossref.org/works/10.1007/BF02478259 | OK (ללא תקציר) |
| https://www.cs.toronto.edu/~hinton/absps/reluICML.pdf | OK (הממיר לא חילץ טקסט, אבל הקובץ נשמר מקומית ועמודים 1–3 נקראו ישירות) |
| https://api.openalex.org/works/doi:10.1037/h0042519 | OK (תקציר קיים, הוחזר כסיכום) |
| https://api.openalex.org/works/doi:10.1007/BF02478259 | OK (ללא תקציר) |
| https://www.deeplearningbook.org/contents/intro.html | FAILED (placeholder של "Content truncated" בלי טקסט) |
| https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/BF02478259?fields=title,authors,year,venue,abstract | FAILED (HTTP 404) |
| https://api.semanticscholar.org/graph/v1/paper/DOI:10.1037/h0042519?fields=title,authors,year,venue,abstract | OK (ללא תקציר, המוציא לאור הסתיר אותו) |
| https://link.springer.com/article/10.1007/BF02478259 | FAILED (הפניית 303 לעמוד הזדהות idp.springer.com, לא נעשה מעקב) |
