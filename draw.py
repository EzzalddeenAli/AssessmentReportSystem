"""This module contains functions for graphing student performance."""

import matplotlib.pyplot as plt

def student_performance_graph(student_marks, filename):
    """This function saves a graph of student performance to a file."""
    subjects = ["English", "Kiswahili", "Mathematics", "Science", "SST/RE"]

    plt.figure(figsize=(6, 4))
    plt.plot(subjects, student_marks, marker='o', color='purple', linestyle='-')
    plt.title("Student Performance")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(filename)
    plt.close()
