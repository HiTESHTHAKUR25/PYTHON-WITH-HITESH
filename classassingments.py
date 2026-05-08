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
    print("Perfect Number by FOR loop")
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
    else:
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



