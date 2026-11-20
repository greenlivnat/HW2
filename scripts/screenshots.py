"""Render README screenshots from book.pdf (pages are found by their content, not by number).

Run from the project root:  python scripts/screenshots.py
Writes screenshots/*.png (PNG, 110 dpi) and prints the page chosen for each shot.
"""
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "book.pdf"
OUT = ROOT / "screenshots"
DPI = "110"

# name -> text that must appear on the page (first match wins); None = fixed page 1 (cover)
SHOTS = {
    "01_cover": None,
    "02_toc": "תוכן העניינים",
    "03_chapter_opener": "מי כתב את התשובה",
    "04_neuron_math": "המשקולת של אותו קלט",
    "05_temperature_chart": "אותם ציונים, שתי טמפרטורות",
    "06_experiment_chart": "דיוק אימון מול דיוק בדיקה",
    "07_appendix_scores": "ציוני הביקורת הפנימית",
}


def page_texts():
    out = subprocess.run(["pdftotext", "-enc", "UTF-8", str(PDF), "-"], capture_output=True,
                         text=True, encoding="utf-8").stdout
    return out.split("\f")


def main():
    OUT.mkdir(exist_ok=True)
    pages = page_texts()
    for name, needle in SHOTS.items():
        if needle is None:
            n = 1
        else:
            hits = [i for i, t in enumerate(pages, 1) if needle in t]
            if not hits:
                print(f"{name}: text not found, skipped"); continue
            n = hits[-1] if name in ("05_temperature_chart", "06_experiment_chart", "07_appendix_scores") else hits[0]
        subprocess.run(["pdftoppm", "-r", DPI, "-png", "-singlefile", "-f", str(n), "-l", str(n),
                        str(PDF), str(OUT / name)], check=True)
        print(f"{name}: page {n}")


if __name__ == "__main__":
    main()
