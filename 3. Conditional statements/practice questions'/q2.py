"""
Take two number as input and print the greater of the 2, if they are equal print both are equal
"""

num1 = int(input("Enter the number = "))
num2 = int(input("Enter the number = "))

if num1 == num2:
    print("Both the numbers are equal")
elif num1 >= num2:
    print(f"The greater number is {num1}")
else:
    print(f"The greater number is {num2}")