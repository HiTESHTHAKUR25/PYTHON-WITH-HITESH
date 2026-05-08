# ========1==========
num = int(input("Enter Number: "))
count = 0 

while num > 0:
    num1 = num%10
    if num1>count:
        count = num1
    else:
        count=count
    num = num//10
    
print(count)



# ============2=============


num= int(input("Enter Numnber: "))
num2 = num%10
num//10
while num>0:
    num1 = num%10
    if num1<num2:
        num2 = num1
    else:
        num2 = num2
    num = num//10

print(num2)

# ============3=========



num = int(input("Enter Number: "))
num2 = len(str(num))
count = 0
while num>0:
    num1 = num%10
    count+=1
    if count == num2:
        print(num1)

    num = num//10





# ========4===========


num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

for i in range(num1,num2+1,1):
    if i %3==0:
        print(i)
    


# ==============5==============


num = int(input("Number: "))
count = 0
for i in range(1,num+1):
    if num%i==0:
        count+=1
print(count)

# ===========6=============



num = int(input("Enter Number: "))
count = 0
for i in range(1,num+1):
    if num%i==0:
        count+=i

print("Sum ",count)


# =========7===========



num1 = int(input("Enter Number: "))
num2 = int(input("Enter Power: "))
count = 1
for i in range(1,num2+1):
    count*=2

print(count)



# ============8========



num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
count = 0
for i in range(num1,num2+1,1):
    if i%5==0:
        count+=1

print(count)

# ==========9------------


num = int(input("Enter Number: "))
square = num**2
count = 0

while square >0:
    num2 = square%10
    count+=num2
    square=square//10

if count==num:
    print("Glowing Success! You've found the Neon Number!")
else:
    print("Try again! Not quite glowing yet.")


# =========10==============




num  = int(input("Enter Number: "))
count=0
while num > 0:
    num%10
    if num%2!=0:
        count+=1
    num = num//10

print("Odd Digits Count: ",count)


