'''2.
A graphics rendering engine displays signal strength in a diamond-shaped visualization.

Write a Python program to print a star diamond pattern.

Input
Enter number of rows: 5

      

    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''
    
    
    
    
num = int(input("Enter Number: "))




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
     



