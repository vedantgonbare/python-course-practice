"""
Q91. Filter Passing Marks
Given an existing dictionary of subjects and their respective marks, 
use dictionary comprehension to generate a new dictionary that includes
only the subjects where the student scored 70 or more (i.e., passed).
"""
subjects = {
    "Mathematics": 88,
    "Science": 95,
    "English": 35,
    "History": 80,
    "Geography": 67,
    "Computer": 91,
}

for key,value in subjects.items():
    if value >= 70:
        print(f"Subject = {key} , Marks = {value}")


