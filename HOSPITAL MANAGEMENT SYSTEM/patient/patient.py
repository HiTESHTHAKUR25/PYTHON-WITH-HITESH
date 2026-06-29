
# 1. Patient Management Package

# Create a package named "patient".

# Create module:
# patient_module.py


# Implement the following functions:

# a) add_patient()

# Take patient details from user:

# - Patient ID
# - Patient Name
# - Age
# - Gender
# - Disease
# - Mobile Number


# Store patient information using list and dictionary.


# b) display_patients()

# Display all registered patients.


# c) search_patient()

# Search patient details using Patient ID.


patient = {}
def adddetails():
    id = int(input("Enter Patient ID: "))
    pname = input("Enter Patient Name: ")
    age = int(input("Enter Patient Age: "))
    gender = input("Enter Patient Gender: ")
    disi = input("Enter Patient Disease: ")
    number = int(input("Enter Mobile Number: "))
    patient[id] = {   "patient_id":id,
                      "patient_name":pname,
                      "patient_age": age,
                      "patient_gender": gender,
                      "patient_disease": disi,
                      "patient_number": number,
                      }


def display_patients():
    print("Patient Details",patient)

def search_patient():
    id = int(input("Enter Patient ID: "))
    if id in patient:
        print(patient[id])
    else:
        print("Patient Not Found")


while True:
    print('''
           :Patient Manu:
          1. Add Patient
          2. Display Patient
          3. Search Patient
          4. Exit''')
    choise = int(input("Choose A Option: "))
    if choise==1:
        adddetails()
    elif choise == 2:
        display_patients()
    elif choise==3:
        search_patient()
    elif choise ==4:
        break
    else:
        print("Wrong Option")

