# 1)	WAP to find out the sum of all integer between 100 and 200 which are divisible by 9
num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))

count=0
for i in range(num1,num2+1):
    if i%9==0:
        count+=i
    
print(count)

# 2)	WAP to print Square, Cube and Square Root of all numbers from 1 to N
import math
num = int(input("Enter Number: "))

for i in range(1,num+1):
    print(f"Square of {i} is {i**2}")
for i in range(1,num+1):
    print(f"Cube of {i} is {i**3}")
for i in range(1,num+1):
    print(f"Square Root Of {i} is {math.sqrt(i)}")



# 3)	WAP to find out all the leap years between two entered years

num1 = int(input("Enter Starting Year: "))
num2 = int(input("Enter Ending Year: "))

for i in range(num1,num2+1):
    if i%4==0 or i%400==0 and i%100!=0:
        print("Leap Year: ",i)



# 1
# 00
# 111
# 0000
# 11111

num = int(input("Enter NUmber: "))

for i in range(1,num+1):
    for j in range(1,i+1):
        if i%2==0:
            print(0,end="")
        else:
            print(1,end="")
    print()


# 5)
# A
# AB
# ABC
# ABCD
# ABCDE


num = int(input("Enter Number: "))

for i in range(1,num+1):
    char = 65
    for j in range(1,i+1):
        print(chr(char),end="")
        char+=1
    print()

# 6)
# a
# ab
# abc
# abcd
# abcde

num = int(input("Enter Number: "))
for i in range(1,num+1):
    char = 97
    for j in range(1,i+1):
        print(chr(char),end="")
        char+=1
    print()



# 7.
# enter n6
#      *
#     **
#    ***
#   ****
#  *****
# ******


num = int(input("Enter Number: "))

for i in range(1,num+1):
    for j in range(1,(num+1)-i):
        print(" ",end="")
    for k in range(num-i,num):
        print("*",end="")
    print()




# enter n6
#  654321
#   65432
#    6543
#     654
#      65
#       6


num = int(input("Enter Number: "))
num = num+1

count=0
for i in range(1,num):
    count+=1
    for k in range(1,count):
        print(" ",end="")
    for j in range(num-1,i,-1):
        print(j,end="")
    print()


# 9.
#     1
#    10
#   101
#  1010
# 10101


num = int(input("Enter Number: "))

for i in range(1,num+1):
    for j in range(1,num-i+1):
        print(" ",end="")
    for k in range(num-i,num):
        if k%2==0:
            print(1,end="")
        else:
            print(0,end="")
    print()




# 10.
# enter number6
# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4

num = int(input("Enter Numbre: "))

for i in range(1,num+1):
    for j in range(0,i):
        print(j,end=" ")
    print()

