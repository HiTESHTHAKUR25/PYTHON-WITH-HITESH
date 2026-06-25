# 1.

# =========================================
# ONLINE SHOPPING CART
# ====================

# A shopping website stores purchased products in a dictionary where:
# Key = Product Name
# Value = Quantity Purchased

# Write a program to:

# * Accept a dictionary from the user.
# * Calculate and display the total quantity of products purchased.

# Sample Input:
# {"Laptop":2,"Mouse":3,"Keyboard":1}

# Sample Output:
# Total Quantity = 6


dic = {"laptop":2,"keyboard":3,"mouse":1}
sum = 0

for k,v in dic.items():
    sum+=v

print(sum)




# 2.

# =========================================
# EMPLOYEE DEPARTMENT COUNT
# =========================

# A company stores employee department names in a list.

# employees = ["HR","IT","HR","Sales","IT","IT","Finance"]

# Write a program to:

# * Count how many employees belong to each department.
# * Store the result in a dictionary.

# Sample Output:
# {'HR': 2, 'IT': 3, 'Sales': 1, 'Finance': 1}

# ---

dic = ["hr","hr","sales","it","it","hr","finance"]
d = {}
for i in dic:
    d[i] = d.get(i,0)+1

print(d)







# 3.

# =========================================
# WEBSITE PAGE VISIT TRACKER
# ==========================

# A website records page visits.

# pages = ["Home","About","Home","Contact","Home","About"]

# Write a program to:

# * Count visits of each page using a dictionary.
# * Display page name and visit count.

# Sample Output:
# Home visited 3 times
# About visited 2 times
# Contact visited 1 time

# ---


pages = ["Home","About","Home","Contact","Home","About"]
d = {}
for visit in pages:
    d[visit] = d.get(visit,0)+1

for k,v in d.items():
    print(k , ": Visited" , v ,": Times")



# 4.

# =========================================
# STUDENT GRADE ANALYSIS
# ======================

# Store student marks in a dictionary.

# students = {
# "Ajay":78,
# "Ravi":92,
# "Neha":85,
# "Aman":65
# }

# Write a program to:

# * Find the student with highest marks.
# * Find the student with lowest marks.

# Sample Output:
# Highest Marks : Ravi 92
# Lowest Marks : Aman 65

# ---

students = {
    "ajay" : 78,
    "ravi" : 92,
    "neha" : 85,
    "aman" : 65
}

large = 0
small = 9999999999999999999999999

for k,v in students.items():
    if v > large:
        large = v
    if small > v:
        small = v
        
print(large)
print(small)



