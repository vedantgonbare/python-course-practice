# 3 int as a parameters and just print the total

# def addition(a, b, c):
#     ans = a + b + c
#     print(f"Total = {ans}")

# addition(10,12,20)


def greet(name, age, gender):
    print(f"Hey my name is {name}, I am {age} years old and i am a {gender}.")


n = input("Enter your name = ")
a = int(input("Enter your age = "))
b = input("Enter your gender = ")

greet(n, a, b)
