# NOTE: in all the programs read length and array elements from user
# =====================================================================
# 1.Student Marks Management
# Create a program to store student marks in a List and perform operations.

# Requirements:

# Add student marks into a List
# Display all marks
# Find highest and lowest marks
# Count students who scored above 75

# Test Cases:

# Input: [45, 67, 89, 90, 76] → Highest = 90, Lowest = 45, Count Above 75 = 3
# Input: [10, 20, 30] → Highest = 30, Lowest = 10, Count Above 75 = 0
# Input: [100, 99, 98] → Highest = 100, Lowest = 98, Count Above 75 = 3



n = int(input("Enter Size of Subject: "))
marks = []
for i in range(1,n+1):
    n1 = int(input(f"Enter {i} Marks"))
    marks.append(n1)

count=0
s1 = marks[0]
for j in marks:
    if j > s1:
        s1 = j
        if j > 75:
            count+=1

s2 = marks[0]
for k in marks:
    if k < s2:
        s2 = k



print(f"Heighest: {s1} , Lowerst: {s2} , Above 75: {count}")





# 2.Employee Salary Processing
# Store employee salaries in a List and calculate details.

# Requirements:

# Store salaries
# Find average salary
# Display salaries greater than average
# Remove salaries below 15000

# Test Cases:

# Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
# Input: [15000, 15000, 15000] → Average = 15000
# Input: [5000, 7000] → Remaining List = []




n = int(input("Enter Size of Employee: "))
salary = []
for i in range(1,n+1):
    n1 = int(input(f"Enter {i} Employee Salary: "))
    salary.append(n1)


sum = 0
for j in salary:
    sum += j
average = sum / len(salary)


above = []
for k in salary:
    if average < k:
        above.append(k)


for l in above:
    if l < 15000:
        above.remove(l)   

print(f"{salary} -> Average = {average} , Above Average: {above}")



# 3.
# # Assignment: Prime Number Analyzer using List (Python)

# ## Scenario

# A coaching institute stores student lucky numbers in a Python List.
# Your task is to analyze the list and identify prime numbers for a scholarship selection process.

# You must iterate through every element of the list and perform prime number analysis.

# ---

# # Requirements

# Write a Python program to:

# 1. Store integer values in a List
# 2. Iterate through all elements of the List
# 3. Check whether each number is prime or not
# 4. Display all prime numbers
# 5. Count total prime numbers
# 6. Count total non-prime numbers
# 7. Find the largest prime number from the List
# 8. Store all prime numbers into another List
# 9. Sort the prime numbers in ascending order and display them

# ---

# # Test Case 1

# ## Input

# [2, 3, 4, 5, 6, 7, 8]

# ## Expected Output

# Prime Numbers: 2 3 5 7
# Prime Count: 4
# Non-Prime Count: 3
# Largest Prime Number: 7
# Prime List: [2, 3, 5, 7]
# Sorted Prime List: [2, 3, 5, 7]

# ---

# # Test Case 2

# ## Input

# [10, 11, 12, 13, 14, 15]

# ## Expected Output

# Prime Numbers: 11 13
# Prime Count: 2
# Non-Prime Count: 4
# Largest Prime Number: 13
# Prime List: [11, 13]
# Sorted Prime List: [11, 13]

# ---

# # Test Case 3

# ## Input

# [1, 2, 17, 19, 20, 25]

# ## Expected Output

# Prime Numbers: 2 17 19
# Prime Count: 3
# Non-Prime Count: 3
# Largest Prime Number: 19
# Prime List: [2, 17, 19]
# Sorted Prime List: [2, 17, 19]

# ---

# # Test Case 4

# ## Input

# [4, 6, 8, 9, 10]

# ## Expected Output

# Prime Numbers: None
# Prime Count: 0
# Non-Prime Count: 5
# Largest Prime Number: Not Available
# Prime List: []
# Sorted Prime List: []

# ---

# # Test Case 5

# ## Input

# [29, 31, 37, 41]

# ## Expected Output

# Prime Numbers: 29 31 37 41
# Prime Count: 4
# Non-Prime Count: 0
# Largest Prime Number: 41
# Prime List: [29, 31, 37, 41]
# Sorted Prime List: [29, 31, 37, 41]

# ---







n = int(input("Enter Size of Number: "))
l = []
for i in range(1,n+1):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)


prime = []
primecount=0
nonprime = []
nonprimecount=0

for j in range(len(l)):
    count = 0
    for k in range(2, int(l[j]**0.5) + 1):
        if l[j] % k == 0:
            count += 1
            break

    if count >= 1 or l[j] <= 1:
        nonprime.append(l[j])
        nonprimecount += 1
    else:
        prime.append(l[j])
        primecount += 1

p1 = prime[0]
p2 = []
for l in prime:
    if l > p1:
        p1 = l
        p2.append(l)





print("Prime Number is: ",prime)
print("Prime Count: ",primecount)
print("Nonprime count: ",nonprimecount)
print("Largest Prime Number: ",p1)
print("Prime Number in Sort Form: ",sorted(prime))





# 4.
# Palindrome Number List Checker
# Scenario

# A system checks lucky numbers which are palindromes.

# Requirements
# Check palindrome numbers
# Store palindrome numbers in list
# Count palindrome numbers
# Find largest palindrome
# Sort palindrome list
# Test Cases

# Input:
# [121, 131, 20, 44, 55, 100]

# Output:

# Palindromes: [121, 131, 44, 55]
# Count: 4
# Largest: 131
# Sorted: [44, 55, 121, 131]





n = int(input("Enter Size of Number: "))
l = []
for i in range(1,n+1):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)


pilindrome = []
count = 0
for i in l:
    s = str(i)
    if s == s[::-1]:
        count+=1
        pilindrome.append(i)


s2 = pilindrome[0]
for k in pilindrome:
    if k > s2:
        s2 = k





print("Palindromes: ",pilindrome)
print("Count",count)
print("Largest Pilindrome: ",s2)
print("Sorted Pilindrome: ",sorted(pilindrome))




# 5.
#  Student Grade Classification System (Python List Assignment)
# 
# 
# A school stores student marks in a list. The system must analyze the marks and generate a **clear performance report** 
# by grouping students into grade categories.
# 
# 
# 
# Write a Python program to:
# 
# * Iterate through the list of marks
# * Assign grades based on marks:
# 
#   * **>= 90 → A**
#   * **>= 75 and < 90 → B**
#   * **>= 50 and < 75 → C**
#   * **< 50 → Fail**
# * Store each category in separate lists
# * Count students in each category
# * Display a **final structured report (important)**
# 
# ---
# 
# 📌 Output Format (Mandatory)
# 
# Your output must be displayed exactly in this format:
# 
# ```
# ===== STUDENT GRADE REPORT =====
# 
# A Grade Students   : [list]
# B Grade Students   : [list]
# C Grade Students   : [list]
# Fail Students      : [list]
# 
# --------------------------------
# A Count   : X
# B Count   : X
# C Count   : X
# Fail Count: X
# --------------------------------
# 
# Total Students: X
# ```
# 
# ---
# 
#  Input
# 
# [95, 82, 67, 45, 30]
# 
# Output
# 
# ```
# ===== STUDENT GRADE REPORT =====
# 
# A Grade Students   : [95]
# B Grade Students   : [82]
# C Grade Students   : [67]
# Fail Students      : [45, 30]
# 
# --------------------------------
# A Count   : 1
# B Count   : 1
# C Count   : 1
# Fail Count: 2
# --------------------------------
# 
# Total Students: 5
# 
# 
# 
# 
# 
# 



#   * **>= 90 → A**
#   * **>= 75 and < 90 → B**
#   * **>= 50 and < 75 → C**
#   * **< 50 → Fail**
# * Store each category in separate lists
# * Count students in each category
# * Display a **final structured report (important)**

# ===== STUDENT GRADE REPORT =====
# 
# A Grade Students   : [95]
# B Grade Students   : [82]
# C Grade Students   : [67]
# Fail Students      : [45, 30]
# 
# --------------------------------
# A Count   : 1
# B Count   : 1
# C Count   : 1
# Fail Count: 2
# --------------------------------
# 
# Total Students: 5

n = int(input("Enter Size of Students: "))
l = []
for i in range(1,n+1):
    n1 = int(input(f"Enter {i} Marks: "))
    l.append(n1)
 
a = []
b = []
c = []
fail= []

for i in l:
    if i > 100:
        print("Wrong Marks")
        break
    elif i >= 90:
        a.append(i)
    elif i >= 75:
        b.append(i)
    elif i >= 50:
        c.append(i)
    else:
        fail.append(i)

print("===== STUDENT GRADE REPORT =====")
print()
print("A Grade Students   :",f"  {a}")
print("B Grade Students   :",f"  {b}")
print("C Grade Students   :",f"  {c}")
print("Fail Students      :",f"  {fail}")
print()
print()
print("--------------------------------")
print("A Count   : ",len(a))
print("B Count   : ",len(b))
print("C Count   : ",len(c))
print("Fail Count: ",len(fail))
print(" --------------------------------")
print()
print("Total Students: ",n)





# # 6.
# # 
# #  Frequency Count of Elements (Advanced Scenario-Based Problem)
# # 
# # 
# # A government survey department collects responses from different regions. Each response is stored as an integer in a list (representing selected option IDs).
# # 
# # The department wants to analyze:
# # 
# # * How many times each option was selected
# # * Most popular option
# # * Least popular option
# # * Detect invalid entries (negative numbers or zeros)
# # 
# # ---
# # 
# #  Requirements
# # 
# # Write a Python program to:
# # 
# # 1. Store survey responses in a list
# # 2. Ignore invalid entries (≤ 0)
# # 3. Count frequency of each valid number
# # 4. Display frequency in sorted order
# # 5. Find the most frequently selected option
# # 6. Find the least frequently selected option (excluding invalid data)
# # 7. Store frequency in a dictionary
# # 
# # ---
# # 
# # 
# # NOTE:
# # * Avoid using built-in `Counter`
# # 
# # Input Format
# # 
# # A list of integers representing responses.
# # 
# # ---
# # 
# # Scenario 1: Normal Survey Data
# # 
# # Input
# # 
# # [1, 2, 2, 3, 3, 3, 4, 1, 2]
# # 
# # Output
# # 
# # ```
# # Frequency Count:
# # 1 → 2
# # 2 → 3
# # 3 → 3
# # 4 → 1
# # 
# # Most Frequent: 2 or 3 (tie)
# # Least Frequent: 4
# # ```
# # 
# # ---
# # 
# # Scenario 2: Data with Invalid Entries
# # 
# # Input
# # 
# # [1, 2, -1, 3, 0, 2, 4, -5, 3, 3]
# # 
# # Output
# # 
# # ```
# # Invalid Entries Ignored: [-1, 0, -5]
# # 
# # Frequency Count:
# # 1 → 1
# # 2 → 2
# # 3 → 3
# # 4 → 1
# # 
# # Most Frequent: 3
# # Least Frequent: 1 or 4
# # ```
# # 
# # ---
# # 
# Scenario 3: / Skewed Data
# # 
# # Input
# # 
# # [5, 5, 5, 5, 2, 2, 1]
# # 
# # Output
# # 
# # ```
# # Frequency Count:
# # 1 → 1
# # 2 → 2
# # 5 → 4
# # 
# # Most Frequent: 5
# # Least Frequent: 1
# # ```
# # 
# # ---
# # 
# Scenario 4: All Same Values
# # 
# # Input
# # 
# # [7, 7, 7, 7, 7]
# # 
# # Output
# # 
# # ```
# # Frequency Count:
# # 7 → 5
# # 
# # Most Frequent: 7
# # Least Frequent: 7
# # ```
# # 
# # ---
# # 
# Scenario 5: Empty / Invalid Only Data
# # 
# # Input
# # 
# # [-1, 0, -3]
# # 
# # Output
# # 
# # ```
# # No valid data found
# # ```
# # 
# # ---


# # 1. Store survey responses in a list
# # 2. Ignore invalid entries (≤ 0)
# # 3. Count frequency of each valid number
# # 4. Display frequency in sorted order
# # 5. Find the most frequently selected option
# # 6. Find the least frequently selected option (excluding invalid data)
# # 7. Store frequency in a dictionary



n = int(input("Enter Size of Srvey: "))
l = []
for i in range(1,n+1):
    n1 = int(input(f"Enter {i} Survey Responses: "))
    if n1 > 0:
        l.append(n1)



l = sorted(l)
l2 = []
l3 = []
for i in l:
    count=0
    for j in l:
        if i == j:
            count+=1
    if i not in l2:
        print(i ,"->", count)
        l3.append(count)
        l2.append(i)

data = {}
for l in range(len(l2)):
    data[l2[l]] = l3[l]



d1 = l3[0]
for d in l3:
    if d > d1:
        d1 = d

a1 = l3[0]
for a in l3:
    if a < a1:
        a1 = a


print(l2)
print(l3)


d3 = l2.index(d1)
d4 = l2.index(a1)


print("Most Frequent: ",l3[d3])
print("Least Frequent: ",l3[d4])




