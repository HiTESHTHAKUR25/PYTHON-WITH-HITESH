# 5. Main Application
# Create main.py file.
# Create a menu-driven program.

# Menu:
# ========== Hospital Management System ==========
# 1. Add Patient
# 2. Display Patients
# 3. Search Patient
# 4. Add Doctor
# 5. Display Doctors
# 6. Book Appointment
# 7. Show Appointments
# 8. Generate Bill
# 9. Exit
# According to user choice call the required functions from packages.
# --------------------------------------------------



while True:
    print(''' Menu:
 ========== Hospital Management System ==========
 1. Add Patient
 2. Add Doctor
 3. Book Appointment
 4. Generate Bill
 5. Exit''')
    choise = int(input("How Can i help you: "))
    match choise:
        case 1:
            import patient
        case 2:
            import doctor
        case 3:
            import appointment
        case 4:
            import billing
        case 5:
            break
        case _:
            print("Wrong Option")