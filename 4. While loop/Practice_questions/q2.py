# Sum of all the numbers from 1 to 100.

start = int(input("Enter the start number = "))
end = int(input("Enter the end number = "))
i = start
total = 0
while i <= end:
    total = total + i
    i += 1

print(f"Total = {total}")