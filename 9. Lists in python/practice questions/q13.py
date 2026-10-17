"""
Question 63  Create a list containing the squares of numbers from 1 to 10 (i.e., [1, 4, 9, ... , 100]).  
# Expected output: # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

def square_nums(lst):
    result = []
    for i in lst:
        if i in lst:
            result.append(i*i)
    return result

nums  = [1,2,3,4,5,6,7,8,9,10]

print(square_nums(nums))