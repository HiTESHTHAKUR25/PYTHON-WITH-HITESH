# Assignment 1: Speed Calculator
km = float(input("Enter distance: "))
time = int(input("Enter time: "))

print(f"Speed: {km/time} km/h")


# Assignment 2: Salary Calculator


wage = int(input("Enter how wage: "))
work = int(input("Enter how many days you work: "))
print(f"Salary: ${wage*work}")


Assignment 3: Electricity Bill Calculator


unit = int(input("Enter total number of unit: "))
print("Bill: ","$",unit*6)



#Assignment 4: Area of Rectangle
 n

len = float(input("Enter Length: "))
bre = float(input("Enter Bredath: "))
print("Area: ",len*bre)

#Assignment 5: Average Marks Calculator

m1 = float(input("Enter math marks: "))
m2 = float(input("Enter physics marks: "))
m3= float(input("Enter chemistry marks: "))
marks = (m1+m2+m3)/3
print("Average: ",marks)


# Assignment 6: Discount Calculator


totalamount = int(input("Enter total amount: "))
discount = (totalamount*10)/100
print("Discount: ",discount)
print("Final: ",totalamount-discount)



# Assignment 7: Circle Area Calculator


redius = float(input("Enter Redius: "))

print("Area: ",redius*redius*3.14)

# Assignment 8: Data Storage Converter


mb = int(input("ENter data in MB: "))
gb = mb / 1024
print("MB: ",mb)
print("GB: ",gb)

# Assignment 9: Fuel Cost Calculator


dis = float(input("Enter total Distance: "))
mil = float(input("Enter total Mileage: "))
pet = float(input("Enter total Petrol price: "))

mileage = dis/mil
cost = mileage*pet

print("Cost: ",cost)



# Assignment 10: Percentage Calculator


totalmr = float(input("Enter total marks: "))
obtained = float(input("Enter obtained marks: "))

per = (obtained/totalmr)*100

print(f"Percentage: {round(per,2)%}")

# Assignment 11: Time Duration Adder




hourse= int(input("Enter hourse: "))
minutes = int(input("Enter minutes: ")) 
seconds = int(input("Enter seconds: "))
hou = hourse * 3600
min = minutes*60


print(f"Total Seconds: ",hou+min+seconds)


# Assignment 12: Change Return System


amount = int(input("Enter Amount: "))

r100 = amount//100
r505 = amount - 100*r100
r50 = r505//50
r101 = r505 - r50*50
r10 = r101 // 10

print(f"Calculates: \n₹100 x {r100} \n₹50 x {r50}\n₹10 x {r10} notes")


# Assignment 13: Compound Interest Calculator


pric = int(input("Enter Principal amount: "))
rate = int(input("Enter Rate: "))
time = int(input("Enter Time: "))
ratee = rate/100
ci = pric *( (1+ratee)**time)

print(f"Compound Interest: ",ci)




# Assignment 14: Simple Profit or Loss Calculator


cp = int(input("Enter the cost price: "))
sp = int(input("Enter the selling price: "))

profit = sp - cp

finalprice = (profit / cp)*100
print(f"Profit: {finalprice}%")


# Assignment 15: Average Speed for Multiple Trips



dis1 = int(input("Enter first distance: "))
time1 = int(input("Enter first time: "))
dis2 = int(input("Enter second distance: "))
time2 = int(input("Enter second time: "))

average1 = dis1 / time1
average2 = dis2 / time2

totalav = (average1+average2)/2

print(f"Average Speed: {totalav} km/h")