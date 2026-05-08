# 1. Utility Toolkit System

# You are developing a Utility Toolkit Application for a small office. Employees use this tool to quickly perform common number operations like checking prime numbers, reversing numbers, etc.

# The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

# Menu Options:
# 1 → Check Prime Number
# 2 → Check Palindrome Number
# 3 → Reverse a Number
# 4 → Count Digits
# 5 → Exit

# Sample Run 1:
# Input:
# Enter your choice: 1
# Enter number: 7

# Output:
# 7 is a Prime Number

# Sample Run 2:
# Input:
# Enter your choice: 2
# Enter number: 121

# Output:
# 121 is a Palindrome Number

# Sample Run 3:
# Input:
# Enter your choice: 3
# Enter number: 456

# Output:
# Reversed Number is: 654

# Sample Run 4:
# Input:
# Enter your choice: 4
# Enter number: 98765

# Output:
# Total digits: 5

# Sample Run 5 (Invalid Choice):
# Input:
# Enter your choice: 9

# Output:
# Invalid choice. Please try again.

# Sample Run 6 (Exit):
# Input:
# Enter your choice: 5

# Output:
# Exiting program... Thank you!

# Requirements:

# * Use while loop to repeat menu
# * Use match-case for decision making
# * Handle negative numbers properly
# * Use only loops and conditions

count = 0
rev = 0
while True:
    print()
    print('''---Menu Options---
1 → Check Prime Number
2 → Check Palindrome Number
3 → Reverse a Number
4 → Count Digits
5 → Exit''')
    print()
    choice = int(input("Choose A Option: "))

    match choice:
        case 1:
            count=0
            num = int(input("Enter Number: "))
            for i in range(1,num+1):
                if num%i==0:
                    count+=1
            if count==2:
                print(num,"is a Prime Number")
            else:
                print("Not Prime")
        case 2:
            num = int(input("Enter Number: "))
            num1 = num
            rev = 0
            while num>0:
                num2 = num%10
                rev = 10*rev+num2
                num = num//10
            
            if rev == num1:
                print(num1,"is a Palindrome Number")
            else:
                print("Not Plindrome")
        case 3:
            num = int(input("Enter NUmber: "))
            rev = 0
            while num>0:
                num2 = num%10
                count +=1
                rev = 10*rev+num2
                num = num//10
            print("Reversed Number is: ",rev)
        case 4:
            num = int(input("Enter Number: "))
            print("Total Digit is: ",len(str(num)))
        case 5:
            print("Exiting program... Thank you!")
            break
        case _:
            print("Invalid choice. Please try again.")
print()
        
    

# 2.
#  Employee Salary Processor

# Scenario:
# You are developing an Employee Salary Processing System for a company’s HR department. The system is used to manage and calculate employee salary details such as allowances, tax deductions, and final payable salary.

# The HR staff may not always follow the correct sequence while using the system. For example, they might try to calculate net salary or tax before entering the basic salary. Your program must handle such situations properly.

# 👉 Important Condition:
# If the Basic Salary is not entered, the system should display:
# "Please enter basic salary first"
# and should not perform any further calculations.

# The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

# Menu Options:
# 1 → Enter Basic Salary
# 2 → Calculate HRA (20%) and DA (10%)
# 3 → Calculate Net Salary
# 4 → Tax Deduction

# * Salary > 50000 → 10% tax
# * Otherwise → 5% tax
#   5 → Display Salary Slip
#   6 → Exit

# ---

# Sample Run 1:
# Input:
# Enter your choice: 3

# Output:
# Please enter basic salary first

# ---

# Sample Run 2:
# Input:
# Enter your choice: 1
# Enter Basic Salary: 40000

# Output:
# Basic Salary recorded successfully

# ---

# Sample Run 3:
# Input:
# Enter your choice: 2

# Output:
# HRA: 8000
# DA: 4000

# ---

# Sample Run 4:
# Input:
# Enter your choice: 3

# Output:
# Net Salary (before tax): 52000

# ---

# Sample Run 5:
# Input:
# Enter your choice: 4

# Output:
# Tax Deduction: 5200

# ---

# Sample Run 6:
# Input:
# Enter your choice: 5

# Output:
# ----- Salary Slip -----
# Basic Salary: 40000
# HRA: 8000
# DA: 4000
# Net Salary: 52000
# Tax: 5200
# Final Salary: 46800

# ---

# Sample Run 7 (Invalid Choice):
# Input:
# Enter your choice: 9

# Output:
# Invalid choice. Please try again.

# ---

# Sample Run 8 (Exit):
# Input:
# Enter your choice: 6

# Output:
# Exiting program... Thank you!


print('''
# Menu Options:
1 → Enter Basic Salary
2 → Calculate HRA (20%) and DA (10%)
3 → Calculate Net Salary
4 → Tax Deduction
5 → Salary Slip
6 → Exit''')
salary = 0
salary2 = 0
hra = 0
da = 0
tax = 0
while True:
    choice = int(input("Choose one option: "))
    match choice:
        case 1:
            salary1 = int(input("Enter Basic Salary: "))
            salary = salary1
            salary2 = salary1
            print("Basic Salary recorded successfully")
            hra1 = salary*0.2
            da1 = salary * 0.1
            hra = hra1
            da = da1
        case 2:
            if salary ==0:
                print("Enter Basic Salary FIrst")
            else:
                print("HRA: ",hra)
                print("DA: ",da)
                salary += hra+da 
        case 3:
            if salary ==0:
                print("Enter Basic Salary FIrst")
            else:
                print("Net Salary (before tax): ",salary+hra+da)
        case 4:
            if salary ==0:
                print("Enter Basic Salary FIrst")
            elif salary >50000:
                tax1 = salary*0.1
                tax = tax1
                print("Tax Deducation: ",tax)
            else:
                tax1 = salary*0.05
                tax = tax1
                print("Tax Deduction: ",tax)
                salary -= tax
        case 5:
            if salary ==0:
                print("Enter Basic Salary FIrst")
            else:
                print("----- Salary Slip -----")
                print("Basic Salary:",salary2)
                print("HRA: ",hra)
                print("DA: ",da)
                print("Net Salary: ",salary2+hra+da)
                print("Tax: ",tax)
                print("Final Salary: ",salary2+hra+da-tax)
                choice -=1
        case 6:
            print("Exiting program... Thank you!")
            break
        case _: 
            if salary ==0:
                print("Enter Basic Salary FIrst")
            else:
                print("Invalid choice. Please try again.")
    print()    




# 3.

#  Smart Banking System

# Scenario:
# You are developing a Smart Banking System for a bank to help customers perform basic banking operations such as deposit, withdrawal, balance checking, and interest calculation.

# Sometimes, users may try to withdraw money or check balance before depositing any amount. Your system must handle such situations properly.

# 👉 Important Condition:
# If no amount has been deposited yet, the system should display:
# "No balance available. Please deposit first"
# and should not allow withdrawal, balance check, or interest calculation.

# The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

# Menu Options:
# 1 → Deposit Money
# 2 → Withdraw Money
# 3 → Check Balance
# 4 → Apply Interest

# * Balance > 50000 → 5% interest
# * Otherwise → 3% interest
#   5 → Exit

# ---

money = 0
money2 = 0
tax = 0 
num1 = 0 
num2 = 0 
num3 = 0 



while True:
    print('''
---Menu Options---
1 → Deposit Money
2 → Withdraw Money
3 → Check Balance
4 → Apply Interest
5 → Exit''')

    choice = int(input("Choose A Number: "))
    match choice:
        case 1:
            money = int(input("Enter amount to deposit: "))
            print("Amount deposited successfully")
            money2 = money
        case 2:
            if money == 0:
                print("No balance available. Please deposit first")
            else:
                num3 = int(input("Enter amount to withdraw: "))
                if num3 > money:
                    print("Insufficient balance")
                else:
                    money2 = money-num3
                    print("Withdrawal successful")
        case 3:
            if money == 0:
                print("No balance available. Please deposit first")
            else:
                print("Current Balance: ",money2)
        case 4:    
            if money == 0:
                print("No balance available. Please deposit first")
            else:
                if money>50000:
                    tax = money*0.05
                    money2+=tax
                    print("Interest added: ",money2)
                else:
                    tax = money*0.03
                    money2 += tax
                    print("Updated Balance: ",money2) 
        case 5:
            print("Exiting system... Thank you!")
            break


        


# 4. Electricity Bill Management System

# You are developing an Electricity Bill Management System for a power distribution company. The system helps calculate electricity bills for customers based on their unit consumption.

# Sometimes, the operator may try to calculate the bill or apply surcharge before entering the number of units consumed. Your system must handle such situations properly.

# 👉 Important Condition:
# If units are not entered, the system should display:
# "Please enter units consumed first"
# and should not perform further calculations.

# The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

# Menu Options:
# 1 → Enter Units Consumed
# 2 → Calculate Bill Amount


# * First 100 units → ₹5 per unit
# * Next 100 units → ₹7 per unit
# * Above 200 units → ₹10 per unit
#   3 → Apply Surcharge
# * If bill > 2000 → 10% surcharge
# * Otherwise → 5% surcharge
#   4 → Display Final Bill
#   5 → Exit

# ---

# Sample Run 1:
# Input:
# Enter your choice: 2

# Output:
# Please enter units consumed first

# ---

# Sample Run 2:
# Input:
# Enter your choice: 1
# Enter units consumed: 250

# Output:
# Units recorded successfully

# ---

# Sample Run 3:
# Input:
# Enter your choice: 2

# Output:
# Bill Amount: 1700

# (Explanation: 100×5 = 500, 100×7 = 700, 50×10 = 500 → Total = 1700)

# ---

# Sample Run 4:
# Input:
# Enter your choice: 3

# Output:
# Surcharge: 85

# ---

# Sample Run 5:
# Input:
# Enter your choice: 4

# Output:
# ----- Final Bill -----
# Units: 250
# Bill Amount: 1700
# Surcharge: 85
# Total Payable: 1785

# ---

# Sample Run 6 (Invalid Choice):
# Input:
# Enter your choice: 9

# Output:
# Invalid choice. Please try again.

# ---

# Sample Run 7 (Exit):
# Input:
# Enter your choice: 5

# Output:
# Exiting system... Thank you!

# ---

unit = 0
units = 0
bill = 0
surge = 0
print()
while True:
    print('''---Menu Options---
1 → Enter Units Consumed
2 → Calculate Bill Amount
3 → Apply Surcharge
4 → Display Final Bill
5 → Exit
''')
    choice = int(input("Choose A Option: "))
    match choice:
        case 1:
            unit = int(input("Enter units consumed: "))
            units = unit
            print("Units recorded successfully")
        case 2:
            if units ==0:
                print("Please enter units consumed first")
            else:
                if units>=200:
                    bill = (100*5)+(100*7)+(units-200)*10
                elif units >= 100:
                    bill  = (100*5)+(units-100)*7
                else:
                    bill = units*5
                print("Total Bill:",bill)
        case 3:
            if units ==0:
                print("Please enter units consumed first")
            else:
                if bill>2000:
                    surge = bill*0.1
                    print("Surcharge:",surge)
                else:
                    surge = bill*0.05
                    print("Surcharge:",surge)
        case 4:
            if units ==0:
                print("Please enter units consumed first")
            else:
                print("----- Final Bill -----")
                print("Units: ",units)
                print("Bill Amount: ",bill)
                print("Surcharge: ",surge)
                print("Total Payable: ",bill+surge)
        case 5:
            print("Exiting system... Thank you!")
            break


    

