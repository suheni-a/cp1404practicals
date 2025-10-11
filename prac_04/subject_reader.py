"""
CP1404 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and display neatly formatted subject details."""
    subjects = load_subjects(FILENAME)  #renamed for clarity
    display_subject_details(subjects)   #new function to print data


def load_subjects(filename):
    """Read data from file formatted like: subject,lecturer,number of students.
    Return a list of lists, e.g. [['CP1401', 'Ada Lovelace', 192], ...]
    """
    subjects = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()  # Remove newline at the end
            parts = line.split(',')  # Split each line into 3 parts
            parts[2] = int(parts[2])  # Convert number of students to int
            subjects.append(parts)  # Add to the main list
    return subjects


def display_subject_details(subjects):
    """Display each subject’s details in a formatted way."""
    for subject in subjects:
        code, lecturer, student_count = subject
        print(f"{code} is taught by {lecturer} and has {student_count} students")


main()
