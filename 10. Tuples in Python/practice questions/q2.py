"""
Q75: Create a tuple of 8 numbers. Using slicing, print the first 3, last 3, and every alternate element.
"""

nums = (1, 2, 3, 4, 5, 6, 7, 8)

n = len(nums)

print(f"First 3 elements = {nums[:3]}")
print(f"Last 3 elements = {nums[-3:]}")
print(f"Alternate element = {nums[::2]}")