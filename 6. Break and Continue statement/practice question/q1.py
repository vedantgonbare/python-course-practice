"""
Taka a number as a  input from user one by one .Skip negative numbers and keep adding the posituve ones.
Stop when the user enters 0 and print the total. (Use both continue and break.)
"""


total = 0
while True:
    num = int(input("Enter a number = "))
    if num == 0:
        break
    if num < 0:
        continue
    total += num
print(total)