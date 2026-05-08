# 1.Digit Product Analyzer System

# A data analytics company studies patterns in numeric transaction IDs to detect hidden behaviors.

# For every entered number, the system analyzes relationships between its digits.

# Write a program to:

# Find the product of every pair of adjacent digits
# Display all the products
# Find the sum of all these products
# Find the smallest product value
# If the sum of products is divisible by the total number of digits, print Stable Number
# Otherwise print Unstable Number

# Use loops wherever required.

# Input:
# 57294

# Output:
# Products: 35 14 18 36
# Sum = 103
# Smallest = 14
# Unstable Number


num = int(input("Enter Number: "))

rev = ""
while num>0:
    rev1 = num%10
    rev = rev+str(rev1)
    num = num//10






num = int(rev)
numm = num
num1 = numm%10
numm = numm//10
sum = 0 
count = 0
num4 = 0
while numm>0:
  count+=1
  num2 = numm%10
  num3 = num2*num1
  sum += num3
  print(num3,end=" ")
  num1 = num2
  numm = numm//10
  if count == 1:
    num4 = num3
  elif count>1:
    if num3<num4:
      num4=num3
    else:
      num4=num4



print()
print("Sum",sum)
print("Smallest digit",num4)

if sum%count==0:
  print("Stable nUmbre")
else:
  print("Unstable Number")

                          

# 2.
# Digit Order Break Analyzer

# A number validation system checks whether digits of an ID follow a strict increasing pattern. The moment the pattern breaks, the system stops further checking.

# Write a program to:

# Traverse the digits from left to right
# Check whether each digit is greater than the previous digit
# If the pattern breaks at any point, stop checking further using break
# Display the position where the order breaks (1-based index)
# If no break occurs, print Strictly Increasing Number

# Use loops and break wherever required.

# Input:
# 12357

# Output:
# Strictly Increasing Number

# Input:
# 12342

# Output:
# Break at position = 4
# Not Increasing Number

num = int(input("Enter Number: "))
numm = num


rev  = ""
while num>0:
  num1 = num%10
  rev = rev+str(num1)
  num = num//10



count=0
rev = int(rev)
num2 = rev%10
rev = rev//10
while rev>0:
  num3 = rev%10
  if num3 > num2:
    num2 = num3
    count+=1
  else:
    print("Break at position: ",num3)
    print("Not Increasing Number")
    break
  rev = rev//10
  

if count==(len(str(numm))-1):
  print("Strictly Increasing Number")



# 3.
# Zero Detection & Early Termination System

# A financial system scans transaction IDs digit by digit. If a digit '0' is found, the system immediately stops processing further digits for security reasons.

# Write a program to:

# Traverse each digit of the number from right to left
# Display each digit processed before encountering 0
# Stop the loop immediately when 0 is found using break
# Count how many digits were processed before termination
# If no zero is found, print No Zero Found

# Use loops and break wherever required.

# Input:
# 572049

# Output:
# Digits Processed: 9 4
# Count = 2
# Zero Found - Process Stopped

# Input:
# 56789

# Output:
# Digits Processed: 9 8 7 6 5
# Count = 5
# No Zero Found

num = int(input("Enter Numbre: "))
numm = num



count = 0
while num>0:
  num1 = num%10
  if count == 0:
    print("Digits Processed:",end=" ")
  if num1 != 0:
    count+=1
    print(num1,end=" ")
  elif num1 == 0:
    print()
    print("Zero Found - Process Stoped")
    break
  num = num//10


print("Count: ",count)
if count==len(str(numm)):
  print("Non Zero Found")



# 4.
# 1. Digit Gap Consistency Checker

# A number analysis system checks whether the gap between digits follows a consistent pattern.

# Write a program to:

# Find the absolute difference between first two digits
# Compare this difference with all next adjacent digit differences
# If any difference is not equal to the first difference, stop using break
# Display:
# - Initial gap
# - Whether all gaps are same or not

# Input:
# 8642

# Output:
# Initial Gap = 2
# Consistent Pattern

# Input:
# 97531

# Output:
# Initial Gap = 2
# Consistent Pattern

# Input:
# 5321

# Output:
# Initial Gap = 2
# Pattern Break Detected


num = int(input("Enter NUmbre: "))
numm = num
rev = 0
for i in range(1,len(str(numm))+1):
  num1 = numm%10
  rev = 10*rev+num1
  numm = numm//10


num2 = rev%10
rev = rev//10
num3 = rev%10
rev = rev//10
num4 = abs(num2-num3)


while rev >0:
  num5 = rev%10
  num6 = abs(num3-num5)
  if num4 != num6:
    print("Intial Gap Is: ",num4)
    print("Pattern Break Detect")
    break
  else:
    num3 = num5
    rev =rev//10
else:
  print("Initial Gap is:",num4)
  print("Consistent Pattern")
  





# 5. Digit Alternating Sum System

# A coding system calculates alternating sum of digits (add, subtract, add...).

# Write a program to:

# Traverse digits from left to right
# Add first digit, subtract second, add third, and so on
# Display final alternating sum
# If result is positive → print Positive Pattern
# Else → print Negative Pattern

# Input:
# 1234

# Output:
# Result = -2
# Negative Pattern

# Input:
# 8642

# Output:
# Result = 8
# Positive Pattern


num = int(input("Enter Number: "))



rev = 0
while num>0:
  num1 = num%10
  rev = rev*10+num1
  num = num//10

count = 1
result1 = 0
result2 = 0

while rev>0:
  num2 = rev%10
  if count%2!=0:
    result1 = result1+num2
    count+=1
  else:
    result2 = result2-num2
    count+=1
  rev = rev//10

result = result1 + result2 
print("Result: ",result)


if result <0:
  print("Negative Pattern")
else:
  print("POsitive Pattern")