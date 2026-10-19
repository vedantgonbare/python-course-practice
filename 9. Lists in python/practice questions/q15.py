"""
Question 65  Write a Python script that iterates through a list of integers and replaces every negative number found in the list with the value 0.

# Example input list: numbers = [5,-3, 8, -1, 0, -10, 12]
# Expected output: [5, 0, 8, 0, 0, 0, 12]

"""

def replace_negative(lst):
    n = len(lst)
    for i in range(0,n):
        if lst[i] < 0:
            lst[i] = 0
    return lst

nums =[1,4,-1,-5,-6,4,9,2,-8]

print(replace_negative(nums))