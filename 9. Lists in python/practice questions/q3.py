"""
Question 3: Find the Largest Flement
Given a list of numbers, write Python code using a loop to find and print the largest element. Do not use the built-in max() function.
"""

# Example:
# numbers = [3,1, 4, 1, 5, 9, 2, 6]
# Expected Output: The larget element is: 9

nums = [6, -5, 4, 2, 10, 91, -75, 49, 9]

maxi = float("-inf")

for num in nums :
    if  num > maxi:
        maxi = num

print(f"Maximum number = {maxi}")
