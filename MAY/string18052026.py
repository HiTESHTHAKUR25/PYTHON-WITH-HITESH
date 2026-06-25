# 1.
# Email Username Validator

# A company wants to check whether an employee email username is valid before creating an official account.

# Conditions:
# - Username should start with a letter
# - Username can contain letters, digits, underscore (_)
# - No spaces allowed
# - Length should be between 5 and 12 characters

# Input:
# Enter username: ajay_123

# Output:
# Valid Username



str = input("Enter: ").lower()
n = len(str)
n1 = str[0]
count=0
count1=0


if n >= 5 and n <= 15:
    if n1 >= "a" and n1 <= "z":
        for i in str:
            if i == " ":
                print("Invalid Username")
                break
            elif i >= "0" and i <= "9":
                count+=1
            elif i == "_":
                count1+=1
            else:
                pass


if count>=1 and count1>=1:
    print("Valid User")
else:
    print("Invalid User")
            





# 2.
# Mobile Number Digit Counter

# A telecom company wants to count how many digits are present in a customer contact number entered with spaces or symbols.

# Input:
# Enter contact number: +91 98765-43210

# Output:
# Total digits: 12



str = input("Enter: ")
count=0
for i in str:
    if i >= "0" and i <= "9":
        count+=1
    

print("Total Digits: ",count)



# 3.
# Word Counter in Complaint Message

# A customer care system wants to count how many words are present in a complaint message.

# Input:
# Enter complaint: Delivery was delayed again today

# Output:
# Total words: 5


str = input("Enter: ").lower()
n = len(str)
count=0
str = str.rstrip()

for i in range(0,n):
    if str[i] == " ":
        if str[i+1] >= "a" and str[i+1] <= "z":
            count+=1

print("Total Words: ",count+1)




# 4.
# Employee ID Validator

# A company wants to validate employee IDs before storing them in the database.

# Conditions:
# - ID must start with "EMP"
# - Total length should be 8
# - Remaining characters should be digits only

# Input:
# Enter Employee ID: EMP10234

# Output:
# Valid Employee ID

str = input("Enter: ").lower()
n= len(str)
count=0
if n == 8:
    for i in range(0,n):
        if str[0] =="e" or str[1] == "m" or str[2]=="p":
            count+=1
        elif i >="0" and i<="9":
            count+=1

if count==n:
    print("Valid Employee ID")
else:
    print("Invalid User ID")




# 5.
# Palindrome Product Code Checker

# A factory wants to identify whether a product code reads the same forward and backward.

# Input:
# Enter product code: MADAM

# Output:
# Palindrome Code

# Input:
# Enter product code: PRODUCT

# Output:
# Not a Palindrome Code




str = input("Enter: ")

rev = ""

for i in range(len(str)-1,-1,-1):
    rev = rev+str[i]


if rev==str:
    print("Plindrom")
else:
    print("Not Plindrom")



# 6.

# Product Code Verification System

# An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

# Conditions:
# - Ignore spaces
# - Ignore case sensitivity

# Input:
# Enter first product code: Dormitory
# Enter second product code: Dirty Room

# Output:
# Both Product Codes are Matching




str1 = input("Enter First Product Number: ").lower()
str2 = input("Enter Second Product Number: ").lower()
str3=""
str4=""
count=0

for i in str1:
    if i!=" ":
        str3=str3+i

for j in str2:
    if j!=" ":
        str4 = str4+j

if len(str3)==len(str4):       
    for l in str3:
        if l in str3:
            count+=1
    

if count==len(str3):
    print("Both Product Codes Are Matching")
else:
    print("Product Codes Are Not Matching")







# 7.
# Smart City Citizen Information Formatter

# The Smart City Management Department is developing a digital portal to store citizen information in a professional format. Many citizens enter their details using small letters, uppercase letters, mixed casing, or numbers, which creates problems while generating official documents like ID cards, electricity bills, tax records, certificates, and address proofs.

# To solve this issue, the department wants a program that automatically converts only the first character of every word into uppercase while keeping the remaining characters unchanged.

# The input may contain:
# - Words already written in uppercase
# - Mixed-case words
# - Numbers
# - Address details
# - Department names
# - City names

# Task:
# Read a complete string from the user and convert the first character of every word into uppercase.

# Conditions:
# - Words may contain spaces between them
# - Do not use built-in title() function
# - Digits should remain unchanged

# Input:
# Enter citizen information:
# deepika padukone from smart city raisen madhya pradesh

# Output:
# Formatted Information:
# Deepika Padukone From Smart City Raisen Madhya Pradesh


# Test Case 2:
# Input:
# Enter citizen information:
# DEEPIKA pADukone ward number 12

# Output:
# Formatted Information:
# DEEPIKA PADukone Ward Number 12


# Test Case 3:
# Input:
# Enter citizen information:
# government engineering college bhopal zone 3

# Output:
# Formatted Information:
# Government Engineering College Bhopal Zone 3


# Test Case 4:
# Input:
# Enter citizen information:
# python FULL stack developer batch 18

# Output:
# Formatted Information:
# Python FULL Stack Developer Batch 18


strg = input("Enter Citizen Information: ")
n = len(strg)
result=""

i = 0 
while i < n:
    if strg[i] == strg[0] and strg[0] != " " and strg[0] >= "a" and strg[0] <= "z":
        upper = ord(strg[0])-32
        result = result + chr(upper)
    elif strg[i-1] == " ":
        if strg[i] >= "a" and strg[i] <= "z":
            upper = ord(strg[i])-32
            result = result+chr(upper)
    else:
        result = result+strg[i]
    i+=1



print(result)






# 8.
# Airport Passenger Name Formatting System

# An international airport is developing an automated passenger management system. Many passengers enter their details in different formats such as lowercase, uppercase, mixed-case letters, and numbers while booking flight tickets online.

# Due to inconsistent formatting, problems occur while generating boarding passes, security verification records, and passenger identity reports.

# To solve this issue, the airport authority wants a program that automatically converts only the first character of every word into uppercase while keeping all remaining characters unchanged.

# The input may contain:
# - Passenger names
# - Passport details
# - Terminal names
# - Seat numbers
# - City names
# - Mixed uppercase/lowercase letters
# - Digits

# Task:
# Read a complete string from the user and convert the first character of every word into uppercase.

# Conditions:
# - Words may contain spaces
# - Digits should remain unchanged
# - Do not use built-in title() function

# Input:
# Enter passenger details:
# deepika padukone flight ai202 terminal 3 mumbai

# Output:
# Formatted Details:
# Deepika Padukone Flight Ai202 Terminal 3 Mumbai


# Test Case 2:
# Input:
# Enter passenger details:
# DEEPIKA pADukone gate number 12

# Output:
# Formatted Details:
# DEEPIKA PADukone Gate Number 12


# Test Case 3:
# Input:
# Enter passenger details:
# international departure terminal delhi airport

# Output:
# Formatted Details:
# International Departure Terminal Delhi Airport


# Test Case 4:
# Input:
# Enter passenger details:
# business class passenger seat b12

# Output:
# Formatted Details:
# Business Class Passenger Seat B12



str = input("Enter Passenger Details: ")
n  = len(str)
result = ""



for i in range(0,n):
    if str[i] == str[0] and str[i] >= "a" and str[i] <= "z":
        upper = ord(str[i])-32
        result = result+chr(upper)
    elif str[i-1] == " ":
        if str[i] >= "a" and str[i] <= "z":
            upper = ord(str[i])-32
            result = result+chr(upper)
    else:
        result = result+str[i]


print(result)
     



