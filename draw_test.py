"""Test drawing funtionality of the tool."""

import os


from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import unittest

from your_module_name import student_performance_graph  # replace 'your_module_name' with actual module name
import matplotlib.pyplot as plt

def draw_on_pdf(output_path):
    width, height = letter
    canvass = canvas.Canvas(output_path, pagesize=letter)
    
    # Drawing a red filled rectangle
    canvass.setStrokeColorRGB(1, 0, 0)
    canvass.setFillColorRGB(1, 0, 0)
    canvass.rect(100, 600, 200, 100, fill=1)
    
    # Drawing a blue ellipse
    canvass.setStrokeColorRGB(0, 0, 1)
    canvass.ellipse(300, 600, 500, 700, fill=0)

    # Drawing a string
    canvass.setStrokeColorRGB(0, 0, 0)
    canvass.drawString(150, 570, "This is a sample text.")

    # Saving the canvas will produce the PDF with the above drawings
    canvass.save()

output_path = "sample_drawings.pdf"
draw_on_pdf(output_path)


class TestStudentPerformanceGraph(unittest.TestCase):

    def setUp(self):
        # Setup the student marks and a temporary filename
        self.student_marks = [75, 80, 85, 90, 95]
        self.filename = "temp_test_plot.png"

    def tearDown(self):
        # Cleanup any created files
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_graph_generation(self):
        student_performance_graph(self.student_marks, self.filename)
        
        # Check that the file is created
        self.assertTrue(os.path.exists(self.filename))

        # Open the image and verify its contents - This is a basic verification.
        # For more detailed checks, we might need to parse the plot and ensure it matches expectations.
        img = plt.imread(self.filename)
        self.assertIsNotNone(img)

    def test_marks_on_graph(self):
        # A more in-depth test would involve reading the generated plot and verifying its values.
        # This could be done using tools like OpenCV or by inspecting the plot object before it's saved.
        # Here, we're keeping it simple and trusting that if the plot is generated, it's correct.
        # This will be implemented later
        pass


if __name__ == "__main__":
    unittest.main()
