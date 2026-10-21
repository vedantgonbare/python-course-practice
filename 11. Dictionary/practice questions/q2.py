"""
Q80: Safe Subject Access (HW)
Define a dictionary with five subjects and their respective marks.
Utilize the get() method to try accessing a subject that is not in the
dictionary, ensuring it prints "Not Available" as a default.

"""
marks = {
    "Science": 98,
    "Maths": 92,
    "English": 75,
    "History": 96,
    "Geography": 74,
}
# subject = "hindi"
# ans = marks.get(subject, "Not Available")
# if ans is None:
#     print("Not Available")
# else:
#     print(ans)

subject = input("Enter subject: ")
print(marks.get(subject, "Not Available"))