from pathlib import Path
import matplotlib.pyplot as plt

stages = ['M5A', 'External review', 'v0.95']
checks = [82, 90, 92]
fig, ax = plt.subplots(figsize=(8,4.5))
bars = ax.bar(stages, checks, color=['#7956D8','#00A9A8','#101B35'], width=.53)
ax.bar_label(bars, padding=5, fontsize=13, fontweight='bold')
ax.set_ylim(0,105)
ax.set_ylabel('Passed automated checks')
ax.set_title('Growth of the quality assurance suite', fontweight='bold')
ax.spines[['top','right']].set_visible(False)
ax.grid(axis='y', alpha=.18)
ax.set_axisbelow(True)
fig.text(.5,.015,'Reported by Claude Code; not an independent grade.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.045,1,1))
fig.savefig(Path(__file__).with_suffix('.png'),dpi=180)
