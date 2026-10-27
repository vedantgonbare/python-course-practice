"""
String Methods: Splitting and Joining 
split(): Break String into List 
join(): Combine List into String 
"""

# text = "Vedant Gonbare is a coder"
# print(text.split())


my_list = ["Vedant", "Gonbare", "is", "a", "coder", 5]
ans =" ".join((str(ch)) for ch in my_list)             # Converting all elements to string and joining them with space
print(ans)
print(type(ans))