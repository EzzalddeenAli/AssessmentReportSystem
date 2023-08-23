"""Tests for app.py"""

import os

import unittest
from io import BytesIO
from flask_testing import TestCase
from your_flask_app_module_name import app


class FlaskAppTestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False  # If you're using Flask-WTF
        return app

    def setUp(self):
        # You can also create a test database here if needed
        pass

    def tearDown(self):
        # Clean up any created files or database changes if required
        pass

    def test_index_page(self):
        response = self.client.get('/')
        self.assert200(response)
        self.assertIn(b'Upload Spreadsheet', response.data)

    def test_upload_invalid_file(self):
        response = self.client.post('/upload', data=dict(
            file=(BytesIO(b'This is not a valid spreadsheet.'), 'test.txt'),
        ))
        self.assert400(response)
        self.assertIn(b'No file uploaded', response.data)

    def test_upload_valid_file(self):
        with open("path_to_a_valid_spreadsheet.xlsx", "rb") as f:
            data = dict(
                file=(BytesIO(f.read()), 'valid_spreadsheet.xlsx'),
            )
        response = self.client.post('/upload', data=data, content_type='multipart/form-data')
        self.assert200(response)
        self.assertIn(b'PDF for Students Report', response.data)  # Assuming such text is in your show_pdf.html

    def test_view_pdf(self):
        response = self.client.get('/view_pdf')
        self.assert200(response)

    def test_serve_non_existent_pdf(self):
        response = self.client.get('/pdfs/non_existent.pdf')
        self.assert404(response)


if __name__ == '__main__':
    unittest.main()
