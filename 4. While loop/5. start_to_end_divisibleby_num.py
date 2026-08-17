# print start to end numbers, which are divisible by 3 and 4

start = int(input("Enter the start number = "))
end = int(input("Enter the end number = "))

i = start
while i <= end:
    if i % 3 == 0 and i % 4 == 0:
        print(i, end=" ")
    i += 1