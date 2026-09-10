"""
Question 5: Calculate the Average  
Given a list of numbers, use a loop to calculate and print their average. 
You can use len() to get the count of elements, but avoid using sum() for the total.  
Format the average to two decimal places.
"""

# Example: 
# scores = [85, 90, 78, 92, 88] 
# Expected Output: The average score is: 86.60

nums = [6, -5, 4, 2, 10, 91, -75, 49, 9]

def calculate_average(nums):
    n= len(nums)
    total = 0
    for num in nums:
        total += num
    return total/n

ans = calculate_average(nums)

print(f"Average = {ans:.3f}")