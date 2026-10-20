"""
Q76: Create a tuple of marks of 6 students. Print the highest, lowest, total, and average.
"""

marks = (53, 90, 75, 88, 67, 85)

n = len(marks)

print(f"Highest marks = {max(marks)}")
print(f"Lowest marks = {min(marks)}")
print(f"Average marks = {sum(marks)/ len(marks):.2f}")
