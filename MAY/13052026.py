#   *****

num = int(input("ENter Numbre: "))

for i in  range(num):
    print("*",end="")


# *
# *
# *
# *
# *


num = int(input("Enter Number: "))

for i in range(num):
    print("*")

# 1
# 00
# 111
# 0000
# 11111


num = int(input("Enter NUmber: "))

for i in range(1,num+1):
    print()
    for j in range(1,i+1):
        if i%2==0:
            print("0",end="")
        else:
            print("1",end="")


# A
# AB
# ABC
# ABCD
# ABCDE


num = int(input("Enter Number: "))

for i in range(1,num+1):
    print()
    char = 65
    for j in range(1,i+1):
        print(chr(char),end="")
        char+=1


# a
# ab
# abc
# abcd
# abcde


num = int(input("Enter Number: "))

for i in range(1,num+1):
    print()
    char = 97
    for j in range(1,i+1):
        print(chr(char),end="")
        char+=1


# *
# * *
# *  *
# *   *
# * * * * *


num = int(input("Enter Number: "))

for i in range(1,num+1):
    print()
    if i == num:
        for l in range(1,num+1+1):
            print("*",end="")
    else: 
        for j in range(1,2):
            print("*",end="")
        if i >= 2:
            for k in range(1,i):
                print(" ",end="")
            for p in range(1,2):
                print("*",end="")



# 1
# 22
# 3 3
# 4  4
# 55555



num = int(input("Enter Number: "))


for i in range(1,num+1):
    print()
    for j in range(1,i+1):
        if 3 <= i <num and j >= 2 and j < i:
            print(" ",end="")
        else:
            print(i,end="")

# A
# AB
# A C
# A  D
# ABCDE



num = int(input("Enter Number: "))


for i in range(1,num+1):
    print()
    char=65
    for j in range(1,i+1):
        if 3 <= i <num and j >= 2 and j < i:
            print(" ",end="")
            char+=1
        else:
            print(chr(char),end="")
            char+=1


# a
# ab
# a c
# a  d
# abcde



num = int(input("Enter Number: "))


for i in range(1,num+1):
    print()
    char=97
    for j in range(1,i+1):
        if 3 <= i <num and j >= 2 and j < i:
            print(" ",end="")
            char+=1
        else:
            print(chr(char),end="")
            char+=1



# 1
# 123
# 12345
# 1234567
# 123456789


num = int(input("Enter Number: "))

count=1
for i in range(1,num+1):
    print()
    if i >=2:
        count+=2
    for j in range(1,count+1):
        print(j,end="")



# 1
# 222
# 33333
# 4444444
# 555555555



num = int(input("Enter Number: "))

count=1
for i in range(1,num+1):
    print()
    if i >=2:
        count+=2
    for j in range(1,count+1):
        print(i,end="")


# *****
# ****
# ***
# **
# *



num = int(input("Enter Number: "))

for i in range(1,num+1):
    print()
    for j in range(i,num+1):
        print("*",end="")



# 55555
# 4444
# 333
# 22
# 1

num = int(input("Enter Number: "))
count=0
for i in range(num,0,-1):
    print()
    count+=1
    for j in range(num,count-1,-1):
        print(i,end="")




# 12345
# 1234
# 123
# 12
# 1


num = int(input("Entre NUmber: "))

for i in range(1,num+1):
    print()
    for j in range(1,num-i+2):
        print(j,end="")



# ABCDE
# ABCD
# ABC
# AB
# A

num = int(input("Entre NUmber: "))

for i in range(1,num+1):
    print()
    count=65
    for j in range(1,num-i+2):
        print(chr(count),end="")
        count+=1


# ABCDE
# A  D
# A C
# AB
# A


num = int(input("Enter Number: "))


for i in range(num,0,-1):
    print()
    char=65
    for j in range(1,i+1):
        if 3 <= i <num and j >= 2 and j < i:
            print(" ",end="")
            char+=1
        else:
            print(chr(char),end="")
            char+=1




#     1
#    12
#   1*3
#  1**4
# 12345


num = int(input("Enter Number: "))


for i in range(1,num+1):
    print()
    for l in range(1,num-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        if 3 <= i <num and j >= 2 and j < i:
            print("*",end="")
        else:
            print(j,end="")



#     A
#    AB
#   A*C
#  A**D
# ABCDE



num = int(input("Enter Number: "))


for i in range(1,num+1):
    print()
    char = 65
    for l in range(1,num-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        if 3 <= i <num and j >= 2 and j < i:
            print("*",end="")
            char+=1
        else:
            print(chr(char),end="")
            char+=1
                        


#     A
#    AB
#   ABC
#  ABCD
# ABCDE





num = int(input("Enter Number: "))


for i in range(1,num+1):
    print()
    char = 65
    for l in range(1,num-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        print(chr(char),end="")
        char+=1
            



#     A
#    AB
#   A_C
#  A__D
# ABCDE



num = int(input("Enter Number: "))


for i in range(1,num+1):
    print()
    char = 65
    for l in range(1,num-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        if 3 <= i <num and j >= 2 and j < i:
            print("_",end="")
            char+=1
        else:
            print(chr(char),end="")
            char+=1
            



# ABCDE
#  A__D
#   A_C
#    AB
#     A

num = int(input("Enter Number: "))


for i in range(num,0,-1):
    print()
    char = 65
    for l in range(1,num-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        if 3 <= i <num and j >= 2 and j < i:
            print("_",end="")
            char+=1
        else:
            print(chr(char),end="")
            char+=1
            

#     *
#    * *
#   * * *
#  * * * *
# * * * * *
num = int(input("Enter Number: "))

for i in range(1,num+1):
    print()
    for j in range(1,num-i+1):
        print(" ",end="")
    for l in range(1,i+1):
        print("* ",end="")



#     1
#    123
#   12345
#  1234567
# 123456789

num = int(input("Enter Number: "))
count=0
for i in range(1,num+1):
    print()
    count+=2
    for j in range(1,num-i+1):
        print(" ",end="")
    for k in range(1,count):
        print(k,end="")
    


#     A
#    ABC
#   ABCDE
#  ABCDEFG
# ABCDEFGHI

num = int(input("Enter Number: "))
count=0
for i in range(1,num+1):
    print()
    count+=2
    char= 65
    for j in range(1,num-i+1):
        print(" ",end="")
    for k in range(1,count):
        print(chr(char),end="")
        char+=1
    

#     *
#    *_*
#   *___*
#  *_____*
# *********

num = int(input("Enter Number: "))
count=0
for i in range(1,num+1):
    print()
    count+=2
    char= 65
    for j in range(1,num-i+1):
        print(" ",end="")
    for k in range(1,2):
        print("*",end="")
    if i >= 2 and i < num:
        for p in range(1,count-2):
            print("-",end="")
        for s in range(1,2):
            print("*",end="")
    elif i == num:
        for h in range(1,num*2-1):
            print("*",end="")
    
    
#     1
#    1*1
#   1***1
#  1*****1
# 111111111

num = int(input("Enter Number: "))
count=0
for i in range(1,num+1):
    print()
    count+=2
    char= 65
    for j in range(1,num-i+1):
        print(" ",end="")
    for k in range(1,2):
        print("1",end="")
    if i >= 2 and i < num:
        for p in range(1,count-2):
            print("*",end="")
        for s in range(1,2):
            print("1",end="")
    elif i == num:
        for h in range(1,num*2-1):
            print("1",end="")
    
    
#     A
#    B B
#   C   C
#  D     D
# EEEEEEEEE

num = int(input("Enter Number: "))
char=64
count=0
for i in range(1,num+1):
    
    print()
    count+=2
    char+=1
    for j in range(1,num-i+1):
        print(" ",end="")
    for k in range(1,2):
        print(chr(char),end="")
    if i >= 2 and i < num:
        for p in range(1,count-2):
            print(" ",end="")
        for s in range(1,2):
            print(chr(char),end="")
    elif i == num:
        for h in range(1,num*2-1):
            print(chr(char),end="")
    
    
#     #
#    *#*
#   **#**
#  ***#***
# ****#****

num = int(input("Enter Number: "))

for i in range(1,num+1):
    print()
    for j in range(1,num-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        if i>=2 and k!=i:
            print("*",end="")
        else:
            print("#",end="")
            for p in range(1,i):
                print("*",end="")



# *********
#  ******* 
#   *****  
#    ***
#     *

num = int(input("Enter Number: "))
count=0
for i in range(1,num+1):
    print()
    for l in range(1,i):
        print(" ",end="")
    for j in range(i,num*2-i+1):
        print("*",end="")



#  * * * * *
#   * * * *
#    * * *
#     * *
#      *

num = int(input("Enter Number: "))
count=0
for i in range(1,num+1):
    print()
    for l in range(1,i):
        print(" ",end="")
    for j in range(i,num+1):
        print(" *",end="")



# 123456789
#  1234567
#   12345
#    123
#     1

num = int(input("Enter Number: "))
count=0
for i in range(1,num+1):
    print()
    for l in range(1,i):
        print(" ",end="")
    for j in range(1,num*2-i-i+2):
        print(j,end="")



# x
# xx
# xxx
# xxxx
# xxx
# xx
# x

num = int(input("Enter Number: "))

for i in range(1,num+1):
    print()
    for j in range(1,i+1):
        print("X",end="")
for p in range(1,num):
    print()
    for q in range(i,p,-1):
        print("X",end="")



# 1
# 12
# 123
# 1234
# 12345
# 1234
# 123
# 12
# 1

num = int(input("Enter Number: "))

for i in range(1,num+1):
    print()
    for j in range(1,i+1):
        print(j,end="")
for p in range(1,num):
    print()
    for q in range(1,i-p+1):
        print(q,end="")



#    1
#   12
#  123
# 1234
#  123
#   12
#    1


num = int(input("Enter Number: "))

for i in range(1,num+1):
    print()
    for j in range(1,num-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end="")
for p in range(1,num):
    print()
    for q in range(1,p+1):
        print(" ",end="")
    for h in range(1,num-p+1):
        print(h,end="")

# 1
# 1 2
# 1  3
# 1   4
# 1  3
# 1 2
# 1


num = int(input("Enter Number: "))

for i in range(1,num+1):
    print()
    for l in range(1,2):
        print(l,end="")
    if i>=2:
        for j in range(1,i):
            print(" ",end="")
    
        for k in range(i,i+1):
            print(i,end="") 
for q in range(1,num):
    print()
    for t in range(1,2):
        print(t,end="")
    for h in range(q,num-2+1):
        print(" ",end="")
    if q < num-1:
        for s in range(num-q,num-q+1):
            print(s,end="")

   




#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *


num  = int(input("Enter Number: "))

for i in range(1,num+1):
     print()
     for j in range(1,num-i+1):
          print(" ",end="")
     for k in range(num-i,num-i+1):
          print("*",end="")
     if i>=2:
          for l in range(num+2-i,num+i-1):
               print("*",end="")
          for p in range(num+i-1,num+i):
               print("*",end="")
     
for a in range(1,num):
     print()
     for b in range(num-a,num):
          print(" ",end="")
     for c in range(a,a+1):
          print("*",end="")
     for d in range(a+1,num*2-a-2):
          print("*",end="")
     if a == num-1:
          pass
     else:
          for e in range(num+a+1,num+a+2):
               print("*",end="")
     

# ***********
# ****   ****
# ***     ***
# **       **
# *         *

num  = int(input("Enter Number: "))

for i in range(1,num+1):
     print()
     for j in range(num,i-1,-1):
          print("*",end="")
     if i >=2:
          for k in range(num+1,num+2*i):
               print(" ",end="")
     else:
          print("*",end="")
     for k in range(num+2,num*2+3-i):
          print("*",end="")




# *         *
# **       **
# ***     ***
# ****   ****
# ***** *****


num = int(input("Enter Number: "))

count=0
for i in range(1,num+1):
    print()
    count+=1
    for j in range(1,i+1):
        print("*",end="")
    for k in range(i,num*2+1-count):
        print(" ",end="")
    for f in range(1,i+1):
        print("*",end="")


# ***** *****
# ****   ****
# ***     ***
# **       **
# *         *
# *         *
# **       **
# ***     ***
# ****   ****
# ***** *****


num = int(input("Enter Number: "))

for i in range(1,num+1):
     print()
     for j in range(num,i-1,-1):
          print("*",end="")
     if i >=2:
          for k in range(num+1,num+2*i):
               print(" ",end="")
     else:
          print("*",end="")
     for k in range(num+2,num*2+-i):
          print("*",end="")
count=0
for i in range(1,num+1):
    print()
    count+=1
    for j in range(1,i+1):
        print("*",end="")
    for k in range(i,num*2+1-count):
        print(" ",end="")
    for f in range(1,i+1):
        print("*",end="")




#     1
#     2
#     3
#     4
# 123454321
#     4
#     3
#     2
#     1


num = int(input("Enter Number: "))

for i in range(1,num+1):
    print()
    if i < num:
        for j in range(1,num):
            print(" ",end="")
    else:
        for k in range(1,num):
            print(k,end="")
    for p in range(1,2):
        print(i,end="")
    if i == num:
        for g in range(num-1,0,-1):
            print(g,end="")

for l in range(num-1,0,-1):
    print()
    for s in range(1,num):
        print(" ",end="")
    for h in range(1,2):
        print(l,end="")


#      1
#     101
#    10101
#   1010101
#  101010101



num  = int(input("Enter Number: "))
count=1
for i in range(1,num+1):
    print()
    count+=2
    for k in range(1,num-i+1):
        print(" ",end="")
    for j in range(1,count-1):
        if j%2==0:
            print("0",end="")
        else:
            print("1",end="")

# *       * 
#   *   *   
#     *     
#   *   *   
# *       * 

num = int(input("Enter Number: "))

for i in range(1,num+1):
    print()
    for k in range(1,num+1):
        if i==k or i+k==num+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")


#  
#      
# | \    / |
# |  \  /  |
# |   \/   |
# |   /\   |
# |  /  \  | 
# | /    \ |

# \    /
#  \  /
#   \/
#   /\
#  /  \
# /    \

num = int(input("Enter Number: "))
count=1
for i in range(1,num+1):
    print()
    count+=2
    for j in range(0,i-1):
        print(" ",end="")
    for k in range(1,2):
        print("\\",end="")
    for l in range(1,num*2-count+2):
        print(" ",end="")
    for h in range(1,2):
        print("/",end="")
count2=0
for p in range(1,num+1):
    print()
    if i >= 2:
        count2+=2
    for q in range(num-p,0,-1):
        print(" ",end="")
    for r in range(1,2):
        print("/",end="")
    for s in range(1,count2-1):
        print(" ",end="")
    for t in range(1,2):
        print("\\",end="")


#    *
#   *_*
#  *___*
# *_____*
#  *___*
#   *_*
#    *



num  = int(input("Enter Number: "))

for i in range(1,num+1):
     print()
     for j in range(1,num-i+1):
          print(" ",end="")
     for k in range(num-i,num-i+1):
          print("*",end="")
     if i>=2:
          for l in range(num+2-i,num+i-1):
               print("_",end="")
          for p in range(num+i-1,num+i):
               print("*",end="")
     
for a in range(1,num):
     print()
     for b in range(num-a,num):
          print(" ",end="")
     for c in range(a,a+1):
          print("*",end="")
     for d in range(a+1,num*2-a-2):
          print("_",end="")
     if a == num-1:
          pass
     else:
          for e in range(num+a+1,num+a+2):
               print("*",end="")



'''84.
    1
   212
  32123
 4321234
543212345'''

num = int(input("Enter Number: "))

for i in range(1,num+1):

    #spaces
    for spaces in range(1,num-i+1):
        print(" ",end="")

    #left numbers
    for numbers in range(i,0,-1):
        print(numbers,end="")
   
    #right numbers
    for numbers in range(2,i+1):
        print(numbers,end="")
    
    print()




#    *
#   *_*
#  *_*_*
# *_*_*_*
#  *_*_*
#   *_*
#    *


num  = int(input("Enter Number: "))
count=1
for i in range(1,num+1):
    print()
    count+=2
    for k in range(1,num-i+1):
        print(" ",end="")
    for j in range(1,count-1):
        if j%2==0:
            print("_",end="")
        else:
            print("*",end="")







'''71.
123456789
 1234567
  12345
   123
    1'''

num = int(input("Enter Number: "))
for i in range(1,num+1):

    #spaces
    for spaces in range(1,i):
        print(" ",end="")
    #numbers
    for star in range(1,num*2+2-i*2):
            print(star,end="")
    print()



'''58.
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5'''

num = int(input("Enter Number: "))

for i in range(1, num + 1):

    # spaces
    for space in range(num - i):
        print(" ", end="")

    # star
    for star in range(1,i*2):
        if star%2!=0:
            print(star//2+1,end="")
        else:
            print(" ",end="")
    print()




