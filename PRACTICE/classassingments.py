# ======1==========


num = int(input("Enter Number: "))
sum = 0
sum2 = 0

for i in range(1,num):
    if num%i==0:
        sum = sum+i

i = 1
while i < num:
    for i in range(1,num):
        if num%i==0:
            sum2 = sum2+i
    i+=1



if sum==num:
    print("Aerfect Number by FOR loop")
    if sum2 == num:
        print("Perfect Number by WHILE loop")
else:
    print("Not perfect")


# ============2===========


# WAP TO SKIP EVEN NO. STOP AT 9 AND DO NOTHING FOR 5

for i in range(1,11):
    if i==5:
        pass
    elif i == 9:
        break
    elif i%2==0:
        continue
    else:s = "                abbkjdbkdbvjdsa"
word = "k"
result = ""
result1 = ""
result2 = ""


for j in s:
    if j == word:
        pass
    else:
        result = result + j

for i in range(0,len(result)):
    if result[i-1]==" " and (result[i]>= "a" and result[i]<="z" or result[i] == " ") :
        pass
    else:
        result1 = result1+result[i]

print(result1)    
n = len(result1)
for k in range(len(result1),0,-1):
    if result1[n-1] >= "a" and result1[n-1] <= "z" and k == n:
        pass
    else:
        result2 = result1[k]+result2

    






print(result2)
print(result1)

print(i)
    



# ================3===========

num = [2,4,6,8,10]
tar = 3

for i in num:
    if i == tar:
        print("Banda Mil Gaya")
        break
else:
    print("Banda Not Found")    

# WAP TO CHECK THE NUMBER IS EVEN OR ODD WITHOUT MODULUS OPERATOR

num = int(input("Enter number: "))

if  num&1==0:
    print("Even")
else:
    print('Odd')



# WAP TO SWAP TWO NUMBER WITHOUT 3 VARIABLE


a = int(input("Enter First Numbre: "))
b = int(input("Enter Seconf Numbre: "))

print(a)
print(b)
a=b^a
b = a^b
a= a^b
print(a)
print(b)





# =================?
num = int(input("Enter NUmber: "))
num2 = int(input("Enter NUmber: "))
num3 = int(input("Enter NUmber: "))


result = num if num>num2 and num>num3 else num2 if num2>num3 else num3
print("Max is:",result)




# =========================
num = int(input("Enter NUmber: "))
num2 = int(input("Enter NUmber: "))


print("equal" if num==num2 else "greater" if num>num2 else "small")



# =================


num1 = int(input("Enter First Number: "))
num2 = int(input("Enter First Number: "))
num3 = (input("Operator: "))


match num3:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "/":
        print(num1/num2)
    case "*":
        print(num1*num2)
    case "**":
        print(num1**num2)
    case "//":
        print(num1//num2)
    case "%":
        print(num1%num2)
    case _:
        print("Wrong Operator")




# ===================



while True:
    print("MANU")
    print("1. ADD")
    print("2. SUB")
    print("3. MULTIPlE")
    print("4 Exit")
    
    choice = int(input("Enter: "))
    match choice:
        case 1:
            num1 = int(input("Enter First Number: "))
            num2 = int(input("Enter Second Number: "))
            print("REsult: ",num1+num2)
        case 2:
            num1 = int(input("Enter First Number: "))
            num2 = int(input("Enter Second Number: "))
            print("REsult: ",num1-num2)
        case 3:
            num1 = int(input("Enter First Number: "))
            num2 = int(input("Enter Second Number: "))
            print("REsult: ",num1*num2)
        case 4:
            print("Your are exit ")
            break


# =========================

# WAP TO INPUT TWO NUMBER AND PRINT TABLE BETWEEN THOS NUMBER
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))


for i in range(num1,num2+1):
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}")
    print()



# WAP TO PRINT
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
num = int(input("Enter Numbre: "))

for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# WAP TO PRINT
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
num = int(input("Enter Numbre: "))

i = 1
while i<=num:
    j = 1
    while i>=j:
        print(j,end=" ")
        j+=1
    i+=1
    print()


# WAP TO PRINT
# *
# * *
# * * *
# * * * *
 
num = int(input("Enter Numbre: "))

i = 1
while i<=num:
    j = 1
    while i>=j:
        print("*",end=" ")
        j+=1
    i+=1
    print()


# WAP TO PRINT
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1 
num = int(input("Enter Numbre: "))

i = num
while i>=1:
    j = i
    while j>=1:
        print(j,end=" ")
        j-=1
    i-=1
    print()

# WAP TO PRINT
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 
num = int(input("Enter Numbre: "))

i = num
while i>=1:
    j = 1
    while j<=i:
        print(j,end=" ")
        j+=1
    i-=1
    print()



# WAP TO PRINT
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 


while True:
    print("1. Number Series")
    print("2. *")
    print("3. #")
    print("4. Exit")
    
    num1 = int(input("Choose An Option: "))

    match num1:
        case 1:
            num = int(input("Enter Numbre: "))
            i = num
            while i>=1:
                j = 1
                while j<=i:
                    print(j,end=" ")
                    j+=1
                i-=1
                print()
        case 2:
            num = int(input("Enter Numbre: "))
            i = num
            while i>=1:
                j = 1
                while j<=i:
                    print("*",end=" ")
                    j+=1
                i-=1
                print()
        case 3:
            num = int(input("Enter Numbre: "))
            i = num
            while i>=1:
                j = 1
                while j<=i:
                    print("#",end=" ")
                    j+=1
                i-=1
                print()
        case 4:
            print("Exit System....!")
            break
        case _:
            print("Wrong Option")




# 1
# * *
# 1 2 3 
# * * * *
# 1 2 3 4 5
num = int(input("Enter Number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        if i%2==0:
            print("*",end=" ")
        else:
            print(j,end=" ")
    print()


# 1
# 1 *
# 1 * 2 
# 1 * 2 *
# 1 * 2 * 3 
num = int(input("Enter Number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        if j%2==0:
            print("*",end=" ")
        else:
            print(j,end=" ")
    print()



# 1 
# 2 3
# 4 5 6
# 7 8 9 10


num = int(input("Enter Number: "))
k=1
for i in range(1,num+1):
    for j in range(1,i+1):
        print(k,end=" ")
        k+=1
    print()

# 1***********1
# 12**********21
# 123********321
# 1234******4321
# 12345****54321
# 123456**654321
# 12345677654321



num = int(input("Enter NUmber: "))

for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end="")
        star = 1
    for k in range(1,((num-i)*2)+1):
        print("*",end="")
    l = i
    while l>=1:
        print(l,end="")
        l-=1
            
            
    print()


#  ********** 
#   ********  
#    ******   
#     ****    
#      ** 


num = int(input("Enter NUmber: "))

for i in range(1,num+1):
    for j in range(1,i+1):
        print(" ",end="")
        star = 1
    for k in range(1,((num-i)*2)+1):
        print("*",end="")
    l = i
    while l>=1:
        print(" ",end="")
        l-=1
            
            
    print()

#         1 
#       1 2 
#     1 2 3 
#   1 2 3 4 
# 1 2 3 4 5 

num = int(input("Enter NUmber: "))

for i in range(1,num+1):
    for j in range(1,num-i+1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print()



#         A 
#       A B 
#     A B C 
#   A B C D 
# A B C D E

num = int(input("Enter NUmber: "))

for i in range(1,num+1):
    char=65
    for j in range(1,num-i+1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(chr(char),end=" ")
        char+=1
    print()


s = (input("Enter : "))

if s == s[::-1]:
     print("pelendrom")
else:
     print("not")
    

# 0   h
# 1   i
# 2   t
# 3   e
# 4   s
# 5   h

s = "hitesh"

for i,ch in enumerate(s):
    print(i," ",ch)


str = 'welcomr'
str = str+"a"
print(str)


str= "welcome"
print(id(str))
str = str+ " hitesh"
print(id(str))








a = "hitesh"
print(a)
del a
print(a)



a = "hitesh"
b = a+"w"
print(a)
del a
print(b)


s = "hitesh thakur "

print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.title())
print(s.swapcase())
print(s.find("z"))




s = "hitesh thakur"
print(s.index("a"))
print(s.rindex("t"))
print(s.count("t"))
print(s.count("t"))
print(s.isalpha())
print("hitesh".isalpha())
print("12345678".isdigit())
print(s.isdigit())
print(s.isalnum())
print("12345gfiue".isalnum())
print("12345gHiue".islower())
print(s.islower())
print(s.isupper())
print("HITESH ".isupper())
print(" ".isspace())
print("".isspace())
print(s.isspace())
print(s.istitle())
print("Hello Hitesh".istitle())
print(s.replace("hitesh","akshay"))
print(s.strip())
print("    hitesh    ".strip())
print("  hitesh      ".lstrip())
print("  hitesh      ".rstrip())
print(s.split())
l=(s.split())
print(l[1])
print("hitesh,thakur,thakur".split())
print("hitesh,thakur,thakur".split(",",2))
l2= ["hitehs","thakur","akshay"]
print(" ".join(l2))




# password chacker

s = input("Enter Password: ")
s1 = len(s)
lower=0
upper=0
digit=0
space=0
special=0
count1=0
if 8 <= s1 <=15:
    for s2 in s:
        if s2>= "A" and s2 <="Z":
            lower=1 
        elif s2 >="a" and s2<'z':
            upper=1
        elif s2 >="0" and s2<="9":
            digit=1
        elif s2 == " ":
            space=1
        else:
            special=1
else:
    print("Password Length is Not Setisfy our Condition")
    count1+=1

if count1 != 1:
    if lower==1 and upper==1 and space!=1 and special==1 and digit==1:
        print("Valid PassWord")
    else:
        print("Invalid PassWord")

        
# using predifine method
# while loop



s = input("Enter Password: ")
s1 = len(s)
lower=0
upper=0
digit=0
space=0
special=0
count1=0
if 8 <= s1 <=15:
    for s2 in s:
        if s2.islower():
            lower=1 
        elif s2.isupper():
            upper=1
        elif s2.isdigit():
            digit=1
        elif s2.isspace():
            space=1
        else:
            special=1
else:
    print("Password Length is Not Setisfy our Condition")
    count1+=1

if count1 != 1:
    if lower==1 and upper==1 and space!=1 and special==1 and digit==1:
        print("Valid PassWord")
    else:
        print("Invalid PassWord")


# using predifine method
# while loop




words = ["java","python","is ","easy"]
print(" ".join(words))
str = " ".join(words)
print(type(str))



print("hitesh,thakur,thakur".split(",",2))
print("hitesh,thakur,thakur".split(",",1))
print("hitesh,thakur,thakur".split(",",0))


str  = "python java react ai asree samjha"

result = str.split(" ",2)
result1 = str.rsplit(" ",2)
print(result)
print(result1)




str1="python"
print(str1.center(20))
str2 = str1.center(20)
print(len(str2))
print(str1.center(40,"*"))

print(str1.ljust(20))
print(str1.ljust(20,"*"))
print(str1.rjust(20))
print(str1.rjust(20,"*"))




str = "python"
print(dir(str))
str1 = "python is nice language"
print(str.startswith(str))
print(str.startswith("py"))
print(str.startswith("pyl"))


print(str1.endswith("python"))
print(str1.endswith(str))



#format()

print("HII I am learning {} and {}".format(str,str1))


print("first: {1} , second: {0}".format("java","python"))

print("name id {name} and age {age}".format(name="bahu", age=30))


print(sorted(str))
print(" ".join(sorted(str)))



print(ord("1"))


# forword and backword direction display
str = input("Enter: ")

n = len(str)

print(n)

i = 0 
while i < n:
    print(str[i],end=" ")
    i+=1
print()
i=n-1
while i >= 0:
    print(str[i],end=" ")
    i-=1
print()
i = -1
while i >= -n:
    print(str[i],end=" ")
    i-=1




for i in range(n-1,-1,-1):
    print(str[i],end=" ")




print(ord("a"))
print(ord("1"))
print(ord("A"))
print(chr(36))
print(chr(39))
print(chr(98))






# WAP TO CONVERT FIRST ChARACTER OF AVERY WORD INTO UPPER CASE
str = input("Enter: ")
str1 = str
n = len(str)
result= ""


i = 0
while i <n:
    if i == 0 or str[i-1]==" ":
        upper = ord(str[i])-32
        result = result+chr(upper)
    else:
        result = result+str[i]
    i=i+1
print(result)




# i = 0
# while i <n:
#     if i == 0 or str[i-1]==" ":
#         if i >= "a" and i <= "z":
#             upper = ord(str[i])-32
#             result = result+chr(upper)
#     else:
#         result = result+str[i]
#     i=i+1
# print(result)





words = str.split()

for w in words:
    result = result+w.capitalize()+" "

print(result)


print(str.title())








# WAP TO CHECK TWO STRINGS ARE ANAGRAMS

str = input("Enter: ")
str2 = input("Enter: ")

count=0
if len(str)== len(str2):
    for i in str:
        for k in str2:
            if i == k:
                count+=1
                break

if count== len(str):
    print("ANAGRAM")
else:
    print("Not Anagram")



# SORTED METHOD

if sorted(str) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")


# IN

count1=0
if len(str) == len(str2):
    for i in str:
        if i in str2:
            count1+=1


if count==len(str):
    print("Anagram")
else:
    print("Not Anagram")









s1 = input("Entre First String: ")
s2 = input("Entre Second String: ")


if len(s1)!=len(s2):
    print("String are not Anagrams")
else:

    visited = []
    flag = 1

    i= 0
    while i < len(s1):
        ch = s1[i]

        if ch not in visited:

            c1=0
            c2=0

            j =0
            while j < len(s1):
                if s1[j]==ch:
                    c2 = c2+1
                    j+=1

            if c1 != c2:
                flag=0
                break

            visited.append(ch)


        i = i+1


if flag == 1:
    print("String are Anagram")
else:
    print("String are not Anagram")










#a2b3

s = input("Enter Value: ")

result = ""


for i in s:
    if i.isalpha():
        result = result+i
        previous = i
    else:
        result = result+previous*(int(i)-1)


print(result)

#aabbb




# a3b5
# adbg



s = input("Enter Value: ")

result = ""


for i in s:
    if i.isalpha():
        result = result+i
        previous = i
    else:
        new = chr(ord(previous)+int(i))
        result = result+new


print(result)






# WAP TO REVERS A STRING


s = input("Enter String: ")
rev = ""
n = len(s)-1
for i in range(n,-1,-1):
    rev = rev+s[i]


print(rev)




# WAP TO REVERS A STRING


s = input("Enter String: ")
rev = ""

rev = s[::-1]

print(rev)


# WAP TO REVERS A STRING WORDS

s = input("Enter String: ")

s1 = s.split(" ")
rev = ""

for i in range(len(s1)-1,-1,-1):
    rev = rev+s1[i]+" "

print(rev)




#



s = input("Entre Value: ")

s1 = s.split(" ")
print(" ".join(s1[::-1]))




# WAP TO REVERSE EACH WORD 

s = input("Entre Value: ")

s1 = s.split()
i = 0
while i < len(s1): 
    word = s1[i]
    rev = ""
    j=len(word)-1
    while j >= 0:
        rev = rev+word[j]
        j = j-1
    print(rev,end=" ")
    i = i+1

# WAP TO 

s = input("Entre Value: ")
s1 = s.split()
for i in s1:
    print(s1[::-1],end=" ")



# WAP TO 

s = input("Entre Value: ")
s2 = s[::-1]
s1 = s2.split()
print(" ".join(s1[::-1]))








# STRING REVERSE WITHOUNT SPLIT
s = input("Enter String: ")

word = ""

for i in range(0,len(s)):
    if s[i] != " ":
        word = s[i]+word
    else:
        print(word,end=" ")
        word = ""

print(word)




#  WAP TO REVERSE SENTENCE + EACH WORD


s= input("Entre String: ")
words = s.split()
i = len(words)-1

while i>=0:
    word = words[i]
    rev = ""
    j = len(word)-1
    while j >=0:
        rev = rev+word[j]
        j = j-1
    print(rev,end=" ")
    i = i-1

# H.W.
# RESULT SHOU;LD BE UPDATED IN REAL STRING
# WAP TO FING NUMBER OF UNIC CHARACTER IN A STRING
# WAP TO REMOVE DUPLICATE WORD FROM A STRING



#  WAP TO FIND SHORTEST WORD IN A SENTENCE

s = input("Entre String: ")


s1 = s.split()
s2 = s1[0]

for i in range(1,len(s1)):
    if len(s2) > len(s1[i]):
        s2 = s1[i]

print("Shortest Word: ",s2)


# WAP TO FIND OCCURENCE OF A WORD IN A STRING OUR PROGRAM COUNT HOW MANY TIMES IN A STRING


s = input("Enter String: ")
word = input("Enter What you find in a string: ")

count = 0

i = 0
while i<= len(s)-len(word):
    j = 0
    match = 1
    while j < len(word):
        if s[i+j] != word[j]:
            match = 0
            break
        j= j+1


    if match == 1:
        count = count+1
    i = i+1

print("Number of Occurrences: ",count)





l1 = []
l2 = ["deepika" , 10,10.4] # list of mixes data
l3 = [10,20,30] # list integers
l4 = [10.2 , 10.4 , 10.3] # list of float
l5 = ["hitehv" , "khgvifwsb" , "sljbfb"] # list of string 

l6 = list("wellcome")
l6.append(12)

l7 = list((12,23,45,"deepika"))
print(l6)

l1 = [2]*5
print(l1)

l2 = [2,"deepika"]*5
print(l2)


l1 = list(range(1,6))
print(l1)

l = [10,20,30,40,50,90]
print(l[1])
print(l[-1])
print(l[-5])
print(l[-5:-1])

for i in l:
    print(i)


for i in range(0,len(l)):
    print(l[i])




for i in range(0,len(l)):
    print(l[i:i*2])



for i in range(0,len(l)):
    print(l[i:len(l)])



print(l[1:3])
print(l[:3])
print(l[2:])
print(l[::-1])
print(l[::2])


l.append(12)
print(l)



l = []
for i in range(1,101):
    if i % 2==0:
        l.append(i)
print(l)


l = []
for i in range(2,101,2):
        l.append(i)
print(l)


l = [10,20,30,405,40]
l.insert(len(l),99)
l.insert(-1,88)
print(l)



s = "                abbkjdbkdbvjdsa"
word = "k"
result = ""
result1 = ""
result2 = ""


for j in s:
    if j == word:
        pass
    else:
        result = result + j

for i in range(0,len(result)):
    if result[i-1]==" " and (result[i]>= "a" and result[i]<="z" or result[i] == " ") :
        pass
    else:
        result1 = result1+result[i]

print(result1)    
n = len(result1)
for k in range(len(result1),0,-1):
    if result1[n-1] >= "a" and result1[n-1] <= "z" and k == n:
        pass
    else:
        result2 = result1[k]+result2

print(result2)
print(result1)











l1 = [10,20,30]
l1.insert(2,40)
l1.append(32)
l1.insert(-10,2222)
l1.insert(100,999)
l1.append((23,45,66,[7366]))
print(l1)

l2 = [1,2,3,4,5]
a = [12,34,66,5,6,6,65,5]
l2.extend([20,30,50,60,70])
l2.extend(a)
print(l2)


l3 = [10,20,30]
l3.append("hello")
l3.extend("hello")
print(l3)


l4 = ["A","B","C"]
l5 = ["A","B","C"]
l6 = ["a","b","c"]

print(l4==l5)
print(l4==l6)
print(l4!=l6)


print(l4 is l5)
print(id(l4))
print(id(l5))

print(id(l5[0]))
print(id(l4[0]))




a = [10,20,30]
b = [5,40,30,20]
print(a>b)

a = ["hitesh","thakur"]
b = ["HITESH","THAKUR"]
print(a>b)




l = [10,20,30]
l[1] = 100
print(l)
l[-1] = 1000
print(l)
l[-10] = 10
print(l)


l = [10,20,30,40]
l[1:3] = [100,80,90]
print(l)

l[:] = [100,200,300,400,500]
print(l)

for i in range(len(l)):
    l[i] = l[i]*2
print(l)

marks = [90,80,70,60]
index = int(input("Entre The Index: "))
value = int(input("Enter Value: "))

marks [index] = value
print(marks)




l = ["deepika" , "rashmika" , "katappa"]
marks = [40,50,60]

name = input("Enter The Name: ")
if name in l:
    index = l.index(name)
    value = int(input("Enter Number: "))
    marks[index] = value
    print(marks)
else:
    print("Student not found")








students = ["moksha" ,"hitesh","vedant"]
name = input("Enter Name: ")
if name in students:
    index = students.index(name)
    name1 = name.upper()
    students[index] = name1
    print(students)
else:
    print("Student Name Not Find")




l = [10,20,30,40]
l.remove(20)
print(l)

l.pop(2)
print(l)

l.clear()
print(l)



l = [10,20,30,40,50,60]
del l[1]
del l[2:4]
print(l)
del l
print(l)



l = [10,21,30,405,12,605040,43]

for i in l[:]:
    if i %2 == 0:
        l.remove(i)

print(l)

# l[:] it will create a copy of list

l = [10,21,30,405,12,605040,43]

for i in l:
    if i %2 == 0:
        l.remove(i)

print(l)


l1 = l.copy()


for i in l1:
    if i %2 == 0:
        l.remove(i)

print(l)


# REMOVE ELIMENT WITH START A
l = ["abd","abdc","www","kdjc"]


for i in l[:]:
    if i.startswith("a"):
        l.remove(i)

print(l)




# WAP TO REMOVE ELIMENT USING USER INPUT
l = ["deepika","rashmika","wwww","rrrr"]
name = input("Enter name: ")

if name in l:
    l.remove(name)
else:
    print("anme not found")

print(l)



l = ["a","b","c","d","a"]
print(l.index("c"))
print(l.count("a"))

l2 = [12,3,4,3,2,3,4,5,6,6]
l2.sort()
print(l2)
l2.sort(reverse=True)
print(l2)


a = ["jhvhh","kjhdbfkwe","jhvf","jhwbf"]
a.sort(key=len)
print(a)

l2 = [-12,3334,454,-344,-455,4-43,2-334,5-444-5,55-5,55-55,-5555]
print(l2)
l2.sort(reverse=True,key=abs)
print(l2)


a = ["Deepika","Rashmika","deepika"]
a.sort(key=str.lower)
print(a)



l = [12,33,4,4,5,5,222,6,6,7,8,9,987,654,3,45,678,9,876,54]
l2 = sorted(l)
l3 = sorted(l,reverse=True)
print(l)
print(l2)
print(l3)


l.reverse()
print(l)


print(max(l))

print(min(l))

print(sum(l))
print(sum(l,1000))


a = [0,False,None]
print(any(a))
a = [0,False,None,True]
print(any(a))




l = [0,False,True]
print(all(l))
l = [1,"abd","hello"]
print(all(l))



l = [10,20,3,404,404,404,3032]

for index,Value in enumerate(l):
    print("index is: ",index,"value is: ",Value)



l = [10,20,3,404,404,404,3032]

for index,Value in enumerate(l,start=1):
    print("index is: ",index,"value is: ",Value)



l = [10,20,3,404,404,404,3032]
l2 = ["kjvb","kjshdv","jhbf","jkjhbf"]
for n,m in zip(l,l2): 
    print("mane: ",n,"value: ",m)



l = [10,20,3,404,404,404,3032]
l2 = [10,20,3,404,404,404,3032]
for n,m in zip(l,l2): 
    if n == m:
        print("Same")
    else:
        print("Not Same")



l = "hitesh"
print(list(l))



# HOW TO READ VALUE OF A LIST FROM USER

l = list(map(int,input("Enter Number: ").split()))
print(l)

l = list(map(int,input("Enter Number: ").split(",")))
print(l)



num = int(input("Enter number: "))
a = []
for i in range(num):
    n = int(input(f"Enter {i} value: "))
    a.append(n)

print(a)


num = int(input("Enter number: "))
a = []
for i in range(num):
    n = (input(f"Enter {i} value: "))
    a.append(n)

print(a)


num = int(input("Enter number: "))
a = []
for i in range(num):
    n = float(input(f"Enter {i} value: "))
    a.append(n)

print(a)





data = input().split()
print(data)
data[0] = int(data[0])
data[1] = float(data[1])
print(data)


print("Enter Id Name and Marks: ")
id , name , marks = input().split()
data = [int(id),name,float(marks)]




# WAP TO ADD ELEMENT ON A LIST

n = int(input("Enter The Size of List: "))
l = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
    sum += n1


print(l)
print(sum)



# WAP TO ADD ELEMENT ON A LIST

n = int(input("Enter The Size of List: "))
l = []
sum = 0
i = 0
while i < n:
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
    sum += n1
    i+=1


print(l)
print(sum)



# WAP TO ADD ELEMENT ON A LIST BUT ONLY EVEN INDEX

n = int(input("Enter The Size of List: "))
l = []
sum = 0
i = 0
while i < n:
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
    i+=1


for j in range(len(l)):
    if j%2==0:
        sum += l[j]




print(l)
print(sum)


# WAP TO ADD ELEMENT ON A LIST BUT ONLY EVEN INDEX

n = int(input("Enter The Size of List: "))
l = []
sum = 0

for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)


for j in range(len(l)):
    if j%2==0:
        sum += l[j]




print(l)
print(sum)



# WAP TO EVEN ELEMENT OF A LIST


n = int(input("Enter The Size of List: "))
l = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
    if n1 %2==0:
        sum += n1


print(l)
print(sum)



# WAP TO ODD ELEMENT OF A LIST


n = int(input("Enter The Size of List: "))
l = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
    if n1 %2!=0:
        sum += n1


print(l)
print(sum)


# WAP TO FIND MAXIMUM ELEMENT IN AN ARRY


n = int(input("Enter The Size of List: "))
l = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)

s1 = l[0]
for j in l:
    if j > s1:
        s1 = j
    

print(l)
print(s1)




# WAP TO FIND MAXIMUM ELEMENT IN AN ARRY


n = int(input("Enter The Size of List: "))
l = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)

s1 = l[0]
for j in range(len(l)):
    if l[j] > s1:
        s1 = l[j]
    

print(l)
print(s1)




# WAP TO FIND MINIMUM ELEMENT IN AN ARRY


n = int(input("Enter The Size of List: "))
l = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)

s1 = l[0]
for j in range(len(l)):
    if l[j] < s1:
        s1 = l[j]
    

print(l)
print(s1)




# WAP TO REMOVE DUPLICATE ELIMENT FROM A LIST


n = int(input("Enter The Size of List: "))
l = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)

l2 = []
for i in l:
    if i not in l2:
        l2.append(i)

print(l2)




# WAP TO FIND SECOND LARGEST ELEMENT IN A LIST


n = int(input("Enter The Size of List: "))
l = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)


l.sort()
print(l[-2])
    



# WAP TO SEPRATE EVEN AND ODD NUMBER FROM A LIST


n = int(input("Enter The Size of List: "))
odd = []
even = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    if n1 %2==0:
        even.append(n1)
    else:
        odd.append(n1)
    
print(even)
print(odd)



# WAP FIND COMMAN ELEMENT IN 2 LIST

n = int(input("Enter The Size of List: "))

l = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
    

n = int(input("Enter The Size of List: "))

l2 = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l2.append(n1)


l3 = []
for i in l:
    if i in l2:
        l3.append(i)



print(l3)
            


# WAP FIND COMMAN ELEMENT IN 2 LIST

n = int(input("Enter The Size of List: "))

l = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
    

n = int(input("Enter The Size of List: "))

l2 = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l2.append(n1)


l3 = []
for i in l:
    count=0
    for j in l2:
        if i == j:
            l3.append(i)



print(l3)
            



# WAP FIND COMMAN ELEMENT IN 2 LIST BUT EVEN AND GREATER THAN 10

n = int(input("Enter The Size of List: "))

l = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
    
print(l)
l2 = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l2.append(n1)
print(l2)

l3 = []
for i in l:
    count=0
    for j in l2:
        if i == j:
            if i % 2==0 and i > 10:
                l3.append(i)



print(l3)
            







# WAP FIND COMMAN ELEMENT IN 2 LIST BUT EVEN AND GREATER THAN 10

n = int(input("Enter The Size of List: "))

l = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
    
print(l)
l2 = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l2.append(n1)
print(l2)

l3 = []
for i in l:
    count=0
    for j in l2:
        if i == j:
            if i % 2==0 and i > 10:
                l3.append(i)



print(l3)
            



# WAP TO MARGE TO LIST WITHOUT DUPLICATES

n = int(input("Enter The Size of List: "))

l = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)


l1 = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)


sum = l+l1

final = []
for i in sum:
    if i not in final:
        final.append(i)



print(final)



# WAP TO REVERSE A LIST WITHOUT BUILT IN FUNCTION
n = int(input("Enter The Size of List: "))

l = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
print(l)

final = []
for i in range(len(l)-1,-1,-1):
    final.append(l[i]) 

print(final)


# 2

b = l[::-1]
print(b)


# WAP TO MOVE ALL ZEROS TO END
n = int(input("Enter The Size of List: "))

l = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
print(l)



zero = []
nonzero = []

for i in l:
    if i == 0:
        zero.append(i)
    else:
        nonzero.append(i)


print(nonzero+zero)



# WAP TO FOR THE PEAK ELIMENT  AN ELIMENT IS CLLAED PEAK ELIMENT IF ITS VALUE IS NOT SMALLER THAN ITS ADJECENT VALUE IF THEY ESIST
#  WAP TO FIND THE INDEX OF ANY ONE ELEMENT


n = int(input("Enter The Size of List: "))
l = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
print(l)

peakindex = -1
n =len(l)
for j in range(n):
    if i == 0:
        if n == 1 or l[i] >= l[i+1]:
            peakindex = i
            break
    elif i == n-1:
        if l[i] >= l[i-1]:
            peakindex = i
            break
    else:
        if l[i] >= l[i-1] and l[i] >= l[i+1]:
            peakindex = i
            break


if peakindex != -1:
    print("Peak element Index Is ",peakindex,"and Value: ",l[peakindex])
else:
    print("No Peak element")



# WAP TO FIND sum of leaders in an array
# AN ELEMNT IS CALLED LEADER THAN ALL ELEMENT OF ITS RIGHT SIDE RIGHT MOST ELEMENT IS ALWAYS A LEADER

n = int(input("Enter The Size of List: "))
l = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
print(l)


sum = 0
n = len(l)
for i in range(n):
    isleader = True
    for j in range(i+1,n):
        if l[i] <= l[j]:
            isleader= False
            break
    if isleader:
        sum += l[i] 



print("Aree Sum of Leader: ",sum)



# GIVAN AN UNSORTED ARRAY OF SIZE N HAVING BOTH NAGATIVE AND POSITIVE INTEGERS THE TASK IS TO PLACE ALL NAGETIVE ELEMENTS AT THE END OF THE ARRAY WITHOUT CHANGING THE ORDER OF POSITIVE ELEMENTS AND NAGATIVE ELEMENTS

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



# WAP TO CYCLICLY ROTATE ARRAY BY 1


n = int(input("Enter The Size of List: "))
l = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
print(l)


n = len(l)
last = l[n-1]

for i in range(n-1,-1,-1):
    l[i] = l[i-1]

l[0] = last
print(l)



# WAP TO CYCLICLY ROTATE ARRAY BY 1


n = int(input("Enter The Size of List: "))
l = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
print(l)

n2 = int(input("Entre Sift Number: "))
n = len(l)
l2 = []
l3 = []
count = 0
for i in range(n-n2+1,n+1):
    l2.append(i)
    if i == n:
        count = 1

if count == 1:
    for j in range(n-n2):
        l3.append(l[j])



print(l2+l3)
print(l)


# WAP TO CYCLICLY ROTATE ARRAY BY 1


n = int(input("Enter The Size of List: "))
l = []
sum = 0
for i in range(n):
    n1 = int(input(f"Enter {i} Number: "))
    l.append(n1)
print(l)

n2 = int(input("Entre Sift Number: "))
n = len(l)
l2 = []
l3 = []
count = 0
for i in range(n-n2+1,n+1):
    l2.append(i)
    if i == n:
        count = 1

if count == 1:
    for j in range(n-n2):
        l3.append(l[j])



print(l2+l3)
print(l)






# list comprehension 

a = [1,2,3,4,5]
b = []
for i in a:
    b.append(i*2)
print(b)

print("Mentos Jindagi")

b  = [i*2 for i in a]
print(b)



# list comprehension with conditional statement

a = [1,2,3,4,5,6,7,8,9]
b = []
for i in a:
    b.append(i*2)
print(b)

print("Mentos Jindagi")

b  = [2*i for i in a if i%2==0]
print(b)


c = [i for i in a if i%2==0 and i>3]
print(c)

d = ["Even" if i%2==0 else "odd"  for i in a]
print(d)

a = ["vedant" , "Deepesh" , "Moksh"]
e = [len(str(i*2)) for i in a]
print(e)



a = ["vedant" , "Deepesh" , "Moksh"]
e = [i for i in a if len(i)>3]
print(e)




f = [i.upper() for i in a]
print(f)

f = [i.title() for i in a]
print(f)

h = [1,2,3,4,5,6,7,8,9]
h = [i*10 if i%2==0 else i for i in h]
print(h)



#  multidimenstional list 2D list


a = [1,2,[3,4],5]
print(a)
print(a[2])
print(a[2][1])
print(a[2][0])
print(a[1])

b = [ 1,2,3,4,["hitesh","vedabnt","moksh",True],"Deepesh"]
print(b[4][2])



# travesing nested list

a = [ 
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

print(a[0])
print(a[1])
print(a[2])

for r in a:
    print(r)




for r in a:
    for c in r:
        print(c,end=",")
    print()


# travesing nested list

a = [ 
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

print(a[0])
print(a[1])
print(a[2])

for r in a:
    print(r)




for r in a:
    for c in r:
        print(c,end=",")
    print()

# using index based loop

for r in range(len(a)):
    for j in range(len(a[r])):
        print(a[r][j],end="-")



# travesing nested list

a = [ 
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

print(a[0])
print(a[1])
print(a[2])


# UPDATING NESTED LIST ELEMRNTS


print(a)
a[1][0] = "hii"
print(a)

a[2] = [9,9,9,9,9]
a = "Sonalic"
print(a)

# ADDING ELEMENTS IN NESTED LIST

a.append([2,3,4])
print(a)
print("hii")
# a[2].append([2,3,4])
print(a)


a[0].remove(20)
print(a)

a.pop(1)
print(a)


 #  matrix representation

a = [ 
    [10,20,30],
    [40,50,60],
    [70,80,90]
]



print(a)
print(*a)

for row in a:
    print(row)



#  matrix representation

a = [ 
    [10,20,30],
    [40,50,60],
    [70,80,90]
]



print(a)
print(*a)

for row in a:
    for v in row:
        print(v,end=" ")
    print()



# WAP TO READ ROWS AND COLUMN FROM USER AND DISPLAY THAM

row = int(input("Enter Row number: "))
column = int(input("Enter Number of column: "))
matrix = []

for i in range(row):
    row = []
    for j in range(column):
        row.append(int(input("Enter Number: ")))
    matrix.append(row)

for i in matrix:
    for j in i:
        print(j,end=" ")
    print()


print(matrix)




# WAP TO SUM OF ALL MATRIX ELMENTS

row = int(input("Enter NUmber of ROWS: "))
column = int(input("Enter Number of COLUMN: "))
matrix = []


sum = 0
for i in range(row):
    row = []
    for j in range(column):
        num = int(input("Enter Number: "))
        sum += num
        row.append(num)

    print()

print(sum)




# WAP TO SUM OF ALL MATRIX ELMENTS

row = int(input("Enter NUmber of ROWS: "))
column = int(input("Enter Number of COLUMN: "))
matrix = []


sum = 0
i = 0
while i < row:
    rows = []
    j = 0
    while j < column:
        num = int(input("Enter Number: "))
        sum += num
        rows.append(num)
        j+=1
    i+=1

    print()

print(sum)





# WAP TO FIND DIAGONAL SUM OF A SQUARE MATRIX


row = int(input("Enter Number of Rows: "))
column = int(input("Enter Number of column: "))

matrix = []

for i in range(row):
    rows = []
    for j in range(column):
        num = int(input("Entre NUmber: "))
        rows.append(num)
    matrix.append(rows)


for k in matrix:
    for l in k:
        print(l,end=" ")
    print()


sum = 0

for m in len(matrix):
    sum += matrix[i][i]


print(sum)




# WAP TO SUM OF ODD NUMBERS IN MATRIX


row = int(input("Enter Number of Rows: "))
column = int(input("Enter Number of column: "))

matrix = []

for i in range(row):
    rows = []
    for j in range(column):
        num = int(input("Entre NUmber: "))
        rows.append(num)
    matrix.append(rows)


for k in matrix:
    for l in k:
        print(l,end=" ")
    print()


sum = 0
for s in matrix:
    for d in s:
        if d%2!=0:
            sum+=d

print("Sum Of ODD Elements: ",sum)




# WAP TO SEARCH ELEMENT IN A MATRIX



row = int(input("Enter Number of Rows: "))
column = int(input("Enter Number of column: "))

matrix = []

for i in range(row):
    rows = []
    for j in range(column):
        num = int(input("Entre NUmber: "))
        rows.append(num)
    matrix.append(rows)


for k in matrix:
    for l in k:
        print(l,end=" ")
    print()

banda = int(input("Enter Search elemnt: "))
count = 0

for s in matrix:
    for k in s:
        if banda==k:
            print("Banda mil gya: ",k)
            count = 1
            break

if count == 0:
    print("Banda not found")






# WAP TO TO REVERSE EACH ROW


row = int(input("Enter Number of Rows: "))
column = int(input("Enter Number of column: "))

matrix = []

for i in range(row):
    rows = []
    for j in range(column):
        num = int(input("Entre NUmber: "))
        rows.append(num)
    matrix.append(rows)


for k in matrix:
    for l in k:
        print(l,end=" ")
    print()

print("Reverse")
matrix1 = []
for p in matrix:
    print(*p[::-1])



# WAP TO TO REVERSE EACH ROW


row = int(input("Enter Number of Rows: "))
column = int(input("Enter Number of column: "))

matrix = []

for i in range(row):
    rows = []
    for j in range(column):
        num = int(input("Entre NUmber: "))
        rows.append(num)
    matrix.append(rows)


for k in matrix:
    for l in k:
        print(l,end=" ")
    print()



for row in matrix:
    i = 0
    j = len(row)-1
    while i < j:
        t= row[i]
        row[i] = row[j]
        row[j] = t
        i = i+1
        j = j-1

print("Reverse Matrix")

for k in matrix:
    for l in k:
        print(l,end=" ")
    print()



# WAP TO ADD TO MATRIX

row = int(input("Enter Number of Rows: "))
column = int(input("Enter Number of column: "))
matrix = []

for i in range(row):
    rows = []
    for j in range(column):
        num = int(input("Entre NUmber: "))
        rows.append(num)
    matrix.append(rows)


print("Matrix2 elements:")
row1 = int(input("Enter Number of Rows: "))
column1 = int(input("Enter Number of column: "))
matrix1 = []

for i in range(row1):
    rows1 = []
    for j in range(column1):
        num1 = int(input("Entre NUmber: "))
        rows1.append(num1)
    matrix1.append(rows1)



if row == row1 and column == column1:
    matrix3 = []
    for i in range(row1):
        rows1 = []
        for j in range(column1):
            num1 = 0
            rows1.append(num1)
        matrix3.append(rows1)


    for row in range(len(matrix3)):
        for clos in range(len(matrix3[row])):
            matrix3[row][clos] = matrix[row][clos] + matrix1[row][clos]

    for k in matrix3:
        for l in k:
            print(l,end=" ")
        print()
else:
    print("Length Are Not Same Of both The matrix")





# WAP TO ADD TO MATRIX

row = int(input("Enter Number of Rows: "))
column = int(input("Enter Number of column: "))
matrix = []

for i in range(row):
    rows = []
    for j in range(column):
        num = int(input("Entre NUmber: "))
        rows.append(num)
    matrix.append(rows)


print("Matrix2 elements:")
row1 = int(input("Enter Number of Rows: "))
column1 = int(input("Enter Number of column: "))
matrix1 = []

for i in range(row1):
    rows1 = []
    for j in range(column1):
        num1 = int(input("Entre NUmber: "))
        rows1.append(num1)
    matrix1.append(rows1)


matrix3 = []
if row == row1 and column == column1:

    for row in range(row):
        rows1 = []
        for clos in range(column):
            rows1.append(matrix[row][clos] + matrix1[row][clos])
        matrix3.append(rows1)    

else:
    print("Length Are Not Same Of both The matrix")


for k in matrix3:
    for l in k:
        print(l,end=" ")
    print()



# WAP TO MULTIPLE TO METRICS

# row = int(input("Enter Number of Rows: "))
# column = int(input("Enter Number of column: "))
# matrix = []

# for i in range(row):
#     rows = []
#     for j in range(column):
#         num = int(input("Entre NUmber: "))
#         rows.append(num)
#     matrix.append(rows)


# print("Matrix2 elements:")
# row1 = int(input("Enter Number of Rows: "))
# column1 = int(input("Enter Number of column: "))
# matrix1 = []

# for i in range(row1):
#     rows1 = []
#     for j in range(column1):
        



# matrix3 = []

# if row == column1:
#     for i in range(row):
#         rows2 = []
#         for j in range(column1):
# else:
#     print("Length Are Not Same Of both The matrix")



# for k in matrix3:
#     for l in k:
#         print(l,end=" ")
#     print()



row = int(input("Enter Number of Rows: "))
column = int(input("Enter Number of column: "))
matrix1 = []

for i in range(row):
    rows = []
    for j in range(column):
        num = int(input("Enter Number: "))
        rows.append(num)
    matrix1.append(rows)


print("Matrix2 elements:")
row1 = int(input("Enter Number of Rows: "))
column1 = int(input("Enter Number of column: "))
matrix2 = []

for i in range(row1):
    rows1 = []
    for j in range(column1):
        num1 = int(input("Enter Number: "))
        rows1.append(num1)
    matrix2.append(rows1)


if column != row1:
    print("Multiplication is not possible")
else:
    result = []
    for i in range(row):
        row3 = []
        for j in range(column1):
            row3.append(0)
        result.append(row3)

    # ✅ FIXED LOOP
    for i in range(row):
        for j in range(column1):
            for s in range(column):
                result[i][j] = result[i][j] + matrix1[i][s] * matrix2[s][j]

    print("\nMatrix 1")
    for i in range(row):
        for j in range(column):
            print(matrix1[i][j], end=" ")
        print()

    print("\nMatrix 2")
    for i in range(row1):
        for j in range(column1):
            print(matrix2[i][j], end=" ")
        print()

    print("\nResult")
    for i in range(row):
        for j in range(column1):   # ✅ FIXED
            print(result[i][j], end=" ")
        print()




# MULTILEVEL NESTED LIST

a = [1,2,[3,4,[4,5,6]]]
print(a)
print(len(a[2][2]))
print(len(a[2]))




# 3D ARRAY

a = [
    [
        [1,2],
        [4,3],
    ],
    [
        
        [7,8],
        [8,9]
        
    ]
]


print((a[1][0]))
print((a[1][1]))
print((a[1]))
print((a[0]))



arr = [
    [   
        [1, 2, 3],
        [4, 5, 6]
    ],
    [  
        [7, 8, 9],
        [10, 11, 12]
    ]
]


# 3D ARRAY



# [2][3][4]
# class-1
#     student1= s1,s2,s3,s4
#     student2= s1,s2,s3,s4
#     student3= s1,s2,s3,s4
# class-2
#     student1= s1,s2,s3,s4
#     student2= s1,s2,s3,s4
#     student3= s1,s2,s3,s4



a = [
    [
        [1,2],
        [4,3],
    ],
    [
        [7,8],
        [8,9] 
    ]
]


for i in range(len(a)):
    print("layer: ",i)
    for j in range(len(a[i])):
        for k in range(len(a[i][j])):
            print(a[i][j][k],end=" ")
        print()
    print()





a = [
    [
        [1,2],
        [4,3],
    ],
    [
        [7,8],
        [8,9] 
    ]
]


for i in range(len(a)):
    print("layer: ",i)
    for j in range(len(a[i])):
        for k in range(len(a[i][j])):
            print(a[i][j][k],end=" ")
        print()
    print()




# WAP TO 3D ARRAY ELEMNTS FROM USER AND DISPLAY THEM


# given an array of n integers and an integer k find the no. of pairs of elemnts in the array whos sum is equal to k

n = int(input("Enter the size of element: "))
l = []
for s in range(n):
    l.append(int(input("Enter The Elemnts: ")))

find = int(input("Enter The find Element: "))
count = 0
for i in range(len(l)):
    for k in range(i):
        if l[i]+l[k] == find:
            count+=1


print("Total Pair: ",count)




# given an array of n integers and an integer k find the no. of pairs of elemnts in the array whos sum is equal to k

n = int(input("Enter the size of element: "))
l = []
for s in range(n):
    l.append(int(input("Enter The Elemnts: ")))

find = int(input("Enter The find Element: "))
count = 0
for i in range(len(l)):
    for k in range(i+1,len(l)):
        if l[i]+l[k] == find:
            count+=1


print("Total Pair: ",count)






#tuple


t = (1,2,3,4)
print(t)
t1 = 1,2,3,4
print(t1)
t = ()
print(t)
t = tuple([1,2,4454,2])
print(type(t))
t = (10)
print(type(t))
t = (10,12)
print(type(t))


a = (1,2,3,4)
print(a[1])
print(a[1:3])
print(a[-2])

# a[0] = 90 not possible
print(a)


t = ([1,2],3,4)
t[0].append(5)
print(t)


t = 10,20,30
print(t)
a,b,c = (10,20,30)
print(a)
print(b)
print(c)


a, *b = (10,20,30)
print(a)
print(b)




a, *b , c = (10,20,30,40,50)
print(a)
print(b)
print(c)


a= (10,20,30,40,50)

print(a.count(20))
print(a.index(20))
print(max(a))
print(min(a))
print(sum(a))



for i in a:
    print("Element: ",i)

for i in range(len(a)):
    print("elements: ",a[i])




a = (10,20,30,40,50)
b = (30,40,609,70)
print(a+b)  #concatiness

print(a*3)  #tuple repetation




# nested tuple


t = ((10,20,30),(30,20,50))
print(t[0])
print(t[0][2])
print(t[1])



id = int(input("Enter id: "))
name = input('Enter NAme: ')
salary = float(input("Enetr Salary: "))
employee = (id,name,salary)
print("Employee Details")
print("ID: ",employee[0])
print("NAME: ",employee[1])
print("SALARY: ",employee[2])




a = (10,20,30,40,50,2)
print(10 in a)
print(3 not in a)



t1 = (1,2,8)
t2 = (1,2,4)
print(t1<t2)


t1 = (1,2,8)
t2 = (1,2,4)
print(t1<t2)
del t2
print(t2)



# CONVERT TUPLE INTO LIST
import sys

t = (1,2,3)
print(t)
t = list(t)
print(t)


print(sorted(t))
print(sys.getsizeof(t))




# NAMED TUPLE

from collections import namedtuple

student = namedtuple("Student",["name","age","city"])
s1= student("abc",23,"mumbai")  
print(s1.name)
print(s1.age)
print(s1.city)




from collections import namedtuple

account = namedtuple("account",["accno","holdername","balance"])

accno = int(input("Enter Account Number: "))
holdername = input("Enetr Name: ")
balance = int(input("Enetr Balance: "))

acc= account(accno,holdername,balance)


print(acc.accno)
print(acc.holdername)
print(acc.balance)




from collections import namedtuple

student = namedtuple("student",["rollno","name","marks"])
n = int(input("Enter Number of students: "))

students = []

for i in range(n):
    print("Enetr Details")
    r = int(input("Enetr Roll No.: "))
    n = input("Enter Name: ")
    m = int(input("Enter Marks: "))
    students.append(student(r,n,m))


print(students)





from collections import namedtuple

student = namedtuple("Student",["name","age","city"])
s1= student("abc",23,"mumbai")


print(student._fields)
print(s1._fields)
print(student._asdict)
print(student._replace)
s2 = s1._replace(age=30)
print(id(s2))
print(id(s1))




from collections import namedtuple

student = namedtuple("Student",["name","age","city"])

data = ["byy",100,"hii"]
s1 = student._make(data)
print(s1.name)
print(s1.age)
print(s1.city)


# SET

s = {1,2,3,4,2,44,5,5,6,6,4,3,6,6,4,32,345,67,65,4}
print(s)

s = set([12,3,4,5,33,5,5,4,3,2,3,4,56,54,3,3,456,7,65,43,2])
print(s)


s = set()
print(s)



# SET

s = {1,2,3,4,2,44,5,5,6,6,4,3,6,6,4,32,345,67,65,4}
print(s)

# print(s[0])

for i in s:
    print(i)

print(5 in s)
print(100 not in s)


s.add(90)
s.update([12,234,23,234,23,234,123])

print(s)

s.remove(1)
print(s)


s = {1,2,3,4,2,44,5,5,6,6,4,3,6,6,4,32,345,67,65,4}
print(s)

s.discard(1)

s.pop()
print(s)




s = {1,2,3,4,4}
print(s)
s.clear()
print(s)



s = {1,2,3,4,4}
print(s)
s.clear()
print(s)



# SET METHAMATICAL OPERATION

s1 = {1,2,3,4,5}
s3 = {1,2,3,4,5,3,55,5,6,7,76,5,4,3,33}
s2 = {1,234,8,90,0,8,6}
print(s1)
print(s2)

print(s1|s2)
print(s1.union(s2))

print(s1&s2)
print(s1.intersection(s2))


print(s2.difference(s1))
print(s2-s1)
print(s1.difference(s2))
print(s1-s2)


print(s1.symmetric_difference(s2))
print(s2.symmetric_difference(s1))
print(s1^s2)




print(s1.issubset(s3))
print(s1.issubset(s2))
print(s1 <= s2)


print(s1.issubset(s2))
print(s3 >= s1)


print(s1.isdisjoint(s2))






#  INPLACE SET OPRATION 

s1 = {1,2,3,4,5,56}
s2 = {2,4,6,8,0,68,9}


s1.update(s2)
print(s1)
print(s2)

s2.update({1,2,3},{3,4,32,2})
print(s2)

s1|=s2
print(s1)


s1 = {1,2,3,4,5,56}
s2 = {2,4,6,8,0,68,9}

s1.intersection_update(s2)
print(s1)

s1&=s2
print(s1)



s1 = {1,2,3,4,5,56}
s2 = {2,4,6,8,0,68,9}
s1-=s2

print(s1)

s1 = {1,2,3,4,5,56}
s2 = {2,4,6,8,0,68,9}
s1^=s2

print(s1)

s = {1,2,3,4,(1,2,45)}
print(s)

s = {1,2,3,[3,4,2],{1332,34,54,2}}
print(s)
s = {1,2,3,{1332,34,54,2}}
print(s)

# set mutable he par set ke under ki values immutable honi chahiye nahi to error ayega




f = frozenset([1,2,3,4,5,5,4,5,3,2,6])
print(f)
print(type(f))


f = frozenset("hii ki haal he")
print(f)
print(type(f))

f = frozenset((1,2,3,4,5,5,4,5,3,2,6))
print(f)

f = frozenset({1,2,3,4,5,5,4,5,3,2,6})
print(f)




s = {12,3,2,1,567,4,3,3,454}
print(id(s))
s.add(200)
print(s)
print(id(s))




f1 = frozenset([1,2,3,4])
f2 = frozenset([2,3,45,78,9,8,5])


print(f1|f2)
print(f1&f2)
f1|=f2
print(f1)



f1 = frozenset([1,2,3,4])
f2 = frozenset([2,3,45,78,9,8,5])


print(f1|f2)
print(f1&f2)
print(id(f1))
f1|=f2
print(f1)
print(id(f1))




# WAP TO COUNT UNIC WORD IN STRING USING SET

name = input("Enter Name: ")
name1 = name.split()
s1 = set(name1)
print(s1)
s2 = list(s1)
print(s2)


# WAP TO CHECK UNIC CHARACTERS IN A STRING using set

str = input("Enetr String: ")
s1 = set(str)
if len(str) == len(s1):
    print("No Duplicate")
else:
    print("Dupplicate Found")



# DICTONARY


dictonary = {
    1 : "deepika",
    2 : "deepesh",
    3 : "vedant"
}

print(dictonary)

d1 = dict({"a":"abc","b":"abcd"})
d2 = dict(a="abc",b = "cde" , c="www")
print(d1)
print(d2)




student = {
    "name" : "deepsh",
    "age" : 50,
    "city" : "indore"
}


# accesing values by keys

print(student.keys())
print(student.values())

print(student["name"])
print(student.get("name"))
print(student.get("city"))


# print(student["salary"])
print(student.get("salary"))
print(student.get("salary","Not Found"))



d = {}
n = int(input("Enter Number of students: "))

for i in range(n):
    name = input("Enter NAme: ")
    marks = int(input("Enter Marks: "))
    d[name] = marks


print(d)
for f in d:
    print(f,d[f])



d = {1:"dipika",2:"hii"}
d[3]="virat"
print(d)

d[4] = "vebhaav"

print(d)

d[3] = "vebhav"
print(d)

# removing elememnts:

d1 = d.pop(1)
print(d)
print(d1)

print(d.pop(3))
print(d)
d2 = d.popitem()
print(d2)


d = {1:"dipika",2:"hii",3:"hiiii"}


while d:
    print(d.popitem())



d = {1:"deepika",2:"moksh",3:"vishnu",4:"deepesh"}
print(d)

del d[3]
# del d[5] it will give error
print(d)


# safe way to delete any key into dectonary

if 5 in d:
    del d[5]


d.clear()
print(d)



d = {1:"deepika",2:"moksh",3:"vishnu",4:"deepesh"}
print(d)

print(d.keys())
print(list(d.keys()))
print(d.values())
print(set(d.keys()))
print(d.setdefault(3))


print(d.items())
print(list(d.items()))


for key, value in d.items():
    print(key,value)



d.update({"salary":900000,"salary2":900000})
d.update({"salary":10000009999})

print(d)


d1 = d.copy()
print(d1)
d1.update({"salary":199212})
print(d)
print(d1)



d = {1:"deepika",2:"moksh",3:"vishnu",4:"deepesh","marks":[89,75]}
print(d)

s1 = d.copy()

s1["marks"][0]=77

print(d)
print(s1)


# dict comprehension
sq = {}
for i in range(1,6):
    sq[i] = i*i

print(sq)

sq = {i:i*i for i in range(1,6)}
print(sq)


se = {i :i*i for i in range(1,11) if i%2==0 }

print(se)


words= {"deepika","thapajii","deepesh"}
d = {word:len(word) for word in words}
print(d)


num = [1,2,3,7,5,6]
r = {x:"even" if x%2==0 else "odd" for x in num}
print(r)


keys= ["name","age","city"]
values = ["deepika",30,"chennai"]

d = {keys[i]:values[i] for i in range(len(keys))}
print(d)


# nested dictonary 

d = {
    101:{"name":"deepu","age":30},
    102:{"name":"deepesh","age":35},
    103:{"name":"vedant","age":20}

}


print(d[101])
print(d[102])
print(d[103])


print(d[101]["name"])
print(d[101]["name"][2])

# modification in nested dictonary

d[101]["name"]="hitesh"
print(d)




d = {
    101:{"name":"deepu","age":30},
    102:{"name":"deepesh","age":35},
    103:{"name":"vedant","age":20}
}
# add new member
d[104]={"name":"moksh","age":20}

print(d)



#  NESTED DICT LOOP

d = {
    101:{"name":"deepu","age":30},
    102:{"name":"deepesh","age":35},
    103:{"name":"vedant","age":20}
}

for k,v in d.items():
    print("ID:",k)
    for k1,v1 in v.items():
        print(k1, "=" ,v1)



company = {
    "emp1":{"name":"deepika","skill":["python","fullstack","java","react"]},
    "emp2":{"name":"deepesh","skill":["javafull stack","video editing"]}
}


print(company["emp1"])
print(company["emp1"]["skill"])
print(company["emp1"]["skill"][1])



response = {
"user":{
"id":101,
"profile":{"name":"deepu","email":"d@gmail.com"}
}
}


print(response["user"]["profile"]["email"])



# USE OF EVAL
d = eval(input("Enter Dictoanry: "))
print(d)
print(type(d))

d1 = input("Enter: ")
print(d1)
print(type(d1))




# WAP TO TACK DICT FROM THE KEY BORD AND PRINT SUM OF VALUES


d = eval(input("Enter Dictoanry: "))
print(d)

s = sum(d.values())
print(s)



# WAP TO TACK DICT FROM THE KEY BORD AND PRINT SUM OF VALUES

n = int(input("Enter Number of items: "))

d = {}

for i in range(n):
    key = input("Enter Key: ")
    value = int(input("Enter Value: "))
    d[key] = value


print(d)
print(sum(d.values()))



# WAP TO TACK DICT FROM THE KEY BORD AND PRINT SUM OF VALUES

n = int(input("Enter Number of items: "))

d = {}

for i in range(n):
    key = input("Enter Key: ")
    value = int(input("Enter Value: "))
    d[key] = value


print(d)
print(sum(d.values()))






# WAP TO FIND NUMBER OF OCCURENCE OF EACH LATTER PRESENT IN THE EVEN STRING

n = (input("Enter Number of items: "))
d = {}

for i in n:
    d[i] = d.get(i,0)+1
print(d)

for k,v in d.items():
    print(k,"occured",v,"times")



# WAP TO FIND NO. OF OCCURENCE OF EACH WOVELS IN THE GIVEN STRING
n = (input("Enter Number of items: "))
d = {}

for i in n:
    if i in ["a","e","i","o","u"]:
        d[i] = d.get(i,0)+1
print(d)

for k,v in d.items():
    print(k,"occured",v,"times")


# WAP TO FIND NO. OF OCCURENCE OF EACH CONSONENTS IN THE GIVEN STRING
n = (input("Enter Number of items: "))
d = {}

for i in n:
    if i not in ["a","e","i","o","u"]:
        d[i] = d.get(i,0)+1
print(d)

for k,v in d.items():
    print(k,"occured",v,"times")



# WAP TO FIND NO. OF OCCURENCE OF EACH CONSONENTS IN THE GIVEN STRING
n = (input("Enter Number of items: "))
d = {}

for i in n:
    if i not in ["a","e","i","o","u"]:
        d[i] = d.get(i,0)+1
print(d)
for k,v in sorted(d.items()):
    print(k,"occured",v,"times")



# WAP TO TRAKE HOW MANY TIME EACH USER TRY TO LOGIN LIst


login = ["deepika","deepesh","sonalika","deepesh","vedant"]
d = {}

for user in login:
    d[user] = d.get(user,0)+1

for k,v in d.items():
    print(k,": Try:",v,"Times")



# WAP TO GROUP WORDS BY LENGTH

name = ["deepika","deepesh","sonalika","deepesh","vedant","a","b","neha","nena"]
g = {}

for w in name:
    l = len(w)
    if l not in g:
        g[l] = []
    g[l].append(w)

print(g)


# WAP TO MERGE TWO DICTONARYES AND SUM THERE VALUES

d1 = {"goa":5,"mumbai":3,"jaipur":6,"thailand":2}
d2 = {"goa":9,"mumbai":8,"jaipur":6,"delhi":3,"hedrabad":8}
d = d1.copy()

for k,v in d2.items():
    d[k] = d.get(k,0)+v
print(d)



# FUNCTION

def Hello():
    print("First Function")

Hello()

def sum():
    num1 = int(input("Enter NUmber: "))
    num2 = int(input("Enter number: "))
    print("Sum is: ",num1+num2)

sum()

def sum(a,b):
    print("Sum is:",a+b)


a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
sum(a,b)




def welcome():
    print("Welcome ")

def hello():
    print("Hello Guys")
    welcome()

def sum(x,y):
    hello()
    print(x+y)

sum(12,23)


def sum(a,b):
    c = a+b
    return c

def mul(a,b):
    d = a*b
    return d

def value():
    x = sum(10,20)
    y = mul(3,4)
    print("Sum is: ",x)
    print("Mul is: ",y)


value()




def sum(a,b):
    c = a+b
    return  c

def mul(a,b):
    d = a*b
    return d
def general():
    x  = sum(12,34)
    y  = mul(12,4)
    print(x)
    print(y)
    

general()



def general():
    sum(12,23)
    # print(c) it will give an error becouse c is not define 


def sum(a,b):
    c =a+b
    return

def main():
    print(sum(12,23))

main()

def hello():
    print("hello")
    return
    print("bye")

def main():
    print("welconmr")
    hello()
    print("done")
    return
main()



#   MULTIPLE VALUES RETURN
def calculate(a,b):
    return a+b,a-b


def main():
    result = calculate(122,23)
    print(result)
    print("sum: ",result[0])
    print("Sub: ",result[1])

    sum1 , diff = calculate(14,23)
    print("sum1: ",sum1)
    print("Diff: ",diff)

main()




def even(a):
    even = []
    for i in range(a+1):
        if i %2 == 0:
            even.append(i)
    return even

def main():
    x= even(10)
    print(x)


main()



lis = [1,2,4,2,3,3,5,66,65,534,2,2,56,6,1]
def even(a):
    even = []
    for i in lis:
        if i % 2 == 0:
            even.append(i)
    return even

def main():
    x= even()
    print(x)


main()


# 2 keyword aurguments
def hello(name,age):
    print("Name is: ",name)
    print("Age is: ",age)

hello(age = 20, name="kitty")


def hello(name,age):
    print("Name is: ",name)
    print("Age is: ",age)

hello(age = 20, name="kitty") # if any wrong aurgument pass here so it will give error

# IMP 
def hello(name,age):
    print("Name is: ",name)
    print("Age is: ",age)


hello(name="kitty", 20) # it will give an error 
hello("kitty",age =  20)  




# DEFAULT PARAMETER 
def hello(name,age,city="indore",profe="1200"):
    print("Name is: ",name)
    print("Age is: ",age)
    print(city)
    print(profe)


 
hello("kitty",30,profe="it")  


# DEFAULT PARAMETER ,KEYWORD AND POSITIONAL PARAMETER
def hello(name,age,city="indore",profe="1200"):
    print("Name is: ",name)
    print("Age is: ",age)
    print(city)
    print(profe)

 
hello("kitty",profe="it",age=300)  


def hello(name,city,age=12,profe="1200"):
    print("Name is: ",name)
    print("Age is: ",age)
    print(city)
    print(profe)

 
hello("kitty","indore",profe="it",age=300)  



# VERIABLE LENGTH AURGUMENT
def display(*hitesh):
    print(hitesh)

display(1,2,3,4,5)


# VERIABLE LENGTH AURGUMENT
def display(*hitesh):
    print(hitesh)

display(1,2,3,4,5,"kuldeeep",2)


def sum(*num):
    total = 0
    for i in num:
        total+=i
    print(total)

sum(1,2,3,5,12,4,2,1234567,23456)


# WAP TO MANU DRIVEN PROGRAM WHERE READ TWO NUMBERS FROM USER AND CHOISE FROM USER IF CHOISE 1 THAN ADDITION IF CHOISE 2 SUBTRACTION IF CHOISE 3 MULTIPLECATION



def add(a,b):
    c = a+b
    return c

def sub(a,b):
    c = a-b
    return c

def mul(a,b):
    c = a*b 
    return c

def main():
    print('''1. add
2. sub
3. mul''')
    choise = int(input("Choose a Option: "))

    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))

    match choise:
        case 1:
            print("Sum is: ".add(a,b))
        case 2:
            print("Subtract is: ",sub(a,b))
        case 3:
            print("Multiplication is: ",mul(a,b))
        case _:
            print("Wrong Option")

main()



def hello(name , *marks ):
    print("Hello " + name)
    print("Marks: ", marks)



hello("hitesh",90,90,80)


def average(*marks):
    return sum(marks)/(len(marks))

print(average(90,80,90,100))

#   PASSING LIST IN ARGS
list1 = [1,2,3,4,5]
def add(a,b,c,d,e):
    return (a+b+c+d+e)

print(add(*list1))



#   PASSING LIST IN ARGS
list1 = [1,2,3,4,5]
def add(*l1):
    s = 0
    for i in l1:
        s+=i
    return s

print(add(1,2,3,2,2,3,2,3))




#   PASSING LIST IN ARGS
list1 = [1,2,3,4,5]
def add(*l1):
    return sum(l1)
print(add(*list1))



#   PASSING LIST IN ARGS
def add(*l1):
    return sum(l1)
print(add(*[10,20,30,40]))


#   PASSING LIST IN ARGS
def add(*l1):
    return sum(l1)
print(add([10,20,30,40])) # this will give error becouse 



# KEYWORD VARIABLE LENGTH AURGUMENT

def display(**hii):
    print(hii)

display(name="kitty",age = 20,address = "indore")



# KEYWORD VARIABLE LENGTH AURGUMENT

def display(**hii):
    print(hii)
    for k,v in hii.items():
        print(k,':',v)

display(name="kitty",age = 20,address = "indore")

# KEYWORD VARIABLE LENGTH AURGUMENT

def display(**info):
    if "name" in info:
        print("Welcome: ",info["name"])
    if "email" in info:
        print("Email: ",info["email"])
    if "address" in info:
        print("Address: ",info["address"])
display(name="kitty",age = 20,address = "indore",email = "kitty!43@gmail.com")



# def diaplay(name,age):
#     print(name,age)

# diaplay("kitty",20)
# diaplay(name="kitty",age=21)

# positional only perameter

def diaplay(name,age,/):
    print(name,age)

diaplay("kitty",20)
diaplay(name="kitty",age=21)



def add(a,b,c,/):
    print(a+b+c)

add(10,20,30)
add(a=200,b=100,c=102)
    


# keyword only paeameter
def add(*,a,b,c):
    print(a+b+c)


add(a=200,b=100,c=102)
add(10,20,30)    



# keyword only paeameter
def add(a,*,b,c):
    print(a+b+c)


add(a=200,b=100,c=102)
add(10,b=20,c=30)
add(10,20,c=10)    


# keyword only paeameter
def add(id,name,/,salary,*,age,address):
    print(id)
    print(name)
    print(salary)
    print(age)
    print(address)


add(101,"kitty",300000,age=20,address="indore")
  

# LAMBDA FUNCTION
fun = lambda a : a*a
print(fun(10))


# WA lambda FUNCTION TO ADD TWO NUMBER

ADD = lambda a,b : a+b
print(ADD(10,20))



# lambda with conditional logic

max = lambda a,b:a if a > b else b
print(max(10,20))



# lambda with conditional logic

max = lambda a,b:a if a > b else b
print(max(10,20))





# map function in python

l1 = [10,20,30,40,50]
def sq(x):
    return x*x
print(list(map(sq,l1)))








n = [2,4,6,8,7,9]
r = map(lambda x:x*x,n)
print(list(r))



n = ["kitty","hitesh","akshay"]
r = map(lambda x:x.capitalize(),n)
print(list(r))



n = ["kitty","hitesh","akshay"]
r = map(lambda x:x.upper(),n)
print(list(r))



n = ["kitty","hitesh","akshay"]
r = map(lambda x:len(x),n)
print(list(r))


# WAP TO ADD TWO LIST

n = ["kitty","hitesh","akshay"]
n2 = ["kitty ","hitesh","akshay","S"]
r = map(lambda x,x1:x+x1,n,n2)
print(list(r))




# WAP TO ADD TWO LIST

n = ["kitty","hitesh","akshay"]
n2 = ["kitty ","hitesh","akshay","S"]
r = map(lambda x,x1:x+x1,n,n2)
print(list(r))

def add(a,b):
    return a+b
r = map(add,n,n2)

print(list(r))




num = [100,200,300,5,25,3]
r = map(lambda x:"even" if x%2==0 else "odd",num)
print(list(r))



marks = [92,60,31,56]

grade = map(lambda x: "A" if x > 75 else "B" if x > 60 else "C" if x > 45 else "F",marks)
print(list(grade))




# filter function
# filter(function , iterable) jo true hoga to rakhega nahi to remove kar dega

l = [12,32,35,677,344,335]

def func(x):
    return x%2==0

r = filter(func,l)
print(list(r))



# filter function
# filter(function , iterable) jo true hoga to rakhega nahi to remove kar dega

l = ["ajay","kitty","akshay","hitesh","deepesh"]

r = filter(lambda x: x.startswith("a"),l)
print(list(r))




# WAP TO FILTER ONLY THOSE LEN > 5


l = ["hii","hitesh","kitty","akshay"]
r = filter(lambda x:len(x) >=5 ,l)
print(list(r))





# WAP TO FILTER ONLY THOSE LEN > 5


l = ["hii","hitesh","kitty","akshay"]
r = filter(lambda x:len(x) >=5 and x.startswith("k") ,l)
print(list(r))




# WAP TO CONVERT STRING INTO INTERGER

l = ["1","2","4","5"]
r = map(lambda x:(int(x)),l)
print(list(r))
# print(type(list(r)[1]))





# WAP TO REMOVE EMPTY STRING FROME A LIST

l = ["","hii","hitesh","kitty"]

r = filter(lambda x:len(x)>1 ,l)
print(list(r))




# WAP TO REMOVE EMPTY STRING FROME A LIST

l = ["","hii","hitesh","kitty"]

r = filter(lambda x:x ,l)
print(list(r))




# wap to square and print even no
l = [1,2,3,56,3,35,4,2,234]

r = filter(lambda x:x%2==0,(map(lambda a:a*a,l)))
print(list(r))




# WAP TO TO REVERSE EACH WORD OF A LIST

l = ["akshay","hitesh","kitty",""]
r = (map(lambda x:x[::-1],l))
print(list(r))




# REDUCE FUNCTION

from functools import reduce

def add(x,y):
    return x+y

num = [1,2,3,4,5,6]
result = reduce(add,num)
print(result)



# REDUCE FUNCTION

from functools import reduce

def add(x,y):
    return x+y

num = [1,2,3,4,5,6]
result = reduce(add,num,100)
print(result)



# REDUCE FUNCTION

from functools import reduce

def add(x,y):
    return x+y

num = [1,2,3,4,5,6]
result = reduce(lambda x,y : x*y,num)
print(result)



# REDUCE FUNCTION

from functools import reduce

def add(x,y):
    return x+y

num = [1,2,3,4,5,6]
result = reduce(lambda x,y : x*y,num,1000)
print(result)




from functools import reduce

num = [11,2324,4432,234,232,2,345]
result = reduce(lambda x,y:x if x>y else y,num)
print(result)


# LEMBDA IN SORTING

num = [5,6,6,2,3,5,7,2,3,5]
names = ["hitesh","vedant","sakshi","abc"]
print(sorted(num))
print(sorted(num,reverse=True))

a = sorted(num ,key=lambda x:x)
print(a)

print(sorted(names,key=lambda x:len(x)))



students = [(("deepika",30),("vedant",55),("sona",20),("akshay",20))]
print(sorted(students))

s2 = sorted(students,key= lambda x:x[1])
print(s2)




# RECURSION

def fact(n):
    if n == 1 or n ==0:
        return 1
    return n*fact(n-1)

def main():
    x = fact(6)
    print(x)

main()


# RECURSION

def fact(n):
    if n == 0:
        return 1
    return n+fact(n-1)

def main():
    x = fact(6)
    print(x)

main() 

# RECURSION
# SUM OF N NATURAL NUMBER
def fact(n):
    if n == 0:
        return 1
    return n+fact(n-1)

def main():
    x = fact(6)
    print(x)

main() 



# RECURSION
# SUM OF N NATURAL NUMBER
def sum(n):
    if n == 0:
        return 0
    return n+sum(n-1)

def main():
    x = int(input("Entert Number: "))
    x1 = sum(x)
    print(x1)

main() 




# RECURSION
# SUM OF N NATURAL NUMBER
def sum(n):
    if n == 1:
        return 1
    return n+sum(n-1)

def main():
    x = int(input("Entert Number: "))
    x1 = sum(x)
    print(x1)

main() 



# WAP TO POWER FUNCTION USING RECURSION

def power(n,n1):
    if n1 == 0:
        return 1
    return n*power(n,n1-1)


def main():
    x = power(2,5)
    print(x)

main()




# WAP TO COUNT digits in a number

def count(num):
    if len(str(num))==1:
        return 1
    return 1+count(num//10)


def main():
    x = count(123456789876543)
    print(x)
main()




# WAP TO COUNT digits in a number

def count(num):
    if num==0:
        return 0
    return 1+count(num//10)


def main():
    x = count(123)
    print(x)
main()





# WAP TO COUNT digits in a number

def count(num):
    if num==0:
        return 0
    return 1+count(num//10)


def main():
    x = count(123)
    print(x)
main()  




# nested func
def hello(name):
    def message():
        return "hello bABY"
    print("hello",name)
    print(message())
    
(hello("hitesh"))



def outer():
    x = 10
    def inner():
        print("Value of ",x)
    inner()

outer()


def outer():
    x = 10
    def inner():
        nonlocal x
        x = 1000
        print("Inner Value is : ",x)
    inner()
    print("Outer Value is: ",x)


outer()




# LEGB

x = 100
def outer():
    x = 90 
    def test():
        print("Inside Func: ",x)
    test()
outer()
print("X is: ",x)


x = 100
def outer():
    # x = 90 
    def test():
        print("Inside Func: ",x)
    test()
outer()
print("X is: ",x)




def outer():
    def test():
        print("Inside Func")
        print(len([12,34,53,1345,123]))
    test()
outer()



def total(price,texrate):
    def tax():
        return price*texrate
    return price + tax()

print(total(1000,0.18))



def bill(amount):
    def discount():
        if amount>10000:
            return amount*0.10
        return 0
    d = discount()
    finalamount = amount-d
    return finalamount

print(bill(150000))




#  HEIGHER ORDER FUCTION

def hello(fun):
    return fun("heyyyy")

def upper(x):
    return x.upper()

print(hello(upper))


def apply(fun,x):
    return fun(x)

def square(n):
    return n*n

print(apply(square,5))




# CLOSURE 

def hello(name):
    message=f"hello {name}"
    def display():
        print(message)
    return display


# closure
h = hello("Kitty")
h()



def counte():
    count=0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment


x = counte()
print(x())
print(x())
print(x())



def cardmaker(greeting , name):
    def card():
        return f"{greeting},{name}"
    return card

first = cardmaker("hii","kitty")
second = cardmaker("hello","hitesh")

print(first())
print(second())





# DECORATOR

def mydesign(func):
    def wraper():
        print("Befor calling the code")
        func()
        print("After Calling the function")
    return wraper

def hello():
    print("Hello Guysss How Are you all")

d = mydesign(hello)
d()





# DECORATOR

def mydesign(func):
    def wraper():
        print("Befor calling the code")
        func()
        print("After Calling the function")
    return wraper

@mydesign
def hello():
    print("Hello Guysss How Are you all")


hello()




loggein = True

def loginrequired(func):
    def wraper():
        if loggein:
            print("Processing.....")
            func()
        else:
            print("Plz login First")
    return wraper

@loginrequired
def profile():
    print("Welcome to over Profile Page")

profile()




login = input("Login or Not: ")

if login == "yes":
    loggein = True
elif login == "no":
    loggein = False
else:
    print("You Enter Wrong input Choose(yes/no)")

 

def loginrequired(func):
    def wraper():
        if loggein:
            print("Processing.....")
            func()
        else:
            print("Plz login First")
    return wraper

@loginrequired
def profile():
    print("Welcome to over Profile Page")

profile()






def mydecor(func):
    def wraper(*args,**kwargs):
        print("Calculation start: ")
        result = func(*args,**kwargs)
        print("Calculation Done")
    return wraper


@mydecor
def add(a,b):
    print("Sum is: ",a+b)


@mydecor
def product(a,b,c,d):
    print("Product is: ",a*b*c*d)

add(10,20)
product(10,2,3,40)




# TYPE HINTS 

def add(a:int,b:int) ->int:
    return a+b

result = (add(10,12.75))
print(result)
print(type(add(10,12)))



# DOC STRING 

def add(a,b):
    '''THis will return a+b'''
    return a+b


print(add.__doc__)



# DOC STRING 

def add(a,b):
    '''THis will return a+b and add two variable'''
    return a+b


print(add.__doc__)
print(help(str.__doc__))
print(int.__doc__)




# MODULES 
# BUILT IN MODULE
print(help("modules"))



import math
print(math.sqrt(16))
print(math.factorial(16))
print(math.pow(16,2))
print(math.ceil(16))




import math

# print(math.__doc__)
# print(help(math))
print(dir(math))




from math import sqrt
print(sqrt(10))



# RANDOM 
import random
print(dir(random))

import random

x = random.random()
print(x)


import random

x = random.uniform(1,10)
print(x)
x = random.randint(1,6)
print(x)
x = random.randrange(1,200,20)
print(x)
y = ["kitty","hitesh","akshay"]
x = random.choice(y)
print(x)
x = random.choices(y,k=2)
print(x)
x = random.sample(y,k=2)
print(x)
x = random.shuffle(y)
print(y)




import random

num = random.randint(1,10)
gues = int(input("Enter THe Number: "))

if num == gues:
    print("Match , Just Looking Like a wowwwww....")
else:
    print("Not Match")




# DATETIME MODUL
from datetime import date

today = date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)




from datetime import datetime

now = datetime.now()
print(now)
print(now.year)
print(now.second)




from datetime import datetime

now = datetime.now()
print(now)
f = now.strftime("%y-%m-%d")
f = now.strftime("%y-%B-%d")
f = now.strftime("%y-%B-%d")
f = now.strftime("%H-%M-%S %p")
f = now.strftime("%I %H-%M-%S %p")
f = now.strftime("%A")
f = now.strftime("%a")
f = now.strftime("%j")
f = now.strftime("%D")
f = now.strftime("%w")
f = now.strftime("%W")
 
print(f)



