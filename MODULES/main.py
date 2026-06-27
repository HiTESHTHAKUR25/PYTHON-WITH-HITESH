import assignment1
import assignment2


print("Which Module You Want to run I have only 2 Modules")
choose = int(input("Chhose a option(1/2): "))
match choose:
    case 1:
        print(assignment1.logic1.empployee())
        x = assignment1.logic1.empage
        x1 = assignment1.logic1.empname
        print(assignment1.logic2.age(x))
        print(assignment1.logic3.senior(x))
        print(assignment1.logic4.dupages(x))
        print(assignment1.logic5.vowels(x1))
        print(assignment1.logic6.longest(x1))
    case 2:
        print(assignment2.logic11.add())
        roll = int(input("Enter Roll Number: "))
        print(assignment2.logic22.totalmarks(roll))
        print(assignment2.logic33.percentage(roll))
        print(assignment2.logic44.grade(roll))
        print(assignment2.logic55.maximum(roll))
        print(assignment2.logic66.minimum(roll))
    case _:
        print("Please Choose Right Option")

