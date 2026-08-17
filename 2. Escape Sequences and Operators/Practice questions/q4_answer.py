"""
As student has scored  marks in 3 subjects . Take all  three as a input,
calculate the total and average and print using f string
"""

physics = int(input("Enter marks obtained in Physics = "))
chemistry = int(input("Enter marks obtained in chemistry = "))
maths = int(input("Enter marks obtained in maths = "))

total = physics + chemistry + maths
print(f"Total marks obtained in 3 subjects = {total}")

print(f"Average of marks obtained in 3 subjects = {total / 3 :.2f}")
    