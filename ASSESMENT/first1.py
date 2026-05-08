
# Digit Frequency Balance Analyzer

# A data security system analyzes numeric IDs to check digit distribution patterns.

# For a given number, the system evaluates how frequently each digit appears.

# Write a program to:

# Count how many times each digit appears in the number
# Display only the digits that appear more than once
# Find the total count of repeated digits
# Find the digit with maximum frequency
# If no digit repeats, print Unique Number
# If at least one digit repeats, print Repeated Pattern Detected

# Use loops wherever required.

# Input:
# 1223451

# Output:
# Repeated Digits: 1 2
# Total Repeated Count = 4
# Max Frequency Digit = 1
# Repeated Pattern Detected

num = int(input("Enter Numbre: "))
numm = num
count=0
print("Repeated Digits: ",end=" ")
num2 = 0
numm1 = 0
while numm>0:
    num1 = numm%10
    numm = numm//10
    if str(num1) in str(numm):
        print(num1,end=" ")
        num2 = num1
        count+=1


print("\nMax Frequency Digit: ",num2)

print("Count: ",count)
if count > 2:
    print("Repeated Pattern Detected")