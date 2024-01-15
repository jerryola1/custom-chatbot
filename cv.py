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
from reportlab.platypus import KeepInFrame
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, KeepInFrame

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

    # Profile Section Heading with Black Background
    profile_heading_start_y = contact_info_y_position - 80  # Adjust the vertical position as needed
    profile_heading_font_size = 14
    profile_heading_height = 20  # Height of the black background for the heading
    profile_text_font_size = 10

    # Draw the black rectangle for the profile section heading background
    c.setFillColor(black)
    #c.rect(0, profile_heading_start_y, width, profile_heading_height, stroke=0, fill=1)

    # Set font color to white for the heading and draw the heading
    #c.setFillColor(white)
    c.setFont("Helvetica-Bold", profile_heading_font_size)
    # heading_text = "PROFILE"
    # c.drawCentredString(width / 2, profile_heading_start_y + (profile_heading_height - profile_heading_font_size) / 2, heading_text)

    # Calculate the width of the "PROFILE" text
    profile_heading_text = "PROFILE"
    profile_heading_width = c.stringWidth(profile_heading_text, "Helvetica-Bold", profile_heading_font_size)

    # Calculate the position to center the heading on the page
    profile_heading_x = (width - profile_heading_width) / 2 - 5 

    # Draw the black background rectangle for the "PROFILE" heading
    c.rect(profile_heading_x, profile_heading_start_y, profile_heading_width + 10, profile_heading_height, stroke=0, fill=1)

    # Draw the "PROFILE" text in white
    c.setFillColor(white)
    c.drawCentredString(width / 2, profile_heading_start_y + (profile_heading_height - profile_heading_font_size) / 2, profile_heading_text)


    # Draw the full-width black HR below the profile heading
    c.setLineWidth(1)
    c.setStrokeColor(black)
    c.line(0, profile_heading_start_y - 1, width, profile_heading_start_y - 1)  # Adjust the y coordinate as necessary

    # Set font color back to black for the profile description
    c.setFillColor(black)

    # Set font for the profile description text
    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    styleN.fontName = 'Helvetica'
    styleN.fontSize = profile_text_font_size
    styleN.leading = 14
    styleN.textColor = black

    # Replace with actual profile text
    profile_text = "A very long overview of your professional background, skills, and achievements. " * 10  # Example long text

    # Create a Paragraph object
    profile_para = Paragraph(profile_text, style=styleN)

    # The width of the KeepInFrame should be the width of the page minus margins
    frame_width = width - 100  # Adjust the margins as needed
    frame_height = 100  # Starting height, KeepInFrame will adjust this as needed

    # Create a KeepInFrame object - it will automatically adjust the height to fit the content
    kif = KeepInFrame(frame_width, frame_height, [profile_para], hAlign='LEFT', vAlign='TOP')

    # Draw the profile text
    frame_x = 50  # Margin on the left
    frame_y = profile_heading_start_y - 100  # Position the frame below the heading with some space
    frame = Frame(frame_x, frame_y, frame_width, frame_height, showBoundary=0)  # showBoundary=1 for debugging
    frame.addFromList([kif], c)

    # Starting Y position for the Professional Experience section
    experience_start_y = frame_y - frame_height - 40  # Adjust this based on where the previous section ends

    # # Professional Experience Heading
    # c.setFont("Helvetica-Bold", 14)
    # c.drawString(50, experience_start_y, "Professional Experience")

    # # Sample experiences
    # experiences = [
    #     "Experience 1: Details about experience 1...",
    #     "Experience 2: Details about experience 2...",
    #     # ... more experiences ...
    # ]

    # # Set font for the experience details
    # c.setFont("Helvetica", 10)
    # text_y = experience_start_y - 20  # Starting position for the first experience

    # Function to add experiences
    def add_experience(text, y_position):
        global text_y  # To modify the external text_y variable
        wrap_width = 450  # Width in which the text should be wrapped
        leading = 14  # Line spacing

        words = text.split()
        line = ''
        text_object = c.beginText(50, y_position)
        text_object.setFont("Helvetica", 10)
        text_object.setLeading(leading)

        for word in words:
            # Check if adding the word exceeds the wrap width
            if c.stringWidth(line + ' ' + word, "Helvetica", 10) <= wrap_width:
                line += ' ' + word if line else word
            else:
                # Draw the line and start a new one
                text_object.textLine(line)
                line = word

        # Add the last line
        text_object.textLine(line)
        c.drawText(text_object)

        # Calculate new Y position
        text_height = len(text_object._lines) * leading
        text_y = y_position - text_height - 10  # Update y-coordinate for the next experience

        # Check for page overflow
        if text_y < 50:  # If near the bottom of the page
            c.showPage()  # Start a new page
            text_y = 800  # Reset y-coordinate for the new page



    # Save the PDF
    c.save()

create_cv()
