"""
Q96. Given a string input, print every alternate character starting from the
very first character, using string slicing. (HW)

"""


def alt_char(text):
    return text[0:-1:2]

print(alt_char("vedantgonbare1234"))
