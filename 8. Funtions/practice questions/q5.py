"""
Write a function called find_max that takes three numbers as
parameters and prints the largest one.

"""


def find_max(a, b, c):
    if (a > b) and (a > c):
        print(f"The greatest number is {a}")
    elif (b > a) and (b > c):
        print(f"The greatest number is {b}")
    else:
        print(f"The greatest number is {c}")


x = int(input("Enter the 1st number = "))
y = int(input("Enter the 2nd number = "))
z = int(input("Enter the 3rd number = "))

find_max(x, y, z)
