# 1.
# Student Registration System – Longest Name

# A school is organizing an inter-school cultural event. During the registration process, the coordinator notices that some students have very long names, which may not fit properly on the printed ID cards.

# As a software developer, your task is to write a Python program that identifies the student with the longest name from the list of registered students using the reduce() function along with a lambda expression.

# Input
# students = ["Riya", "Christopher", "Aman", "Neha", "Siddharth"]
# Expected Output
# Student with the longest name: Christopher

from functools import reduce


students = ["Riya", "Christopher", "Aman", "Neha", "Siddharth"]

n1 = ""
result = reduce(lambda x,y:x if len(x)>len(y) else y,students)
print(result)




# 2.
# Hospital Management System – Oldest Patient

# A hospital wants to give priority to the oldest patient during a free health check-up camp. The patient details are stored as tuples containing the patient's name and age.

# As a Python developer, write a program to identify the oldest patient using the reduce() function with a lambda expression.

# Input
# patients = [
#     ("Rahul", 45),
#     ("Sneha", 62),
#     ("Amit", 38),
#     ("Kiran", 71),
#     ("Pooja", 55)
# ]
# Expected Output
# Oldest Patient: Kiran


from functools import reduce
patients = [
    ("Rahul", 45),
    ("Sneha", 62),
    ("Amit", 38),
    ("Kiran", 71),
    ("Pooja", 55)
]

result = reduce(lambda x,y:x if x[1]>y[1] else y , patients)
print(result[0])



# 3.
# Cricket Tournament – Highest Run Scorer

# A cricket academy wants to reward the player who scored the highest number of runs in a tournament.

# Write a Python program to identify the highest run scorer using reduce() and a lambda expression.

# Input
# players = [
#     ("Virat", 78),
#     ("Rohit", 102),
#     ("Gill", 89),
#     ("KL Rahul", 65),
#     ("Iyer", 91)
# ]
# Expected Output
# Highest Run Scorer: Rohit

from functools import reduce

players = [
    ("Virat", 78),
    ("Rohit", 102),
    ("Gill", 89),
    ("KL Rahul", 65),
    ("Iyer", 91)
]

result = reduce(lambda x,y:x if x[1]>y[1] else y,players)
print(result[0])




