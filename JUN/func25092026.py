from functools import reduce
# Employee Data Processing System

# A company stores information about its employees in two forms:

# A list of employee ages.
# A string containing employee names separated by spaces.

# The HR department wants a Python application that can perform different operations on this data through a menu-driven system. To make the application modular and easy to maintain, each operation must be implemented using a separate function that accepts data as a parameter and returns the result.

# Problem Statement

# Develop a menu-driven Python application called Employee Data Processing System.

# The program should allow the HR department to perform the following operations:

# Functions on Employee Ages (List)
# 1. find_second_highest_age(age_list)
# Accept a list of employee ages.
# Return the second highest age.
# 2. count_senior_employees(age_list)
# Accept a list of employee ages.
# Consider employees aged 50 years or above as senior employees.
# Return the count of senior employees.
# 3. remove_duplicate_ages(age_list)
# Accept a list of employee ages.
# Return a new list after removing duplicate ages while maintaining the original order.
# Functions on Employee Names (String)
# 4. count_names_starting_with_vowel(names)
# Accept a string containing employee names separated by spaces.
# Return the number of names that start with a vowel (A, E, I, O, U).
# 5. longest_name(names)
# Accept a string containing employee names separated by spaces.
# Return the employee name having the maximum number of characters.
# Menu
# ========== EMPLOYEE DATA PROCESSING SYSTEM ==========
# 1. Find Second Highest Employee Age
# 2. Count Senior Employees
# 3. Remove Duplicate Ages
# 4. Count Names Starting with a Vowel
# 5. Find Longest Employee Name
# 6. Exit
# ====================================================
# Enter your choice:
# Sample Input
# Employee Ages:
# 34 55 29 60 55 42 60 51

# Employee Names:
# Ajay Rahul Esha Omkar Ishita Neha
# Sample Output
# Second Highest Age : 55
# Senior Employees : 4
# Unique Ages : [34, 55, 29, 60, 42, 51]
# Names Starting with Vowel : 3
# Longest Employee Name : Ishita
# Instructions
# Implement all operations using separate functions.
# Each function must accept parameters and return the result.
# Do not print results inside the functions.
# The menu should continue to appear until the user selects Exit.
# Display an appropriate message for an invalid choice.
# Use meaningful function and variable names and follow proper indentation

empname = []
empage = []
def empployee():
    emp1 = int(input("How Many Employee In your company: "))
    for i in range(emp1):
        name = input("Enter Employee Name: ")
        empname.append(name)

    for i in range(emp1):
        age = int(input("Enter Employee Age: "))
        empage.append(age)


def age(age1):
    x = sorted(age1)
    return x[-2]


def senior(emp3):
    x1 = filter(lambda x:x > 50 ,emp3)
    return list(x1)


def dupages(dupage):
    x = set(dupage)
    return list(x)

def vowels(name):
    x = filter(lambda x: x.startswith("a") or x.startswith("e"),name)
    return list(x)


def longest(name):
    x = max((name))
    return x
    


    
while True:
    print(''' ========== EMPLOYEE DATA PROCESSING SYSTEM ==========
 1. Find Second Highest Employee Age
 2. Count Senior Employees
 3. Remove Duplicate Ages
 4. Count Names Starting with a Vowel
 5. Find Longest Employee Name
 6. Exit''')
    choose = int(input("Choose a number: "))
    
    match choose:
        case 1:
            empployee()
            print(age(empage))
        case 2:
            print(senior(empage))
        case 3:   
            print(dupages(empage))
        case 4:
            print(vowels(empname))
        case 5:
            print(longest(empname))
        case 6:
            break
            
    