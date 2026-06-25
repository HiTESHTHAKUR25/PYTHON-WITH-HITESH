
# ====================================================================

# 1. First Non-Repeating Number
#    ====================================================================

# Scenario

# An online voting system stores vote IDs in a list.

# Find the first vote ID that appears only once.

# Requirements

# * Read N and list elements from user
# * Find the first non-repeating number
# * If no such number exists, display an appropriate message

# Test Case 1

# Input:
# [4, 5, 1, 2, 1, 2, 4]

# Output:
# First Non-Repeating Number = 5

# Test Case 2

# Input:
# [7, 7, 8, 8]

# Output:
# No Non-Repeating Number Found

# ---


n = int(input("Enter Length of List: "))
l = []
for i in range(1,n+1):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
print(l)

s = "".join(str(i) for i in l)

final = ""
for i in range(len(s)):
    if s[i] not in s[i+1:len(s)]:
        final = s[i]
        break


print(final)







# 2. First Repeating Number
# =========================

# Scenario

# A security system logs employee IDs.

# Find the first ID that repeats in the list.

# Requirements

# * Read N and list elements from user
# * Find the first repeating number
# * If no repeating number exists, display an appropriate message

# Test Case 1

# Input:
# [10, 5, 3, 4, 3, 5]

# Output:
# First Repeating Number = 3

# Test Case 2

# Input:
# [1, 2, 3, 4]

# Output:
# No Repeating Number Found

# ---




n = int(input("Enter Length of List: "))
l = []
for i in range(1,n+1):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
print(l)

s = "".join(str(i) for i in l)

final = ""
for i in range(len(s)):
    if s[i]  in s[i+1:len(s)]:
        final = s[i]
        break


print(final)





# 
# ====================================================================
# 3. Missing Number Detector
# ==========================
# 
# Scenario
# 
# Numbers from 1 to N should exist in a sequence, but one number is missing.
# 
# Requirements
# 
# * Read N and list elements from user
# * Find the missing number
# * Assume numbers belong to the range 1 to N+1
# 
# Test Case 1
# 
# Input:
# [1, 2, 3, 5]
# 
# Output:
# Missing Number = 4
# 
# Test Case 2
# 
# Input:
# [2, 3, 4, 5]
# 
# Output:
# Missing Number = 1
# 
# Test Case 3
# 
# Input:
# [1, 2, 4, 5]
# 
# Output:
# Missing Number = 3
# 
# ---
# 
# 


n = int(input("Enter Length of List: "))
l = []
for i in range(1,n+1):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
print(l)


l1 = []
for i in range(l[0],l[-1]+1):
    l1.append(i)

for k in range(len(l)):
    if l1[k] != l[k]:
        print("Missing Number: ",l1[k])
        break
    else:
        if l[0] == 2:
            print("Missing Number: ",1)
            break



# 
# 4. Longest Consecutive Sequence
# ===============================
# 
# Scenario
# 
# Find the longest sequence of consecutive numbers present in the list.
# 
# Requirements
# 
# * Read N and list elements from user
# * Find the length of the longest consecutive sequence
# * Display the sequence length
# 
# Test Case 1
# 
# Input:
# [100, 4, 200, 1, 3, 2]
# 
# Output:
# Longest Consecutive Length = 4
# 
# Explanation:
# Sequence = 1, 2, 3, 4
# 
# Test Case 2
# 
# Input:
# [10, 11, 12, 20]
# 
# Output:
# Longest Consecutive Length = 3
# 
# ---
# 
# 


n = int(input("Enter Length of List: "))
l = []
for i in range(1,n+1):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
print(l)


count = 0
l = sorted(l)

s1 = l[0]
for j in l:
    if s1 == j:
        count+=1
        s1+=1



print(count)





# ====================================================================
# 5. Equilibrium Index Finder
# ===========================

# Scenario

# Find an index where:

# # Sum of elements on the left side

# Sum of elements on the right side

# Requirements

# * Read N and list elements from user
# * Find equilibrium index
# * If not found, display message

# Test Case 1

# Input:
# [1, 3, 5, 2, 2]

# Output:
# Equilibrium Index = 2

# Explanation:
# 1 + 3 = 2 + 2

# Test Case 2

# Input:
# [1, 2, 3]

# Output:
# No Equilibrium Index Found

# ---



n = int(input("Enter Length of List: "))
l = []
for i in range(1,n+1):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
print(l)


n1 = len(l)
n2 = n1//2
sum1 = 0
sum2 = 0
for j in range(n2):
    sum1+=1

for k in range(n1-n2+1,n1):
    sum2+=l[k]


if sum1 == sum2:
    print("Equilibrium Index: ",n2)
else:
    print("No Equilibrium Index Found")

# ====================================================================
# 6. Product Except Self
# ======================

# Scenario

# For every element, calculate the product of all other elements except itself.

# Requirements

# * Read N and list elements from user
# * Create a new list containing products
# * Display the result

# Test Case 1

# Input:
# [1, 2, 3, 4]

# Output:
# [24, 12, 8, 6]

# Test Case 2

# Input:
# [2, 3, 5]

# Output:
# [15, 10, 6]

# ---




n = int(input("Enter Length of List: "))
l = []
for i in range(1,n+1):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
print(l)

l1 = []
for j in range(n):
    pro = 1
    for k in range(n):
        if l[j] != l[k]:
            pro *= l[k]
    l1.append(pro)


print(l1)





# ====================================================================
# 7. Array Rotation Analyzer
# ==========================

# Scenario

# Rotate the array K times towards the right.

# Requirements

# * Read N and list elements from user
# * Read K
# * Rotate the array
# * Display rotated array

# Test Case 1

# Input:
# Array = [1, 2, 3, 4, 5]
# K = 2

# Output:
# [4, 5, 1, 2, 3]

# Test Case 2

# Input:
# Array = [10, 20, 30, 40]
# K = 1

# Output:
# [40, 10, 20, 30]

# ---



n = int(input("Enter Length of List: "))
l = []
for i in range(1,n+1):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
print(l)
num = int(input("Enter Rotate Number: "))



l1 = []
count = 0
for j in range(len(l)-num,len(l)):
    l1.append(l[j])
    count +=1
    if count == num:
        for k in range(len(l)-num):
            l1.append(l[k])



print(l1)


# 
# ====================================================================
# 8. Majority Element Detector
# ============================
# 
# Scenario
# 
# Find an element occurring more than N/2 times.
# 
# Requirements
# 
# * Read N and list elements from user
# * Find majority element
# * If not present, display appropriate message
# 
# Test Case 1
# 
# Input:
# [2, 2, 1, 2, 3, 2, 2]
# 
# Output:
# Majority Element = 2
# 
# Test Case 2
# 
# Input:
# [1, 2, 3, 4]
# 
# Output:
# No Majority Element Found
# 
# ---
# 
# 



# # ====================================================================
# # 9. Happy Number List Analyzer
# # =============================

# # Scenario

# # Store numbers in a list and identify Happy Numbers.

# # A number is called Happy if repeatedly replacing it by the sum of squares of its digits eventually becomes 1.

# # Example

# # 19

# # 1² + 9² = 82

# # 8² + 2² = 68

# # 6² + 8² = 100

# # 1² + 0² + 0² = 1

# # Therefore, 19 is a Happy Number.

# # Another Example

# # 7

# # 7² = 49

# # 4² + 9² = 97

# # 9² + 7² = 130

# # 1² + 3² + 0² = 10

# # 1² + 0² = 1

# # Therefore, 7 is a Happy Number.

# # Non-Happy Number Example

# # 4

# # 4² = 16

# # 1² + 6² = 37

# # 3² + 7² = 58

# # 5² + 8² = 89

# # 8² + 9² = 145

# # 1² + 4² + 5² = 42

# # 4² + 2² = 20

# # 2² + 0² = 4

# # Again 4 appears and the cycle repeats.

# # Therefore, 4 is NOT a Happy Number.

# # Requirements

# # * Read N and list elements from user
# # * Find all Happy Numbers
# # * Store Happy Numbers in another list
# # * Count Happy Numbers
# # * Find Largest Happy Number
# # * Display Happy Number List

# # Test Case 1

# # Input:
# # [19, 7, 4, 20]

# # Output:
# # Happy Numbers = [19, 7]
# # Count = 2
# # Largest Happy Number = 19

# # Test Case 2

# # Input:
# # [13, 10, 4]

# # Output:
# # Happy Numbers = [13, 10]
# # Count = 2
# # Largest Happy Number = 13

# # Test Case 3

# # Input:
# # [2, 3, 4]

# # Output:
# # Happy Numbers = []
# # Count = 0
# # Largest Happy Number = Not Available

# # ---





n = int(input("Enter Length of List: "))
l = []
for i in range(1,n+1):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)



l2 = []
for i in l:
    se1 = set()
    num = i
    while num != 1 and num not in se1:
        se1.add(num)

        total = 0 
        temp = num

        while temp > 0:
            num1 = temp%10
            total += num1**2
            temp = temp//10
        num = total            



    if num == 1:
        l2.append(i)
    
if len(l2) > 0:
    l3 = l2[0]
    for d in l2:
        if d > l3:
            l3 = d
    



if len(l2) >0:
    print("Happy Numbers: ",l2)
    print("Count: ",len(l2))
    print("Largest Happy Number: ",l3)

else:
    print("Their Is no happy Number")
    print("Count: ",0)
    print("Largest Happy Number: Not Available")







n = int(input("Enter Length of List: "))
l = []
for i in range(1,n+1):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
print(l)


sorted(l)

major = []
value = []
for j in l:
    count = 0
    if j not in value:
        for k in l:
            if j == k:
                count+=1
        major.append(count)
        value.append(j)



flag = 0
p1 = major[0]
for p in major:
    if p >= p1:
        p1 = p




vi = major.index(p1)
print("Majority Element Found: ",value[vi])



# ---

# ====================================================================
# 10. Find Duplicate Numbers
# ==========================

# Scenario

# A company stores employee IDs in a list. Some IDs may appear more than once due to data entry errors.

# Requirements

# * Read N and list elements from user
# * Find all duplicate numbers
# * Store duplicates in another list
# * Count total duplicate numbers
# * Display duplicates in sorted order

# Test Case 1

# Input:
# [1, 2, 3, 2, 4, 5, 1]

# Output:
# Duplicate Numbers = [1, 2]
# Count = 2

# Test Case 2

# Input:
# [10, 20, 30]

# Output:
# No Duplicate Numbers Found

# ---


n = int(input("Enter Length of List: "))
l = []
for i in range(1,n+1):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
print(l)



duplicate = []
for i in l:
    count = 0
    for j in l:
        if i == j:
            count+=1
            if i not in duplicate and count > 1:
                duplicate.append(i)

print("uplicate Numbers: ",duplicate)
print("count: ",len(duplicate))



