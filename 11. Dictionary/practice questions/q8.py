"""
Q86. Subjects and Marks
Create a dictionary of 6 subjects and their respective marks. Print the subject
with the highest marks and the one with the lowest, using max() and min()
functions alongside a lambda expression.

"""
subjects = {
    "Mathematics": 88,
    "Science": 95,
    "English": 72,
    "History": 80,
    "Geography": 67,
    "Computer": 91,
}

ans1 = max(subjects.items(), key=lambda x: x[1])
ans2 = min(subjects.items(), key=lambda x: x[1])
# print(f"Maximum marks ={ans1}")
# print(f"Minimum marks = {ans2}")
print(f"Highest: {ans1[0]} — {ans1[1]}")
print(f"Lowest: {ans2[0]} — {ans2[1]}")