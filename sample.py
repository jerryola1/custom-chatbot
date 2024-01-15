from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

# Create a SimpleDocTemplate object for multi-page support
doc = SimpleDocTemplate("cv_template1.pdf", pagesize=A4)

# Sample content for the professional experience section
experiences = [
    "Experience 1: Details about experience 1...",
    "Experience 2: Details about experience 2...",
    # Add more experiences as needed
]

# Get standard styles
styles = getSampleStyleSheet()
styleN = styles['Normal']

# List to hold the flowables
flowables = []

# Add the 'Professional Experience' heading
flowables.append(Paragraph("<b>Professional Experience</b>", styleN))
flowables.append(Spacer(1, 12))

# Add each experience as a Paragraph
for experience in experiences:
    flowables.append(Paragraph(experience, styleN))
    flowables.append(Spacer(1, 12))  # Add space after each experience

# Build the document
doc.build(flowables)
