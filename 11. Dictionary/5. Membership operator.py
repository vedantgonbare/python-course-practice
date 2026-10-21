student = {
    "Name": "Vedant",
    "age": 23,
    "Gender": "Male",
    "City": "Mumbai",
}

# print("age" in student)
# print("marks" in student)
# print("marks" not in student)

k = input("Enter the key = ")
if k in student:
    print(student[k])
else:
    print("Key does not exist")