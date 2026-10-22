# squares = {}
# for i in range(1, 11):
#     squares[i] = i * i           # Normal method using for loop
# print(squares)

# Dictionary comprehension - same result in one line 
squares = {i: i * i for i in range(1, 6)} 
print (squares)  #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}  



# new_list = []
# for i in range(1, 6):
#     new_list.append(i)          # List Comprehension
# print(new_list)
