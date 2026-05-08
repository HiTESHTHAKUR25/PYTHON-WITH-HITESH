#===========1===========
bill = int(input("Enter units consumed: "))
if bill >= 100:
    bill1 = 100*5
    if bill >= 200:
        bill2 = 100*7
        bill3 = bill-200
        bill4 = bill3*10
        print("Total Electricity Bill: ",bill1+bill2+bill4)
    else:
        print("Total Electricity Bill: ",bill1+(bill-100)*7)
else:
    print("Total Electricity Bill: ",bill*5)




# =========2===========

marks = int(input("Enter marks: "))

if marks >= 90:
    proint("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 50:
    print("Grade D")
else:
    print("Fail")



    # =============3==========



income = int(input("Enter annual income: "))

if income >= 1000000:
    tax = income * 0.3
    print("Tax Payable: ",tax)
elif income > 500000:
    tax1 = income*0.2
    print("Tax Payable: ",tax1)
elif income > 250000:
    tax2 = income * 0.05
    print("Tax Payable: ",tax2)
else:
    print("No tax moj lo roj lo ")


    # ==========4=============

    amount = int(input("Enter purchase amount: "))

if amount>5000:
    discount = amount * 0.2
    print("Final Amount: ",amount-discount)
elif amount > 2000:
    discount1 = amount * 0.1
    print("Final Amount: ",amount-discount1)
else:
    discount2 = amount * 0.05
    print("Final Amount: ",amount-discount2)



# ===========5==============

age = int(input("Enter Age: "))

if age >= 60:
    print("Ticket Price: ",200)
elif age >= 12:
    print("Ticket Price: ",150)
else:
    print("Ticket Price: ",100)

    # ===========6========


salary = int(input("Enter salary: "))
ex = int(input("Enter year of experience: "))

if ex >= 10:
    bonus = salary*0.2
    print("Bonus Amount: ",bonus)
elif ex >= 5:
    bonus1 = salary*0.1
    print("Bonus Amount: ",bonus1)
elif ex >= 2:
    bonus2 = salary * 0.05
    print("Bonus Amount: ",bonus2)
else:
    print("No Bonus")


    # ==============7=============



    amount = int(input("Enter Account Balance: "))

if amount >= 5000:
    print("Maximum Withdrawal Limit: 5000")
elif amount >= 1000:
    print("Maximum Withdrawal Limit: 1000")
else:
    print("Withdrawal not allowed")

    # ===========8===========


    temp = int(input("Enter Temprature: "))

if temp > 35:
    print("Hot")
elif temp >= 21:
    print("Warm")
elif temp >= 0:
    print("Cold")
else:
    print("Freezing")



    # ============9=========

attendence = int(input("Enter Attendence Percentage: "))

if attendence >= 75:
    print("Eligible")
elif attendence >= 60:
    print("Eligible with warning")
else:
    print("Not Eligible")


    # =============10===========



data = float(input("Enter daily data usage: "))

if data >= 3:
    print("Recommended Plan: Premium Plan")
elif data >= 1:
    print("Recommended Plan: Standard Plan")
else:
    print("Recommended Plan: Bsic Plan")




# ==========11-======

dis = int(input("Enter Distance: "))
clas = input("Enter Class(AC/SLEEPER): ") 

if dis <= 100:
    if clas == "ac":
        print("Total Fare: 200")
    else:
        print("Total Fare: 100")
elif dis > 500:
    if clas =="ac":
        print("Total Fare: 1000")
    else:
        print("Total Fare: 500")
else:
    if clas == "ac":
        print("Total Fare: 600")
    else:
        print("Total Fare: 300")






    # ===========12==========
bill = int(input("Enter Bill Amount: "))


if bill > 5000:
    gst = bill*0.18
    print("Final BIll Amoount: ",bill+gst)
elif bill> 1000:
    gst1 = bill*0.12
    if bill > 3000:
        print("Final BIll Amoount: ",bill+gst1+200)
else:
    gst2 = bill*0.05
    print("Final BIll Amoount: ",bill+gst)


    # ===========13=======



salary = int(input("Enter Salary: "))
rating = float(input("Enter Rating: "))

if rating >= 5:
    hike = salary * 0.25
    print("Revised Salary: ",salary+hike)
elif rating >= 4:
    hike = salary*0.2
    if salary < 20000:
        print("Revised Salary: ",salary+2000+hike)
    else:
        print("Revised Salary: ",salary+hike)
elif rating >= 3:
    hike = salary *0.1
    print("Revised Salary: ",salary+hike)
elif rating >= 2:
    hike = salary*0.05
    print("Revised Salary: ",salary+hike)
else:
    print("No Hike")




# ===============14=============




cata = input("Enter Course Catahory: ")
user = input("Enter User Type: ")

cata = cata.lower()
user = user.lower()

if user == "student":
    if cata == "programming":
        print("Fianl Course Free: ",5000-5000*0.2)
    elif cata == "design":
        print("Fianl Course Free: ",4000-4000*0.2)
    else:
        print("Fianl Course Free: ",3000-3000*0.2)
elif user == "working professional":
    if cata == "programming":
        print("Fianl Course Free: ",5000-5000*0.1)
    elif cata == "design":
        print("Fianl Course Free: ",4000-4000*0.1)
    else:
        print("Fianl Course Free: ",3000-3000*0.1)
else:
    if cata == "programming":
        print("Fianl Course Free: ",5000)
    elif cata == "design":
        print("Fianl Course Free: ",4000)
    else:
        print("Fianl Course Free: ",3000)



        # ===============15=========




vehicle = input("Enter Vehicle Type: ")
hours = float(input("Enter Hours Parked: "))
vehicle = vehicle.lower()

if vehicle == "bike":
    if hours > 5:
        print("Total Parking Fee: ",10*hours+100)
    else:
        print("Total Parking Fee: ",10*hours)
elif vehicle == "car":
    if hours > 5:
        print("Total Parking Fee: ",20*hours+100)
    else:
        print("Total Parking Fee: ",20*hours)
elif vehicle == "bus":
    if hours > 5:
         print("Total Parking Fee: ",50*hours+100)
    else:
        print("Total Parking Fee: ",50*hours)
else:
    print("Your Vehicle is not register in over list ")
    print("Sorry ")

