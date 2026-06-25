# 1.
#  Second Largest Unique Number
# Scenario

# A sports academy stores athlete scores in a list.

# Find the second largest unique score.

# Requirements
# Read N and list elements from user
# Find second largest unique number
# If not available, display a message
# Test Case

# Input:

# [10, 20, 30, 40, 40]

# Output:

# Second Largest = 30


n = int(input("Enter The Size of List: "))
l = []
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
print(l)

l3 = []
for i in l:
    if i not in l3:
        l3.append(i)

s2 = sorted(l3)
print(s2[-2])




# 2.
# Student Pass List Generator (Using List Comprehension)

# A school stores student marks in a list. Generate a new list containing only the marks of students who have passed (marks ≥ 40).

# Requirements
# Read N and marks from user
# Use List Comprehension
# Create Pass List
# Display Pass Count
# Test Case

# Input:

# [25, 40, 55, 78, 30, 90]

# Output:

# Pass List = [40, 55, 78, 90]
# Pass Count = 4




l = [25, 40, 55, 78, 30, 90]

count = 0
b = [i for i in l if i >= 40 ]
print(b)
print(len(b))




# 3.
# A company stores employee salaries in a list. Employees earning less than ₹30,000 receive a ₹5,000 bonus.

# Requirements
# Read N and salaries from user
# Use List Comprehension
# Create Updated Salary List after bonus
# Display updated salaries
# Test Case

# Input:

# [25000, 35000, 28000, 50000]

# Output:

# Updated Salary List = [30000, 35000, 33000, 50000]


l = [25000, 35000, 28000, 50000]



b = [i+5000 if i < 30000 else i for i in l]
print(b)




# 4.

# ====================================================================
#  Warehouse Inventory Multiplication Analyzer
# ====================================================================


# A warehouse stores product quantities in different sections and racks.
# The inventory data is maintained in the form of a matrix.

# Rows represent warehouse sections.
# Columns represent racks.
# Each cell contains the quantity of products stored.

# The warehouse manager wants to display the inventory matrix and find
# the multiplication of all quantities stored in the warehouse.

# Requirements

# * Read number of rows from user
# * Read number of columns from user
# * Read all matrix elements from user
# * Display the complete matrix
# * Find multiplication of all elements
# * Display the final product

# Test Case 1

# Input:

# Rows = 2
# Columns = 3

# Matrix:

# 1 2 3
# 4 5 6

# Output:

# Matrix:

# 1 2 3
# 4 5 6


# Rows = 3
# Columns = 2

# Matrix:

# 2 3
# 4 5
# 1 2

# Output:

# Matrix:

# 2 3
# 4 5
# 1 2

# Multiplication of All Elements = 240

# ------------------------------------------------------------

# Test Case 3

# Input:

# Rows = 2
# Columns = 2

# Matrix:

# 10 2
# 3 1

# Output:

# Matrix:

# 10 2
# 3 1

# Multiplication of All Elements = 60

# ------------------------------------------------------------

# Test Case 4

# Input:

# Rows = 2
# Columns = 2

# Matrix:

# 0 2
# 3 4

# Output:

# Matrix:

# 0 2
# 3 4

# Multiplication of All Elements = 0

# ------------------------------------------------------------

# Additional Requirements

# Also display:

# Total Number of Elements
# Largest Element
# Smallest Element
# Multiplication of All Elements

# Sample Output

# ===== MATRIX REPORT =====

# Matrix:

# 1 2 3
# 4 5 6

# Total Elements            : 6
# Largest Element           : 6
# Smallest Element          : 1
# Multiplication of Elements: 720

# ====================================================================




row = int(input("Enter Number of ROWS: "))
column = int(input("Enter NUmber of COLUMN: "))



mul = 1
matrix = []
large = 0
small = 99999999999999999999999999999

for i in range(row):
    rows = []
    for j in range(column):
        num = (int(input(f"Enter Element Number {[i],[j]}: ")))
        mul *= num 
        if num >= large:
            large = num
        if num <= small:
            small = num
        rows.append(num)
    matrix.append(rows)

for i in matrix:
    for j in i:
        print(j,end=" ")
    print()



print(large)
print(small)
print(mul)





# 5.

# ====================================================================
#  Student Classroom Matrix Analysis
# ====================================================================

# Scenario

# A school stores student marks in a matrix.

# Rows represent different classrooms.
# Columns represent students in each classroom.

# The principal wants to analyze the performance of each classroom by
# calculating the total marks scored by students in every row.

# Requirements

# * Read number of rows from user
# * Read number of columns from user
# * Read all matrix elements from user
# * Display the complete matrix
# * Find Row Wise Sum
# * Display sum of each row separately

# Test Case 1

# Input:

# Rows = 3
# Columns = 3

# Matrix:

# 10 20 30
# 40 50 60
# 70 80 90

# Output:

# Matrix:

# 10 20 30
# 40 50 60
# 70 80 90

# Row 1 Sum = 60
# Row 2 Sum = 150
# Row 3 Sum = 240

# ------------------------------------------------------------

# Test Case 2

# Input:

# Rows = 2
# Columns = 4

# Matrix:

# 1 2 3 4
# 5 6 7 8

# Output:

# Matrix:

# 1 2 3 4
# 5 6 7 8

# Row 1 Sum = 10
# Row 2 Sum = 26

# ------------------------------------------------------------

# Test Case 3

# Input:

# Rows = 2
# Columns = 2

# Matrix:

# 100 200
# 300 400

# Output:

# Matrix:

# 100 200
# 300 400

# Row 1 Sum = 300
# Row 2 Sum = 700

# ------------------------------------------------------------

# Additional Challenge

# Also Display:

# * Row Wise Sum
# * Row Wise Average
# * Row Having Maximum Sum
# * Grand Total of Matrix

# Sample Output

# ===== MATRIX REPORT =====

# Matrix:

# 10 20 30
# 40 50 60
# 70 80 90

# Row 1 Sum = 60
# Row 2 Sum = 150
# Row 3 Sum = 240

# Row 1 Average = 20.0
# Row 2 Average = 50.0
# Row 3 Average = 80.0

# Maximum Sum Row = Row 3
# Grand Total = 450

# ====================================================================




row = int(input("Enter Number of ROWS: "))
column = int(input("Enter NUmber of COLUMN: "))


matrix = []
sum1 = 0
for i in range(row):
    rows = []
    for j in range(column):
        num = (int(input(f"Enter Element Number {[i],[j]}: ")))
        sum1+=num
        rows.append(num)
    matrix.append(rows)


l2 = []
for i in matrix:
    sum = 0
    for j in i:
        sum += j
    l2.append(sum)


for s in range(len(l2)):
    print(f"Row {s+1} Sum: ",l2[s])


for j in range(len(l2)):
    print(f"Row {s+1} Average: ",l2[j]/column)



n1 = l2[0]
count = 0
for i in l2:
    if i > n1:
        n1 = i
        count+=1

print("Maximum Sum Row: rows",count)
print("Grand Total: ",sum1)





