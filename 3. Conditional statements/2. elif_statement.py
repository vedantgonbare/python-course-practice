marks =float(input("Enter your marks = "))

if marks >= 91 and marks <= 100:
    print("Grade A")
elif marks >= 81 and marks <= 90:
    print("Grade B")
elif marks >= 71 and marks <= 80:
    print("Grade C")
elif marks >= 61 and marks <= 70:
    print("Grade D")
elif marks>=0 and marks <=60:
    print("Fail")
else:
    print("Invalid Marks")