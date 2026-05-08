print('''# ========================================
# Assignment 1: Time Converter
# ========================================''')
second = int(input("Enter totall duration in seconds: "))

var = second//3600
print(var, " :  Hours")

var2 = second - 3600*var
var3 = var2//60
print(var3, " :  Minuts")

var4 = var2 - 60 * var
print(var4,":  Second")


print('''========================================
Assignment 2: Lifetime Calculator
========================================''')


age = int(input("Enter your age: "))

days = age*365
print("Days: ",days)

hours = days * 24
print("Hours: ",hours)

minutes = hours * 60
print("Minutes: ",minutes)

print('''========================================
Assignment 3: Split the Bill
========================================''')

totalbill = float(input("Enter Total Bill: "))
friends = int(input("Enter number of friends: "))

totalvalue = totalbill / friends

print(totalvalue)


print('''========================================
Assignment 4: Travel Fare Calculator
========================================''')

totalkm = float(input("Enter total number of kilomiters: "))
totalmoney = totalkm * 15

print(f"Total fare: ₹{totalmoney}")


print('''========================================
Assignment 5: Shopping Tax Calculator
========================================''')

totalcart = float(input("Enter total cart value: "))

tax = (totalcart*12)/100

print("Your total cart amount: ",totalcart)
print("Tax: ",tax)


print('''========================================
Assignment 6: Smart Coin Machine
========================================''')


amount = int(input("Enter amount: "))

coin10 = amount // 10
coin1 = amount - (10 * coin10)
coin2 = coin1 // 5

print(f"Output: ₹10 x {coin10} , ₹5 x {coin2}")

print('''# ========================================
# Assignment 7: Temperature Converter
# ========================================''')

tem = int(input("Enter temprecher: "))
f = (tem * 9/5) + 32

print("Celsius: ",tem)
print("Fahranheit: ",f)

print('''# ========================================
# Assignment 8: Simple Interest Calculator
# ========================================''')


amount = int(input("Enter amount:; "))
rate = int(input("Enter rate of interest:; "))
time = int(input("Enter time(in year):; "))

si = (amount * rate*time) / 100

print("Simple interest: ",si)