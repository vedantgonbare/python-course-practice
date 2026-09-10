"""
Question 6: Element-wise Sum of Two Lists
Given two lists of the same length,
write Python code using a loop to create a new list where each element is the sum of the corresponding elements from both original lists.
"""

# Example:
# list1 = [10, 20, 30, 40]
# list2 = [1, 2, 3, 4]
# Expected Output: [11, 22, 33, 44]

# list_a = [5, 15, 25]
# list_b = [2,4,6]
# Expected Output: [7,19, 31]


nums1 = [6, -5, 4, 2, 10, 91, -75, 49, 9]
nums2 = [4, 1, 54, 76, 41, 85, 3, 44, 2]


def sum_of_two_lists(lst1, lst2):
    new_list = []
    n = len(lst1)
    for i in range(0, n):
        total = lst1[i] + lst2[i]
        new_list.append(total)
    return new_list


ans = sum_of_two_lists(nums1, nums2)
print(ans)
