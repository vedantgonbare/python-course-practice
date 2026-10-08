"""
Question 4: Check for Target Existence 
Write a program that takes a list and a target number. 
Use a loop to determine if the target number exists in the list. Do not use the in operator.
"""

def does_target_exist(lst, target):
    for num in lst:
        if num == target:
            return True
    return False


nums = [6, -5, 4, 2, 10, 91, -75, 49, 9]

print(does_target_exist(nums, -75))
print(does_target_exist(nums, 27))
print(does_target_exist(nums, -5))
print(does_target_exist(nums, 9))
print(does_target_exist(nums, 0))
