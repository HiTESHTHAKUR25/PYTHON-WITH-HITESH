# ====================1========

salary = int(input("Salary: "))
cs = int(input("Credit Score: "))
el = int(input("Existing Loans: "))

if salary >= 30000 and cs >= 750:
        print("Conditional Approval ")
else:
        if el < 2:
            if salary >= 30000:
                print("Conditional Approval")
        else:
            print("Rejected")

# ====================2========

cv = int(input("Cart Value: "))
ut = input(("User Type: "))


if cv >= 5000:
    if ut == "premium":
        discount = cv*0.2
        price = cv - discount
        print(f"Your Got 20% (₹{discount}) on your cart value \nSo final price is {price}")
    else:
        discount2 = cv*0.1
        finalpricee = cv - discount2
        print(f"Your Got 10% (₹{discount2}) on your cart value \nSo final price is {finalpricee}")
elif (cv >= 2000 and cv < 5000):
        discount1 = cv*0.1
        finalprice = cv - discount1
        print(f"Your Got 10% (₹{discount1}) on your cart value \nSo final price is {finalprice}")
else:
    print("Final Amount: ",cv)


#========3========



unit = int(input("Enter Units: "))

if unit >= 300:
    print("Hight Usage")
elif unit >= 200:
    print("Moderate Usage")
elif unit >= 100:
    print("Normal Usage")
else:
    print("Low Usage")



#===========4==========

age = int(input("Age: "))
weight = int(input("Weight: "))
goal = (input("Goal: "))

if age >= 18:
    if weight >= 80:
        if goal =="weight loss":
            print("Cardio Plan")
        else:
                print("Strength Plan")
    else:
        print("General Fitness Plan")
else:
    print("Not Allowed")


#========5=========

balance = int(input("Balance: "))
wa = int(input("Withdrawal Amount: "))
pin = (input("PIN: "))

if balance >= wa:
    if wa <= 10000:
        if len(pin) == 4:
            print("Transaction Successful")
        else:
            print("Invalid PIN")
    else:
        print("Limit Exceeded")
else:
    print("Insufficient Balance")


#=============6============

age = int(input("Age: "))
st = input("Show Time (morning/evening): ")
day = input("Day (weekday/weekend): ")

if age < 18:
    if st == "morning":
        print("Ticket Price ₹100")
    else:
        print("Ticket Price ₹150")
else:
    if st == "evening":
        if day == "weekend":
            print("Ticket Price ₹300")
        else:
            print("Ticket Price ₹250")
    else:
        print("Ticket Price ₹200")


#=====7=========

ex = float(input("Experience: "))
rating = float(input("Performance Rating: "))
salary = int(input("Salary: "))

if ex >= 6:
    if rating >= 4:
        if salary <= 50000:
            bonus = salary * 0.2
            print("Bonus: ",bonus)
        else:
            bonus1 = salary * 0.1
            print("Bonus: ",bonus1)
    else:
        bonus2 = salary * 0.05
        print("Bonus: ",bonus2)
else:
    print("No Bonus For You")


#========7==========

