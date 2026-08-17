"""
Take a number as input. Using the ternary operator, print "Even" or "Odd" in a single line.
"""
a = int(input("Enter 1st number = "))
a = "Even" if a %2 ==0 else "Odd"
print (a)