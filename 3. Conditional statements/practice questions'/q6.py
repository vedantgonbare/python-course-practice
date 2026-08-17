"""
Take three numbers as input. Print the largest of the three without using any
built-in function.
"""

num1 = int(input("Enter 1st Number = "))
num2 = int(input("Enter 2nd Number = "))
num3 = int(input("Enter 3rd Number = "))

if (num1 > num2) and (num1 >num3):
    print(f"The largest number is {num1}")
elif (num2 > num1) and (num2 >num3):
    print(f"The largest number is {num2}")
else:
    print(f"The largest number is {num3}")