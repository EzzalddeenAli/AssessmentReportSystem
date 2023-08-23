"""Tests for comments.py"""

import unittest
from comments import generate_subject_comments, _generate_swahili_comments, generate_overall_comment

class TestGenerateSubjectComments(unittest.TestCase):
    """Tests for the generate_subject_comments function."""

    def test_basic_marks_ranges(self):
        """Test basic marks ranges."""
        # Testing various mark ranges
        marks_list = [85, 77, 65, 52, 45]
        expected_comments = [
            "Excellent, keep it up!",
            "Vema kabisa, lenga juu zaidi!",
            "Good, there's room for improvement.",
            "Average, strive to do better next time.",
            "Below Average, let's work harder."
        ]
        self.assertEqual(
            generate_subject_comments(marks_list),
            expected_comments
            )

    def test_swahili_subject(self):
        """Test the Swahili subject."""
        # Only testing the Swahili subject
        marks_list = [0, 85, 0, 0, 0]
        expected_comments = [
            "No marks entered, please double check.",
            "Bora, endelea na bidii hiyohiyo!",
            "No marks entered, please double check.",
            "No marks entered, please double check.",
            "No marks entered, please double check."
        ]
        self.assertEqual(
            generate_subject_comments(marks_list),
            expected_comments
            )

    def test_edge_cases(self):
        """Test edge cases."""
        # Empty list
        self.assertEqual(generate_subject_comments([]), [])

        # Marks is None
        self.assertEqual(
            generate_subject_comments([None]),
            ["No marks entered, please double check."]
        )

        # Marks is 0
        self.assertEqual(
            generate_subject_comments([0]),
            ["No marks entered, please double check."]
        )

    def test_swahili_comments_function(self):
        """Test the _generate_swahili_comments function."""
        # Test Swahili comments separately
        self.assertEqual(
            _generate_swahili_comments(85),
            "Bora, endelea na bidii hiyohiyo!"
            )
        self.assertEqual(
            _generate_swahili_comments(77),
            "Vema kabisa, lenga juu zaidi!"
            )
        self.assertEqual(
            _generate_swahili_comments(65),
            "Vizuri, kuna fursa ya kuimarika."
            )
        self.assertEqual(
            _generate_swahili_comments(52),
            "Wastani, jitahidi kufanya vizuri zaidi."
            )
        self.assertEqual(
            _generate_swahili_comments(45),
            "Chini ya wastani, tufanye kazi kwa bidii."
            )
        self.assertEqual(
            _generate_swahili_comments(None),
            "Hakuna alama zilizoingizwa, tafadhali angalia."
            )
        self.assertEqual(
            _generate_swahili_comments(0),
            "Hakuna alama zilizoingizwa, tafadhali angalia."
            )

    def test_value_errors(self):
        """Test value errors."""
        # Negative marks
        with self.assertRaises(ValueError):
            generate_subject_comments([-5])

        # Marks greater than 100
        with self.assertRaises(ValueError):
            generate_subject_comments([105])


class TestGenerateSwahiliComments(unittest.TestCase):
    """Tests for the generate_subject_comments function."""

    def test_basic_marks_ranges(self):
        """Test basic marks ranges."""
        # Testing various mark ranges
        marks_list = [85, 77, 65, 52, 45]
        expected_comments = [
            "Excellent, keep it up!",
            "Vema kabisa, lenga juu zaidi!",
            "Good, there's room for improvement.",
            "Average, strive to do better next time.",
            "Below Average, let's work harder."
        ]
        self.assertEqual(
            generate_subject_comments(marks_list),
            expected_comments
            )

    def test_swahili_subject(self):
        """Test the Swahili subject."""
        # Only testing the Swahili subject
        marks_list = [0, 85, 0, 0, 0]
        expected_comments = [
            "No marks entered, please double check.",
            "Bora, endelea na bidii hiyohiyo!",
            "No marks entered, please double check.",
            "No marks entered, please double check.",
            "No marks entered, please double check."
        ]
        self.assertEqual(
            generate_subject_comments(marks_list),
            expected_comments
            )

    def test_edge_cases(self):
        """Test edge cases."""
        # Empty list
        self.assertEqual(
            generate_subject_comments([]),
            []
            )

        # Marks is None
        self.assertEqual(
            generate_subject_comments([None]),
            ["No marks entered, please double check."]
        )

        # Marks is 0
        self.assertEqual(
            generate_subject_comments([0]),
            ["No marks entered, please double check."]
        )

    def test_value_errors(self):
        """Test value errors."""
        # Negative marks
        with self.assertRaises(ValueError):
            generate_subject_comments([-5])

        # Marks greater than 100
        with self.assertRaises(ValueError):
            generate_subject_comments([105])


class TestGenerateOverallComment(unittest.TestCase):
    """Tests for the generate_overall_comment function."""

    def test_high_score(self):
        """Test a high score."""
        marks = {
            'English': 90,
            'Math': 89,
            'Swahili': 85,
            'Science': 93,
            'History': 93,
            }
        total_marks = 450
        name = "Alice"
        expected_comment = ("Outstanding job, Alice! Your average score of 450 out of 500  "
                            "is truly remarkable. You particularly excelled in Science. "
                            "Keep reaching for the stars and celebrate your "
                            "achievements. You're soaring higher than an eagle!")
        self.assertEqual(
            generate_overall_comment(
            marks,
            total_marks,
            name
            ),
            expected_comment
            )

    def test_medium_high_score(self):
        """Test a medium high score."""
        marks = {
            'English': 70,
            'Math': 85,
            'Swahili': 65,
            'Science': 55,
            'History': 65,
            }
        total_marks = 340
        name = "Bob"
        expected_comment = ("Impressive work, Bob! With an average score of 340 out of 500,"
                            " you're making great strides. You performed notably in Math. "
                            "Keep focusing on areas like Science to achieve "
                            "even more. You're as dedicated as a beaver building a dam!")
        self.assertEqual(
            generate_overall_comment(marks, total_marks, name),
            expected_comment
            )

    def test_no_marks(self):
        """Test no marks."""
        marks = {
            'English': 0,
            'Math': 0,
            'Swahili': 0,
            'Science': 0,
            'History': 0,
            }
        total_marks = 0
        name = "Charlie"
        expected_comment = (
            "Total marks for Charlie is 0. "
            "Please double check the marks entered."
            )
        self.assertEqual(
            generate_overall_comment(
            marks,
            total_marks,
            name
            ),
            expected_comment
            )

    def test_good_score(self):
        """Test a good score."""
        marks = {
            'English': 60,
            'Math': 62,
            'Swahili': 60,
            'Science': 58,
            'History': 60,
            }
        total_marks = 300
        name = "David"
        expected_comment = ("Well done, David! You scored an average of 300 out of 500. "
                            "Your strong point was English. With some more attention to "
                            "Science, you can achieve even greater heights. "
                            "You're as agile as a cheetah on the hunt!")
        self.assertEqual(
            generate_overall_comment(marks, total_marks, name),
            expected_comment
            )

    def test_fair_score(self):
        """Test a fair score."""
        marks = {
            'English': 50,
            'Math': 50,
            'Swahili': 50,
            'Science': 50,
            'History': 50,
            }
        total_marks = 250
        name = "Eva"
        expected_comment = ("Fair performance, Eva. With an average score of 250"
                            " out of 500, your skills in English stood out. "
                            "Building on areas like Swahili will elevate your results. "
                            "You're as persistent as a tortoise on a mission!")
        self.assertEqual(
            generate_overall_comment(marks, total_marks, name),
            expected_comment
            )

    def test_below_average_score(self):
        """Test a below average score."""
        marks = {
            'English': 40,
            'Math': 42,
            'Swahili': 43,
            'Science': 45,
            'History': 50,
            }
        total_marks = 220
        name = "Frank"
        expected_comment = ("Continue your journey, Frank. Your average score of 220"
                            " suggests potential for improvement. Your best was History."
                            " Dedicating time to subjects like English will "
                            "make a difference. You're as tenacious as a kangaroo in the outback!")
        self.assertEqual(
            generate_overall_comment(
            marks,
            total_marks,
            name
            ),
            expected_comment
            )

    def test_low_score(self):
        """Test a low score."""
        marks = {
            'English': 30,
            'Math': 32,
            'Swahili': 35,
            'Science': 35,
            'History': 40,
            }
        total_marks = 172
        name = "Grace"
        expected_comment = ("There's room for growth, Grace. With an average score"
                            " of 172, focusing on all areas, especially English, will"
                            " be beneficial. Your efforts in History are commendable."
                            " Stay persistent and keep believing in yourself! "
                            "You're as tenacious as a mountain goat on a steep cliff!"
                            )
        self.assertEqual(
            generate_overall_comment(
            marks,
            total_marks,
            name
            ),
            expected_comment
            )


if __name__ == "__main__":
    unittest.main()
