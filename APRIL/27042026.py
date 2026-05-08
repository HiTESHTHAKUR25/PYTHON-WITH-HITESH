# 1. Product of Odd Numbers up to N

# A puzzle game rewards players by multiplying odd numbers up to n.
# Write a program using loops to find product of odd numbers.

# Input:
# 5

# Output:
# 15

num = int(input("Enter Number: "))
count=1
for i in range(1,num+1):
    if i%2!=0:
        count=count*i


print(count)



# 2. Count Numbers Divisible by 7 Between Two Numbers

# A company filters lucky coupon numbers divisible by 7.
# Write a program using loops to count such numbers in range.

# Input:
# 1 30

# Output:
# Count = 4

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
count=0
for i in range(num1,num2+1):
    if i%7==0:
        count+=1
    
print(count)





# 3. Display Numbers Ending with 5

# A supermarket tracks token numbers ending in 5.
# Write a program using loops to display numbers ending with 5 between two numbers.

# Input:
# 10 40

# Output:
# 15 25 35


num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))


for i in range(num1,num2+1):
    if i%5==0 and i%2!=0:
        print(i)




# 4. Strong Number Checker

# A digital lock opens only for strong numbers.

# A strong number is a number whose sum of factorial of digits equals the number.

# Example:
# 145 = 1! + 4! + 5!

# Write a program using loops to check strong number.

# Input:
# 145

# Output:
# Strong Number

num = int(input("Enter Number: "))
num2 = num
sum = 0
while num>0:
    num1 = num%10

    fact = 1
    for i in range(1,num1+1):
        fact *= i
    
    sum+=fact
    num = num//10

if num2 == sum:
    print("Strong number")
else:
    print("not Strong number")




========5=========

n = int(input("Enter Number = "))
sum = 0
m = n
while n>0:
  digit = n%10
  sum+=digit
  n= n//10

if m%sum==0:
 print("Harshad Number")
else:
 print("Not Harshad Number")




# 6. Automorphic Number Checker

# A digital security company designs smart lockers that open only for special self-matching numeric codes. When a user enters a number, the system squares the number and checks whether the result ends with the same digits as the original code. If yes, the locker grants access.

# An automorphic number is a number whose square ends with the same number.

# Example:
# 25² = 625

# Write a program using loops to check whether the entered number is an Automorphic number.

# Input:
# 25

# Output:
# Automorphic Number


num = int(input("Entetr Number: "))

count = 1
num1 = num**2

for i in range(1,len(str(num))+1):
  count *= 10

num2 = num1%count

if num2 == num:
  print("Automorphic Number")
else:
  print("Not Automorphic Number")



# 7. Duck Number Checker

# A verification system is used by an e-commerce company to validate promotional coupon numbers. Coupon numbers containing at least one zero in between digits are considered special duck numbers. However, if the number starts with zero, it is rejected immediately.

# A duck number is a number that contains at least one zero but does not start with zero.

# Example:
# 1023

# Write a program using loops to check whether the entered number is a Duck number.

# Input:
# 1023

# Output:
# Duck Number


num = int(input("Enter Numbre: "))
count = 1

for i in range(1,len(str(num))-1):
  count*=10
numm = str(num)

if num//count!=0:
  if "0" in (numm):
    print("Duck Number")
  else:
    print("NOt Duck Number")
else:
  print("NOt Duck Number")



# 8.
# Mirror Difference Transaction Verification System
# A multinational banking company processes thousands of daily transaction IDs. To detect suspicious patterns and validate system-generated IDs,
#  the security software performs a Mirror Difference Verification Test.
# For every entered transaction ID:

# Reverse the digits of the transaction ID

# Find the absolute difference between the original ID and the reversed ID


# Count the total number of digits in the difference


# Apply the following conditions using if-elif-else:

# If the difference is 0, print Perfect Match


# Else if the difference is divisible by 9, print Verified


# Else print Rejected


# Write a program to automate this verification process using loops and conditional statements.
# Input:
# 4215
# Output:
# Reverse = 5124Difference = 909Digits = 3Verified
# Input:
# 1221
# Output:
# Reverse = 1221Difference = 0Digits = 1Perfect Match
# Input:
# 1234
# Output:
# Reverse = 4321Difference = 3087Digits = 4Verified

num = int(input("Enter Number: "))
numm = num
rev = ""

while numm>0:
  num1 = numm%10
  rev =rev + str(num1)
  numm = numm//10
rev = int(rev)
print("Reverse:",rev)

diffrence = rev-num
print("Deffrence:",diffrence)

count=0
for i in range(1,len(str(diffrence))+1):
  count+=1
print("Digits:",count)

if diffrence==0:
  print("Perfect Match")
elif diffrence %9==0:
  print("Verified")
else:
  print("Rejected")




# 9.
# Step Difference Number Analyzer

# A mathematics research center studies hidden patterns inside numbers.
# For every entered number, the system compares adjacent digits step by step.

# Write a program to:

# Find the absolute difference between every pair of adjacent digits
# Display all step differences
# Find the sum of all step differences
# Find the largest step difference
# If the sum of step differences is divisible by the number of digits, print Balanced Number
# Otherwise print Unbalanced Number

# Use loops wherever required.

# Input:
# 57294
# Output:
# Step Differences: 2 5 7 5
# Sum = 19
# Largest = 7
# Unbalanced Number



num = int(input("Enter NUmber: "))
numm = num
num1 = numm%10
numm = numm//10
step = ""
while numm>0:
  num2 = numm%10
  if num2>num1:
    num3 = num2-num1
    step = step+str(num3)
  else:
    num4 = num1-num2
    step = step+str(num4)
  numm = numm//10
  num1 = num2

stepp = int(step)
stepp1 = ""
sum = 0
count = 0
while stepp>0:
  count+=1
  step1 = stepp%10
  sum = sum+step1
  stepp1 = stepp1+str(step1)
  stepp = stepp//10



step2 = int(stepp1)
larg = step2%10
step2 = step2//10

for i in range(1,len(str(step2))+1):
  larg1 = step2%10
  if larg1>larg:
    larg = larg1
  else:
    larg = larg



if sum%count==0:
  print("balanced Number")
else:
  print("Unbalanced Number")

print("Step Differences: ",stepp1)
print("Sum: ",sum)
print("Largest:",larg)



 