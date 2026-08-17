# start to end , print start to end

start = int(input("Enter a number = "))
end = int(input("Enter a number = "))

total = 0

for i in range(start, end + 1):
    total += i

print(total)
