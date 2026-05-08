
# 1. Hello & Name Printer
# Write a program to print:
# Hello
# Your Name
print("==============1================")
print("Hello \nHitesh Thakur")


# 2. Menu Display
# Write a program to display:
# === Welcome to Coffee Shop ===
# 1. Espresso     $3
# 2. Latte        $4
# 3. Cappuccino   $5
# ==============================

print("==============2================")
print('''=== Welcome to Coffee Shop ==== 

1. Espresso     $3
2. Latte        $4
3. Cappuccino   $5
=============Thankyou=================
''')


# 3. Resume Format
# Write a program to display:
# === Resume ===
# Name       : Alice Johnson
# Email      : alice@example.com
# Skills     :
#   - Java
#   - HTML & CSS
#   - Problem Solving
# Experience : 2 years at XYZ Ltd.
print("==============3================")
print('''
=== Resume ===
Name       : Alice Johnson
Email      : alice@example.com
Skills     :
  - Java
  - HTML & CSS
  - Problem Solving
 Experience : 2 years at XYZ Ltd.''')





# 4. Star Pattern(without loop)
# Write a program to print:
# *****
# *****
# *****
print("==============4================")
print('*****\n*****\n*****')



# 5. Special Characters
# Write a program to print:
# @ # $ % ^ & *

print("==============5================")
print("@ # $ % ^ & *")



# Print User Details
# Take input:
# - Name
# - Age
# - City
# Display them properly.
print("==============6================")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")

print(f"Your Name is {name} and your are {age} year old , address {address}")



# 7. Full Name Display
# Take first name and last name as input and display:
# Full Name: John Doe
print("==============7================")

name1 = input("Enter your first name: ")
lastname = input("Enter your last name: ")
print(f"Full Name : {name1}{lastname}")





# 8. Simple Input Display
# Take two numbers as input and print them on separate lines.
print("==============8================")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("First number: ",num1)
print("Second number: ",num2)



# 9. Three Inputs Display
# Take three values from user and print each on new line.
print("==============9================")

num3 = int(input("Enter first number: "))
num4 = int(input("Enter second number: "))
num5 = int(input("Enter third number: "))
print("First number: ",num3)
print("Second number: ",num4)
print("Third number: ",num5)


# 10. Input and Echo
# Take input from user and print:
# You entered: <input>

print("==============10================")

value = input("Enter anything : ")
print("You entered: ",value)


# 11. Greeting Message
# Take name as input and print:
# Hello <name>
# Welcome to Python
print("==============11================")


name2 = input("Enter your name: ")
print("Hello ",name2)
print("Welcome to Python")


# 12. Favorite Things
# Take input:
# - Favorite food
# - Favorite color
# Display:
# I like <food> and my favorite color is <color>
print("==============12================")

food = input("Enter your Favorite Food: ")
color = input("Enter your Favorite Color: ")
print(f"I like {food} and my favorite color is {color}")


# 13. College Details
# Take input:
# - College Name
# - Course
# - Year
# Display in proper format.
print("==============13================")


cname = input("Enter your college name: ")
coname = input("Which course: ")
year = input("Enter your college year name: ")

print(f"Your College name is {cname} and course {coname} you are in {year}")




# 14. Email Display
# Take email as input and print:
# Your email is: <email>
print("==============14================")


ename = input("Enter your Email: ")
print("Your email is : ",ename)


# 15. Bio Data
# Take input:
# - Name
# - Age
# - Phone
# Display:
# --- Bio Data ---
# Name  :
# Age   :
# Phone :
print("==============15================")


name3 = input("Enter your name: ")
age = int(input("Enter your age: "))
phone = input("Enter your Phone number: ")

print(" --- Bio Data --- ")
print(f'''Name  : {name3}
Age   : {age}
Phone : {phone}''')

print("==============THANKYOUR================")