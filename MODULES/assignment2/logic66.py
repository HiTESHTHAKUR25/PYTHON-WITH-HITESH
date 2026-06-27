from .logic11 import students
def minimum(rollno):
    mini = students[rollno]["marks"]
    return min(mini)