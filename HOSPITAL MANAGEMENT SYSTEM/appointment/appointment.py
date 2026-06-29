# 3. Appointment Management Package
# Create a package named "appointment".
# Create module:
# appointment_module.py
# Implement:
# a) book_appointment()
# Take appointment details:

# - Appointment ID
# - Patient ID
# - Doctor ID
# - Appointment Date
# - Appointment Time
# Store appointment information.
# b) show_appointments()
# Display all booked appointments.


appointment_data = {}

def appointment():
    aid = int(input("Enter Appointment ID: "))
    pid = int(input("Enter Patient ID: "))
    did = int(input("Enter Doctor ID: "))
    adate = int(input("Enter Appointment Date: "))
    atime = int(input("Enter Appointment Time: "))
    appointment_data[aid] = {
        "appoinment_id":aid,
        "patient_id":pid,
        "doctor_id":did,
        "appointment_date":adate,
        "appointment_time":atime
    }

def show_appointments():
    print(appointment_data)
    


while True:
    print('''Manu
          1. Apply Appointment
          2. Display Appointment
          3. Exit''')
    
    chhose = int(input("Chhose A option: "))
    if chhose == 1:
        appointment()
    elif chhose==2:
        show_appointments()
    elif chhose ==3:
        break
    else:
        print("Wrong Option")