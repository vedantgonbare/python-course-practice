"""
Take a year an input and check if its a leap year .
leap year is when its divisible by 4 ,but not by 100, unless it is also divisible by 400.
"""

year = int(input("Enter year = "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a leap year")
