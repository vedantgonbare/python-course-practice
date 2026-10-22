"""
Q92. Combine Lists into Dictionary
You have two separate lists: one containing subject names and another containing corresponding marks.
 Create a dictionary from these two
lists using dictionary comprehension, mapping each subject to its mark.

"""

subjects = ["Mathematics", "Science", "History", "Computer"]
marks = [88, 95, 80, 91]

new_dict = dict(zip(subjects, marks))
print(new_dict)