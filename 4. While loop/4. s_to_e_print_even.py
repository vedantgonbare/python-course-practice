# start to end print even numbers

start = int(input("Enter the start number = "))
end = int(input("Enter the end number = "))
i = start

while i <= end:
    if i %2 == 0:
        print(i, end=" ")
    i += 1