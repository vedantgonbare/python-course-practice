"""
Q97: Email Validation
Take an email as input. Validate that it contains exactly one @ and at
least one .. Print "Valid" or "Invalid".
"""

# email = input("Enter an email: ")
# if email.count("@gmail.com") == 1 and email.count(".") >=1:
#     print("Valid")
# else:
#     print("Invalid")



def check_email(email: str):
    if email.count("@") == 1 and "gmail.com" in email:
        return "Valid"
    return "Invalid"

email = "vedantgonbare18@gmail.com"
print(check_email(email))