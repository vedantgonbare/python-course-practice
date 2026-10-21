student = {
    "Name": "Vedant",
    "age": 23,
    "Gender": "Male",
    "City": "Mumbai",
}
print(student,id(student))

# DELETE

# student.pop("Name")    # 1st way
# student.clear()        # 2nd way [its clears the whole dictionary (empty dictionary)]
del student["age"]       # 3rd way del can be used anywhere to delete anyting .
print(student,id(student))