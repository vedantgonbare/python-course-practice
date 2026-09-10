"""
Question 4: Check for Target Existence 
Write a program that takes a list and a target number. 
Use a loop to determine if the target number exists in the list. Do not use the in operator.
"""

# Example: 
# my_list = [10,20,30,40,50] 
# target = 30 
# Expected Output: 30 exists in the list.  

# target = 60 
# Expected Output: 60 does not exist in the list.

nums = [6, -5, 4, 2, 10, 91, -75, 49, 9]

def does_target_exists(lst, target):
    for num in lst:
        if num == target:
            return True
    return False


print(does_target_exists(nums, 18))
print(does_target_exists(nums, 10))
print(does_target_exists(nums, 75))