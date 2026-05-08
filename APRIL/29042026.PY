# 1. Triple Operation Prime Verification System

# A cybersecurity company generates a security score from entered access code.

# Write a program to:

# - Find sum of digits of the number
# - Reverse the number
# - Find absolute difference between original number and reverse
# - Add digit sum and difference
# - Check whether final result is Prime or Not Prime

# Input:
# 4215

# Output:
# Sum of Digits = 12
# Reverse = 5124
# Difference = 909
# Final Result = 921
# Not Prime


num = int(input("Enter Number: "))
numm= num
sum = 0
rev = 0


while num > 0:
    num1 = num%10
    sum+=num1
    rev= 10*rev+num1
    num = num//10


print("Sum of Digits: ",sum)
print("Reverse: ",rev)
print("Difference",num-rev)
print("Final Result: ",sum+(num-rev))

for i in range(2,numm):
    if numm%i==0:
        print("Not Prime")
        break
else:
    print("prime")



# 2. Multi Stage Prime Lock System

# A smart locker opens only if final derived number is prime.

# Write a program to:

# - Find sum of digits
# - Find product of digits
# - Find difference between product and sum
# - Count digits in difference
# - Add digit count to difference
# - Check whether final result is Prime or Not

# Input:
# 234

# Output:
# Sum = 9
# Product = 24
# Difference = 15
# Digits = 2
# Final Result = 17
# Prime

num = int(input("Enter Number: "))
numm= num
sum = 0 
product = 1
while num>0:
    num1 = num %10
    sum +=num1
    product *= num1
    num = num//10

print("Sum:",sum)
print("Product:",product)
print("Difference:",product-sum)
countt= product-sum
count = len(str(countt))
print("Digits:",count)
print("Final Results:",count+countt)

for i in range(2,num):
    if numm%i==0:
        print("Not Prime")
        break
else:
    print("Prime")



# 3. Perfect Number Reward System

# A gaming company rewards users if entered number is a Perfect Number.

# (Perfect Number = sum of proper factors equals number)

# Write a program using for-else loop to:

# - Find sum of proper factors
# - If sum equals number print Reward Unlocked
# - Else print Try Again

# Input:
# 6

# Output:
# Reward Unlocked



num = int(input("Enter Number: "))
per = 0

for i in range(1,num+1//2):
    if num%i==0:
        per = per+i


if num == per:
    print("Reward Unlocked")
else:
    print("Try Again")



# 4.Unique Digit Security Scanner

# A smart locker accepts only numbers whose all digits are unique.

# Write a program using for-else loop to:

# - Check every digit
# - If any repeated digit found reject
# - Else accept

# Input:
# 57294

# Output:
# Valid Unique Code


num = int(input("Enter Number: "))
numm= len(str(num))


for i in range(1,numm):
    num1 = num%10
    num = num//10
    num2=str(num1)
    num3=str(num)


    if num2 in num3:
        print("Rejcet")
        break
else:
    print("Valid Unique Code")
    


# 5.Number Stability Analyzer

# A science lab studies whether digits are in increasing order.

# Write a program using for-else loop:

# - If every next digit is greater than previous print Stable Number
# - Else Unstable Number

# Input:
# 12359

# Output:
# Stable Number


num = int(input("Enter Number: "))
numm = len(str(num))
num2 = num%10
numm1 = num//10
for i in range(1,numm+1):
    num1 = numm1%10
    if num1<=num2:
        num2 = num1
        numm1 = numm1//10
        print("Stable Number")
        break
    
else:
    print("UnStable Number")


# 6.
# Next Prime Cabin Number Generator

# A luxury hotel gives only prime numbered cabins to VIP guests.

# Manager enters the last allotted cabin number.
# System must find the next available prime cabin number.

# Write a program using loops.

# Input:
# 24

# Output:
# Next Prime Cabin = 29

n = int(input("Enter Numbre: "))

num = n + 1

while True:
    count = 0
    
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    
    if count == 2:
        print("Next Prime Cabin =", num)
        break
    
    num += 1



#  7
#  Alternate Digit Prime Checker

# A math lab adds alternate digits from right side.

# Write a program to:

# - Find sum of alternate digits
# - Check whether sum is Prime or Not

# Input:
# 12345

# Output:
# Alternate Sum = 9
# Not Prime


num = int(input("Entre Number: "))
sum = 0 
while num>0:
    num1 = num%10
    if num1%2!=0:
        sum=sum+num1
    num = num//10

print(sum)

for i in range(2,sum):
    if sum%i==0:
        print("Not Prime")
        break
else:
    print("Prime")



# 8.
#  ATM Note Counter

# A bank ATM dispenses ₹100 notes.

# Write a program to:

# - Read withdrawal amount
# - Count how many ₹100 notes needed using loop

# Input:
# 700

# Output:
# Notes = 7


num = int(input("Enter Number: "))
count=0
while num>0:
    if num>=100:
        count+=1
    num = num-100


print(count)





# 9.
#  Bike Service Kilometer Checker

# A bike needs service every 3000 km.

# Write a program to:

# - Read travelled kilometers
# - Print every service checkpoint till entered km

# Input:
# 10000

# Output:
# 3000 6000 9000

num = int(input("Enter Number: "))
while num>=3000:
    num1 = num//3000
    print(num1*3000,end=" ")
    num = num-3000




# 10.
# Lift Mode Operation – Advanced Smart Elevator System

# A smart building elevator works in multiple intelligent modes based on the mode number entered by the control panel.  
# The system must automatically execute floor movement instructions using loops.

# Write a program:

# - If mode = 1  
#   Normal Up Mode activated.  
#   Read current floor and destination floor.  
#   Print all floors from current to destination in ascending order.

# - Else if mode = 2  
#   Down Mode activated.  
#   Read current floor and destination floor.  
#   Print all floors from current to destination in descending order.

# - Else if mode = 3  
#   Energy Saving Mode activated.  
#   Read destination floor.  
#   Lift starts from ground floor (0) and stops only on alternate floors till destination.

# - Else  
#   Emergency Mode activated.  
#   Print "Emergency Alarm" 4 times using loop.

# Input:
# 3
# 6

# Output:
# 0 2 4 6


# Input:
# 1
# 2
# 7

# Output:
# 2 3 4 5 6 7


# Input:
# 2
# 8
# 3

# Output:
# 8 7 6 5 4 3


# Input:
# 5

# Output:
# Emergency Alarm
# Emergency Alarm
# Emergency Alarm
# Emergency Alarm

mode = int(input("Enter Mode: "))

if mode ==1:
    print("Normal Up Mode activated.")
    num1 = int(input("Enter Current Floor: ")) 
    num2 = int(input("Enter Destination Floor: ")) 
    for i in range(0,num2+1,2):
        print(i,end=" ")
elif mode == 2:
    print("Down Mode activated.")
    num3 = int(input("Enter Current Floor: ")) 
    num4 = int(input("Enter Destination Floor: ")) 
    for i in range(num3,num4+1):
        print(i,end=" ")
elif mode==3:
    print("Energy Saving Mode activated.")
    num5 = int(input("Enter Destination Floor: "))
    for i in range(0,num5+1):
        print(i,end=" ")
else:
    print("Emergency Mode activated.")
    for i in range(1,5):
        print("Emergency Alarm")
    

    