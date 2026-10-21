students = {"Name": "Vedant", "age": 23}
print(students, id(students))

# Update
students["age"] = 18  # Updating the value of a key.
print(students, id(students))

# ADD
students["Gender"] = "Male"  # Adding single new key-value pair 
students.update(
    {
        "City": "Mumbai",
        "Phone": 9321761874,
        "State": "Maharashtra",
        "age": 23,  # if the key value pair already exist then it will update the value of key
    }
)  # Adding multiple key-value pairs in a single method
print(students, id(students))
