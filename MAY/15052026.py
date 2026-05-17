# 1.Vowel Counter in Customer Feedback

#  A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

# Input: Enter feedback message: Hello Customer Service

# Output: Total vowels: 8



num = input("Enter Value: ")
num.lower()
count=0
for s in num:
    if s == "a" or s== 'e' or s== "i" or s== "o" or s== "u":
        count+=1
    
print("Total vowels: ",count)




# 2.
# Space Counter in Chat Messages

# A chat application wants to calculate how many spaces are used in a message.

# Input: Enter chat message: Good morning everyone how are you

# Output: Total spaces: 5


char = input("Enter Value: ")
count=0
for s in char:
    if s==" ":
        count+=1



print("Total Spaces: ",count)






# 3.
# Character Occurrence Checker in Product Review

# An e-commerce website wants to know how many times a particular character appears in a product review.

# Input: Enter product review: this product is really good Enter character to check: o

# Output: Character 'o' occurs: 4 times

char = input("Enter: ")
char.lower()
count=0
for i in char:
    if i =="o":
        count+=1


print(f"Character 'o' occurs: {count} Times")


# 4.
# Consonant Counter in Student Name Record

# A school management system wants to count how many consonants are present in student names.

# Input: Enter student name: Ajay Singh Thakur

# Output: Total consonants: 11

# NOTE:

# Ignore case sensitivity (treat A and a same)
# Consider only English alphabets for vowel/consonant counting
# Vowels: A, E, I, O, U



char = input("Enter Student Name: ")
char.lower()

count=0

for s in char:
    if s == "a" or s== 'e' or s== "i" or s== "o" or s== "u":
        pass
    elif s==" ":
        pass
    else:
        count+=1

print("Total Consonants: ",count)



# 5.
# Advanced Password Security Checker

# A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

# Conditions: Password must:

# Start with an uppercase letter
# End with a digit
# Contain at least 2 digits
# Contain at least 1 special character (@ # $ % & *)
# Must not contain spaces
# Length should be between 8 and 15 characters

# Input: Enter password: Python@45

# Output: Secure Password


char = input("Entert PassWord: ")


upper=0
count=0
space=0
special=0
count1=0
last=0

leng = len(char)
leng= leng-1
if 8 <= leng <=15:
    for i in char:
        if i >= "0" and i <="9":
            count+=1
        elif i==" ":
            space=1
        elif i >= "A" and i <= "Z" or i >= "a" and i <="z":
            pass
        else:
            special=1
if char[leng]>="0" and char[leng]<="9":
    last=1

if char[0] >= "A" and char[0] <="Z":
    upper=1


if upper == 1 and count>=2 and special==1 and last==1 and space==0 :
    print("Secure Password")
else:
    print("Weak PassWord")





# 6.
# Railway Ticket PNR Analyzer

# A railway department wants to verify whether a PNR number is valid.

# Conditions:
# - PNR must start with "PNR"
# - Total length should be 12 characters
# - Remaining characters should be digits

# Input:
# Enter PNR: PNR123456789

# Output:
# Valid PNR Number


pnr = input("Enter PNR: ").lower()
pnr1=0
pnr2=0
pnr3=0


if len(pnr)==12:
    if pnr[0:3]=="pnr":
        pnr2=1
        for i in pnr:
            if i >="0" and i<="9":
                pnr1=1
            else:
                if i >="a" and i<="z":
                    pnr3+=1

if pnr2 == 1 and pnr1 == 1 and pnr3==3:
    print("Valid PNR Number")
else:
    print("Invalid PNR")



# 7.
# Vehicle Number Plate Checker

# The traffic department wants to validate vehicle registration numbers.

# Conditions:
# - First 2 characters should be alphabets
# - Next 2 should be digits
# - Total length should be 10

# Input:
# Enter vehicle number: MP04AB1234

# Output:
# Valid Vehicle Number





char = input("Enter Vehicle Number: ").lower()

num=0
num1=0
num2=0
num3=0
if len(char)==10:
    if char[0]>="a" and char[0]<="z" and char[1]>="a" and char[1]<="z":
        num=1


    if char[2] >="0" and char[2]<="9" and char[3] >="0" and char[3]<="9":
        num1 = 1

    if char[4]>="a" and char[4]<="z" and char[5]>="a" and char[5]<="z":
        num2=1


    for j in range(5,9):
        if char[j] >= "0" and char[j] <="9":
            num3+=1
else:
    print("Wrong num")


if num == 1 and num2 ==1 and num1==1 and num3==3:
    print("Valid Vehicle Number")
else:
    print("InValid Vehicle Number")



