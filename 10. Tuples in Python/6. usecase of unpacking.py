# make a functions which returns min and max of a list


def min_max(lst):
    # Logic
    mini = min(lst)
    maxi = max(lst)
    return maxi, mini          # Returning a tuple


ans1, ans2 = min_max([5, 6, 56, 46, 23, 1, 88, 2, 47, 8])
print(f"Maximum = {ans1}")
print(f"Minimum = {ans2}")