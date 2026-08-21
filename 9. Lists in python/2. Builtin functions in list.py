marks = [45, 34, 54, 65, 23, 65, 76, 91]

# To get the length
n = len(marks)
print(f"Length of the list = {n}")

# MAX MIN TOTAL
maxi = max(marks)
print(f"Maximum makrs = {maxi}")
mini = min(marks)
print(f"Minimum makrs = {mini}")
total = sum(marks)
print(f"The total marks = {total}")

# To sort using sorted() function, it will always return you a new list
new_list1 = sorted(marks, reverse=True)
new_list2 = sorted(marks)

print(f"The sorted list 1 = {new_list1}")
print(f"The sorted list 2 = {new_list2}")

