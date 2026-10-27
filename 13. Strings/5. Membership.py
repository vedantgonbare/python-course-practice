text = "programming"

# In \ Not In

# print("p" in text)
# print("P" in text)
# print("Z" not in text)
# print("m" not in text)
# print("gram" in text)
# print("grame" in text)

# total = 0
# for char in text:
#     if (
#         char == "a"
#         or char == "e"
#         or char == "i"
#         or char == "o"
#         or char == "u"
#         or char == "A"
#         or char == "E"
#         or char == "I"
#         or char == "O"
#         or char == "U"
#     ):
#         total += 1
# print(total)


total = 0
for char in text:
    if char in "AEIOUaeiou":
        total += 1
print(total)
