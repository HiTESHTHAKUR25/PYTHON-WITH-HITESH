students = {}


def add():
    name = input("Enter Student Name: ")
    rollno = int(input("Enter Roll Number: "))
    sub1 = float(input("Enter first Subject marks: "))
    sub2 = float(input("Enter second Subject marks: "))
    sub3 = float(input("Enter third Subject marks: "))
    sub4 = float(input("Enter fourth Subject marks: "))
    sub5 = float(input("Enter fifth Subject marks: "))
    students[rollno] = {"name" : name , "marks" : [sub1,sub2,sub3,sub4,sub5]}
    print(students[rollno]["marks"])
