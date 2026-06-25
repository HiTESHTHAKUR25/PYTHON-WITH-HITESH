# recursion:
# Assignment 1: Smart Street Lights (Fibonacci Series)

# A smart city installs street lights in a newly developed area. The number of lights installed each month follows the Fibonacci pattern.

# Month 1 → 0 lights
# Month 2 → 1 light
# Every following month, the number of lights installed is the sum of the previous two months.

# As a software developer, your task is to help the city planning department generate the installation schedule.

# Task

# Write a recursive function to print the first N Fibonacci numbers.

# Input
# Enter the number of months:
# 7
# Output
# 0 1 1 2 3 5 8


def light(n):
    if n <= 1:
        return n
    return light(n-1)+light(n-2)


def main():
    for i in range(7):
        print(light(i),end=" ")

main()





# Assignment 2: Binary Converter for Embedded System

# An embedded systems company develops microcontrollers that understand only binary values. Engineers enter decimal numbers, and the software must convert them into binary before sending them to the device.

# As a software developer, write a recursive program to perform this conversion.

# Task

# Write a recursive function to convert a decimal number into its binary representation.

# Input
# Enter a decimal number:
# 25
# Output
# Binary Number = 11001

# Note: Do not use Python's built-in bin() function.


def binary(n):
    if n == 0 or n == 1:
        return n
    return n%2

def main():
    a = ""
    i = 25
    while i > 0:
        a += str(binary(i))
        i= i//2
    
    print(a[::-1])
main()





# Assignment 4:
#  Lottery Ticket Verification (Count Occurrences Using Recursion)

# A lottery company assigns a unique ticket number to every participant. Before announcing the results, the company wants to determine how many times a lucky digit appears in a ticket number. This helps identify tickets eligible for special bonus rewards.

# As a software developer, your task is to write a recursive Python program that counts the number of times a given digit appears in the ticket number.

# Task

# Write a recursive function to count the occurrences of a given digit in a ticket number.

# Input Format
# The first line contains an integer representing the Ticket Number.
# The second line contains an integer representing the Lucky Digit.
# Output Format

# Display the number of times the lucky digit appears in the ticket number using the format:

# Digit <Lucky Digit> appears <Count> times.
# Sample Input
# Enter Ticket Number:
# 1122334412

# Enter Lucky Digit:
# 2
# Sample Output
# Digit 2 appears 3 times.
# Sample Input 2
# Enter Ticket Number:
# 987654321

# Enter Lucky Digit:
# 5
# Sample Output 2
# Digit 5 appears 1 time.
# Sample Input 3
# Enter Ticket Number:
# 11111111

# Enter Lucky Digit: 
# 2
# Sample Output 3
# Digit 2 appears 0 times.


def lucky(n,n1):
    if n == 0:
        return 0
    
    if n%10 == n1:
        return 1+lucky(n//10,n1)
    else:
        return lucky(n//10,n1)

def main():
    n = int(input("Enter Number: "))
    n1 = int(input("Enter Find number: "))
    x = lucky(n,n1)
    print(x)

main()




#  23/06/2026


# 4.
# Assignment 10: Cyber Security (Strong Password Check)

# A cybersecurity company considers a numeric password to be "strong" if every digit is even.

# Task

# Write a recursive function to check whether all digits of the given number are even.

# Input 1
# Enter Password:
# 248620
# Output 1
# Strong Password
# Input 2
# Enter Password:
# 248621
# Output 2
# Weak Password


def passwd(n):
    if n==0:
        return True
    digit = n%10
    
    if digit%2 != 0:
        return False
    
    return passwd(n//10)

def main():
    x = int(input("Enter Number: "))
    if passwd(x):
        print("Strong Password")
    else:
        print("Weak Password")

main()    





# 5.
#  Hospital Record System (Search Digit)


# A hospital stores patient IDs as numbers. The administrator wants to verify whether a specific digit exists in a patient ID.

# Task

# Write a recursive function to determine whether a given digit is present.

# Input
# Enter Patient ID:
# 5837264

# Enter Digit:
# 7
# Output
# Digit Found

def digit(n,n1):

    if n == 0:
        return False

    digits = n%10
    if n1 == digits:
        return True
    
    return digit(n//10,n1)


def main():
    x = int(input("Enter Patient ID: "))
    x1 = int(input("Enter Digit: "))

    if digit(x,x1):
        print("Digit Found")
    else:
        print("Not Found")


main()

    


# 6.
#  Mobile Recharge System

# A telecom company issues lucky recharge coupons only if the coupon number is prime.

# Task

# Write a recursive function to determine whether a given number is prime.

# Input
# Enter Coupon Number:
# 29
# Output
# Prime Number



def prime(n,n1):
    
    if n1 == 1:
        return True
    
    if n%n1==0:
        return False
    
    return prime(n,n1-1)


def main():
    x = int(input("Enter Number: "))

    if x<2:
        print("Not Prime Number")
    elif prime(x,x-1):
        print("Prime Number")
    else:
        print("Not Prime")


main()




