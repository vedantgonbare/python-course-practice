"""
Q78: Write a function get_stats(nums) that takes a tuple of numbers and returns a tuple containing the sum, average, minimum, and maximum. Unpack
the returned tuple and print each value.
"""

def get_stats(nums):
        maximum = max(nums)
        minimum = min(nums)
        total = sum(nums)
        average = sum(nums) / len(nums)
        return (total, average, maximum, minimum)


total, average, maximum, minimum = get_stats((1, 2, 3, 4, 5, 6))

print(f"Maximum = {maximum}")
print(f"Minimum = {minimum}")
print(f"total = {total}")
print(f"average = {average}")