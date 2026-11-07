"""Build report.pdf: for each problem, the handwritten pseudocode photo,
the commented Python code, citations and links.

Put photos in pseudocode/ named frog_jmp.jpg, perm_check.jpg, ... (.jpg or .png)
and fill in the two links below, then run:  python3 make_report.py
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (Image, PageBreak, Paragraph, Preformatted,
                                SimpleDocTemplate, Spacer)

STUDENT_NAME = "[Your Name]"
GITHUB_LINK = "[https://github.com/your-username/codility-solutions]"
AI_CHAT_LINK = "[link to this AI conversation]"

PROBLEMS = [
    ("FrogJmp", "frog_jmp", "3-time_complexity/frog_jmp"),
    ("PermCheck", "perm_check", "4-counting_elements/perm_check"),
    ("MissingInteger", "missing_integer", "4-counting_elements/missing_integer"),
    ("MaxCounters", "max_counters", "4-counting_elements/max_counters"),
    ("PassingCars", "passing_cars", "5-prefix_sums/passing_cars"),
]

styles = getSampleStyleSheet()
code_style = styles["Code"].clone("code", fontSize=7.5, leading=9.5)
here = os.path.dirname(os.path.abspath(__file__))


def photo(stem):
    for ext in (".jpg", ".jpeg", ".png"):
        path = os.path.join(here, "pseudocode", stem + ext)
        if os.path.exists(path):
            img = Image(path)
            scale = min(16 * cm / img.imageWidth, 11 * cm / img.imageHeight)
            img.drawWidth, img.drawHeight = img.imageWidth * scale, img.imageHeight * scale
            return img
    return Paragraph(f"<i>[Add pseudocode/{stem}.jpg]</i>", styles["Normal"])


story = [Paragraph("Codility Practice: Five Problems", styles["Title"]),
         Paragraph(f"Name: {STUDENT_NAME}", styles["Normal"]),
         Paragraph(f"GitHub repository: {GITHUB_LINK}", styles["Normal"]),
         Paragraph(f"AI conversation: {AI_CHAT_LINK}", styles["Normal"]),
         PageBreak()]

for i, (title, stem, path) in enumerate(PROBLEMS, 1):
    url = f"https://app.codility.com/programmers/lessons/{path}/"
    with open(os.path.join(here, stem + ".py")) as f:
        code = f.read()
    story += [Paragraph(f"{i}. {title}", styles["Heading1"]),
              Paragraph(f"Problem: {url}", styles["Normal"]),
              Paragraph("1. Handwritten pseudocode", styles["Heading3"]), photo(stem),
              Paragraph("2. Python code", styles["Heading3"]), Preformatted(code, code_style),
              Paragraph("3. Citations", styles["Heading3"]),
              Paragraph(f"Problem statement: Codility Lessons, {url}<br/>"
                        "AI tool: Claude (Anthropic), used to help draft the solution and pseudocode.",
                        styles["Normal"]),
              Paragraph("4. Links", styles["Heading3"]),
              Paragraph(f"GitHub: {GITHUB_LINK}<br/>AI conversation: {AI_CHAT_LINK}", styles["Normal"]),
              PageBreak()]

SimpleDocTemplate(os.path.join(here, "report.pdf"), pagesize=A4,
                  leftMargin=2 * cm, rightMargin=2 * cm,
                  topMargin=1.8 * cm, bottomMargin=1.8 * cm).build(story)
print("Wrote report.pdf")
