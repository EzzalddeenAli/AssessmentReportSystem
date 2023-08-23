"""Tests for pdf generator, file with the main content in it."""

import unittest

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from report_generator import generate_student_report


class TestGenerateStudentReport(unittest.TestCase):

    def test_generate_student_report_with_perfect_scores(self):
        # Arrange
        canvass = io.BytesIO()
        canvas = canvas.Canvas(canvass)

        # Act
        student_data = [1, "John Doe", "Male", 100, 100, 100, 100, 100, 100]
        generate_student_report(
            canvas,
            0,
            student_data,
            set([100]),
            (
                "Number of Students",
                "English",
                "Math",
                "Science",
                "Swahili",
                "SST/RE",
                "Overall",
                )
            )
        )

        # Assert
        canvas.save()
        actual_output = canvas.getvalue().decode("utf-8")

        expected_output = """
        STUDENT ID. NUMBER: 1
        NAME:  John Doe
        GENDER:  Male
        STUDENT POSITION:  1 / 1
        John Doe's Performance
        Subject | Student's Mark | Class Avg. | Comment
        ------ | ------ | ------ | ------
        English | 100 | 100 |
        Math | 100 | 100 |
        Science | 100 | 100 |
        Swahili | 100 | 100 |
        SST/RE | 100 | 100 |
        Overall | 96 | 100 |
    """

        self.assertEqual(
            actual_output,
            expected_output,
            )

    def test_generate_student_report_with_failing_grades(self):
        # Arrange
        canvass = io.BytesIO()
        canvas = canvas.Canvas(canvass)

        # Act
        student_data = [1, "John Doe", "Male", 0, 0, 0, 0, 0, 0]
        generate_student_report(
            canvas,
            0,
            student_data,
            set([0]),
            (
                "Number of Students",
                "English",
                "Math",
                "Science",
                "Swahili",
                "SST/RE",
                "Overall",
                )
            )
        )

        # Assert
        canvas.save()
        actual_output = canvas.getvalue().decode("utf-8")

        expected_output = """
        STUDENT ID. NUMBER: 1
        NAME:  John Doe
        GENDER:  Male
        STUDENT POSITION:  1 / 1
        John Doe's Performance
        Subject | Student's Mark | Class Avg. | Comment
        ------ | ------ | ------ | ------
        English | 0 | 0 |
        Math | 0 | 0 |
        Science | 0 | 0 |
        Swahili | 0 | 0 |
        SST/RE | 0 | 0 |
        Overall | 0 | 0 |
    """

        self.assertEqual(
            actual_output,
            expected_output,
            )

    def test_generate_student_report_with_mixed_grades(self):
        # Arrange
        canvass = io.BytesIO()
        canvas = canvas.Canvas(canvass)

        # Act
        student_data = [1, "John Doe", "Male", 70, 90, 50, 60, 80, 75]
        generate_student_report(
            canvas,
            0,
            student_data,
            set([70, 50, 60, 80, 75]),
            (
                "Number of Students",
                "English",
                "Math",
                "Science",
                "Swahili",
                "SST/RE",
                "Overall",
                )
            )
        )

        # Assert
        canvas.save()
        actual_output = canvas.getvalue().decode("utf-8")

        expected_output = """
            STUDENT ID. NUMBER: 1
            NAME:  John Doe
            GENDER:  Male
            STUDENT POSITION:  1 / 5
            John Doe's Performance
            Subject | Student's Mark | Class Avg. | Comment
            ------ | ------ | ------ | ------
            English | 70 | 70 |
            Math | 90 | 70 |
            Science | 50 | 60 |
            Swahili | 60 | 80 |
            SST/RE | 80 | 75 |
            Overall | 71 | 70 |
        """

            self.assertEqual(
                actual_output,
                expected_output,
                )

    def test_generate_student_report_with_missing_data(self):
        # Arrange
        canvass = io.BytesIO()
        canvas = canvas.Canvas(canvass)

        # Act
        student_data = [1, None, "Male", 70, 90, 50, 60, 80, 75]
        generate_student_report(
            canvas,
            0,
            student_data,
            set([70, 50, 60, 80, 75]),
            (
                "Number of Students",
                "English",
                "Math",
                "Science",
                "Swahili",
                "SST/RE",
                "Overall",
                )
            )
        )

        # Assert
        canvas.save()
        actual_output = canvas.getvalue().decode("utf-8")

        expected_output = """
            STUDENT ID. NUMBER: 1
            NAME:  
            GENDER:  Male
            STUDENT POSITION:  1 / 5
            John Doe's Performance
            Subject | Student's Mark | Class Avg. | Comment
            ------ | ------ | ------ | ------
            English | 70 | 70 |
            Math | 90 | 70 |
            Science | 50 | 60 |
            Swahili | 60 | 80 |
            SST/RE | 80 | 75 |
            Overall | 71 | 70 |
        """

            self.assertEqual(
                actual_output,
                expected_output,
                )
    
    def test_generate_student_report_with_long_name(self):
        """Test for a student with a very long name.

        This name should be the one that does not fit in the
        given box. This is still an open bug to be handled later.
        """
        # Arrange
        canvass = io.BytesIO()
        canvas = canvas.Canvas(canvass)

        # Act
        student_data = [1, "This Is The Master Of The Art", "Male", 70, 90, 50, 60, 80, 75]
        generate_student_report(
            canvas,
            0,
            student_data,
            set([70, 50, 60, 80, 75]),
            (
                "Number of Students",
                "English",
                "Math",
                "Science",
                "Swahili",
                "SST/RE",
                "Overall",
                )
            )
        )

        # Assert
        canvas.save()
        actual_output = canvas.getvalue().decode("utf-8")

        expected_output = """
        STUDENT ID. NUMBER: 1
        NAME:  This is a very long name
        GENDER:  Male
        STUDENT POSITION:  1 / 5
        This is a very long name's Performance
        Subject | Student's Mark | Class Avg. | Comment
        ------ | ------ | ------ | ------
        English | 70 | 70 |
        Math | 90 | 70 |
        Science | 50 | 60 |
        Swahili | 60 | 80 |
        SST/RE | 80 | 75 |
        Overall | 71 | 70 |
    """

        self.assertEqual(
            actual_output,
            expected_output,
            )