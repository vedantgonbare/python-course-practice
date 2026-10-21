"""
Q79: Student Profile (HW)
Create a dictionary for a student, including keys like name, age,
city, and marks (as a list of scores). Print each piece of
information using its key.

"""

student = {
    "Name": "Vedant",
    "Age": 23,
    "City": "Mumbai",
    "Marks": [98, 88, 82, 93, 75],
}

for i in student.keys():
    print(f" {i} = {student[i]}")

