#ASSINGNMENT 1
bill = float(input("Enter your Total Bill: "))
friends = int(input("Enter total number of your friends: "))
gst = bill*0.05
service = bill*0.1


totalbill = bill+gst+service

final = totalbill/friends

print("FINAL BILL: ",totalbill)
print("EACH PERSON PAYS: ",final)


#ASSINGNMENT 2


mobile = int(input("Mobile Price: "))
down = int(input("Down Payment: "))

rem = mobile-down
interest = rem*0.1
totals = rem + interest
emi = totals/10


print("Remaining Amount: ",rem)
print("Total with Interest: ",totals)
print("Monthly EMI: ",emi)


#ASSINGNMENT 3

m1 , m2 , m3 , m4 , m5 = map(float,input("Enter your 5 subject marks: ").split())

total  = (m1+m2+m3+m4+m5)
average = total / 5
percentage = (total/500)*100

print("AVERAGE: ",average)
print("PERCENTAGE: ",percentage)

#ASSINGNMENT 4

speed = int(input("Speed: "))
t1,t2 = map(int,input("Time(Hours Minutes): ").split())

totaltime = ((t1*60)+t2)/60
distance = totaltime*speed

print("Total Time: ",round(totaltime),"Hours")
print("Distance: ",distance,"km")





#ASSINGNMENT 5


salary = int(input("Monthly salary: "))
days = int(input("Working days: "))
hours = int(input("Working hours per day: "))

totaldays = salary/days
totalhours= totaldays/hours

print("Salary per day: ",totaldays)
print("Salary per hours: ",totalhours)



#ASSINGNMENT 6

data = int(input("DATA: "))

mb = data * 1024
kb = data * 1024 * 1024

print("IN MB : ",mb)
print("IN GB : ",kb)


#ASSINGNMENT 7
runs = int(input("Total runs: "))
over = float(input("Over: "))

runrate = runs/over
totalball = ((int(over))*6) 
totalballss = over*10
totalbal = totalballss%10
totalballs = totalbal+totalball


print("Total Balls: ",totalballs)
print("Run Rate: ",round(runrate,2))


#ASSINGNMENT 8
principle = int(input("Principal amount: "))
rate = int(input("Rate: "))
time = int(input("Time: "))
rate = rate/100
ci = principle *( (1+rate)**time)

print("Amount after interest: ",ci)



#ASSINGNMENT 9

dis = int(input("Distance: "))
mil = int(input("Mileage: "))
pet = int(input("Petrol price: "))

usdpet = dis/mil
totalcost = pet*usdpet

print("Petrol Used: ",usdpet,"liters")
print("Total Cost: ",totalcost)

#ASSINGNMENT 11
print(50 + (10 * (+(2**3))) / 4 - (-6 % 4))

#ASSINGNMENT 12

print(100 - (20 * (3**2)) + (40 / (+5)) - (-3))
#ASSINGNMENT 13


print(25 + (5 * (6**2) // 3) - (-(8 % 5)) + (+2))
#ASSINGNMENT 14

print((80 / (4 * 2)) * (+(2**2)) + 15 - (-(9 % 2)))

#ASSINGNMENT 15

print(60 + (12 * (2**3) // (+(4))) - (-(10 % 3)))

#ASSINGNMENT 16

print(45 + (15 * (2**2)) - (20 / (+(5))) + (-(7 % 3)))