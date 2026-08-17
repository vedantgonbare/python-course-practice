"""
Take a person's age and whether they have a valid ID (True/False) as input. They
can enter a venue only if they are 18 or older AND have a valid ID. Print the
appropriate message.
"""
age = 20
valid_id = True

if age >= 18:
    if valid_id == True:
        print("Entry allowed")
    else:
        print("Entry not allowed")
else:
        print("Entry not allowed")