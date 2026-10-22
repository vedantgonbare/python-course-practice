# marks = {"math": 85, "science": 92, "english": 60, "hindi": 45}

# # keep only subjets where marks > 80
# top = {sub: m for sub, m in marks.items() if m > 80}
# print(f"Top marks = {top}")

# # transform double all marks
# double = {sub: m * 2 for sub, m in marks.items()}
# print(f"Double marks ={double}")


# Creating a dict from two lists

subjects = ["math", "science", "english"]
scores = [85, 92, 78]

result = dict(zip(subjects, scores))
print(result)
