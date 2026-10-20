my_tuple = (1, 2, 3, "Vedant", "Gonbare", "Mumbai", 23)

n= len(my_tuple)

for i in range(0, n):
    print(my_tuple[i], end=" ") 

print()
for ele in my_tuple:
    print(ele, end=" ")


print()
for index, value in enumerate(my_tuple):
    print(f"Index = {index} and value = {value}")