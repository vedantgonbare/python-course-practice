marks = {
    "Science": 96,
    "Maths": 98,
    "English": 75,
    "History": 95,
    "Geography": 92,
}

# print(marks["Science"])      # Standard printing
# print(marks.get("Sciencee", 0))  # GET Method returns the value

subject = "History"

ans = marks.get(subject)
if ans is None:
    print("Subject not found")
else:
    print(f"Marks scored = {ans}")