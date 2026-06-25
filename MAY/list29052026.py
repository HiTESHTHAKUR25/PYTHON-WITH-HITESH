# Given an array elevation[] of size N, find the index of any one peak checkpoint.
# 
# Test Case 1
# 
# Input:
# elevation = [1200, 1450, 1700, 1600, 1500]
# 
# Output:
# 2
# 
# Explanation:
# 1700 is greater than both adjacent values 1450 and 1600.
# 
# Test Case 2
# 
# Input:
# elevation = [800, 900, 950, 1000]
# 
# Output:
# 3
# 
# Explanation:
# Last element can also be a peak because it has no right neighbor.
# 
# Test Case 3
# 
# Input:
# elevation = [3000]
# 
# Output:
# 0
# 
# Explanation:
# Single element is always a peak.
# 

n = int(input("Enter The Size of List: "))
l = []
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
print(l)

n = len(l)
peakindex = []

for i in range(n):
    if i == 0:
        if n == 1 or l[i] >= l[i+1]:
            peakindex.append(i)
    elif i == n-1:
        if l[i] >= l[i-1]:
            peakindex.append(i)
    else:
        if l[i] >= l[i-1] and l[i] >= l[i+1]:
            peakindex.append(i)

print(peakindex)
n5 = peakindex[0]
if len(peakindex) != 0:
    print("Peak Checkpoint: ",l[n5])
else:
    print("Theire Is no have any peak point:")





# 2.
# Smart City Traffic Peak Load Analyzer

# Problem Statement

# A smart city monitors traffic density at different time intervals in a day.

# An element is called a peak traffic point if it is greater than or equal to its adjacent elements.

# You are given an array traffic[] of size N.

# Tasks:

# Find all peak elements
# Calculate the sum of all peak traffic values
# Find the product of all peak traffic values
# Return the maximum peak value

# Note:
# If only one element exists, it is the only peak.

# Test Case 1

# Input:
# traffic = [10, 50, 30, 70, 60, 90, 80]

# Output:
# Peaks = [50, 70, 90]
# Sum = 210
# Product = 315000
# Max Peak = 90

# Test Case 2

# Input:
# traffic = [100, 200, 150, 180, 170]

# Output:
# Peaks = [200, 180]
# Sum = 380
# Product = 36000
# Max Peak = 200

# Test Case 3

# Input:
# traffic = [5]

# Output:
# Peaks = [5]
# Sum = 5
# Product = 5
# Max Peak = 5



n = int(input("Enter The Size of List: "))
l = []
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
print(l)

sum = 0
peakpro = 1
peakvalues = []

for i in range(len(l)):
    if i == 0:
        if n == 1 or l[i] >= l[i+1]:
            peakvalues.append(l[i])
            sum += int(l[i])
            peakpro *= l[i]
    elif i == n-1:
        if l[i] >= l[i-1]:
            peakvalues.append(l[i])
            sum += int(l[i])
            peakpro *= l[i]
    else:
        if l[i] >= l[i-1] and l[i] >= l[i+1]:
            peakvalues.append(l[i])
            sum += int(l[i])
            peakpro *= l[i]



print("Peaks: ",peakvalues)
print("Total Sum of all Peak Values: ",sum)
print("Product Of all Peak Values: ",peakpro)

big = peakvalues[0]
for i in peakvalues:
    if i > big:
        big = i

print("Max Peak: ",big)




# 3.
# Industrial Sensor Peak Energy Monitoring System

# Problem Statement

# A factory machine records energy consumption at regular intervals.

# A peak is defined as a value greater than or equal to its neighbors.

# Tasks:

# Find all peak energy values
# Compute sum of squares of peak values
# Compute average of peak values
# Return difference between max peak and min peak
# If no peaks, return -1

# Test Case 1

# Input:
# energy = [20, 40, 30, 60, 50]

# Output:
# Peaks = [40, 60]
# Sum of squares = 5200
# Average = 50
# Difference = 20

# Test Case 2

# Input:
# energy = [10, 20, 15, 25, 20, 30]

# Output:
# Peaks = [20, 25, 30]
# Sum of squares = 1525
# Average = 25
# Difference = 10

# Test Case 3

# Input:
# energy = [5]

# Output:
# Peaks = [5]
# Sum of squares = 25
# Average = 5
# Difference = 0


n = int(input("Enter The Size of List: "))
l = []
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
print(l)

peak = []
sum = 0
sqsum = 0

for i in range(n):
    if i == 0:
        if n == 1 or l[i] >= l[i+1]:
            num = l[i]
            sum += num
            sqsum += num**2
            peak.append(num)
    elif i == n-1:
        if l[i] >= l[i-1]:
            num = l[i]
            sum += num
            sqsum += num**2
            peak.append(num)
    else:
        if l[i] >= l[i-1] and l[i] >= l[i+1]:
            num = l[i]
            sum += num
            sqsum += num**2
            peak.append(num)




print("Peaks: ",peak)
print("Sum of Peak Square: ",sqsum)
print("Average: ",sum/len(peak))
print("Diffrence: ",peak[len(peak)-1]-peak[0])



# 4.

# Problem: Sum of Leaders in an Array After Filtering Invalid Data (Python)

# Definition

# A company collects daily performance scores of employees. However, the dataset may contain invalid entries.

# An element is called a leader if:

# It is greater than all elements to its right side
# The element must be valid, i.e., it should not be:
# Negative number
# Zero

# Rightmost valid element is always considered a leader.

# Input Format
# First line → integer n
# Second line → n space-separated integers

# Output Format
# Single integer → sum of all valid leader elements
# If no valid elements exist → return -1

# Rules
# Before finding leaders:

# Ignore all negative values and zeros
# Work only on positive numbers
# Then find leaders from the filtered sequence

# Test Case 1

# Input:
# 8
# 16 0 17 4 -3 3 5 2

# Processing:
# Filtered array:
# [16, 17, 4, 3, 5, 2]

# Leaders:
# [17, 5, 2]

# Output:
# 24

# Test Case 2

# Input:
# 6
# -1 0 -5 0 -2 -3

# Output:
# -1

# Test Case 3

# Input:
# 5
# 10 20 30 40 50

# Processing:
# Filtered array:
# [10, 20, 30, 40, 50]

# Leaders:
# [50]

# Output:
# 50






n = int(input("Enter The Size of List: "))
l2 = []
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l2.append(n1)
print(l2)

l = []
for j in l2:
    if j > 0:
        l.append(j)



leader = []
sum = 0

for i in range(len(l)):
    flag = 1
    for j in range(i+1,len(l)):
        if l[i] <= l[j]:
            flag = 0
            break
    if flag == 1:
        if l[i] > 0:
            leader.append(l[i])
            sum += l[i]


if len(l) > 0:
    print("Leader: ",leader)
    print("Sum: ",sum)
    print("Filtered: ",l)
else:
    print("-1")




# 5.
# Given an unsorted array arr[] of size N having both negative and positive integers. 
# The task is place all negative element at the end of array without changing the order of positive element and negative element.

# Example 1:
# Input : 
# N = 8
# arr[] = {1, -1, 3, 2, -7, -5, 11, 6 }
# Output : 
# 1  3  2  11  6  -1  -7  -5

# Example 2:
# Input : 
# N=8
# arr[] = {-5, 7, -3, -4, 9, 10, -1, 11}
# Output :
# 7  9  10  11  -5  -3  -4  -1


n = int(input("Enter The Size of List: "))
l = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
print(l)


positive = []
nagative = []
for i in l:
    if i >= 0:
        positive.append(i)
    else:
        nagative.append(i)


print(positive+nagative)






# 6.

# A security system logs employee entry IDs during a day.

# Only prime-numbered IDs are considered valid VIP entries.

# Tasks:

# Extract all prime IDs from the list
# Find the sum of prime IDs
# Find the maximum prime ID
# Count how many prime entries exist

# Input:
# A list of integers (may contain duplicates and non-prime numbers)

# Example 1

# Input:
# [12, 5, 7, 9, 11, 14, 17]

# Output:
# Prime IDs = [5, 7, 11, 17]
# Sum = 40
# Max = 17
# Count = 4

# Example 2

# Input:
# [4, 6, 8, 10]

# Output:
# Prime IDs = []
# Sum = 0
# Max = -1
# Count = 0


n = int(input("Enter The Size of List: "))
l = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
print(l)


allprime = []
sum = 0
for i in l:
    for j in range(2,len(l)//2+1):
        if i % j ==0:
            break
    else:
        allprime.append(i)
        sum += i


print("All Prime: ",allprime)
print("Sum: ",sum)
print("Count: ",len(allprime))



s1 = allprime[0]
for k in allprime:
    if k > s1:
        s1 = k


print("Max Prime: ",s1)





# 7.
# Factory Production – Factorial Expansion List

# Problem Statement

# A factory produces items where production capacity is defined using factorial growth.

# Given a list of numbers, replace each number with its factorial value.

# Then perform analysis on the resulting list.

# Tasks:

# Convert each element to factorial
# Find sum of all factorial values
# Find maximum factorial value
# Count how many factorial values are even

# Input:
# A list of integers

# Example 1

# Input:
# [3, 4, 5]

# Processing:
# 3! = 6
# 4! = 24
# 5! = 120

# Output:
# [6, 24, 120]
# Sum = 150
# Max = 120
# Even Count = 3


n = int(input("Enter The Size of List: "))
l = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
print(l)




allfact = []
sum = 0
for i in l:
    fact = 1
    for k in range(1,i+1):
        fact = fact*k
    allfact.append(fact)
    sum += fact


print(allfact)
print("Sum: ",sum)
print("Count: ",len(allfact))

s1 = allfact[0]
for l in allfact:
    if l > s1:
        s1 = l


print("Sum of All Fact is: ",s1)



