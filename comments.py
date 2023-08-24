"""This module contains functions that provide comments that are added to the report forms."""

def format_student_marks(student_marks: list) -> list:
    """Format the student marks."""
    formatted_student_marks = []

    for marks in student_marks:
        if marks is None or marks == "" or marks == " ":
            formatted_student_marks.append(0)
        elif isinstance(marks, str):
            formatted_student_marks.append(int(marks))
        else:
            formatted_student_marks.append(marks)

    return formatted_student_marks

def generate_subject_comments(marks_list: list) -> list:
    """This function returns a list of comments based on the marks.

    Args:
        marks_list (list): A list of marks.

    Returns:
        list: A list of comments.
    """
    marks_list = format_student_marks(marks_list)

    if marks_list[-1] > 100:
        marks_list[-1] /= 11

    comments = []

    # general comments for all subjects
    for marks in marks_list:
        if marks:
            if marks >= 80:
                comments.append("Excellent, keep it up!")
            elif marks >= 75:
                comments.append("Very Good, aim higher!")
            elif marks >= 60:
                comments.append("Good, there's room for improvement.")
            elif marks>= 50:
                comments.append("Average, strive to do better next time.")
            elif marks >= 0:
                comments.append("Below Average, let's work harder.")
            elif marks < 0:
                comments.append("Marks < 0, please double check.")
        else:
            comments.append("No marks entered, please double check.")

    swahili_comment = _generate_swahili_comments(marks_list[1])
    comments[1] = swahili_comment

    return comments

def _generate_swahili_comments(marks: int) -> str:
    """This function returns a comment based on the swahili marks.

    Args:
        marks (int): The marks.

    Returns:
        str: A comment based on the marks.
    """
    # This is mainly for the total marks
    if marks > 100:
        marks /= 5

    # provide comments for swahili performances
    swahili_marks = ""

    if marks:
        if marks >= 80:
            swahili_marks = "Bora, endelea na bidii hiyohiyo!"
        elif marks >= 75:
            swahili_marks = "Vema kabisa, lenga juu zaidi!"
        elif marks >= 60:
            swahili_marks = "Vizuri, kuna fursa ya kuimarika."
        elif marks >= 50:
            swahili_marks = "Wastani, jitahidi kufanya vizuri zaidi."
        elif marks >= 0:
            swahili_marks = "Chini ya wastani, tufanye kazi kwa bidii."
        elif marks < 0:
            swahili_marks = "Alama zimepungua 0, tafadhali angalia."
    else:
        swahili_marks = "Hakuna alama zilizoingizwa, tafadhali angalia."

    return swahili_marks

def generate_overall_comment(
        student_subject_marks,
        student_total_marks,
        student_name,
        ) -> str:
    """This function generates a comment based on the student's performance.

    Args:
        student_subject_marks (dict): A dictionary containing the student's marks for each subject.
        student_total_marks (int): The student's total marks.
        student_name (str): The student's name.

    Returns:
        str: A comment based on the student's performance.
    """
    sorted_subjects_by_marks = sorted(
        student_subject_marks.items(),
        key=lambda x: x[1],
        reverse=True,)

    first_highest_subject = sorted_subjects_by_marks[0][0]
    second_highest_subject = sorted_subjects_by_marks[1][0]
    first_lowest_subject = sorted_subjects_by_marks[-1][0]
    second_lowest_subject = sorted_subjects_by_marks[-2][0]

    comment = ""

    if student_total_marks > 500:
        comment = (f"Total marks for {student_name} is {student_total_marks}. "
                f"Please check the marks entered.")

    if student_total_marks >= 350:
        comment = (f"Outstanding job, {student_name}! Your average score of "
                f"{student_total_marks:.0f} out of 500 is truly remarkable. "
                f"You particularly excelled in {first_highest_subject}, "
                f"put more focus on areas like "
                f"{first_lowest_subject} to achieve even more. Keep reaching for"
                f" the stars and celebrate your achievements. You're soaring higher than an eagle!"
                )

    elif student_total_marks >= 325:
        comment = (f"Impressive work, {student_name}! With an average score of "
                f"{student_total_marks:.0f} out of 500, you're making great strides. You performed "
                f"notably in {first_highest_subject}. Keep focusing on areas like "
                f"{first_lowest_subject} and {second_lowest_subject} to achieve even more. "
                f"You're as dedicated as a beaver building a dam!"
                )

    elif student_total_marks >= 300:
        comment = (f"Well done, {student_name}! You scored an average of {student_total_marks:.0f}"
                f" out of 500. Your strong point was {first_highest_subject} followed by "
                f"{second_highest_subject}. With some more attention"
                f" to {first_lowest_subject} and {second_lowest_subject}, you can achieve even "
                f"greater heights. You're as agile as a cheetah on the hunt!"
                )

    elif student_total_marks >= 275:
        comment = (f"Good effort, {student_name}! Your average score of {student_total_marks:.0f} "
                f"out of 500 shows potential. While {first_highest_subject} and "
                f"{second_highest_subject} was a highlight, focusing on"
                f" {first_lowest_subject} and {second_lowest_subject} will bring even better "
                f"results. You're as determined as a hummingbird searching for nectar!"
                )

    elif student_total_marks >= 250:
        comment = (f"Fair performance, {student_name}. With an average score of "
                f"{student_total_marks:.0f} out of 500, your skills in {first_highest_subject} "
                f"and {second_highest_subject} stood out. Building on areas like "
                f"{second_lowest_subject} and {second_lowest_subject} will elevate your results. "
                f"You're as persistent as a tortoise on a mission!"
                )

    elif student_total_marks >= 225:
        comment = (f"Continue your journey, {student_name}. Your average score of "
                f"{student_total_marks:.0f} suggests potential for improvement. Your best was "
                f"{first_highest_subject}. Dedicating time to subjects like {first_lowest_subject} "
                f"and {second_lowest_subject} will make a difference. "
                f"You're as tenacious as a kangaroo in the outback!"
                )

    elif student_total_marks >= 200:
        comment = (f"Keep pushing forward, {student_name}. An average score of "
                f"{student_total_marks:.0f} highlights {first_highest_subject} as a strength. "
                f"Seeking support, from your colleagues and teachers, "
                f"in areas like {first_lowest_subject} will lead to progress. "
                f"You're as adaptable as an octopus exploring the ocean floor!"
                )

    elif student_total_marks >= 175:
        comment = (f"There's room for growth, {student_name}. With an average score of "
                f"{student_total_marks:.0f}, focusing on all areas, especially "
                f"{first_lowest_subject}, will be beneficial. Your efforts in "
                f"{first_highest_subject} are commendable. Stay persistent and keep believing "
                f"in yourself! You're as tenacious as a mountain goat on a steep cliff!"
                )

    elif student_total_marks:
        comment = (f"Keep persevering, {student_name}. Your average score of "
                f"{student_total_marks:.0f} shows there's opportunity for growth. While "
                f"{first_highest_subject} showed promise, areas like {first_lowest_subject} "
                f"need more focus. Remember: every step forward counts."
                f" You're as spirited as a lion chasing its prey!"
                )

    elif student_total_marks < 0:
        comment = (f"Total marks for {student_name} is less than 0. "
                f"Please check the marks entered."
                )

    else:
        comment = (f"Total marks for {student_name} is {student_total_marks}. "
                f"Please check the marks entered."
                )

    return comment
