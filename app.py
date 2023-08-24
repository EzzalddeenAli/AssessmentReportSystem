"""This module contains the Flask app that serves the API endpoints."""

import os
import base64
from flask import Flask, request, send_from_directory, render_template
from spreadsheet_reader import read_spreadsheet
from pdf_generator import generate_pdf


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
OUTPUT_FOLDER = 'pdfs/'

# Ensure directories exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def convert_pdf_to_base64(pdf_file_path):
    """This function converts a PDF file to a base64 string.

    Args:
        pdf_file_path (str): The path to the PDF file.

    Returns:
        str: A base64 string representation of the PDF file.
    """
    with open(pdf_file_path, "rb") as pdf_file:
        encoded_string = base64.b64encode(pdf_file.read()).decode('utf-8')
    return encoded_string

@app.route('/upload', methods=['POST'])
def upload_file():
    """This function uploads a spreadsheet and generates PDFs for each student.

    The spreadsheet is assumed to have the headers in the first row and the
    data in the subsequent rows. Users would need to ensure that the spreadsheet
    is in this format.

    Args:
        None

    Returns:
        str: A string indicating whether the PDFs were generated successfully.
    """
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']
    if file.filename == '':
        return 'No file selected', 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Expecting student_records structure as:
    # Student ID, Student Name, Gender, English, Kiswahili,
    # Mathematics, Science, SST/RE, Total, Position
    (
        school_name,
        class_name,
        term_name,
        class_records,
        number_of_students,
    ) = read_spreadsheet(file_path)

    # We generate a single PDF now with all student records
    output_path = os.path.join(
        OUTPUT_FOLDER,
        "all_students_report.pdf",
        )

    title_records = [
            school_name,
            class_name,
            term_name,
        ]

    class_averages_with_total = list(class_records[-2][3:15])

    mean = sum(list(class_records[-2][3:14])) / 11

    class_averages_with_mean = list(list(class_records[-2][3:14]) + [mean])

    class_averages = [
        class_averages_with_total,
        class_averages_with_mean,
        ]

    generate_pdf(
        title_records,
        class_records,
        class_averages,
        output_path,
        number_of_students,
        )

    # Check if the PDF has any size to it
    if os.path.getsize(output_path) == 0:
        return 'PDF is empty. Something went wrong.', 500

    # Convert the PDF to Base64
    pdf_base64_data = convert_pdf_to_base64(output_path)
    return render_template(
        'show_pdf.html',
        pdf_base64_data=pdf_base64_data,
        number_of_students=number_of_students,
        )

@app.route('/pdfs/<filename>', methods=['GET'])
def serve_pdf(filename):
    """This function serves a PDF file.

    Args:
        filename (str): The name of the PDF file to serve.

    Returns:
        str: A string indicating whether the PDF was served successfully.
    """
    file_path = os.path.join(OUTPUT_FOLDER, filename)
    if not os.path.exists(file_path):
        return "File not found", 404
    return send_from_directory(OUTPUT_FOLDER, filename, as_attachment=True)

@app.route('/')
def index():
    """This function serves the index page.

    Args:
        None

    Returns:
        str: A string indicating whether the index page was served successfully.
    """
    return render_template('upload_form.html')

@app.route('/view_pdf', methods=['GET'])
def view_pdf():
    """This function serves the index page.

    Args:
        None

    Returns:
        str: A string indicating whether the index page was served successfully.
    """
    return render_template('embedded_pdf.html')


if __name__ == '__main__':
    app.run(debug=True)
