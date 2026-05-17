
# 3) X Star Pattern
#     *   *     *    *
#      * *
#       *
#      * *
#     *   *



num = int(input("Enter Number: "))
count=0
count1=0
for i in range(1,num+1):
    print()
    count +=1
    count1 +=1
    for j in range(1,num*2+1):
        if j == num+count:
            print("*",end="")
        elif i+j==6:
            print("*",end="")
        else:
            print(" ",end="")






# 4) Vertical Diamond
#        *
#       * *
#      *   *
#       * *
#        *
   


num = int(input("Enter Number: "))


for i in range(1,num+1):
   print()
   for j in range(i,num):
        print(" ",end="")
   print("*",end="")
   for k in range(2,2*i+1):
        print(" ",end="")
   if i != 1:
      print("*",end="")
    

if j ==5:
     print("")





# 14) Spiral Number Square
#      1   2   3   4
#     12  13  14   5
#     11  16  15   6
#     10   9   8   7



num = int(input("Enter Number: "))
count=1
for i in range(1,num+1):
     print()
     for j in range(1,num+1):
          print(count,end="  ")
          count+=1
