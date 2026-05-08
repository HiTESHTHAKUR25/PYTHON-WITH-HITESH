
withdraw = int(input("Enter Withdrawal Amount: "))
balance = 100000
pin = 1234
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