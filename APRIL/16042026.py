# ====================1========

age = int(input("Enter Age: "))
id = (input("Do you have ID (yes/no): "))

if(age>=18):
    print("Eligible to vote")
if(id == "yes"):
    print("Allowed inside booth")




#==================2============

marks = int(input("Enter marks: "))

if(marks>=75):
    print("DISTINCTION")
elif(marks>=40):
    print("PASS")



# ==================3==============

value = int(input("Enter cart value: "))

if(value>=500):
    print("Free delivery applied")
if(value>=1000):
    print("Discount Coupon unlocked")


# ==============4============

age = int(input("Enter age: "))
bmi = int(input("Enter BMI: "))


if(age>=18):
    print("Gym access granted")
if(bmi>25):
    print("Enter in the weight loss program ")



# =============5=============


username = (input("Enter username: "))
passwd = (input("Enter password: "))

if(username == "admin"):
    print("Valid user")
if(len(passwd)>=8):
    print("Strong password")



    # ===================6==============

temp = int(input("Enter tempreature: "))
hum = int(input("Enter huidity: "))


if(temp>=30):
    print("Hot day")
if(hum>=70):
    print("High humidity alert")

    # =========7===========




    salary = int(input("Enter salary: "))

if(salary>=30000):
    print("Eligible for PF")
if(salary>=50000):
    print("Eligible for bonus")




    # =============8========


    
num = int(input("Enter number: "))

if(num%2==0):
    print("EVEN")
if(num%5==0):
    print("Divisible by 5")


    # ==============9 ============


    mem = input("Membership active (yes/no): ")
book = int(input("Books issued: "))

if(mem == "yes"):
    print("Entry allowed")
if(book<3):
    print("Can issue more book")



    # ===================10===========


    marks = int(input("Enter marks: "))
attendence = int(input("Enter attendence: "))

if(marks>=40):
    print("Pass")
if(attendence >= 75):
    print("Eloigible for certificate")