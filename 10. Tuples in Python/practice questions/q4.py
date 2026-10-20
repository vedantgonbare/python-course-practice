"""
Q77: Take 5 numbers as input from the user, store them in a tuple, and print the tuple along with its minimum and maximum.
"""

num1 = int(input ("Enter your First number = "))
num2 = int(input ("Enter your Second number = "))
num3 = int(input ("Enter your Third number = "))
num4 = int(input ("Enter your Fourth number = "))
num5 = int(input ("Enter your Fifth number = "))

my_nums = (num1, num2, num3, num4, num5)

print(f"Your Tuple = {my_nums}")
print(f"Maximum number = {max(my_nums)}")
print(f"Minimum number = {min(my_nums)}")