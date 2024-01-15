from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.enums import TA_CENTER

# # Set up the PDF file
# c = canvas.Canvas("cv_template.pdf", pagesize=A4)
# width, height = A4  # A4 size

# # Set up the styles
# styles = getSampleStyleSheet()
# styleN = styles['Normal']
# styleH = styles['Heading1']

# # Define custom styles for the CV
# custom_style = ParagraphStyle(
#     'custom',
#     parent=styles['Normal'],
#     fontName='Helvetica',
#     fontSize=10,
#     leading=12,
#     alignment=TA_CENTER,
# )

# # Define the coordinates for the header, which will need to be adjusted
# x_center = width / 2
# y_position = height - 100  # Adjust this value as needed

# # Add the header (Name and Surname, Job title)
# c.setFont("Helvetica-Bold", 24)  # Adjust the font size as needed
# c.drawCentredString(x_center, y_position, "NAME AND SURNAME")
# c.setFont("Helvetica", 14)
# c.drawCentredString(x_center, y_position - 30, "JOB TITLE")  # Adjust for correct spacing

# # Placeholder for the contact information graphics - to be added later

# # Save the PDF to see the header
# #c.save()

# #print("Initial CV structure with header has been created: cv_template.pdf")

# # Placeholder function for contact graphics
# def add_contact_info_placeholder(canvas_obj, x, y):
#     canvas_obj.setStrokeColorRGB(0, 0, 0)  # Set color to black
#     canvas_obj.setLineWidth(1)
#     # Draw rectangles as placeholders for icons
#     canvas_obj.rect(x, y, 16, 16)  # Adjust size as needed
#     # Placeholder for text next to the icon
#     canvas_obj.drawString(x + 20, y, "Contact Information Placeholder")

# # Header is already added from previous code

# # Coordinates for the contact information placeholders
# x_left_margin = 50  # Adjust this value as needed
# y_contact_info = y_position - 70  # Adjust this value as needed

# # Add placeholders for contact information graphics
# add_contact_info_placeholder(c, x_left_margin, y_contact_info)  # For Personal Address
# add_contact_info_placeholder(c, x_left_margin, y_contact_info - 20)  # For Email
# add_contact_info_placeholder(c, x_left_margin, y_contact_info - 40)  # For Mobile

# # Continue adding the other sections...

# # Save the PDF and check the layout
# c.save()

# print("Added contact information placeholders to the CV template: /mnt/data/cv_template.pdf")


#from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, white

def draw_icon_placeholder(c, x, y, size=12):
    """Draws a circular icon placeholder at the specified coordinates."""
    c.circle(x, y, size // 2, stroke=1, fill=0)

def create_cv():
    """Creates the CV template."""
    c = canvas.Canvas("cv_template.pdf", pagesize=A4)
    width, height = A4

    c.setFillColor(black)

    # Draw the rectangle for the background
    header_height = 80  # The height of the header background
    header_y_position = height - header_height - 60  # Adjust the vertical position of the header
    c.rect(0, header_y_position, width, header_height, stroke=0, fill=1)

    # Set the fill color back to white for the text
    c.setFillColor(white)  # RGB color for white

    # Header with name and job title
    c.setFont("Helvetica-Bold", 24)
    # The text is moved down by half the header height to center it
    c.drawCentredString(width / 2, header_y_position + (header_height / 2) - 12, "NAME AND SURNAME")
    c.setFont("Helvetica", 12)
    c.drawCentredString(width / 2, header_y_position + (header_height / 4) - 6, "JOB TITLE")

    # Reset the fill color to black for the rest of the text
    c.setFillColor(black)  # Black

    # Contact Information Section
    contact_info_y_position = height - 180  # Starting Y position of the contact info
    contact_font = "Helvetica"
    contact_font_size = 10
    icon_size = 12  # Size of the icon
    text_offset_from_icon = 15  # Distance of text from the icon
    details_offset = 15  # Space between the label and details
    column_width = width / 3  # Divide the width of the page into 3 columns

    # Define a function to draw a contact information column
    def draw_contact_column(column_x_center, label, details):
        # Calculate the center for the icons and text
        icon_center_y = contact_info_y_position + icon_size // 2
        label_y_position = contact_info_y_position - (icon_size + text_offset_from_icon)
        details_y_position = label_y_position - details_offset
        
        # Draw icon placeholder
        draw_icon_placeholder(c, column_x_center, icon_center_y, icon_size)
        
        # Draw label
        c.setFont("Helvetica-Bold", contact_font_size)
        c.drawCentredString(column_x_center, label_y_position, label)
        
        # Draw details
        c.setFont("Helvetica", contact_font_size)
        c.drawCentredString(column_x_center, details_y_position, details)

    # Draw the columns for Personal Address, Email, and Mobile
    draw_contact_column(column_width / 2, "Personal Address", "1234 Street Address, City, Country")
    draw_contact_column(width / 2, "Email", "example@email.com")
    draw_contact_column(width - (column_width / 2), "Mobile", "+123456789")

    # Save the PDF
    c.save()

create_cv()
