"""
Q93. Take a name as input from the user. Print its first character, its last
character, and the total length of the name.

"""

def print_details(name):
    first_char = name[0]
    last_char = name[-1]
    n = len(name)
    print(f"First = {first_char} Last = {last_char} Length = {n}")

print_details(input("Enter name = "))