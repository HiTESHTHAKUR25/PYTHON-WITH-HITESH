empname = []
empage = []
def empployee():
    emp1 = int(input("How Many Employee In your company: "))
    for i in range(emp1):
        name = input("Enter Employee Name: ")
        empname.append(name)

    for i in range(emp1):
        age = int(input("Enter Employee Age: "))
        empage.append(age)