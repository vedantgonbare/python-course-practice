# print start to end using while loop

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))
i = start

while i <= end:
    print(i, end=" ")
    i += 1

print(f"After while loop, start value is {start}")