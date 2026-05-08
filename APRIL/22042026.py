# ===========1=========



age= int(input("Policy Age: "))
amount = int(input("Claim Amount: "))
actype = input("Accident Type: ") 


if age >= 2:
    if amount <= 50000:
        if actype == "minor":
            print("Claim Status = Approved")
        else:
            print("Claim Status = Approved with Investigation")
    elif amount <= 200000:
        if actype == "major":
            print("Claim Status = Approved with Investigation")
        else:
            print("Claim Status = Reject")
    else:
        print("Claim Status = Reject")
else:
    if actype == "minor":
        print("Claim Status = Reject")
    else:
        print("Claim Status = Pending Review")




# =========2==========

marks = int(input("Marks: "))
score = int(input("Entrance Score: "))
cat = (input("Category: "))


if marks >= 70:
    if score >= 80:
        if cat == "general":
            print("Admission Statu: Admit")
        else:
            print("Admission Statu: Admit with scholarship")
    else:
        if marks >= 85:
            print("Admission Statu: Admit Under Management Quota")
        else:
            print("Admission Statu: Reject ")
else:
    if cat != "general":
        if marks >=60:
            if score >= 70:
                print("Admission Statu: Waitlist")
    else:
        print("Admission Statu: Reject")



# =====3=====


salary = int(input("Salary: "))
cs = int(input("Credit Score: "))
el = int(input("Existing Loans: "))


if salary >= 30000:
    if cs >= 750:
        if el == 0:
            print("Risk Level: Low Risk")
        elif el <= 2:
            print("Risk Level: Medium Risk")
        else:
            print("Risk Level: Hight Risk")
    else:
        if salary >= 50000:
            if cs >= 650:
                print("Risk Level: Medium Risk")
            else:
                print("Risk Level: High Risk")
else:
    print("Not Eligible")



# =========4=======


subs = input("Subscription: ")
prog = int(input("Progress: "))
ts = int(input("Test Score: "))

if subs =="premium":
    if prog >= 80:
        if ts >= 70:
            print("Access Status: Unlock Certificate")
        else:
            print("Access Status: Retry Test")
    else:
        print("Access Status: First Complete Course")
elif subs == "basic":
    if prog >= 50:
        print("Access Status Limited Access")
    else:
        print("Access Status: Lock Content")
else:
    print("Access Status: Deny Access")


# ======5==========




stock  = int(input("Stock: "))
priority  = (input("Priority: "))
dist  = int(input("Distance: "))

if stock >= 100:
    if priority == "high":
        if dist <= 200:
            print("Dispatch Status: Dispatch via Immediately")
        else:
            print("Dispatch Status: Dispatch via Fast Courier")
    else:
        if stock >= 300:
            print("Dispatch Status: Bulk Dispatch")
else:
    if stock >= 50:
        if priority == "high":
            print("Dispatch Status: Dispatch via Partially")
        else:
            print("Dispatch Status: Hold")
    else:
        print("Dispatch Status: Out Of Stock")



=======6======='


amount = int(input("Transaction Amount: "))
location = (input("Location: "))
age = int(input("Account Age: "))

if amount >= 100000:
    if location == "international":
        otp = int(input("Enter OTP: "))
        if len(otp) == 4:
            print("Transaction Status: Flagged")
        else:
            print("Transaction Status: Block")
    elif location == "domestic":
        if amount >= 50000:
            if age >= 2:
                print("Transaction Status: Flagged")
            else:
                print("Transaction Status: Flag")
        else:
            print("Transaction Status: Allow")
else:
    print("Transaction Status: Allow")


# ==========7=============


demand = int(input("Demand: "))
time = input("Time: ")
dist = int(input("Distance: "))


if demand >= 80:
    if time == "peak":
        if dist >= 10:
            print("Fare Multiplier = 2x Fare")
        else:
            print("Fare Multiplier = 1.5x Fare")
    else:
        if demand >= 90:
            print("Fare Multiplier = 1.8x Fare")
        else:
            print("Fare Multiplier = 1.3x Fare")
elif demand >= 50:
    if time == "peak":
        print("Fare Multiplier = 1.2x Fare")
    else:
        print("Fare Multiplier = Normal Fare")
else:
    print("Fare Multiplier = Normal Fare")


# ===============8===========




sm = float(input("Soil Moisture: "))
temp = int(input("Temprature: "))
crop = input("Crop: ")

if sm <=30:
    if temp >= 35:
        if crop == "wheat":
            print("Irrigation = High Water Supply")
        else:
            print("Irrigation = Modrate Water Supply")
    else:
        print("Irrigation = Modrate Water Supply")
elif sm <= 60:
    rain = input("Rainfall: ")
    if rain == "yes":
        print("Irrigation = Delay Irrigation")
    else:
        print("Irrigation = Light Irrigation")
else:
    print("Irrigation = No Irrigation")



# ==========9==============



ex = float(input("Experience: "))
rating = float(input("Rating: "))
project = int(input("Project: "))

if ex >= 5:
    if rating >= 4:
        if project >= 3:
            salary = int(input("Salary: "))
            if salary >= 50000:
                print("Promotion Status = Promoted with 30% hike")
            else:
                print("Promotion Status = Promoted with 20% hike")
        else:
            print("Promotion Status = Promoted with 10% hike")
    else:
        print("Promotion Status = No Promotion")
else:
    if rating == 5:
        print("Promotion Status = Fast Track Promotion")
    else:
        print("Promotion Status = No Promotion")



# =========10==============







amount = int(input("Order Amount: "))
ct = input("Customer Type: ")
method = input("Payment Method: ")

if amount >= 2000:
    if ct == "vip":
        if method == "online":
            print("Offer = Free Dessert + 20% Discount")
        else:
            print("Offer = Free Dessert ")
    else:
        if amount >= 5000:
            print("Offer = 15% Discount")
        else:
            print("Offer = 10% Discount")
elif amount >= 1000:
    if ct == "vip":
        print("Offer = 10% Discount")
    else:
        print("Offer = 5% Discount")
else:
    print("Offer = No Offer For You")