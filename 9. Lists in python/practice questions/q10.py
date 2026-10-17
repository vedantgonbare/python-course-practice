"""
Q60. Given two lists, merge them into a single new list without modifying the originals.
"""
# def merge_list(lst1, lst2):
#     return lst1 + lst2

# num1 = [1, 2, 3, 4]
# num2 = [5, 6, 7, 8]

# print(merge_list(num1, num2))

def merge_list(lst1, lst2):
    new_list = []
    for num in lst1:
        new_list.append(num)
    for num in lst2:
        new_list.append(num)
    return new_list

num1 = [1, 2, 3, 4]
num2 = [5, 6, 7, 8]

print(merge_list(num1, num2))