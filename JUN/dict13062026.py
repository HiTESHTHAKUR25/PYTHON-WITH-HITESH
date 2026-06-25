# Hospital Patient Management System

patients = {}

while True:
    print("\n=====================================")
    print(" HOSPITAL PATIENT MANAGEMENT SYSTEM")
    print("=====================================")
    print("1. Add New Patient")
    print("2. Search Patient")
    print("3. Update Patient Disease")
    print("4. Delete Patient Record")
    print("5. Display All Patients")
    print("6. Count Total Patients")
    print("7. Display Patients By Disease")
    print("8. Display Oldest Patient")
    print("9. Display Youngest Patient")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        pid = int(input("Enter Patient ID: "))
        if pid in patients:
            print("Patient ID already exists.")
        else:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            gender = input("Enter Gender: ")
            disease = input("Enter Disease: ")
            doctor = input("Enter Doctor Name: ")

            patients[pid] = {
                "name": name,
                "age": age,
                "gender": gender,
                "disease": disease,
                "doctor": doctor
            }
            print("Patient Added Successfully")

    elif choice == 2:
        pid = int(input("Enter Patient ID: "))
        if pid in patients:
            p = patients[pid]
            print(f"\nPatient ID : {pid}")
            print(f"Name       : {p['name']}")
            print(f"Age        : {p['age']}")
            print(f"Gender     : {p['gender']}")
            print(f"Disease    : {p['disease']}")
            print(f"Doctor     : {p['doctor']}")
        else:
            print("Patient Record Not Found")

    elif choice == 3:
        pid = int(input("Enter Patient ID: "))
        if pid in patients:
            new_disease = input("Enter New Disease: ")
            patients[pid]["disease"] = new_disease
            print("Disease Updated Successfully")
        else:
            print("Patient Not Found")

    elif choice == 4:
        pid = int(input("Enter Patient ID: "))
        if pid in patients:
            del patients[pid]
            print("Patient Record Deleted Successfully")
        else:
            print("Patient Not Found")

    elif choice == 5:
        for pid, p in patients.items():
            print("\n------------------------------")
            print(f"Patient ID : {pid}")
            print(f"Name       : {p['name']}")
            print(f"Age        : {p['age']}")
            print(f"Disease    : {p['disease']}")
            print(f"Doctor     : {p['doctor']}")

    elif choice == 6:
        print("Total Patients :", len(patients))

    elif choice == 7:
        d = input("Enter Disease: ")
        found = False
        for pid, p in patients.items():
            if p["disease"].lower() == d.lower():
                print(pid, p["name"])
                found = True
        if not found:
            print("No Patient Found")

    elif choice == 8:
        if patients:
            oldest = max(patients, patients[x]["age"]) 
            p = patients[oldest]
            print("\nOldest Patient Details")
            print(oldest, p)
        else:
            print("No Data")

    elif choice == 9:
        if patients:
            youngest = min(patients, patients[x]["age"])
            p = patients[youngest]
            print("\nYoungest Patient Details")
            print(youngest, p)
        else:
            print("No Data")

    elif choice == 10:
        print("Thank You For Using Hospital Patient Management System")
        break

    else:
        print("Invalid Choice")








# Student Management System

students = {}

while True:
    print("\n=========================================")
    print(" STUDENT MANAGEMENT SYSTEM")
    print("=========================================")
    print("1. Add New Student")
    print("2. Search Student")
    print("3. Update Course")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Count Total Students")
    print("7. Display Students By Course")
    print("8. Display Students By City")
    print("9. Highest Fee Student")
    print("10. Lowest Fee Student")
    print("11. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        sid = int(input("Enter Student ID: "))
        if sid in students:
            print("Student ID Already Exists")
        else:
            name = input("Enter Name: ")
            course = input("Enter Course: ")
            mobile = input("Enter Mobile: ")
            fees = int(input("Enter Fees: "))
            city = input("Enter City: ")

            students[sid] = {
                "name": name,
                "course": course,
                "mobile": mobile,
                "fees": fees,
                "city": city
            }
            print("Student Added Successfully")

    elif choice == 2:
        sid = int(input("Enter Student ID: "))
        if sid in students:
            s = students[sid]
            print(f"\nStudent ID : {sid}")
            print(f"Name       : {s['name']}")
            print(f"Course     : {s['course']}")
            print(f"Mobile     : {s['mobile']}")
            print(f"Fees       : {s['fees']}")
            print(f"City       : {s['city']}")
        else:
            print("Student Not Found")

    elif choice == 3:
        sid = int(input("Enter Student ID: "))
        if sid in students:
            new_course = input("Enter New Course: ")
            students[sid]["course"] = new_course
            print("Course Updated Successfully")
        else:
            print("Student Not Found")

    elif choice == 4:
        sid = int(input("Enter Student ID: "))
        if sid in students:
            del students[sid]
            print("Student Deleted Successfully")
        else:
            print("Student Not Found")

    elif choice == 5:
        for sid, s in students.items():
            print("\n-----------------------------")
            print(f"Student ID : {sid}")
            print(f"Name       : {s['name']}")
            print(f"Course     : {s['course']}")
            print(f"Fees       : {s['fees']}")

    elif choice == 6:
        print("Total Students :", len(students))

    elif choice == 7:
        c = input("Enter Course: ")
        found = False
        for sid, s in students.items():
            if s["course"].lower() == c.lower():
                print(sid, s["name"])
                found = True
        if not found:
            print("No Students Found")

    elif choice == 8:
        city = input("Enter City: ")
        for sid, s in students.items():
            if s["city"].lower() == city.lower():
                print(sid, s["name"])

    elif choice == 9:
        if students:
            max_id = max(students, key=lambda x: students[x]["fees"])
            print("Highest Fee Paying Student:", max_id, students[max_id])
        else:
            print("No Data")

    elif choice == 10:
        if students:
            min_id = min(students, key=lambda x: students[x]["fees"])
            print("Lowest Fee Paying Student:", min_id, students[min_id])
        else:
            print("No Data")

    elif choice == 11:
        print("Thank You For Using Student Management System")
        break

    else:
        print("Invalid Choice")