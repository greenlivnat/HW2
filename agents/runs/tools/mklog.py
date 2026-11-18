"""Assemble an agents/runs/<agent>_<unit>_r<N>.md run log.
Usage: python mklog.py <out_path> <title> <meta_table_md_file_or_-> <prompt_file> <raw_file> <gate_md_file>
Meta and gate are files in the scratchpad (UTF-8)."""
import sys
out, title, meta, prompt, raw, gate = sys.argv[1:7]
r = lambda f: open(f, encoding='utf-8').read()
txt = f"# {title}\n\n{r(meta)}\n## הפרומפט המלא שנשלח\n\n```\n{r(prompt).rstrip()}\n```\n\n## הפלט הגולמי שהסוכן החזיר (כלשונו)\n\n```\n{r(raw).rstrip()}\n```\n\n{r(gate)}"
open(out, 'w', encoding='utf-8').write(txt)
print('wrote', out)
