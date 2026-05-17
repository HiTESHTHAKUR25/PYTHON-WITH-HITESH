# 1) Hollow Pyramid
#         *
#        * *        
#       *   *
#      *     *
#     *********

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
            print(" ",end="")
        for s in range(1,2):
            print("*",end="")
    elif i == num:
        for h in range(1,num*2-1):
            print("*",end="")


         



# 2) Hollow Rectangle
#     *********
#     *       *
#     *       *
#     *       *
#     *********


num = int(input("Enter Numbre: "))

for i in range(1,num+1):
    print()
    for j in range(2,num*2):
        if i == 1 or i == num:
            print("*",end="")
        else:
            if j == 2 or j == num*2-1:
                print("*",end="")
            else:
                print(" ",end="")    


 


 
# 3) X Star Pattern
#     *   *     
#      * *
#       *
#      * *
#     *   *



num = int(input("Enter Number: "))

for i in range(1,num+1):
    print()
    for k in range(1,num+1):
        if i==k or i+k==num+1:
            print("*",end="")
        else:
            print(" ",end="")




# 4) Vertical Diamond
#        *
#       * *
#      *   *
#     *     *
#      *   *
#       * *
#        *

num  = int(input("Enter Number: "))

for i in range(1,num+1):
     print()
     for j in range(1,num-i+1):
          print(" ",end="")
     for k in range(num-i,num-i+1):
          print("*",end="")
     if i>=2:
          for l in range(num+2-i,num+i-1):
               print(" ",end="")
          for p in range(num+i-1,num+i):
               print("*",end="")
     
for a in range(1,num):
     print()
     for b in range(num-a,num):
          print(" ",end="")
     for c in range(a,a+1):
          print("*",end="")
     for d in range(a+1,num*2-a-2):
          print(" ",end="")
     if a == num-1:
          pass
     else:
          for e in range(num+a+1,num+a+2):
               print("*",end="")
     

# 5) Number-Star Palindrome
#     12344321
#     123**321
#     12****21
#     1******1


num = int(input("Enter Number: "))

for i in range(1,num+1):
     print()
     for j in range(1,num+2-i):
          print(j,end="")
     if i >= 2:
          for k in range(1,i):
               print("**",end="")
     for l in range(num-i+1,0,-1):
          print(l,end="")




# 6) Number Triangle with Dashes
#     - - - - 1
#     - - - 2 3
#     - - 3 4 5
#     - 4 5 6 7
#     5 6 7 8 9


num = int(input("Enter Number: "))

for i in range(1,num+1):
     count=i
     print()
     for j in range(1,num-i+1):
          print("-",end=" ")
     for k in range(num-i,num):
          print(count,end=" ")
          count+=1
         


# 7) Reverse Number Triangle
#     - - - -
#     2 - - -
#     4 3 - -
#     6 5 4 -
#     8 7 6 5



num = int(input("Enter Number: "))


for i in range(1,num+1):
     print()
     count = i
     for j in range(num-i+1,num):
          print(count,end=" ")
          count+=1
     for k in range(i,num):
          print("-",end=" ")



# 8) Border Number Pattern
#     1 2 3 4 5
#     2       5
#     3       5
#     4       5
#     5 5 5 5 5


num = int(input("Enter Number: "))

for i in range(1,num+1):
     print()
     if i >= 2:
          for j in range(1,num+1):
               if j == 1:
                    print(i,end=" ")
               elif j == num:
                    print(num,end=" ")
               elif i == num:
                    print(num,end=" ")
               else:
                    print(" ",end=" ")
     else:
          for l in range(1,num+1):
               print(l,end=" ")

# 9) Hollow Diamond Square   {mistake}
#     ***********
#     ****   ****
#     ***     ***
#     **       **
#     *         *
#     *         *
#     **       **
#     ***     ***
#     ****   ****
#     ***********

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

for p in range(1,num+1):
     print()
     for q in range(num-p+1,num+1):
          print("*",end="")
     for k in range(p,num*2-p+1):   # isme spaces ko odd me print karani he 
          print(" ",end="")
     for k in range(num*2-p,num*2):
          print("*",end="")

          
# 10) Slanted Star Block
#     ****
#      ****
#       ****
#        ****


num = int(input("Enter Number: "))

for i in range(1,num+1):
     print()
     for j in range(1,num+i):
          print(" ",end="")
     for k in range(num,num+4):
          print("*",end="")


# 11) Butterfly Number Pattern {mistake}
#     1      1
#     12    21
#     123  321
#     12344321
#     123  321
#     12    21
#     1      1




num = int(input("Enter Number: "))
count=3
for i in range(1,num+1):
     print()
     for j in range(1,i+1):
          print(j,end="")
     for k in range(i+1,num*2-i+1):
          print(" ",end="")
     for l in range(i,0,-1):
          print(l,end="")
for p in range(num-1,0,-1):
     print()
     for j in range(1,p+1):
          print(j,end="")
     for k in range(p+1,num*2-p+1):
          print(" ",end="")
     for l in range(p,0,-1):
          print(l,end="")
          

# 12) Hollow Diamond Numbers {mistake}
#        1
#       2 2
#      3   3
#     4     4
#      3   3
#       2 2
#        1


num = int(input("Enter Number: "))

#    1
#   1 2
#  1   3
# 1     4
#  1   3
#   1 2
#    1


for i in range(1,num+1):
     print()
     for j in range(1,num-i+1):
          print(" ",end="")
     for k in range(num-i,num-i+1):
          print(i,end="")
     if i>=2:
          for l in range(num+2-i,num+i-1):
               print(" ",end="")
          for p in range(num+i-1,num+i):
               print(p,end="")
     
for a in range(1,num):
     print()
     for b in range(num-a,num):
          print(" ",end="")
     for c in range(a,a+1):
          print(c,end="")
     for d in range(a+1,num*2-a-2):
          print(" ",end="")
     if a == num-1:
          pass
     else:
          for e in range(num+a+1,num+a+2):
               print(e,end="")
     


# 13) Number X Pattern
#     1   5
#      2 4
#       3
#      2 4
#     1   5



num = int(input("Enter Number: "))

for i in range(1,num+1):
    print()
    for k in range(1,num+1):
        if i==k or i+k==num+1:
            print(k,end="")
        else:
            print(" ",end="")


# 15) Zig-Zag Star
#     *   *   *
#       *   *
#     *   *   *


num = int(input("Enter number: "))
num = num+1
for i in range(1,num):
     print()
     for j in range(1,num):
          if i%2==0 :
               if j < num-1:
                    print("   *",end="")
          else:
               print(" * ",end=" ")




# 16) Palindrome Pyramid
#             1
#            121
#           12321
#          1234321
#         123454321


num = int(input("Enter Number: "))

for i in range(1,num+1):
     print()


     for j in range(1,num-i+1):
          print(" ",end="")


     for k in range(1,i+1):
          print(k,end="")


    
     for l in range(i-1,0,-1):
         print(l,end="")




# 17) Hollow Hourglass
#      * * * * *
#       *     *
#         * *
#          *
#         * *
#       *     *
#      * * * * *


num = int(input("Enter Number: "))


for i in range(1,num+1):
     print()
     for j in range(1, num+1):
          if i == 1 or i == num:
               for l in range(1,2):
                    print("*",end=" ")
          elif i == j or i+j==num+1:
               print("*",end=" ")
          else:
               print(" ",end=" ")




# 18) Binary Floyd Triangle
#     1
#     0 1
#     1 0 1
#     0 1 0 1



num = int(input("Enter Number: "))

for i in range(1,num+1):
     print()
     for j in range(1,i+1):
          if 1==i or (i+j)%2==0:
               print("1",end=" ")
          else:
               print("0",end=" ")




# 19) Reverse Number Cross
#     5   5
#      4 4
#       3
#      4 4
#     5   5


num = int(input("Enter Number: "))

count=1
numm = 0
for i in range(1,num+1):
     numm+=2
     print()
     for j in range(1,num+1):
          if i==j or i+j==num+1:
               if j<num//2+1 and i < num//2+1 :
                    print(j+num-count,end="")
               elif j<num//2+1 and i > num//2+1:
                    print(j+numm-num-1,end="")
               else:
                    print(j,end="")
               count+=1
          else:
               print(" ",end="")






# 20) Continuous Diamond Numbers
#            1
#           2 3
#          4 5 6
#         7 8 9 10
#          4 5 6
#           2 3
#            1


num   = int(input("Enter Number: "))

count=1
for i in range(1,num+1):
     print()
     for j in range(1,num-i+1):
          print(" ",end="")

     for k in range(1,i+1):
          print(f"{count} ",end="")
          count+=1
for p in range(1,num):
     print()
     for q in range(1,p+1):
          print(" ",end="")
     for s in range(1,num-p+1):
          if p>=2:
               print(num-p+s-1,end=" ")
          else:
               print(num-p+s,end=" ")









# 21) Inverted Hollow Pyramid
#     *********
#      *     *
#       *   *
#        * *
#         *



num = int(input("Enter Number: "))


for i in range(1,num+1):
     print()
     if i == 1:
          for j in range(1,num*2):
               print("*",end="")
     else:
          for k in range(1,i):
               print(" ",end="")
          print("*",end="")

          for p in range(1, 2 * (num - i)):
               print(" ", end="")
          if i != num:
               print("*", end="")






# 22) Plus Star Pattern
#         *
#         *
#     *********
#         *
#         *

num = int(input("Enter Number: "))
numm = num//2+1
for i in range(1,num+1):
     print()
     if i==numm:
          for j in range(1,num*2):
               print("*",end="")
     else:
          for i in range(1,num):
               print(" ",end="")
          for k in range(1,2):
               print("*",end="")


# 23) Number Sandglass {mistake}
#     123454321
#      1234321
#       12321
#        121
#         1
#        121
#       12321
#      1234321
#     123454321


num = int(input("Enter Number: "))


for i in range(1,num+1):
    print()
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,num-i+2):
        print(k,end="")
    for l in range(num-1,i-1,-1):
        print(l,end="")

for p in range(1,num):
    print()
    for q in range(1,num-p):
        print(" ",end="")
    for r in range(1,p+2):
        print(r,end="")
    for s in range(num+1,num-p+1,-1):
        print(s,end="")



# 24) Right Hollow Number Triangle
#     1                     
#     12
#     1 3
#     1  4
#     12345




num = int(input("Enter Number: "))
count=3
for i in range(1,num+1):
     print()
     for j in range(1,2):
          print(1,end="")
          if i == num:
               for l in range(2,num+1):
                    print(l,end="")
          elif i == j+1 == 2:
               print(2,end="")
          else:
               for p in range(1,i-1):
                    print(" ",end="")
               if i >= 3:
                    for q in range(1,2):
                         print(count,end="")
                         count+=1
               



# 25) Continuous Number Pyramid
#             1
#            2 3
#           4 5 6
#          7 8 9 10


num   = int(input("Enter Number: "))

count=1
for i in range(1,num+1):
     print()
     for j in range(1,num-i+1):
          print(" ",end=" ")
     for k in range(1,i+1):
          print(f"{count} ",end=" ")
          count+=1

# 26) Hollow Square
#     *****
#     *   *
#     *   *
#     *   *
#     *****


num = int(input("Enter Number: "))


for i in range(1,num+1):
     print()
     for j in range(1,num+1):
          if i == 1 or i == num:
               print("*",end="")
          else:
               if j == 1 or j == num:
                    print("*",end="")
               else:
                    print(" ",end="")



# 27) Diagonal Number Square
#     1 - - -
#     - 2 - -
#     - - 3 -
#     - - - 4


num = int(input("Enter Number: "))


for i in range(1,num+1):
     print()
     for j in range(1,num+1):
          if i == j:
               print(i,end=" ")
          else:
               print("-",end=" ")


