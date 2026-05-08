# ===========1============

num = int(input("Enter number: "))
sum = 0
for i in range(1,num+1):
    sum+=i
print(sum)


# ======2==============



num = int(input("Enter number: "))
fact = 1

for i in range(1,num+1):
    fact*=i
print(fact)




# ==========3=============

num = int(input("Enter number: "))

for i in range(1,11):
    print(f"{num} X i = {num*i}")


# ==========4========

num = int(input("Enter NUmber : "))
n1 = str(num)
n1 = len(n1)
for i in range(1,n1+1):
    num1 = (num)%10
    print(num1,end="")
    num = (num)//10


# ========5=========



num = int(input("Enter Number: "))
n2 = num
n1 = str(num)
n1 = len(n1)
numm = 0

for i in range(1,n1+1):
    num1 = num%10
    numm = numm*10+num1
    num = num//10


if numm == n2:
    print("Palindrome")
else:
    print("Not")


# second method

n= input("Enter number: ")
rev = ""

for i in n:
    rev = i+rev

n1 = int(n)
rev1 = int(rev)
if rev1 == n1:
    print("Plindron")
else:
    print("Not ")


# =====6========


num = int(input("Enter Number: "))
num5 = num
n1 = len(str(num))
arm = 0

for i in range(1,n1+1):
    num1 = num%10
    arm += num1*num1*num1
    num = num//10

print(arm)
print(num5)
if num5 == arm:
    print("Armstrong")
else:
    print("Not")


# real armstrong number find program
num = int(input("Number: "))
num3 = num
sum = 0
num1 = len(str(num))

for i in range(1,num1+1):
    num2 = num%10
    sum=sum+num2**num1
    num = num//10

if num3 == sum:
    print("Armstrong")
else:
    print("Not Armstrong")


# ==========7==============



num = int(input("Enter Number: "))
count1 = 0
count2 = 0

while num > 0:
    num1 = num%10
    if num1%2 == 0:
        count1 += 1
    else:
        count2+=1 
    num = num//10


print("Even count: ",count1)
print("Odd count: ",count2)



# ==============8================




num = int(input("Enter Number: "))
count2 = 0

while num > 0:
    num1 = num%10
    if num1%2 != 0:
        count2 += 1
    num = num//10


print("Odd count: ",count2)


# ===============9-===============




num = int(input("Enter Number: "))
num11 = str(num)
even = 0
while num>0:
    num1 = num%10
    if num1%2==0:
        even+=1
    num = num//10

if even == len(num11):
    print("All Even")
else:
    print("Not All Even")

# ==========10==========



num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

if num1%2!=0:
    num1 = num1+1

for i in range(num1,num2+1,2):
    print(i)



# =========11=========




num = int(input("Enter NUmber: "))
digit = int(input("Enter Digit: "))

count1 = 0
count2 = 0


while num > 0:
    num1 = num%10
    if num1%digit==0:
        count1+=1
    else:
        count2+1
    num = num//10

if digit%2==0:
    print(count1)
else:
    print(count2)


# ==========12========





num = int(input("Enter Number: "))
mul = 1
while num>0:
    num1 = num%10
    mul = mul*num1
    num = num//10
print(mul)


if mul%2==0:
    print("Even")
else:
    print("Odd")


# =========13===========


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1>num2:
    for i in range(num1,num2-1,-1):
        print(i,sep=" → ")
elif num2>num1:
    for i in range(num1,num2+1,1):
        print(i,sep="→")
else:
    print("Both are same")



# ===========14=============


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


if num1>num2:
    for i in range(num1,num2-1,-1):
        print(i,end=" → ")
elif num2>num1:
    for i in range(num1,num2+1,1):
        print(i,end=" → ")
else:
    print("Both are same")

    




