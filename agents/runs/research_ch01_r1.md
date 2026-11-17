# הרצה: research-agent, יחידה ch01, סבב 1 (M2)

| שדה | ערך |
|---|---|
| תאריך | 2026-11-17 |
| סוכן | `research-agent` |
| הופעל על ידי | Orchestrator, אחת משבע הרצות שרצו במקביל |
| התחלה | 15:23:40 JST בקירוב |
| סיום | 15:29:19 JST בקירוב (משך לפי הכלי: 339.4 שניות) |
| שימוש | 34 קריאות לכלים, 63,615 טוקנים |
| קובץ פלט | `docs/sources/chapter_01.md` |

## הפרומפט המלא שנשלח

```
M2 RESEARCH, unit ch01, round 1.

Read first: agents/research_agent.md (UPDATED spec: record fields incl. mandatory access level, one record per URL, examples/formulas/data section, visualization ideas, fetch log, open-API fallback rules), docs/PRD.md sections 5 and 10, docs/OUTLINE.md.

Chapter 1 — "מהי בינה מלאכותית?" (~2 pages). Topics per PRD §5: definition of AI; the difference between AI, machine learning and deep learning; what makes a system "learn"; key question: how does AI differ from ordinary software (rules written by a programmer vs. behavior learned from data). Visual element in OUTLINE: concept map.

Requirements:
- At least 2, ideally 3–5, VERIFIED reliable sources; prefer academic/scientific (peer-reviewed papers, recognized textbooks, official institutional documents). Candidates you MAY check (do not assume they exist or what they say — verify by fetching): McCarthy et al. 1955 Dartmouth proposal (official Stanford copy); Turing 1950 "Computing Machinery and Intelligence"; Tom Mitchell's definition of learning (Machine Learning, 1997); Samuel 1959; LeCun, Bengio & Hinton 2015 "Deep learning"; official definitions (e.g. OECD AI system definition). Choose what you can actually verify.
- For each record, state access level (טקסט מלא / תקציר בלבד / מטא-דאטה בלבד) honestly.
- Provide usable examples, definitions to quote/paraphrase, and any numbers — each tied to a source ID and location.
- Provide visualization ideas (marked as your suggestions).
- NEVER invent sources, DOIs, URLs, quotes or numbers. Unverified → mark לא אומת and exclude from usable claims.

Output: write ONLY docs/sources/chapter_01.md (Hebrew; bibliographic fields in original language). IDs: S-ch01-01, S-ch01-02, ... Structure: header; records; "דוגמאות, נוסחאות ונתונים"; "רעיונות להמחשה (הצעות)"; "פערים / לא אומת"; "יומן אחזורים" (every URL tried, OK/FAILED + reason).

Final message: your structured report (verified sources count with access level each, all URLs OK/FAILED, gaps, files written).
```

## הפלט הגולמי שהסוכן החזיר (כפי שהתקבל אצל ה-Orchestrator)

```
## Research report for ch01, round 1

I wrote `C:\biu01\HW2\ai_book_starter\docs\sources\chapter_01.md`. It has 10 records: 8 are verified and usable, and 2 are verified only for bibliographic details. The minimum of 2 verified sources is met.

**Path conflict to check:** the role spec and your prompt both say to write per-chapter files to `docs/sources/chapter_XX.md`, so I did that. My system prompt says to write only to `docs/SOURCES.md`. I did not touch `docs/SOURCES.md`; merging into it needs a separate run. Please confirm with `git status` that the new file is the only change.

### 1. Sources, with access level

| ID | Source | Access level |
|---|---|---|
| S-ch01-01 | McCarthy, Minsky, Rochester, Shannon, Dartmouth Proposal (31 Aug 1955), McCarthy's Stanford site | טקסט מלא (full text) |
| S-ch01-02 | Turing 1950, "Computing Machinery and Intelligence", Mind LIX(236):433–460, DOI 10.1093/mind/LIX.236.433 | טקסט מלא (HTML on the OUP site; the PDF is subscribers only) |
| S-ch01-03 | Mitchell 2006, "The Discipline of Machine Learning", CMU-ML-06-108 | טקסט מלא (title page, abstract and pp. 1–2 read: §1 and §2.1) |
| S-ch01-04 | Mitchell 1997, *Machine Learning* (McGraw Hill, ISBN 0070428077), book page | מטא-דאטה בלבד (metadata only) |
| S-ch01-05 | LeCun, Bengio, Hinton 2015, "Deep learning", Nature 521:436–444, DOI 10.1038/nature14539 | תקציר בלבד (abstract only, via Europe PMC) |
| S-ch01-06 | Samuel 1959, IBM J. R&D 3(3):210–229, DOI 10.1147/rd.33.0210 | מטא-דאטה בלבד (metadata only) |
| S-ch01-07 | Stone et al., AI100 2016 report, "Defining AI" page (Stanford) | טקסט מלא (the page) |
| S-ch01-08 | Same AI100 report, "AI Research Trends" page | טקסט מלא (the page) |
| S-ch01-09 | OECD AI Principles page: the official definition of "AI system" | טקסט מלא (the page) |
| S-ch01-10 | Russell, Perset, Grobelnik 2023, "Updates to the OECD's definition of an AI system explained" | טקסט מלא |

**What the sources cover:**
- **Defining AI:** S-01, S-07 and S-09.
- **Machine learning and what makes a system "learn":** S-03 gives the T/P/E definition. It also contrasts ML with hand-programming: computer science is "manually program computers", ML is getting computers "to program themselves".
- **Deep learning:** S-05 (abstract) and S-08.
- **History:** S-01 and S-02.

The file also contains:
- **Examples, formulas and data:** 6 definitions, a conceptual T/P/E scheme, 6 examples and 9 numbers or dates. Each has a source ID and a location.
- **Visualization ideas:** 5 ideas, marked as my suggestions. The first is the concept map of nested circles that OUTLINE calls for.

### 2. URL fetch log
**OK**
- http://www-formal.stanford.edu/jmc/history/dartmouth/dartmouth.html
- https://academic.oup.com/mind/article/LIX/236/433/986238
- https://oecd.ai/en/wonk/ai-system-definition-update
- https://oecd.ai/en/ai-principles
- https://api.crossref.org/works/10.1038/nature14539
- https://api.openalex.org/works/doi:10.1038/nature14539 (no abstract)
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038/nature14539&resultType=core&format=json (includes the abstract)
- https://api.crossref.org/works/10.1147/rd.33.0210
- https://api.semanticscholar.org/graph/v1/paper/DOI:10.1147/rd.33.0210?fields=... (no abstract; gives the year wrongly as 1995)
- http://www.cs.cmu.edu/~tom/mlbook.html
- http://www.cs.cmu.edu/~tom/pubs/MachineLearning.pdf (the summarizer could not decode it, so I read the saved PDF directly)
- http://www.cs.cmu.edu/~tom/mlbook/keyIdeas.pdf (downloaded but not read; not used as a source)
- https://ai100.stanford.edu/2016-report/section-i-what-artificial-intelligence/defining-ai
- https://ai100.stanford.edu/2016-report/section-i-what-artificial-intelligence/ai-research-trends
- https://ai100.stanford.edu/2016-report

**FAILED**
- http://jmc.stanford.edu/articles/dartmouth/dartmouth.pdf: SSL certificate mismatch.
- https://www.nature.com/articles/nature14539: 303 redirect to a login page.
- https://api.semanticscholar.org/graph/v1/paper/DOI:10.1038/nature14539?...: HTTP 404.
- https://ieeexplore.ieee.org/document/5392560: page came back empty.
- http://www.cs.cmu.edu/~tom/files/MachineLearningTomMitchell.pdf: larger than the 10MB fetch limit.

**Deliberately not fetched**
- http://www.cs.virginia.edu/~evans/greatworks/samuel1959.pdf: an unofficial copy.

### 3. Gaps and unverified items
1. **Mitchell 1997 definition:** I did not read the book's own T/P/E definition (chapter 1) or its checkers example. The writer should cite the equivalent 2006 definition in S-03 instead.
2. **Samuel 1959:** only the bibliographic details are verified. The well-known quote "learn without being explicitly programmed" is not verified in any source and must not be used.
3. **The AI ⊃ ML ⊃ DL hierarchy:** no verified source states it directly. It can only be supported indirectly (S-08, S-05, S-03), so the chapter should present it as the author's own summary.
4. **Not checked this round:** Russell & Norvig's textbook and Goodfellow et al. Neither can be cited.
5. **LeCun 2015:** abstract only, so claims from it must stay at the level of the abstract.
6. **OECD definition date:** the exact approval date of the updated definition is not verified. S-09 only says the Recommendation was "updated in May 2024".
7. **Turing's 10^9:** the superscript was lost in the HTML ("109"). Reading it as 10^9 is the obvious interpretation but I did not check it against the original PDF.

### 4. Files written
- `C:\biu01\HW2\ai_book_starter\docs\sources\chapter_01.md` (new). No other project files were touched.
```

## קבצים שנוצרו או שונו
- נוצר: `docs/sources/chapter_01.md` (32,802 בתים)
- `git status` (15:31:49): השינויים היחידים הם `docs/sources/` וקובצי ההרצה שה-Orchestrator כתב. אין שינויים בקבצים במעקב.

## שער האיכות של ה-Orchestrator
| בדיקה | תוצאה |
|---|---|
| קובץ קיים, עם כל הסעיפים | ✅ |
| לפחות 2 מקורות מאומתים | ✅ 10 רשומות: 7 בטקסט מלא, 1 בתקציר בלבד, 2 במטא-דאטה בלבד |
| רמת גישה לכל רשומה | ✅ (10 מתוך 10) |
| כיסוי PRD סעיף 5 | ✅ הגדרת AI, ההבדל בין AI, ‏ML ו-DL, ומה הופך מערכת ל"לומדת" |
| כתיבה רק בתחום | ✅ |

**הערכת איכות:** חזק. המקורות ההיסטוריים (Dartmouth, ‏Turing) והגדרה רשמית (OECD) נקראו בטקסט מלא. הסוכן נמנע בצדק מהציטוט המפורסם שמיוחס ל-Samuel, כי לא אומת.

**ממצא חשוב על ההגדרות:** הסוכן דיווח שבהגדרות שלו (system prompt) כתוב "Write ONLY to docs/SOURCES.md". זה הנוסח **הישן** של `.claude/agents/research-agent.md`, לפני העדכון שבוצע היום לפני ההרצה. **מסקנה:** Claude Code טוען את הגדרות תתי-הסוכנים בתחילת הסשן, ולכן עריכה של הקובץ באמצע הסשן לא משפיעה עד הסשן הבא. במקרה הזה לא נגרם נזק: הפרומפט ומפרט התפקיד (`agents/research_agent.md`, שהסוכן קורא בכל הרצה) הגדירו את הנתיב החדש. הממצא נרשם בלקחים.

**החלטה:** השער עבר.
