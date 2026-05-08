# 1. Adjacent Digit Difference Analyzer

# A system analyzes differences between consecutive digits in a number.

# Write a program to:

# Find the difference between every pair of adjacent digits
# Display all differences
# Count how many differences are even
# Find the largest difference
# If all differences are same → print Uniform Difference
# Else → print Non-Uniform Pattern

# Input:
# 84261

# Output:
# Differences: 4 2 4 5
# Even Differences Count = 3
# Max Difference = 5
# Non-Uniform Pattern

num = int(input("Enter Number: "))
num4 = num
numm = num
rev = 0

while numm>0:
    num1 = numm%10
    rev = rev*10+num1
    numm = numm//10



num2 = rev%10
rev  = rev//10
numm1 = ""
count =0
while rev>0:
    num3 = rev%10
    num4 = num3-num2
    num4 = abs(num4)
    if num4%2==0:
        count+=1
    numm1 += str(num4)
    num2 = num3
    rev = rev//10

numm1 = int(numm1)
print("Diffrence:",numm1)
print("Even Differences Count:",count)

numm2 = numm1%10
numm1 = numm1//10
while numm1>0:
    numm3 = numm1%10
    if numm3>numm2:
        numm2=numm3
    numm1 = numm1//10
    

print("Max Diffrence:",numm2)

num5 = num4%10
num4 = num4//10

if str(num5) in str(num4):
    print("Uniform Difference")
else:
    print("Non-Uniform Difference")



# 2. Digit Sum Mirror Checker

# A validation system checks symmetry in digit sums.

# Write a program to:

# Split number into two halves
# Find sum of first half digits
# Find sum of second half digits
# Display both sums
# If both sums are equal → print Balanced Number
# Else → print Unbalanced Number

# Input:
# 123321

# Output:
# First Half Sum = 6
# Second Half Sum = 6
# Balanced Number

num = int(input("ENter Number: "))
numm = num
length = len(str(num))
length = length//2

count = 10**length
count1=count

numm1 = numm%count
numm2 = numm//count1

int(numm1)
int(numm2)

num1 = 0
while numm1>0:
    numm5 = numm1%10
    num1 = num1+numm5
    numm1 = numm1//10

num2 = 0
while numm2>0:
    numm6 = numm2%10
    num2 = numm6+num2
    numm2 = numm2//10




if num1 == num2:
    print("Balanced Number")
else:
    print("Unbalanced Number")



# 3.
# Digit Neighbor Sum Analyzer

# A system analyzes the relationship between a digit and its immediate neighbors.

# Write a program to:

# Traverse digits from left to right (ignore first and last digit)
# For each digit, calculate sum of its adjacent digits
# Check if current digit is equal to the sum of its neighbors
# Display such digits
# Count how many such digits exist
# If none found → print No Matching Digit
# Else → print Neighbor Sum Pattern Found

# Input:
# 121314

# Output:
# Matching Digits: 2 3
# Count = 2
# Neighbor Sum Pattern Found

num = int(input("Enter Numbre: "))
numm = num


rev  = 0 
while numm>0:
    num1 = numm%10
    rev = rev*10+num1
    numm = numm//10



num2 = rev%10
rev = rev//10
count=0
print("Matching Digits: ",end=" ")

while rev>0:
    num3 = rev%10
    rev = rev//10
    num4 = rev%10
    if (num2+num4)==num3:
        print(num3,end=" ")
        count+=1
        num2 = num3
    else:
        num2 = num3


print("\nCount:",count)

if count>0:
    print("Neighbor Sum Pattern Found")
else:
    print("No Matching Digit")


# 4.Digit Gap Analyzer

# A system analyzes the gap between consecutive digits.

# Write a program to:

# Traverse digits from left to right
# Find the absolute difference between current digit and next digit
# Display each difference
# Count how many differences are greater than 2
# Find the maximum difference
# If all differences ≤ 2 → print Smooth Number
# Else → print Irregular Pattern

# Input:
# 86421

# Output:
# Differences: 2 2 2 1
# Count (>2) = 0
# Max Difference = 2
# Smooth Number


num = int(input("Enter Number: "))
numm = num 

rev = 0

while numm>0:
    num1 = numm%10
    rev = 10*rev+num1
    numm = numm//10


num2 = rev%10
rev = rev//10
diff = ""
maxa = 0

while rev>0:
    num3 = rev%10
    num4 = num3-num2
    num2 = num3
    num4 = abs(num4)
    diff += str(num4)
    rev = rev//10

diff=int(diff)
diffa = diff
print("Differences:",diff)

count = 0
while diff>0:
    num5 = diff%10
    if num5>2:
        count+=1
    diff = diff//10

print("Count:",count)

num5 = diffa%10
diffa = diffa//10
while diffa>0:
    num6 = diffa%10
    if num6>num5:
        num5 = num6
    diffa = diffa//10
    
print("Max Diffrence:",num5)

if num5<=2:
    print("Smooth NUmbre")
else:
    print("Irregular Pattern")

# 5.
# Tech Number Checker

# A number is called a Tech Number if:

# It has even number of digits
# Split it into two equal halves
# Add both halves
# Square the sum
# If result equals original number → Tech Number

# Write a program to:

# Count digits
# If digits are even, split the number
# Find sum of both halves
# Square the sum
# Display intermediate values
# Check and print result

# Input:
# 2025

# Output:
# First Half = 20
# Second Half = 25
# Sum = 45
# Square = 2025
# Tech Number



num = int(input("Entre Number: "))
num1 = num

lennum = len(str(num1))
splitt = lennum//2


if lennum%2==0:
    num2 = 10**splitt    
    numm1 = num1//num2
    numm2 = num1%num2
    num3 = numm1+numm2
    num4= num3**2

    print("First Half:",numm1)
    print("Second Half:",numm2)
    print("Sum:",num3)
    print("Square:",num4)
    
    if num == num4:
        print("Tech Number:")
    else:
        print("Not-Tech Number:")

