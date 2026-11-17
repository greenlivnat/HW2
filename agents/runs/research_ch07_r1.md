# הרצה: research-agent, יחידה ch07, סבב 1 (M2)

| שדה | ערך |
|---|---|
| תאריך | 2026-11-17 |
| סוכן | `research-agent` |
| הופעל על ידי | Orchestrator, אחת משבע הרצות שרצו במקביל |
| התחלה | 15:23:40 JST בקירוב |
| סיום | 15:28:23 JST בקירוב (משך לפי הכלי: 283.4 שניות) |
| שימוש | 32 קריאות לכלים, 48,614 טוקנים |
| קובץ פלט | `docs/sources/chapter_07.md` |

## הפרומפט המלא שנשלח

```
M2 RESEARCH, unit ch07, round 1.

Read first: agents/research_agent.md (UPDATED spec: record fields incl. mandatory access level, one record per URL, examples/formulas/data section, visualization ideas, fetch log, open-API fallback rules), docs/PRD.md sections 5 and 10, docs/OUTLINE.md.

Chapter 7 — "האדם במעגל והעתיד" (~2 pages). Topics per PRD §5: effects on studying and work; human–machine collaboration (human-in-the-loop); skills for checking AI outputs; thinking about the future. Visual: scenario + summary and questions.

Requirements:
- At least 2, ideally 3–5, VERIFIED reliable sources; prefer peer-reviewed studies and official institutional reports. Candidates you MAY check (verify by fetching): Brynjolfsson, Li & Raymond "Generative AI at Work" (NBER working paper 2023 / QJE 2025); Noy & Zhang 2023 "Experimental evidence on the productivity effects of generative artificial intelligence" (Science); Dell'Acqua et al. 2023 "Navigating the Jagged Technological Frontier" (HBS working paper); UNESCO 2023 "Guidance for generative AI in education and research"; Amershi et al. 2019 "Guidelines for Human-AI Interaction" (CHI); EU AI Act Article 14 on human oversight (official EUR-Lex text). Choose what you can actually verify.
- Record access level honestly. Any effect sizes / percentages must be quoted exactly with location and the study's context (population, task) so they are not over-generalized.
- Visualization ideas (marked as suggestions).
- NEVER invent sources, DOIs, URLs, quotes or numbers.

Output: write ONLY docs/sources/chapter_07.md (Hebrew; bibliographic fields in original language). IDs: S-ch07-01, ... Structure: header; records; "דוגמאות, נוסחאות ונתונים"; "רעיונות להמחשה (הצעות)"; "פערים / לא אומת"; "יומן אחזורים".

Final message: structured report (verified sources count + access level each, all URLs OK/FAILED, gaps, files written).
```

## הפלט הגולמי שהסוכן החזיר (כפי שהתקבל אצל ה-Orchestrator)

```
RESEARCH REPORT: unit ch07, round 1

I wrote one file: C:\biu01\HW2\ai_book_starter\docs\sources\chapter_07.md. Chapter 7 now has 9 verified records (S-ch07-01 to 09), well above the minimum of 2. The main gap: no peer-reviewed study on how AI affects students' learning was found or verified. UNESCO, at landing-page level, is the only source on studying.

1. Verified sources and access level
- **S-ch07-01** Noy & Zhang, Science 381(6654):187–192, 2023, DOI 10.1126/science.adh2586. Abstract only, read via Crossref (science.org returned 403).
- **S-ch07-02** Brynjolfsson, Li & Raymond, "Generative AI at Work", NBER WP 31161, 2023, DOI 10.3386/w31161. Abstract only.
- **S-ch07-03** Same authors, The Quarterly Journal of Economics 140(2):889–942, 2025, DOI 10.1093/qje/qjae044. Abstract only, rebuilt from OpenAlex.
- **S-ch07-04** Dell'Acqua et al. (9 authors), "Navigating the Jagged Technological Frontier", Organization Science 37(2):403–423, 2026, DOI 10.1287/orsc.2025.21838. Abstract only, via Crossref and OpenAlex. I verified the published journal version, not the 2023 HBS working paper (which returned 403).
- **S-ch07-05** Amershi et al., "Guidelines for Human-AI Interaction", CHI 2019, DOI 10.1145/3290605.3300233. Abstract only, from the Microsoft Research landing page.
- **S-ch07-06** The official camera-ready PDF of the same paper. Full text, pages 1–3 read, including Table 1 with all 18 guidelines (G1–G18) in 4 phases.
- **S-ch07-07** UNESCO (Miao & Holmes), "Guidance for generative AI in education and research", 2023. Abstract only (landing page). The full document on unesdoc returned 403.
- **S-ch07-08** EU AI Act Art. 14 "Human oversight", from the European Commission's AI Act Service Desk page (consolidated text as at 27 July 2026). Full text of Article 14 only. The EUR-Lex/Official Journal text could not be loaded.
- **S-ch07-09** EU-OSHA page on Regulation (EU) 2024/1689. Metadata only: full title, adoption on 13 June 2024, application dates.

Effect sizes are quoted exactly, each with its population and task:
- **Noy & Zhang:** time −40%, quality +18%, from 453 professionals doing writing tasks.
- **Brynjolfsson, Li & Raymond:** +14% on average and +34% for novices, from 5,179 support agents (working paper). The journal version says +15% from 5,172 agents. The two versions differ, and the file warns the Writer about this.
- **Dell'Acqua et al.:** 12.2% more tasks and 25.1% faster inside the frontier; "19% less likely" to get a correct answer outside it; 758 workers.

2. URLs fetched (23 entries, also logged in the file)
OK:
- https://www.nber.org/papers/w31161
- https://api.crossref.org/works/10.1126/science.adh2586
- https://api.openalex.org/works/doi:10.2139/ssrn.4573321
- https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research
- https://api.crossref.org/works/10.1287/orsc.2025.21838
- https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14
- https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/
- https://api.crossref.org/works?query.title=Generative+AI+at+Work&query.author=Brynjolfsson&rows=3
- https://api.crossref.org/works/10.1145/3290605.3300233
- https://api.openalex.org/works/doi:10.1093/qje/qjae044
- https://osha.europa.eu/en/legislation/directive/regulation-20241689eu-artificial-intelligence
- https://www.microsoft.com/en-us/research/wp-content/uploads/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf
- One WebSearch query, used only to find URLs.

FAILED:
- https://www.science.org/doi/10.1126/science.adh2586 (403)
- https://www.hbs.edu/faculty/Pages/item.aspx?num=64700 (403)
- https://www.hbs.edu/ris/Publication%20Files/24-013_d9b45b68-9e74-42d6-a1c6-c72fb70c7282.pdf (403)
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321 (403)
- https://unesdoc.unesco.org/ark:/48223/pf0000386693 (403)
- Five EUR-Lex URLs, all returning empty content:
  - eli/reg/2024/1689/oj/eng
  - eli/reg/2024/1689/oj
  - eli/reg/2024/1689/oj/eng/xhtml
  - legal-content TXT/HTML?uri=OJ:L_202401689
  - legal-content TXT/PDF?uri=OJ:L_202401689

3. Gaps and unverified items
- **Students' learning:** no empirical, peer-reviewed study on AI's effect on learning (see above). A further research round is advisable if the chapter is to make an empirical claim about studying.
- **UNESCO age limit:** the guidance calls for an age limit, but the page I read gives no specific age. Any age figure is unverified.
- **HBS working-paper version of Dell'Acqua et al.:** not verified. Figures that appear only there (for example a quality-improvement percentage, or "percentage points" wording) must not be used.
- **AI Act Official Journal text:** the publication date (12 July 2024) and later amendments came only from search results and are unverified. Binding legal quotes should be checked against EUR-Lex.
- **Future-of-work forecasts** (job creation or loss numbers): no source checked, so no such numbers should go in the chapter.
- **Automation bias:** I found no empirical research on it, only the legal definition in Art. 14(4)(b).
- **Noy & Zhang:** the full text was not read.

The file also contains a data table, six visualization ideas (marked as suggestions, including a fictional scenario and a conceptual "jagged frontier" diagram with no invented data), and the fetch log.

4. Files written
- C:\biu01\HW2\ai_book_starter\docs\sources\chapter_07.md (new)

No other files were touched. docs/SOURCES.md was not created or changed, as instructed for this per-chapter run.
```

## קבצים שנוצרו או שונו
- נוצר: `docs/sources/chapter_07.md` (23,709 בתים, MD5 `8377e3a6...` בסוף סבב 1)
- `git status` (15:29:22): אין שינויים בקבצים במעקב.

## שער האיכות של ה-Orchestrator
| בדיקה | תוצאה |
|---|---|
| קובץ קיים, עם כל הסעיפים | ✅ |
| לפחות 2 מקורות מאומתים | ✅ 9 רשומות |
| רמת גישה לכל רשומה | ✅ (9 מתוך 9). רוב הרשומות בתקציר בלבד, ורק 2 בטקסט מלא |
| גדלי אפקט עם הקשר (אוכלוסייה ומשימה) | ✅, כולל אזהרה על פער בין גרסאות של Brynjolfsson et al. |
| כיסוי PRD סעיף 5 | ⚠️ **חלקי.** "השפעות על לימודים" מכוסה רק ברמת דף הנחיתה של UNESCO, בלי מחקר אמפירי |
| כתיבה רק בתחום | ✅ |

**החלטה:** השער עבר מבחינת הפורמט, אבל יש פער כיסוי. **הופעל סבב 2** (`research_ch07_r2.md`) כדי למצוא מחקרים אמפיריים על השפעת AI על למידה של סטודנטים.
