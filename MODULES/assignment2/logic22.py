from .logic11 import students
def totalmarks(rollno):
    sum = 0
    lis1 = students[rollno]["marks"]
    for i in lis1:
        sum+=i
    return sum
