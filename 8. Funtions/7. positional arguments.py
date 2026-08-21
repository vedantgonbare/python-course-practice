# Keywords arguments


def calculate_marks(maths, eng, hindi, comp, history):
    print(f"maths = {maths}")
    print(f"eng = {eng}")
    print(f"hindi = {hindi}")
    print(f"comp = {comp}")
    print(f"history = {history}")
    total_marks = maths + eng + hindi + comp + history
    print(f"Total marks scored = {total_marks}")


calculate_marks(hindi=43, maths=50, history= 68,comp= 100,eng=66)
