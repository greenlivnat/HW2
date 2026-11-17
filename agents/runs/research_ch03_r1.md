# הרצה: research-agent, יחידה ch03, סבב 1 (M2)

| שדה | ערך |
|---|---|
| תאריך | 2026-11-17 |
| סוכן | `research-agent` |
| הופעל על ידי | Orchestrator, אחת משבע הרצות שרצו במקביל |
| התחלה | 15:23:40 JST בקירוב |
| סיום | 15:27:12 JST בקירוב (משך לפי הכלי: 211.4 שניות) |
| שימוש | 18 קריאות לכלים, 41,417 טוקנים |
| קובץ פלט | `docs/sources/chapter_03.md` |

## הפרומפט המלא שנשלח

```
M2 RESEARCH, unit ch03, round 1.

Read first: agents/research_agent.md (UPDATED spec: record fields incl. mandatory access level, one record per URL, examples/formulas/data section, visualization ideas, fetch log, open-API fallback rules), docs/PRD.md sections 5 and 10, docs/OUTLINE.md. Also note the verified smoke-test sources in agents/runs/smoke_test/sources_smoke.md (Rumelhart et al. 1986; Stanford CS231n optimization notes) — you may re-verify and reuse them under new IDs if relevant.

Chapter 3 — "הרשת הנוירונית מבפנים" (~3 pages). Topics per PRD §5: the artificial neuron; weights and bias; layers; activation functions; the formula z = \sum_{i=1}^{n} w_i x_i + b with an interpretation of each component; limits of the brain analogy. Key question: how do numbers connect to a prediction? Visual: formula + small schematic.

Requirements:
- At least 2, ideally 3–5, VERIFIED reliable sources; prefer academic/scientific. Candidates you MAY check (verify by fetching): McCulloch & Pitts 1943; Rosenblatt 1958 "The perceptron" (Psychological Review); Stanford CS231n "Neural Networks Part 1" notes (which discuss the neuron model, activation functions and the biological analogy's limits); Goodfellow, Bengio & Courville "Deep Learning" (note: deeplearningbook.org failed to fetch in the smoke test — try other chapters/URLs or skip); Nair & Hinton 2010 ReLU (ICML). Choose what you can actually verify.
- Record access level honestly. Capture the exact formula form(s) used in sources (with location) and source-backed statements about activation functions (sigmoid, tanh, ReLU) and about the biological analogy's limits.
- Visualization ideas (marked as suggestions).
- NEVER invent sources, DOIs, URLs, quotes or numbers.

Output: write ONLY docs/sources/chapter_03.md (Hebrew; bibliographic fields in original language). IDs: S-ch03-01, ... Structure: header; records; "דוגמאות, נוסחאות ונתונים"; "רעיונות להמחשה (הצעות)"; "פערים / לא אומת"; "יומן אחזורים".

Final message: structured report (verified sources count + access level each, all URLs OK/FAILED, gaps, files written).
```

## הפלט הגולמי שהסוכן החזיר (כפי שהתקבל אצל ה-Orchestrator)

```
## Research report: ch03, round 1 ("הרשת הנוירונית מבפנים")

I verified 4 sources for chapter 3, which meets the minimum of 2. Two of them I read in full text. Everything is in `C:\biu01\HW2\ai_book_starter\docs\sources\chapter_03.md`, and that is the only file I wrote. I did not write `docs/SOURCES.md`, as you instructed.

### 1. Verified sources

| ID | Source | Access level | Reliability |
|---|---|---|---|
| S-ch03-01 | Stanford CS231n notes, "Neural Networks Part 1", https://cs231n.github.io/neural-networks-1/ (no author or year shown on the page) | טקסט מלא | High for concepts; medium as a bibliographic source |
| S-ch03-02 | Nair & Hinton, "Rectified Linear Units Improve Restricted Boltzmann Machines", ICML 2010 (PDF on Hinton's University of Toronto site) | טקסט מלא, pages 1–3 only | High |
| S-ch03-03 | Rosenblatt 1958, "The perceptron…", Psychological Review 65(6):386–408, DOI 10.1037/h0042519 | תקציר בלבד | High (bibliographic details and the historical fact only) |
| S-ch03-04 | McCulloch & Pitts 1943, "A logical calculus…", Bull. Math. Biophysics 5(4):115–133, DOI 10.1007/BF02478259 | מטא-דאטה בלבד | High (bibliographic details only) |

What these sources support, each with its section or page in the file:
- **Neuron formula:**
  - CS231n gives σ(Σᵢ wᵢxᵢ + b), with the text "dot product … adds the bias and applies the non-linearity".
  - Nair & Hinton give the vector form x = v·wᵀ + b (eq. 7) and a sigmoid of a weighted sum plus bias (eq. 2).
- **Activation functions:**
  - Sigmoid, tanh, ReLU and Leaky ReLU, with their formulas and quoted pros and cons (CS231n).
  - max(0, x) and its gradient (Nair & Hinton, section 4).
- **Limits of the brain analogy:** CS231n says "very coarse" and lists four reasons: neuron types, nonlinear dendrites, a synapse is a dynamical system rather than a single weight, and spike timing.
- **Layers and parameter counts:** network 3→4→2 has 26 parameters, and network 3→4→4→1 has 41.
- **Numbers to a prediction:** a single neuron with a sigmoid acts as a binary classifier (logistic regression).
- **Biological numbers:** about 86 billion neurons and about 10^14 to 10^15 synapses, as quoted in the CS231n notes.

The file also has the five requested sections: examples, formulas and data (12 items with locations), visualization ideas (5, marked as suggestions), gaps, and the fetch log.

### 2. URLs fetched
- https://cs231n.github.io/neural-networks-1/: OK (2 fetches)
- https://api.crossref.org/works/10.1037/h0042519: OK (no abstract)
- https://api.crossref.org/works/10.1007/BF02478259: OK (no abstract)
- https://www.cs.toronto.edu/~hinton/absps/reluICML.pdf: OK. The fetch tool could not extract text, but the PDF was saved locally and I read pages 1–3 directly.
- https://api.openalex.org/works/doi:10.1037/h0042519: OK (the abstract came back only as a summary)
- https://api.openalex.org/works/doi:10.1007/BF02478259: OK (no abstract)
- https://api.semanticscholar.org/graph/v1/paper/DOI:10.1037/h0042519?fields=title,authors,year,venue,abstract: OK (the publisher hid the abstract)
- https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/BF02478259?fields=title,authors,year,venue,abstract: FAILED (HTTP 404)
- https://www.deeplearningbook.org/contents/intro.html: FAILED (placeholder of "Content truncated", no text)
- https://link.springer.com/article/10.1007/BF02478259: FAILED (303 redirect to a login page)

### 3. Gaps and unverified items
- **Goodfellow, Bengio & Courville, "Deep Learning":** not verified, and not included.
- **McCulloch & Pitts (1943):** only the bibliographic details are verified. The writer must not describe what the paper says, for example a threshold neuron.
- **Rosenblatt (1958):** verified only at the level of the abstract, and the abstract came back as a summary rather than verbatim. The writer must not describe how the perceptron works based on this source.
- **"Factor of 6" ReLU speedup:** it comes only from what CS231n reports about Krizhevsky et al. I did not open the original paper.
- **86 billion neurons and 10^14 to 10^15 synapses:** these come from course notes, not a primary neuroscience source.
- **The PRD's separate z notation:** no source writes z = Σwᵢxᵢ + b and then f(z) as two separate steps. The sources put the whole sum inside the function. The split form means the same thing and is just a teaching notation.
- **CS231n author and year:** not shown on the page, so not verified.
- **DOI or PMLR page for Nair & Hinton:** not verified.
- **Numerical example in the chapter:** any worked example with made-up numbers has no source behind it. Per PRD §10 it must be labeled as an illustration.

### 4. Files written
- `C:\biu01\HW2\ai_book_starter\docs\sources\chapter_03.md` (new file; I created the `docs\sources\` directory as part of this)
```

## קבצים שנוצרו או שונו
- נוצר: `docs/sources/chapter_03.md` (21,972 בתים)
- `git status` (15:28:03): השינוי היחיד הוא `?? docs/sources/`. אין שינויים בקבצים במעקב.

## שער האיכות של ה-Orchestrator
| בדיקה | תוצאה |
|---|---|
| קובץ קיים, עם כל הסעיפים (רשומות, דוגמאות, המחשה, פערים, יומן) | ✅ |
| לפחות 2 מקורות מאומתים | ✅ 4 מקורות (2 בטקסט מלא, 1 בתקציר בלבד, 1 במטא-דאטה בלבד) |
| רמת גישה מצוינת לכל רשומה | ✅ |
| נוסחה ופעילות מגובות במקור | ✅ CS231n ו-Nair & Hinton (בטקסט מלא) |
| כתיבה רק בתחום | ✅ |

**הערכת איכות:** הכיסוי של PRD סעיף 5 מלא: נוירון, משקלים והטיה, שכבות, פונקציות הפעלה, הנוסחה ומגבלות האנלוגיה למוח. המקורות ההיסטוריים (1943, 1958) מאומתים רק ביבליוגרפית, ולכן מותר להשתמש בהם רק כציון היסטורי. המספרים הביולוגיים מגיעים ממקור משני.

**החלטה:** השער עבר.
