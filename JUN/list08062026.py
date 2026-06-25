# 1.
# =========================================
# STUDENT CLUB MEMBERSHIP SYSTEM
# =========================================

# A college has two clubs:
# 1. Coding Club
# 2. Robotics Club

# Store student IDs of both clubs using sets.

# Menu:
# 1. Add Student to Coding Club
# 2. Add Student to Robotics Club
# 3. Display Students in Coding Club
# 4. Display Students in Robotics Club
# 5. Find Students in Both Clubs
# 6. Find Students Only in Coding Club
# 7. Find Students Only in Robotics Club
# 8. Display All Unique Club Members
# 9. Display Total Unique Club Members
# 10. Exit

# Requirements:
# - Use two sets.
# - Apply intersection, difference, and union operations.



coding = set()
robotics = set()

num1 = int(input("Enter Number of Student in Coding Club: "))
for i in range(num1):
    id = int(input(f"Enter {i+1} Student ID: "))
    coding.add(id)



num2 = int(input("Enter Number of Student in Robotics Club: "))
for i in range(num2):
    id = int(input(f"Enter {i+1} Student ID: "))
    robotics.add(id)


print("Coding club Students ID's: ",coding)
print("Robotics Club Students ID's: ",robotics)


print("Who Have in both Clubs: ",coding&robotics)

print("Only Coding Club: ",coding-robotics)

print("Only Robotics Club: ",robotics-coding)

print("All unic Club Member: ",coding.union(robotics))

print("All unic Club Member: ",len(list(coding.union(robotics))))






# 2.
# =========================================
# ONLINE COURSE ENROLLMENT SYSTEM
# =========================================

# An institute offers:
# 1. Python Course
# 2. Java Course

# Store enrolled student email IDs using sets.

# Menu:
# 1. Enroll Student in Python
# 2. Enroll Student in Java
# 3. Display Python Students
# 4. Display Java Students
# 5. Find Students Enrolled in Both Courses
# 6. Find Students Enrolled Only in Python
# 7. Find Students Enrolled Only in Java
# 8. Check Enrollment in Python Course
# 9. Display Total Unique Students
# 10. Exit

# Requirements:
# - Use two sets.
# - Use membership operator (in).
# - Use union, intersection and difference operations.


python = set()
java = set()


while True:
    print(''' Menu:
 1. Enroll Student in Python
 2. Enroll Student in Java
 3. Display Python Students
 4. Display Java Students
 5. Find Students Enrolled in Both Courses
 6. Find Students Enrolled Only in Python
 7. Find Students Enrolled Only in Java
 8. Check Enrollment in Python Course
 9. Display Total Unique Students
 10. Exit''')
    
    choose = int(input("Choose a Number: "))

    match choose:
        case 1:
            id = int(input("Enetr No. of Students Who Enrolled in Python: "))
            for i in range(id):
                mail = input(f"Enetr {i+1} Email: ")
                python.add(mail)

        case 2:
            id = int(input("Enetr No. of Students Who Enrolled in Java: "))
            for i in range(id):
                mail = input(f"Enetr {i+1} Email: ")
                java.add(mail)
        
        case 3:
            print("Those Who Enrolled in Python: ",python)
        
        case 4:
            print("Those Who Enrolled in Java: ",java)

        case 5:
            print("Those Participated in both PYTHON AND JAVA: ",python|java)
        
        case 6:
            print("Only In PYTHON: ",python)
        case 7:
            print("Only in JAVA: ",java-python)
        case 8:
            print(python-java)

        case 9:
            print(len(python|java) - len(python&java))

        case 10:
            break




# 3.
# =========================================
# WEBSITE VISITOR TRACKING SYSTEM
# =========================================

# A website stores unique visitor IDs.

# Menu:
# 1. Add Visitor
# 2. Remove Visitor
# 3. Check Visitor
# 4. Display All Visitors
# 5. Count Unique Visitors
# 6. Clear Visitor Data
# 7. Exit

# Requirements:
# - Use a set to store visitor IDs.
# - Duplicate visitor IDs should not be stored.
# - Use add(), remove(), and membership operations.



visitor = set()
rvisitors  = set()


while True:
    print(''' Menu:
 1. Add Visitor
 2. Remove Visitor
 3. Check Visitor
 4. Display All Visitors
 5. Count Unique Visitors
 6. Clear Visitor Data
 7. Exit
''')
    choose = int(input("Choose a option: "))

    match choose:
        case 1:
            
            num  = (input("Enter Visitor ID: "))
            if num not in visitor:
                visitor.add(num)
        case 2:
            remo = (input("Enetr Remover Visitor ID: "))
            visitor.remove(remo)
            rvisitors.add(remo)
        case 3:
            print("All Visitor ID's")
            print(visitor)
        case 4:
            print("All Unique Visitors: ",visitor)
        case 5:
            print("Total all Visitors Count: ",len(visitor&rvisitors))
        case 6:
            print("Confermation (if you want to clear the visitors than click (yes) other wise (no))")
            chhose = input("Enter What do you Want: ")
            if chhose == "yes":
                visitor.clear()
                print("Thank you ")
            else:
                print("Thank you Your DAta is safe")

        case 7:
            break




# 5.
# =========================================
# LIBRARY ISBN MANAGER
# =========================================

# A library stores unique ISBN numbers of books.

# Menu:
# 1. Add ISBN
# 2. Remove ISBN
# 3. Search ISBN
# 4. Display ISBN List
# 5. Count Books
# 6. Exit

# Requirements:
# - Use Set.
# - Duplicate ISBNs are not allowed.

isbn = set()

while True:
    print(''' Menu:
 1. Add ISBN
 2. Remove ISBN
 3. Search ISBN
 4. Display ISBN List
 5. Count Books
 6. Exit''')
    
    choose = int(input("Choose A option: "))

    match choose:
        case 1:
            num = int(input("Enter ISBN Number: "))
            if num not in isbn:
                isbn.add(num)
                print("Added Successfully")
            else:
                print("This Is Aleready Present in our Library")
        
        case 2:
            remo = int(input("Enter ISBN: "))
            if remo in isbn:
                isbn.remove(remo)
                print("Removed Successfully")
            else:
                print("Wrong ISBN")
        case 3:
            search = int(input("Enter ISBN: "))
            if search in isbn:
                print("It is Present")
            else:
                print("It is not Present")
        case 4:
            print("All ISBN: ",list(isbn))
        case 5:
            print("Total Number of Book: ",len(list(isbn)))
        case 6:
            break



# 6.

# =========================================
# COMMON CHARACTER FINDER
# =========================================

# Enter two strings and find common characters.

# Menu:
# 1. Enter First String
# 2. Enter Second String
# 3. Display Common Characters
# 4. Count Common Characters
# 5. Exit

# Example:
# String1: python
# String2: typhoon

# Output:
# {p, t, h, o, n}


str1 = set()
str2 = set()

while True:
    print(''' Menu:
 1. Enter First String
 2. Enter Second String
 3. Display Common Characters
 4. Count Common Characters
 5. Exit''')
    
    choose = int(input("Choose A Option: "))

    match choose:
        case 1:
            s1 = input("Enter First String: ")
            str1.update(s1)
        case 2:
            s2 = input("Enter Second String: ")
            str2.update(s2)
        case 3:
            print("Common Characters are: ",(str1)&(str2))
        case 4:
            print("Common Characters are: ",len(list(str1&str2)))
        case 5:
            break





# 7.
# =========================================
# MISSING ALPHABET FINDER
# =========================================

# Enter a sentence and find which
# alphabets are missing.

# Menu:
# 1. Enter Sentence
# 2. Display Missing Alphabets
# 3. Count Missing Alphabets
# 4. Exit

# Requirements:
# - Use Set containing a-z.


senatce = set()
count =0
alph = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z'}
while True:
    print(''' Menu:
 1. Enter Sentence
 2. Display Missing Alphabets
 3. Count Missing Alphabets
 4. Exit
''')
    choose = int(input("Choose a Option: "))

    match choose:
        case 1:
            num = input("Enter The Sentance: ")
            senatce.update(num)
        case 2:
            print("Missing Eliments: ",alph-senatce)
        case 3:
            print("Total Missing elements: ",len(list(alph-senatce)))
        case 4:
            break







# 8.
# =========================================
# ALLOWED CHARACTER VALIDATOR
# =========================================

# Allowed characters are:
# A-Z, a-z, 0-9

# Store allowed characters in a Frozen Set.

# Menu:
# 1. Enter Username
# 2. Validate Username
# 3. Display Allowed Characters
# 4. Exit

# Requirements:
# - Use Frozen Set.
# - Username should contain only allowed characters.a



# =========================================
# ALLOWED CHARACTER VALIDATOR (match-case)
# =========================================


char = frozenset("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")

username = ""

while True:
    print("\n--- MENU ---")
    print("1. Enter Username")
    print("2. Validate Username")
    print("3. Display Allowed Characters")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    match choice:
        case 1:
            username = input("Enter Username: ")

        case 2:
            if username == "":
                print("Please enter username first!")
            else:
                is_valid = True

                for ch in username:
                    if ch not in char:
                        is_valid = False
                        break

                if is_valid:
                    print("Valid Username")
                else:
                    print("Invalid Username (Only A-Z, a-z, 0-9 allowed)")

        case 3:
            print("Allowed Characters:")
            print(char)

        case 4:
            print("Exiting program...")
            break

        case _:
            print("Invalid choice")





