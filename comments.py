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

    if student_total_marks > 1100 or student_total_marks < 0:
        comment = (f"Total marks for {student_name} is {student_total_marks}. "
                f"Please check the marks entered.")

    if student_total_marks >= 1000:
        comment = (f"Outstanding job, {student_name}! Your stellar score of "
                   f"{student_total_marks:.0f} out of 1100 is truly remarkable. "
                   f"You particularly excelled in {first_highest_subject}. "
                   f"Keep polishing areas like {first_lowest_subject} and {second_lowest_subject}. "
                   f"to rise to the top. You're soaring higher than an eagle!")

    elif student_total_marks >= 900:
        comment = (f"Exceptional performance, {student_name}! Your score of "
                   f"{student_total_marks:.0f} showcases your dedication. "
                   f"Your prowess in {first_highest_subject} is commendable, but don't forget to "
                   f"hone areas like {first_lowest_subject}. "
                   f"You're as determined as a cheetah on the hunt!")

    elif student_total_marks >= 800:
        comment = (f"Fabulous work, {student_name}! With a score of "
                   f"{student_total_marks:.0f}, you're making waves. "
                   f"You've done notably well in {first_highest_subject}. Continue to refine "
                   f"skills in areas like {first_lowest_subject} and {second_lowest_subject}. "
                   f"You're as dedicated as a beaver building a dam!")

    elif student_total_marks >= 700:
        comment = (f"Great effort, {student_name}! Your score of "
                   f"{student_total_marks:.0f} is commendable. While you shined in"
                   f" {first_highest_subject} and {second_highest_subject}, there's more room for "
                   f"improvement in {first_lowest_subject} and {second_lowest_subject}. "
                   f"You're as agile as a monkey swinging through trees!")

    elif student_total_marks >= 650:
        comment = (f"Good job, {student_name}. A total score of "
                   f"{student_total_marks:.0f} showcases your potential. Your skills in "
                   f"areas like {first_highest_subject} and {second_highest_subject} are "
                   f"evident. Yet, focus on {first_lowest_subject} and {second_lowest_subject} "
                   f"for holistic growth. You're as brave as a lion facing a storm!")

    elif student_total_marks >= 600:
        comment = (f"Stay determined, {student_name}. Your score of "
                   f"{student_total_marks:.0f} is a testament to your hard work. "
                   f"{first_highest_subject} and {second_highest_subject} was a highlight, but "
                   f"don't neglect areas like {first_lowest_subject} and {second_lowest_subject}. "
                   f"You're as persistent as a tortoise on a mission!")

    elif student_total_marks >= 550:
        comment = (f"Continue pushing, {student_name}. Your score of "
                   f"{student_total_marks:.0f} shows promise to your performance. "
                   f"While {first_highest_subject} and {second_highest_subject} was your strength, "
                   f"put some elbow grease into {first_lowest_subject} and "
                   f"{second_lowest_subject}. You're as tenacious as a kangaroo in the outback!")

    elif student_total_marks >= 500:
        comment = (f"Every step is progress, {student_name}. With "
                   f"{student_total_marks:.0f}, you have shown that you have potential. "
                   f"Your efforts in {first_highest_subject} are noteworthy. But, there's"
                   f" room for growth in {first_lowest_subject} and {second_lowest_subject}. "
                   f"You're as adaptable as an octopus exploring the ocean floor!")

    def generate_overall_comments_less_than_500(student_total_marks: int):
        """This function generates a comment based on the student's performance.

        Args:
            student_total_marks (int): The student's total marks.

        Returns:
            str: A comment based on the student's performance.
        """
        comment = ""
        if student_total_marks >= 450:
            comment = (f"Stay engaged, {student_name}. With a score of "
                       f"{student_total_marks:.0f}, you can go extra mile and achieve more. "
                       f"Your strengths lie in {first_highest_subject}, but areas like "
                       f"{first_lowest_subject} and {second_lowest_subject} need your attention. "
                       f"You're as determined as a hummingbird searching for nectar!")

        elif student_total_marks >= 400:
            comment = (f"Keep the momentum, {student_name}. A score of "
                       f"{student_total_marks:.0f} hints at your capabilities. You did well in"
                       f" {first_highest_subject} and {second_highest_subject}, but it's essential"
                       f" to strengthen your skills in {first_lowest_subject} and "
                       f"{second_lowest_subject} to rise."
                       f" You're as spirited as a hawk soaring the skies!")

        elif student_total_marks >= 300:
            comment = (f"Your journey is important, {student_name}. With a score of "
                       f"{student_total_marks:.0f}, the sky's the limit. "
                       f"While {first_highest_subject} showed some bright moments, more effort in "
                       f"{first_lowest_subject} will help you rise to your potential. "
                       f"You're as curious as a cat exploring its surroundings!")

        elif student_total_marks >= 200:
            comment = (f"Every effort counts, {student_name}. Your score of "
                       f"{student_total_marks:.0f} is a stepping stone. "
                       f"Your potential in {first_highest_subject} is clear. However, work on areas"
                       f" like {first_lowest_subject} to enhance your prowess. "
                       f"You're as resilient as a cactus in the desert!")

        elif student_total_marks >= 100:
            comment = (f"Beginnings are full of lessons, {student_name}. A score of "
                    f"{student_total_marks:.0f} means there's much to learn. "
                    f"You have some skills in {first_highest_subject}, but look into nurturing "
                    f"{first_lowest_subject} and {second_lowest_subject}. "
                    f"You're as lively as a fish in the water!")

        else:
            comment = (f"Every new start is an opportunity, {student_name}. With a score of "
                    f"{student_total_marks:.0f}, growth awaits. "
                    f"Your interest in {first_highest_subject} is evident. Yet, delve deeper into "
                    f"{first_lowest_subject} and {second_lowest_subject} to make strides. "
                    f"You're as sturdy as an oak tree in its prime!")

        return comment

    comments_less_500 = generate_overall_comments_less_than_500(student_total_marks)

    if comment:
        return comment

    return comments_less_500
