from .logic11 import students
def maximum(rollno):
    maxi = students[rollno]["marks"]
    return max(maxi)