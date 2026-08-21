"""
Write a lambda function that takes a number and returns "Positive", or
"Negative".
"""


number = lambda n : "Positive" if n>=0 else "Negative"

print(number(12))
print(number(-12))