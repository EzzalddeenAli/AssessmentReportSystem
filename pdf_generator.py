"""This module contains the function for generating a PDF file for all the students."""

import io

import re

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

from reportlab.platypus import Table, TableStyle

from comments import generate_subject_comments
from comments import generate_overall_comment

import matplotlib
import matplotlib.pyplot as plt


matplotlib.use('Agg')  # Set the backend to Agg


def start_new_page(
        canvass: canvas.Canvas,
        width: int,
        height: int,
        title_details: list,
        ) -> int:
    """This function starts a new page in the PDF file.

    Args:
        c (canvas.Canvas): The canvas object for the PDF file.
        width (int): The width of the PDF file.
        height (int): The height of the PDF file.
        title_details (list): The details to be displayed on top of the report form.

    Returns:
        int: The y position of the next line, so that student details can be placed.
    """
    canvass.showPage()
    canvass.setFont("Helvetica-Bold", 22)

    # Set the starting position (from the top of the page)
    y_position = height - 30

    (
        school_name,
        class_name,
        term_name
        ) = title_details

    # Draw and center the school name
    school_text_width = canvass.stringWidth(
        school_name,
        "Helvetica-Bold",
        22,
        )

    canvass.drawString(
        (width - school_text_width) / 2,
        y_position,
        school_name,
        )

    # Update the position for the class name
    # Adjust this value for desired spacing
    y_position -= 25
    class_text_width = canvass.stringWidth(
        class_name,
        "Helvetica-Bold",
        22,
        )

    canvass.drawString(
        (width - class_text_width) / 2,
        y_position,
        class_name,
        )

    # Update the position for the term name
    # Adjust this value for desired spacing
    y_position -= 25
    term_text_width = canvass.stringWidth(
        term_name,
        "Helvetica-Bold",
        22,
        )

    canvass.drawString(
        (width - term_text_width) / 2,
        y_position,
        term_name,
        )

    # Adjust this value for desired spacing
    y_position -= 15

    # Setting the color to gray
    canvass.setStrokeColorRGB(0.45, 0.45, 0.45)  # mid-gray

    # Drawing the thicker line.
    canvass.setLineWidth(3)
    canvass.line(
        50,
        y_position + 10,
        width - 50,
        y_position + 10,
        )

    # Adjust the y_position and reset line width for the second line
    y_position -= 3
    canvass.setLineWidth(1)

    canvass.line(
        50,
        y_position + 10,
        width - 50,
        y_position + 10,
        )

    return y_position

def draw_7x4_table(canvass, _x, _y):
    """Draw a 7x4 table onto a canvas.

    Args:
        canvass (canvas.Canvas): The canvas to draw on.
        _x (int): The x-coordinate where the table starts.
        _y (int): The y-coordinate where the table starts.

    Returns:
        None
    """
    data = [
        [
            'Header 1',
            'Header 2',
            'Header 3',
            'Header 4',
            ],
        ['-', '-', '-', '-'],
        ['-', '-', '-', '-'],
        ['-', '-', '-', '-'],
        ['-', '-', '-', '-'],
        ['-', '-', '-', '-'],
        ['-', '-', '-', '-'],
    ]

    table = Table(data)
    table.setStyle(
        TableStyle(
            [
        (
            'BACKGROUND',
            (0, 0),
            (-1, 0),
            colors.gray,
            ),
        (
            'TEXTCOLOR',
            (0, 0),
            (-1, 0),
            colors.whitesmoke,
            ),
        (
            'ALIGN',
            (0, 0),
            (-1, -1),
            'CENTER',
            ),
        (
            'FONTNAME',
            (0, 0),
            (-1, 0),
            'Helvetica-Bold',
            ),
        (
            'BOTTOMPADDING',
            (0, 0),
            (-1, 0),
            12,
            ),
        (
            'BACKGROUND',
            (0, 1),
            (-1, -1),
            colors.beige,
            ),
        (
            'GRID',
            (0, 0),
            (-1, -1),
            1,
            colors.black
            ),
    ]
    )
    )

    _, _h = table.wrapOn(canvass, 0, 0)
    table.drawOn(canvas, _x, _y - _h)

def format_class_average(class_average: str) -> str:
    """This function formats the class averages.

    Args:
        class_average (str): A class averages.

    Returns:
        str: A formatted class average.
    """
    # Convert the value to a string for processing
    class_average_str = str(class_average).strip()

    # If the class_average is None or an empty string, return '0.00'
    if not class_average_str:
        return '0.00'

    # Check if class_average string contains a float or integer value
    if re.match(r"^\d+\.\d+$", class_average_str) or re.match(r"^\d+$", class_average_str):
        return f"{float(class_average_str):.2f}"

    # It contains non-float or non-int at this point
    return '0.00'

def generate_student_report(
        canvass: canvas.Canvas,
        y_offset: int,
        student: list,
        class_averages: set,
        number_number_column_heads: tuple,
        ) -> int:
    """This function generates a report for a single student.

    Args:
        canvass (canvas.Canvas): The canvas object for the PDF file.
        y_offset (int): The y offset for the student details.
        student (list): A tuple containing the student details.
        class_averages (list): A tuple containing the class performance.
        number_number_column_heads (tuple): A tuple containing the number
            of students and column heads.

    Returns:
        int: The y offset for the next line.
    """
    canvass.setFont("Helvetica", 12)

    # Displaying the student details
    canvass.drawString(
        300,
        y_offset + 90,
        f"NAME:  {student[1]}".upper(),
        )

    student_id = student[0]
    if isinstance(
        student_id,
        float
        ):
        student_id = int(student_id)

    canvass.drawString(
        100,
        y_offset + 45,
        f"STUDENT ID.:  {student_id}",
        )

    # Draw rectangle around student id number
    canvass.rect(308, y_offset + 75, 121, -22)

    # Draw rectangle around student gender
    canvass.rect(434, y_offset + 75, 122, -22)

    # Draw a rectangle around student's position
    canvass.rect(55, y_offset + 75, 248, -22)

    # Draw rectangle around student name
    canvass.rect(55, y_offset + 48, 248, -22)

    # Draw rectangle around student name
    canvass.rect(308, y_offset + 48, 248, -22)

    # Add student's gender
    canvass.drawString(
        100,
        y_offset + 15,
        f"GENDER:  {student[2]}".upper(),
        )

    student = list(student)
    if isinstance(student[9], float):
        student[9] = int(student[9])

    canvass.drawString(
        300,
        y_offset + 15,
        f"STUDENT POSITION:  "
        f"{student[9]}  /  {number_number_column_heads[0]}",
        )

    # canvass.setFont("Helvetica", 13)
    # canvass.drawString(
    #     243,
    #     y_offset - 15,
    #     f"{student[1].split(' ')[0].title()}'s Performance",
    #     )
    # canvass.setFont("Helvetica", 12)

    # Creating a table for subjects and marks
    subjects = number_number_column_heads[1][3:15]

    comments = generate_subject_comments(
        list(student[3:15])
        )

    data = [[
        "Subject",
        "Student's Mark",
        "Class Avg.",
        "Comment",
        ]]

    for i, subject in enumerate(subjects):
        data.append([
            subject,
            format_mark(student[i + 3]),
            format_class_average(class_averages[i]),
            comments[i],
            ]
            )

    # Adjusting size:
    # Define the column widths
    col_widths = [80, 80, 80, 210]
    # Define the row heights
    row_heights = [
        25,
        20,
        20,
        20,
        20,
        20,
        20,
        20,
        20,
        20,
        20,
        20,
        20
        ]

    bold_last_row_index = len(data) - 1

    table = Table(
        data,
        colWidths=col_widths,
        rowHeights=row_heights,
        )

    table.setStyle(TableStyle([
        (
        'BACKGROUND',
        (0, 0),
        (-1, 0),
        colors.gray,
        ),
        (
        'TEXTCOLOR',
        (0, 0),
        (-1, 0),
        colors.whitesmoke,
        ),
        (
        'ALIGN',
        (0, 0),
        (-1, -1),
        'CENTER',
        ),
        (
        'FONTNAME',
        (0, 0),
        (-1, 0),
        'Helvetica-Bold',
        ),

        # Set font to bold for the last row
        (
            'FONTNAME',
            (0, bold_last_row_index),
            (-1, bold_last_row_index),
            'Helvetica-Bold',
            ),

        (
        'BOTTOMPADDING',
        (0, 0),
        (-1, 0),
        12,
        ),
        # ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        (
        'GRID',
        (0, 0),
        (-1, -1),
        1,
        colors.black,
        ),     # Inside lines
        (
        'BOX',
        (0, 0),
        (-1, -1),
        1,
        colors.black,
        ),     # Outer frame
    ]))

    # Drawing the table on the canvas
    table.wrapOn(canvass, 100, 200)
    # Adjust the offsets accordingly
    table.drawOn(canvass, 80, y_offset - 244)

    return y_offset - 200  # Adjust this value as needed

def format_mark(mark) -> int:
    """This function formats the results to be displayed on the report form.

    This takes decimals and converts them to integers.
    If there's a NoneType object, it replaces it with an empty string.
    If there's a float, it converts it to an integer.
    If there's a string containing a float or integer, it converts them accordingly.
    Else, returns 0.
    """

    # Check if mark is None or empty string
    if mark is None or mark == "" or mark == " ":
        return 0

    # Convert float to integer
    if isinstance(mark, float):
        return int(mark)

    # Return mark if it's an integer
    if isinstance(mark, int):
        return mark

    # Check if string contains float or integer and convert to integer
    #if isinstance(mark, str)

    # Float regex pattern
    if re.match(r"^\d+\.\d+$", mark):
        return int(float(mark))

    # Integer regex pattern
    if re.match(r"^\d+$", mark):
        return int(mark)

    return 0

def add_class_performance_page(canvass, width, height, class_performance):
    """This function adds a page to the PDF file with the class performance.

    Args:
        canvass (canvas.Canvas): The canvas object for the PDF file.
        width (int): The width of the PDF file.
        height (int): The height of the PDF file.
        class_performance (tuple): A tuple containing the class performance.

    Returns:
        None
    """
    start_new_page(
        canvass,
        width,
        height,
        []
        )

    canvass.setFont("Helvetica", 18)

    y_offset = 150
    details = [
        f"English Average: {class_performance[3]}",
        f"Kiswahili Average: {class_performance[4]}",
        f"Mathematics Average: {class_performance[5]}",
        f"Science Average: {class_performance[6]}",
        f"SST/RE Average: {class_performance[7]}",
        f"Class Mean Score: {class_performance[8]}"
    ]

    for detail in details:
        canvass.drawString(
            100,
            height - y_offset,
            detail
            )
        y_offset += 30

def create_student_plot_buffer(
        student_marks,
        class_averages,
        column_heads,
        ):
    """This function creates a buffer containing a plot of student marks.

    Args:
        marks (list): A list of the student's marks.
        class_averages (list): A list of the class averages.
        column_heads (list): A list of the column heads.

    Returns:
        io.BytesIO: A buffer containing the plot.
    """
    student_name = student_marks[1].split(' ')[0].title()
    student_marks = list(student_marks[3:15])
    # class_averages = list(class_averages)

    student_marks[-1] = int(student_marks[-1]) / 11

    fig, axis = plt.subplots(figsize=(2.5, 1.1))

    # Add or remove subjects as per your data
    subjects = column_heads[3:14] + ['TOT']

    for index, mark in enumerate(student_marks):
        student_marks[index] = format_mark(mark)

    # change all the subjects to three characters long
    # these should be capitalized as well
    for index, subject in enumerate(subjects):
        subjects[index] = subject[:3].upper()

    axis.bar(
        subjects,
        student_marks,
        label=f"{student_name}'s Marks",
        width=0.4,
        color="gray",
        )

    axis.plot(
        subjects,
        class_averages,
        label="Class Averages",
        color="red",
        marker='o',
        markersize=1.3,
        linewidth=0.5,
        )

    axis.set_ylabel(
        'Performance',
        fontsize=4,
        )

    axis.tick_params(
        axis='y',
        which='major',
        labelsize=3,
        )

    axis.set_xticks(subjects)

    axis.set_xticklabels(
        subjects,
        fontsize=4,
        # rotation=45,
        )  # Set font size for subjects here
    # Adjust the pad to reduce the distance. You can modify the value as per your needs.
    axis.tick_params(axis='x', which='major', pad=1)

    title = f"{student_name}'s Marks vs Class Averages"
    axis.set_title(
        title,
        fontsize=4.5,
        y=0.95,
        color='#000000',
        )
    axis.legend(fontsize=3)

    # Adjusting the thickness of the frame/spines
    for spine in axis.spines.values():
        # Adjust the value as required
        spine.set_linewidth(0.3)

    plt.tight_layout(
        pad=0.2,
        w_pad=0.3,
        h_pad=0.5,
        )

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=600)
    plt.close(fig)

    buf.seek(0)

    return buf

def get_subject_marks(
        subjects: str,
        student_records: list,
        ) -> dict:
    """This function returns a dictionary of subject marks.

    Args:
        student_records (list): A list of student records.

    Returns:
        dict: A dictionary of subject to marks.
    """
    student_subject_marks = {}

    for index, subject in enumerate(subjects):
        student_subject_marks[
            subject
            ] = format_mark(
            student_records[index + 3]
            )

    return student_subject_marks

def add_overall_comments(
        canvass: canvas.Canvas,
        y_position: int,
        subjects: list,
        student_records: list,
        head_teacher: str,
        ) -> None:
    """Add an overall comment to the canvas.

    Args:
        canvass (canvas.Canvas): The canvas object for the PDF file.
        y_position (int): The y position to start writing comments.
        subjects (list): A list of subjects.
        student_records (list): The student's marks.
        head_teacher (str): Headteacher's information to be displayed on the report form.

    Returns:
        None
    """
    student_name = ' '.join(student_records[1].split(' ')[:2]).title()
    student_total_marks = student_records[8]

    comment = generate_overall_comment(
        get_subject_marks(subjects, student_records),
        format_mark(student_total_marks),
        student_name,
        )

    canvass.setFont("Helvetica", 12)

    # canvass.drawString(
    #     100,
    #     y_position,
    #     "Overall Comment:",
    #     )

    # draw rectangle
    canvass.rect(80, 189, 450, -63)

    # start position of the text
    text_object = canvass.beginText(
        90,
        y_position,
        )
    text_object.setFont(
        "Helvetica",
        12,
        )
    text_object.setTextOrigin(
        90,
        y_position,
        )

    # Split the comment by words and add them line by line
    overall_comment = "Overall Comment:"
    words = [overall_comment] + comment.split(' ')

    line = []
    for word in words:
        # You might need to adjust this length check for your specific needs
        if canvass.stringWidth(
            ' '.join(line + [word]),
            "Helvetica",
            12,
            ) < 430:
            line.append(word)
        else:
            text_object.textLine(' '.join(line))
            line = [word]
    if line:
        text_object.textLine(' '.join(line))

    canvass.drawText(text_object)

    # draw rectangle
    canvass.rect(80, 121, 450, -63)

        # start position of the text
    text_object = canvass.beginText(
        90,
        y_position + 5,
        )
    text_object.setFont(
        "Helvetica",
        12,
        )
    text_object.setTextOrigin(
        90,
        y_position - 68,
        )

    # Split the comment by words and add them line by line
    overall_comment = "Headteacher's Remarks:"
    words = [overall_comment] + head_teacher.split(' ')

    line = []
    for word in words:
        # You might need to adjust this length check for your specific needs
        if canvass.stringWidth(
            ' '.join(line + [word]),
            "Helvetica",
            12,
            ) < 430:
            line.append(word)
        else:
            text_object.textLine(' '.join(line))
            line = [word]
    if line:
        text_object.textLine(' '.join(line))

    canvass.drawText(text_object)

    # draw two vertical lines
    canvass.line(
        50,
        53,
        50,
        704,
        )
    canvass.line(
        562,
        53,
        562,
        704,
        )

    # draw the thinner horizontal line
    canvass.line(
        50,
        53,
        562,
        53,
        )

    # Drawing the thicker line.
    canvass.setLineWidth(3)
    canvass.line(
        50,
        50,
        562,
        50,
        )

    # get the line width back to normal
    canvass.setLineWidth(1)

def generate_pdf(
        title_records: list,
        class_records: list,
        class_averages: list,
        output_path: str,
        number_of_students: int,
        ) -> None:
    """This function generates a PDF file for all the students.

    Args:
        title_records (list): A list of tuples containing the title details.
        class_records (list): A list of tuples containing the class marks.
        class_averages (list): A list of tuples containing the class average marks.
        output_path (str): The path to the output PDF file.
        number_of_students (int): The number of students in the class.

    Returns:
        None
    """
    (
        school_name,
        class_name,
        term_name
        ) = title_records

    column_heads = list(class_records[0])

    canvass = canvas.Canvas(
        output_path,
        pagesize=letter,
        )

    width, height = letter

    for student in class_records[1:-2]:
        # Start a new page for the student
        y_position = start_new_page(
            canvass,
            width,
            height,
            [
                school_name,
                class_name,
                term_name,
                ],
            )

        # Change any None values to 0
        def format_student_marks(student):
            """This function formats student's details, replaces None with zero."""
            for index, item in enumerate(student):
                if item is None:
                    student[index] = 0

        student = list(student)

        format_student_marks(student)

        # Step 1: Generate student details first
        # y_offset = y_position - 70  # Adjust this as needed
        y_position = generate_student_report(
            canvass,
            y_position - 70,
            student[:15],
            class_averages[0],
            (
                number_of_students,
                column_heads,
            ),
            ) - 210

        # Step 3: Add overall comment to the student
        add_overall_comments(
            canvass,
            y_position - 38,
            column_heads[3:14],
            student[:15],
            # The headteacher's comment
            class_records[-1][0],
            )

        # img = ImageReader(
        #     create_student_plot_buffer(
        #     student,
        #     class_records[-2][3:9],
        #     )
        # )

        # y_position -= 210  # Adjust this as needed
        # For example, 10% from the left edge
        # Adjust width and height as needed
        canvass.drawImage(
            ImageReader(
            create_student_plot_buffer(
            student[:15],
            class_averages[1],
            column_heads,
            )
        ),
            (width * 0.1) + 10,
            y_position - 24,
            width=width * 0.7,
            height=height * 0.235,
            )

    canvass.save()
