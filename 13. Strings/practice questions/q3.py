"""
Q95. Read a sentence from the user. Count and print the total number of
vowels (a, e, i, o, u, case-insensitive) present in it, using a for loop. (HW)

"""

text = input("Enter a word = ")
total = 0
for char in text:
    if char in "aeiouAEIOU":
        total += 1
print(total)
