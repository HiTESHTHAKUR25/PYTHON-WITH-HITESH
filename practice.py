name = ""
number = 0
pan = 0
account = 0
pin = 0
balance = 0



print("---Wellcome To Laxmi Chit Fund---")



print("1. New User")
print("2. You Have Already Account")
choice = int(input("Chhose One of them: "))
count = 1
counts1=0
start=0
match choice:
    case 1:
        if count == 1:
            name = input("Enter Your Full Name: ")
            pan_no = input("Enter Your Pan Number: ")
            phone_number = int(input("Enter Your Phone Number: "))
            name = name
            pan = pan_no
            number = phone_number
            if len(str(pan_no)) == 10 and len(str(phone_number)) == 10:
                print("Your Account Created Successfuly")
                count +=1
            else:
                print("Wrong Entered Information")
            if count == 2:
                accno = 100001
                account = accno
                print("You Account Number is:",accno)
                print()
                print("---Create Your Pin---")
                count+=1
            if count == 3:
                while True:
                    pin = int(input("Enter 4 Digit Pin: "))
                    pinn = len(str(pin))
                    if pinn==4:
                            print("Pin Created Successfuly")
                            count+=1
                            break
                    else:
                        print("Wrong Pin")
                        break
            if count == 4:
                while True:            
                    print("        1. Zero Balance")
                    print("        2. Deposite Amount")
                    option = int(input("Choose an Option: "))
                    if option == 1:
                        balance = 0
                        start+=1
                        break
                    elif option == 2:
                        amount = int(input("Entetr Amount: "))
                        balance = amount
                        start+=1
                        break
                    else:
                        print("You Choose Wrong Option")

    case 2:
        pinn = int(input("Enter Your Pin: "))
        if pinn==pin: 
            print("Name :",name)
            print("Number :",number)
            print("PAN :",pan)
            print("Account :",account)
            print("Balance :",balance)
        else:
            print("Wrong Pin")   

if start==1:
    while True:
        print()
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Change Pin")
        print("5. Delete Your Account")
        print("6. Details")
        print("7. Exit")  
        print()  
        option = int(input("Choose An Option: "))
        match option:
            case 1:
                deposit = int(input("Enter Amount: "))
                if deposit<0:
                    print("Wrong Amount")
                else:
                    balance += deposit
                    print("Balance: ",balance)
                    print("Deposite Successfull")
            case 2:
                withdraw = int(input("Enter Withdrawal Amount: "))
                coun = 0 
                coun1 = 3
                while True:
                    pinn = int(input("Enter Pin: "))
                    if coun1 < 1:
                        print("Maximum attempts exceeded. Please try again later.")
                        break
                    elif pinn==pin:
                        if withdraw > balance:
                            print("Insufficient Balance")
                        else:
                            balance = balance-withdraw
                            print("Withdrawal Successfull")
                            print("Available Balance: ",balance)
                            
                            break
                    else:
                        print("Wrong Pin")
                        print(f"You left {coun1} Attempt")
                        coun1 -=1
                        coun+=1       
            case 3: 
                pinm = int(input("Enter Pin: "))
                if pinm == pin:
                    print("Balance:",balance)
                else:
                    print("Wrong Pin")
            case 4:
                while True:
                    pin1 = int(input("Enter New Pin: "))
                    if len(str(pin1))==4:
                        if pin1 != pin:
                            pin=pin1
                            print("Pin Change Successfull")
                            break
                        else:
                            print("Duplicate Pin")
                    else:
                        print("Enter 4 Digit Pin")
            case 5:
                sure = input("Last Chance Delete or Not: ").lower()
                if sure == "yes":
                    name = ""
                    number = 0
                    pan = 0
                    account = 0
                    pin = 0
                    balance = 0
                    print("Your Account is Delete")
                    break
                elif sure == "no":
                    print("Your Account Is Safe")
                else:
                    print("You choose Wrong Option")
            case 6:
                pin5 = int(input("Enter Pin: "))
                if pin5 == pin:
                    print("Name :",name)
                    print("Number :",number)
                    print("PAN :",pan)
                    print("Account :",account)
                    print("Balance :",balance)
                else:
                    print("Wrong Pin")
            case 7:
                print("Exiting system... Thank you!")
                break
            case _:
                print("Please Choose Right OPtion")
          
                        

