"""
Q58. Find the largest and smallest number in a list without using built-in functions like max() or min().  

Hint: Use a loop and a variable to track the current largest/smallest as you go through the list. 
Example: if the list is [3, 1, 4, 1, 5],the largest is 5 and smallest is 1.
"""

nums = [6, -5, 4, 2, 10, 91, -75, 49, 9]

maxi = float("-inf")
mini = float("+inf")

for num in nums :
    if  num > maxi:
        maxi = num

for num in nums :
    if  num < mini:
        mini = num

print(f"Maximum number = {maxi}")
print(f"Minimum number = {mini}")