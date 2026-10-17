"""
Question 64  Given a list of numbers (which may contain duplicates), write a Python script that takes an integer as input from the user and removes all occurrences of that integer from the list.  
# Example input list: my_list = [10, 20, 10, 30, 20, 10, 40] #
#  If user enters 10, expected output: [20, 30, 20, 40]
"""

# def remove_occurence(lst, target):
#     new_list = []
#     for num in lst:
#         if num != target:
#             new_list.append(num)
#     return new_list

# nums = [1,1,1,1,1,1,1,1,1,1,1,2,3,1,5,6,4,1,7,8,1]
# print(remove_occurence(nums, 1))

def remove_occurrence(lst,target):
    while target in lst:
        lst.remove(target)

nums = [1,1,1,1,1,1,1,1,1,1,1,2,3,1,5,6,4,1,7,8,1]

remove_occurrence(nums, 1)
print(f"nums = {nums}")
