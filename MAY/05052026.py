# 1. Smart Shopping Mall Discount System
# A shopping mall offers discounts based on customer type and purchase amount.
# If the customer is premium, they get 20% discount when the amount is more than 5000, otherwise 10%.
# If the customer is regular, they get 10% discount when the amount is more than 3000, otherwise 5%.
# Write a program to calculate the final payable amount using inline if only.


num = int(input("Enter Number: "))
pre = input("Enter: ")

print("20% Discount" if pre == "premium" and num >5000 else "10% Discount" if pre == "regular" and num > 3000 else "5% Discount"  )




# 2. University Result Processing System
# A university wants to automatically assign grades based on marks.
# Marks ≥90 → A+
# Marks ≥75 → A
# Marks ≥60 → B
# Marks ≥50 → C
# Below 50 → Fail
# Write a program using a single nested inline if expression to display the grade.


num = int(input("Enter Marks: "))

print("+A" if num>=90 else "A" if num>=75 else "B" if num >= 60 else "C" if num>=50 else "Fail"  )


# 3. Employee Bonus Distribution System
# A company provides bonuses based on years of experience.
# Experience >10 years → 30% bonus
# Experience >5 years → 20% bonus
# Otherwise → 10% bonus
# Write a program to calculate the total salary after adding bonus using inline if.

num = int(input("Enter Year Experience: "))

print("30% Bonus" if num>10 else "20% Bonus" if num>5 else "10% Bonus")


# 4.Electricity Billing System
# An electricity board calculates bills based on units consumed:
# Up to 100 units → ₹5 per unit
# 101–300 units → ₹7 per unit
# Above 300 units → ₹10 per unit
# Write a program to compute total bill using inline if.

num = int(input("Enter Your Electricity: "))


print((100*5+100*7+((num-200)*10)) if num>300 else (100*5+(num-100)*7) if num > 100 else num*5)



# 5.
# Calendar System – Leap Year Checker
# A digital calendar system needs to check whether a year is a leap year.
# A year is a leap year if:

# It is divisible by 400, OR
# It is divisible by 4 but not by 100
# Write a program using inline if to display whether the year is a leap year or not.

num = int(input("Year: "))


print("It is A LeaP Year" if (num%4==0 or num&400==0 and num%100!=0) else "It Is Not A leap Year")


# 6.
# Data Validation System – Character Identifier
# A system needs to validate user input characters.
# If the input is:
# Alphabet → display "Alphabet"
# Digit → display "Digit"
# Otherwise → display "Special Character"
# Write a program using inline if to classify the character.


num = (input("Enter: "))
print("Alphabet" if ('A' <= num <= 'Z' or 'a' <= num <= 'z')else "Digits"  if "0"<= num <="9" else "Special Character" )