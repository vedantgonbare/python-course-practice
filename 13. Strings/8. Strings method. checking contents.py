"""
CHECKING CONTENT (T/F)
isalpha(): All Letters?
isdigit(): All Digits?
isalnum(): AlphaNumeric Only?
isspace(): All Whitespace?
startswith() and endswith()
"""

text = "Vedant Gonbare"
# print(text.isalpha())
# print(text.isdigit())
# print(text.isalnum())
# print(text.isspace())
# print(text.startswith("v"))
# print(text.endswith("e"))

age = input("Enter age = ")

if age.isdigit():
    if int(age) >= 18:
        print("You can vote")
    else:
        print("Cannot vote")
else:
    print("Please enter proper age .")
