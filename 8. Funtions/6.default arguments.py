def calculate_marks(maths, eng, hindi, comp, history=0):
    print(f"maths = {maths}")
    print(f"end = {eng}")
    print(f"hindi = {hindi}")
    print(f"comp = {comp}")
    print(f"history = {history}")
    total_marks = maths + eng + hindi + comp + history
    print(f"Total marks scored = {total_marks}")


calculate_marks(43, 50, 68, 100)
