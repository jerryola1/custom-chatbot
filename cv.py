from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.enums import TA_CENTER


#from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, white

# Function to draw an icon from an image file
def draw_icon(c, image_path, x, y, width, height):
    """Draws an image icon at the specified coordinates with the given size."""
    c.drawImage(image_path, x, y, width, height, preserveAspectRatio=True)

def draw_icon_placeholder(c, x, y, size=12):
    """Draws a circular icon placeholder at the specified coordinates."""
    c.circle(x, y, size // 2, stroke=1, fill=0)

def create_cv():
    """Creates the CV template."""
    c = canvas.Canvas("cv_template.pdf", pagesize=A4)
    width, height = A4

    # Define the size for the icons
    icon_width = 16
    icon_height = 16

    # Set font to measure text width
    font_size = 24
    c.setFont("Helvetica-Bold", font_size)
    name = "NAME AND SURNAME"
    job_title = "JOB TITLE"
    name_width = c.stringWidth(name, "Helvetica-Bold", font_size)
    job_title_width = c.stringWidth(job_title, "Helvetica-Bold", font_size)

    # Use the wider of the two text widths
    max_text_width = max(name_width, job_title_width)

    # Calculate rectangle width (text width + padding)
    rect_padding = 20  # Adjust padding as needed
    rect_width = max_text_width + rect_padding * 2

    c.setFillColor(black)

    # Draw the rectangle for the background
    header_height = 80  # The height of the header background
    header_y_position = height - header_height - 60  # Adjust the vertical position of the header
    # Calculate x-coordinate for rectangle so it's centered
    rect_x_position = (width - rect_width) / 2
    c.rect(rect_x_position, header_y_position, rect_width, header_height, stroke=0, fill=1)

    # Set the fill color back to white for the text
    c.setFillColor(white)  # RGB color for white

    # Header with name and job title
    c.setFont("Helvetica-Bold", 24)
    # The text is moved down by half the header height to center it
    padding_top = 20  # Adjust this value for top padding
    c.drawCentredString(width / 2, header_y_position + header_height - padding_top - 12, "NAME AND SURNAME")
    c.setFont("Helvetica", 12)
    c.drawCentredString(width / 2, header_y_position + header_height - padding_top - 36, "JOB TITLE")

    # Reset the fill color to black for the rest of the text
    c.setFillColor(black)  # Black

    # Contact Information Section
    contact_info_y_position = height - 180  # Starting Y position of the contact info
    contact_font = "Helvetica"
    contact_font_size = 10
    icon_size = 12  # Size of the icon
    text_offset_from_icon = 5  # Distance of text from the icon
    details_offset = 15  # Space between the label and details
    column_width = width / 3  # Divide the width of the page into 3 columns

    # # Define a function to draw a contact information column
    # def draw_contact_column(column_x_center, label, details):
    #     # Calculate the center for the icons and text
    #     icon_center_y = contact_info_y_position + icon_size // 2
    #     label_y_position = contact_info_y_position - (icon_size + text_offset_from_icon)
    #     details_y_position = label_y_position - details_offset
        
    #     # Draw icon placeholder
    #     draw_icon_placeholder(c, column_x_center, icon_center_y, icon_size)
        
    #     # Draw label
    #     c.setFont("Helvetica-Bold", contact_font_size)
    #     c.drawCentredString(column_x_center, label_y_position, label)
        
    #     # Draw details
    #     c.setFont("Helvetica", contact_font_size)
    #     c.drawCentredString(column_x_center, details_y_position, details)

    # # Draw the columns for Personal Address, Email, and Mobile
    # draw_contact_column(column_width / 2, "Personal Address", "1234 Street Address, City, Country")
    # draw_contact_column(width / 2, "Email", "example@email.com")
    # draw_contact_column(width - (column_width / 2), "Mobile", "+123456789")

    # Define a function to draw a contact information column with real icons
    def draw_contact_column_with_icon(column_x_center, icon_path, label, details):
        # Calculate the positions for the icon, label, and details
        icon_y = contact_info_y_position + icon_height // 2
        label_y_position = contact_info_y_position - (icon_height + text_offset_from_icon)
        details_y_position = label_y_position - details_offset
        
        # Draw the icon
        draw_icon(c, icon_path, column_x_center - icon_width // 2, icon_y, icon_width, icon_height)

        # Draw label
        c.setFont("Helvetica-Bold", contact_font_size)
        c.drawCentredString(column_x_center, label_y_position, label)
        
        # Draw details
        c.setFont("Helvetica", contact_font_size)
        c.drawCentredString(column_x_center, details_y_position, details)


    # Draw the columns with actual icons
    draw_contact_column_with_icon(column_width / 2, "location_icon.png", "Personal Address", "1234 Street Address, City, Country")
    draw_contact_column_with_icon(width / 2, "email_icon.png", "Email", "example@email.com")
    draw_contact_column_with_icon(width - (column_width / 2), "phone_icon.png", "Mobile", "+123456789")

    # Draw the horizontal line below the contact information
    # contact_line_y = contact_info_y_position - 40
    # c.line(50, contact_line_y, width - 50, contact_line_y)

    # Profile Section Heading with Black Background
    profile_heading_start_y = contact_info_y_position - 100  # Adjust the vertical position as needed
    profile_heading_font_size = 14
    profile_heading_height = 20  # Height of the black background for the heading
    profile_text_font_size = 10

    # Draw the black rectangle for the profile section heading background
    c.setFillColor(black)
    c.rect(0, profile_heading_start_y, width, profile_heading_height, stroke=0, fill=1)

    # Set font color to white for the heading and draw the heading
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", profile_heading_font_size)
    heading_text = "PROFILE"
    c.drawCentredString(width / 2, profile_heading_start_y + (profile_heading_height - profile_heading_font_size) / 2, heading_text)

    # Draw the full-width black HR below the profile heading
    c.setLineWidth(1)
    c.setStrokeColor(black)
    c.line(0, profile_heading_start_y - 1, width, profile_heading_start_y - 1)  # Adjust the y coordinate as necessary

    # Set font color back to black for the profile description
    c.setFillColor(black)

    # Set font for the profile description text
    profile_text = "A brief overview of your professional background, skills, and achievements." # Replace with actual profile text
    text_object = c.beginText(50, profile_heading_start_y - 40)  # Position the text below the heading
    text_object.setFont("Helvetica", profile_text_font_size)
    text_object.setLeading(14)  # Set the space between lines of text

    # Add the profile text
    text_object.textLines(profile_text)
    c.drawText(text_object)




    # Save the PDF
    c.save()

create_cv()
