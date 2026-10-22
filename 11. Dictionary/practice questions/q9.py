"""
Q87. Student Details
Create a nested dictionary containing details for 4 students, where each
student entry includes their name, age, and city. Write a loop to print the full
details of each student in a clear, readable format.

"""

students = {
    "student1": {"name": "Aarav", "age": 20, "city": "Mumbai"},
    "student2": {"name": "Priya", "age": 21, "city": "Pune"},
    "student3": {"name": "Rahul", "age": 19, "city": "Nashik"},
    "student4": {"name": "Sneha", "age": 22, "city": "Thane"},
}

result =[]
for stu, detail in students.items():
    result = detail["name"], detail["age"], detail["city"]
    print(result)