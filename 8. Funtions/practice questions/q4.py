"""
Write a function called rectangle_area that takes length and breadth
as parameters and prints the area.

"""

def rectangle_area(length, breadth):
    area = length * breadth
    print(f"Area of the rectangle is {area}")


a = int(input("Enter the length of the rectangle = "))
b = int(input("Enter the breadth of the rectangle = "))

rectangle_area(a, b)
