marks = {
    "math": 85,
    "science": 92,
    "english": 60,
    "hindi": 78,
}

ans = dict(sorted(marks.items(), key=lambda x: x[1]))
print(ans)

# my_list = [("Eng", 75), ("Sci", 98), ("Maths", 92), ("Geo", 95)]
# print(my_list)
# print(dict(my_list))