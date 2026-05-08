pin = 6512
coun = 0 
coun1 = 3
while True:
    pinn = int(input("Enter PIn: "))
    if coun1 < 1:
        print("Maximum attempts exceeded. Please try again later.")
        break
    if pinn==pin:
        print("Do Work")
        break
    else:
        print("Wrong Pin")
        print(f"You left {coun1} Attempt")
        coun1 -=1
        coun+=1