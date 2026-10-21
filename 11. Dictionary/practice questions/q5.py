"""
Q83: Subject Performance Analysis
Given a dictionary of marks for different subjects, loop over its values()
to calculate and print the total marks and the average mark obtained.

"""

marks = {
    "Science": 98,
    "Maths": 92,
    "English": 75,
    "History": 96,
    "Geography": 74,
}

total_subjets = len(marks)
total_marks = 0

for mark in marks.values():
    total_marks += mark

print(f"Total marks = {total_marks}")
print(f"Average = {total_marks / total_subjets}")
