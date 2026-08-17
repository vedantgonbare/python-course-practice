"""
Take a number as input and print if its positive , negative or zero
"""

num = int(input("Enter the number = "))

if num >= 1:
    print(f"The number {num} is a Positive number")
elif num <= -1:
    print(f"The number {num} is a Negative number")
else:
    print("Zero")