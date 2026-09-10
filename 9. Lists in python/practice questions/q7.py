"""
Question 57: Check if a List is Sorted
Write a program that takes a list of numbers and, using a loop, determines whether it is sorted in ascending order.
Print True if it is sorted, and False otherwise.  Do not use built-in sort or sorted() functions for checking.
"""

# Example 1:
# numbers = [1, 5, 10, 15, 20]
# Expected Output: True

# Example 2:
# numbers = [1, 10, 5, 15, 20]
# Expected Output: False

# Example 3:
# numbers = []
# Expected Output: True (An empty list is considered sorted)





def is_sorted(lst):
    n = len(lst)
    for i in range(0, n - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

nums = [3, 6, 8, 9, 13, 17, 18, 23, 45, 58, 79, 100]
print(is_sorted(nums))