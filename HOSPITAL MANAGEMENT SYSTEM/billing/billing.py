# 4. Billing Package
# Create a package named "billing".
# Create module:
# billing_module.py
# Implement:
# generate_bill()
# Take:
# - Patient ID
# - Consultation Charges
# - Medicine Cost
# - Test Charges
# Calculate total amount:
# Total Bill = Consultation Charges + Medicine Cost + Test Charges
# Display complete bill.


def total_bill():
    pid = int(input("Enter PID: "))
    ccharge = int(input("Enter Consultant Charge: "))
    medicine = int(input("Enter Madicine Cost: "))
    testcharge = int(input("Enter Test Charge: "))

    totalbill = ccharge+medicine+testcharge
    print(f"Patient ID: {pid}. Total Bill is: {totalbill}")

total_bill()