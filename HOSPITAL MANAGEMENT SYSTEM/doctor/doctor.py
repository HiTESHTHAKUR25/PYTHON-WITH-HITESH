# -------------------------------------------------
# 2. Doctor Management Package
# Create a package named "doctor".
# Create module:
# doctor_module.py
# Implement the following functions:

# a) add_doctor()
# Take doctor details:

# - Doctor ID
# - Doctor Name
# - Specialization
# - Experience
# - Consultation Fees

# Store doctor information using list and dictionary.
# b) display_doctors()
# Display all doctor details.


doctors = {}

def adddoctor():
    id = int(input("Enter Doctor ID: "))
    dname = input("Enter Doctor Name: ")
    special = input("Enter Doctor Specialization: ")
    ex = input("Enter Doctor Experience: ")
    fee = int(input("Enter Doctor Consultation Fees: "))
    doctors[id] = {   "Doctor_id":id,
                      "Doctor_name":dname,
                      "Doctor_special": special,
                      "Doctor_experience": ex,
                      "Doctor_fees": fee,
                      }
    

def display_doctors():
    print("Doctors Information:",doctors)


while True:
    print('''Manu
          1. Add Doctor
          2. Display Doctors
          3. Exit''')
    choise = int(input("Chhoose a option: "))
    if choise == 1:
        adddoctor()
    elif choise == 2:
        display_doctors()
    elif choise ==3:
        break
    else:
        print("Wrong Option")