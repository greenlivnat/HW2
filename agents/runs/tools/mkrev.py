"""Create reviewer task file. Usage: python mkrev.py <n> <round> <gate_note> [prev_report]"""
import sys
n, rnd, note = sys.argv[1], int(sys.argv[2]), sys.argv[3]
prev = sys.argv[4] if len(sys.argv) > 4 else None
nn = f"0{n}"
T = f"""M3 {'RE-REVIEW' if prev else 'REVIEW'}, unit ch{nn}, round {rnd}.

Read first: agents/reviewer_agent.md; docs/STYLE_GUIDE.md (binding: voice, integrity rules, dough-story arc §3, box markers §4, illustration/formula/table/placeholder markers §5, palette §6, length §7); docs/PRD.md v1.4 (§5 chapter {n}, §6, §10, §11); docs/OUTLINE.md; docs/SOURCES.md (§1, §3.{n}, §3.8, §4); docs/sources/chapter_{nn}.md (full records); the Writer's task file agents/runs/tasks/writer_ch{nn}_r1_prompt.txt (it lists the chapter-specific source rules the Writer had to obey); chapters/chapter_01.txt (approved; for continuity and to detect repeated analogies).
{"Previous report: " + prev + ". Give EVERY previous defect a status (תוקן / לא תוקן / חלקי); new defect IDs continue the numbering. Compare versions with read-only git diff --no-index between agents/runs/versions/chapter_" + nn + "_r" + str(rnd-1) + ".txt and chapter_" + nn + "_r" + str(rnd) + ".txt." if prev else ""}

Deliverable: chapters/chapter_{nn}.txt (= agents/runs/versions/chapter_{nn}_r{rnd}.txt). No .tex/PDF yet: PDF-dependent DoD items are "לא רלוונטי בשלב זה".

Orchestrator gate note: {note}

Check:
1. FACTS & SOURCES (highest priority): every citation against its record's supported claims and access level; metadata-only records used only bibliographically; no item from SOURCES.md §3.8; no violation of the chapter-specific rules in the task file; every number/date carries a source and context; invented examples clearly framed as illustrations; no facts about baking chemistry; uncited substantive claims. Spot-check at least 2 claims against the original online source with WebFetch where reachable (blocked sites per STATUS §6: nature.com, science.org, ACM DL, PubMed, deeplearningbook.org, EUR-Lex — use the record instead).
2. STRUCTURE: PRD §5 topics for chapter {n} covered; opening question; "תובנות מרכזיות" (4–6); required special elements (chapter 3: formula + explanation of each component; chapter 4: the 9-block diagram exactly per OUTLINE incl. 'קבלת הטקסט' and the loop; chapter 5: table + chart markers and [ממתין ל-M4] placeholders with NO invented results); at least one [איור] line in STYLE_GUIDE §5 format using the palette.
3. STORY & CONTINUITY: the dough story advances per STYLE_GUIDE §3 (not restarted); consistent with chapter 1; no repeated analogies from chapter 1.
4. BOXES: 2–4 boxes, correct markers, fit the topic, no two of the same type in a row, each adds content, 40–120 words each.
5. STYLE: original voice (no imitation of any author), rich and accessible Hebrew, no clichés, no repetition, terms explained at first use, grammar/gender agreement, no Hebrew sentence starting with a Latin-script word.
6. LENGTH: STYLE_GUIDE §7 band; count clean words with Python (`python`, remove [..] markers and '##', count tokens containing a word character, body before "## מקורות לפרק").
7. ORIGINALITY: no near-translations of source sentences.

Output: write ONLY agents/runs/review_ch{nn}_r{rnd}.md (Hebrew): header (incl. URLs fetched + result); {"previous-defect status table; " if prev else ""}defect table (ID R-ch{nn}-NN, location, category עובדות/מקורות/מבנה/סגנון/מקוריות/עיצוב/טכני, severity קריטי/בינוני/קל, description, suggested fix); citation verification table; boxes & illustration checklist; short style assessment; DoD summary; `SCORE: <n>/100` (facts & sources 40, structure 20, style 25, length & format 15); LAST line exactly `VERDICT: PASS` or `VERDICT: REVISE` (REVISE if any open קריטי or בינוני defect). For each defect say whether fixing it needs a NEW source (route to research) or only rewriting.

Final message (SHORT, ≤ 200 words): path, defect counts by severity and category, IDs of קריטי/בינוני defects with one line each, which defects need new sources, score, verdict line.
"""
open(f"agents/runs/tasks/reviewer_ch{nn}_r{rnd}_prompt.txt", "w", encoding="utf-8").write(T)
print("ok", n, rnd)
