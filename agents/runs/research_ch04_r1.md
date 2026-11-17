# הרצה: research-agent, יחידה ch04, סבב 1 (M2)

| שדה | ערך |
|---|---|
| תאריך | 2026-11-17 |
| סוכן | `research-agent` |
| הופעל על ידי | Orchestrator, אחת משבע הרצות שרצו במקביל |
| התחלה | 15:23:40 JST בקירוב |
| סיום | 15:28:33 JST בקירוב (משך לפי הכלי: 293.0 שניות) |
| שימוש | 32 קריאות לכלים, 84,689 טוקנים |
| קובץ פלט | `docs/sources/chapter_04.md` |

## הפרומפט המלא שנשלח

```
M2 RESEARCH, unit ch04, round 1.

Read first: agents/research_agent.md (UPDATED spec: record fields incl. mandatory access level, one record per URL, examples/formulas/data section, visualization ideas, fetch log, open-API fallback rules), docs/PRD.md sections 5 and 10, docs/OUTLINE.md (note the proposed 9-block diagram).

Chapter 4 — "כיצד מודל שפה מייצר תשובה" (~3 pages). Topics per PRD §5: tokens; representations (embeddings); attention; next-token prediction; choosing from probabilities (softmax, sampling, temperature); a process diagram with ≥8 blocks and a discussion of how simplified it is. Key question: what happens after we type a question?

Requirements:
- At least 2, ideally 4–6, VERIFIED reliable sources; prefer academic/scientific with full text open. Candidates you MAY check (verify by fetching; arXiv abs pages and ACL Anthology usually work): Vaswani et al. 2017 "Attention Is All You Need"; Sennrich, Haddow & Birch 2016 BPE subword units (ACL); Radford et al. 2019 GPT-2 report; Brown et al. 2020 GPT-3; Holtzman et al. 2020 "The Curious Case of Neural Text Degeneration" (nucleus sampling); Mikolov et al. 2013 word2vec; official tokenizer documentation (e.g. Hugging Face tokenizers docs). Choose what you can actually verify.
- Record access level honestly. Capture source-backed formulas (e.g. scaled dot-product attention, softmax) with exact location, and which sources support each block of the 9-block diagram in OUTLINE (map block → source ID, or mark unsupported).
- Visualization ideas (marked as suggestions).
- NEVER invent sources, DOIs, URLs, quotes or numbers.

Output: write ONLY docs/sources/chapter_04.md (Hebrew; bibliographic fields in original language). IDs: S-ch04-01, ... Structure: header; records; "דוגמאות, נוסחאות ונתונים" (incl. diagram-block mapping); "רעיונות להמחשה (הצעות)"; "פערים / לא אומת"; "יומן אחזורים".

Final message: structured report (verified sources count + access level each, all URLs OK/FAILED, gaps, files written).
```

## הפלט הגולמי שהסוכן החזיר (כפי שהתקבל אצל ה-Orchestrator)

```
## דוח Research Agent: יחידה ch04, סבב 1

I wrote the sources file for chapter 4 with 8 verified sources, which meets the minimum of 2 and the target of 4–6. It is the only file I changed. All 9 diagram blocks are mapped to sources except "ניקוי קלט" (input cleaning), which turned out to be weak. That block needs your decision (see section 3, gap 1).

### 1. Chapter covered and verified sources
Chapter 4, "כיצד מודל שפה מייצר תשובה". 8 verified sources:

| ID | Source | Access level |
|---|---|---|
| S-ch04-01 | Vaswani et al., 2017, "Attention Is All You Need", arXiv 1706.03762 | טקסט מלא (pp. 2–5, 7) |
| S-ch04-02 | Sennrich, Haddow & Birch, 2016, ACL, pp. 1715–1725, DOI 10.18653/v1/P16-1162 | טקסט מלא (pp. 1715–1718) |
| S-ch04-03 | Holtzman et al., 2020, ICLR, "The Curious Case of Neural Text Degeneration", arXiv 1904.09751 | טקסט מלא (pp. 1–6) |
| S-ch04-04 | Radford et al., GPT-2 technical report (OpenAI) | טקסט מלא (pp. 1–4). The year 2019 is not on the PDF and was confirmed only indirectly, through S-ch04-03. |
| S-ch04-05 | Mikolov et al., 2013, word2vec, arXiv 1301.3781 | טקסט מלא (pp. 1–2) |
| S-ch04-06 | Hugging Face docs, "Tokenization algorithms" | טקסט מלא |
| S-ch04-07 | Hugging Face docs, "Generation strategies" | טקסט מלא |
| S-ch04-08 | Brown et al., 2020, GPT-3, arXiv 2005.14165 | תקציר בלבד |

The file also contains:
- **Formulas with exact locations:**
  - F1, scaled dot-product attention: S-01, Eq. 1, §3.2.1, p. 4.
  - F2/F2', next-token factorization: S-03 Eq. 1, p. 3, and S-04 Eq. 1, p. 2.
  - F3, softmax with temperature: S-03 Eq. 4, §3.3, p. 6.
  - F4, top-p: S-03 Eq. 2, p. 4.
- **A numbers table**, every value with its location.
- **Ready-to-use examples:** BPE on hug/pug, BPE on low/lower, King−Man+Woman, flat vs. peaked distributions.
- **The block-to-source map for the 9-block diagram:**
  - Blocks 3–9 have strong support.
  - Block 1 has partial support. No source describes a chat interface.
  - Block 2, "ניקוי קלט", has weak support and is problematic (gap 1).
  - Per the sources, blocks 4–9 repeat once for every new token, so the diagram needs a loop arrow back.
- **Source-backed points for the "how simplified is the diagram" discussion.**
- **7 visualization ideas**, marked as suggestions. Any invented values in them must be labeled as demo data.

### 2. URLs fetched
1. https://arxiv.org/abs/1706.03762: OK
2. https://arxiv.org/pdf/1706.03762v7: OK (the fetch tool couldn't extract the PDF text, so I read the downloaded file directly; same for the other PDFs below)
3. https://aclanthology.org/P16-1162/: OK (metadata only; the page has no abstract)
4. https://aclanthology.org/P16-1162.pdf: OK
5. https://arxiv.org/abs/1904.09751: OK
6. https://arxiv.org/pdf/1904.09751v2: OK
7. https://arxiv.org/html/1904.09751v2: OK
8. https://arxiv.org/abs/2005.14165: OK (abstract only)
9. https://arxiv.org/abs/1301.3781: OK
10. https://arxiv.org/pdf/1301.3781v3: OK
11. https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf: OK
12. https://huggingface.co/docs/transformers/tokenizer_summary: OK
13. https://huggingface.co/docs/transformers/generation_strategies: OK
14. https://huggingface.co/docs/transformers/model_doc/gpt2: OK (read, but not used as a source)
15. https://openai.com/index/better-language-models/: FAILED (HTTP 403)
16. https://api.openalex.org/works?search=Language%20Models%20are%20Unsupervised%20Multitask%20Learners&per-page=3: OK, but the GPT-2 report was not in the results
17. https://api.semanticscholar.org/graph/v1/paper/search?query=Language+Models+are+Unsupervised+Multitask+Learners&...: FAILED (HTTP 429)

### 3. Gaps and unverified items
1. **The "ניקוי קלט" block has no source support.** S-ch04-04 (§2.2, §3.1) actually describes the opposite: GPT-2 deliberately avoids lossy preprocessing such as lower-casing. I suggest rewording the block or marking it in the diagram as a simplification. Changing OUTLINE.md requires explaining the change to the user.
2. **Commercial chatbot layers have no source.** This covers system prompts, chat templates, instruction tuning, RLHF and filters. The chapter must not discuss them without another source.
3. **Hebrew tokenization:** not verified, so the chapter should give no numbers.
4. **Sizes of current models beyond GPT-2 and GPT-3:** not verified.
5. **Conference venues:** GPT-3 at NeurIPS 2020 and Vaswani et al. at NIPS 2017 were not verified. Both records cite arXiv only.
6. **GPT-2 report year:** confirmed only indirectly through Holtzman et al. Direct checks failed (403 from OpenAI, 429 from Semantic Scholar, no match in OpenAlex).
7. **Temperature, top_k and top_p:** not explained in the version of the Hugging Face page that I read. They are covered only by S-ch04-03.
8. **Diagram caveat:** Vaswani's original Transformer is an encoder-decoder built for translation, so Figure 1 should not be presented as an exact picture of a chatbot. I noted this in the S-ch04-01 record.

### 4. Files written
- C:\biu01\HW2\ai_book_starter\docs\sources\chapter_04.md (new file)

I did not touch any other file. I did not change `docs/SOURCES.md`: per the task, merging the per-chapter files into it is a separate run.
```

## קבצים שנוצרו או שונו
- נוצר: `docs/sources/chapter_04.md` (33,296 בתים, MD5 `18e0a006...`)
- `git status` (15:29:27): אין שינויים בקבצים במעקב.

## שער האיכות של ה-Orchestrator
| בדיקה | תוצאה |
|---|---|
| קובץ קיים, עם כל הסעיפים | ✅ |
| לפחות 2 מקורות מאומתים | ✅ 8 מקורות: 7 בטקסט מלא, 1 בתקציר בלבד |
| רמת גישה לכל רשומה | ✅ (8 מתוך 8) |
| נוסחאות עם מיקום מדויק | ✅ קשב, פירוק לטוקן הבא, softmax עם טמפרטורה, top-p |
| מיפוי 9 הבלוקים | ✅ 7 בלוקים בתמיכה חזקה, 1 חלקית, 1 חלשה ("ניקוי קלט") |
| כתיבה רק בתחום | ✅ |

**הערכת איכות:** זה המחקר החזק ביותר מבחינה מדעית. כמעט כל המקורות הם מאמרים מקוריים בטקסט מלא.

**הבלוק "ניקוי קלט":** לפי המקור, מודלים כמו GPT-2 דווקא נמנעים מעיבוד מקדים כזה. הבלוק מופיע ב-OUTLINE, ושינוי ב-OUTLINE הוא החלטה של המשתמשת. **ההמלצה שלי:** בשלב M4 לשנות את שם הבלוק ל"קבלת הטקסט" (או לסמן אותו כפישוט). כך התרשים יישאר עם 9 בלוקים (הדרישה היא 8 לפחות), ולא תיווצר טענה שאין לה מקור. זו החלטה פתוחה ולא ליקוי במחקר.

**החלטה:** השער עבר.
