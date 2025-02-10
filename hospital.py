import os
print(45 * "+")
print("+ Welcome to Hospital +".center(45))
print(45 * "+")
doctor_list = {
    "name": "Josh Sing",
    "address": "Jalandhar",
    "age": 23,
    "health_department": "Cardiology",
    "id": 2343
}
patients = {}  
medicine = {}
appointments = {}  
def hospital_record():
    with open("Hospital_record.txt", "a") as file:
        for patient_id, details in patients.items():
            file.write(f"{patient_id}: {details}\n")
def pharma_record():
    with open("Medicine_record.txt", "a") as file:
        for med, price in medicine.items():
            file.write(f"{med}: {price}\n")
def add_patient():
    try:
        patient_id = int(input("Enter the Patient ID number: "))
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        address = input("Enter the address: ")
        health_problem = input("Enter the problem: ")
        patients[patient_id] = {
            "name": name,
            "age": age,
            "address": address,
            "health_problem": health_problem
        }
        print(f"Patient {name} added successfully!")
    except ValueError:
        print("Invalid input! Please enter correct data types.")
def see():
    while True:
        print("\nSelect an option to view details:")
        print("1. Doctor Details\n2. Patient Details\n3. Medicine Details\n4. Appointments\n5. Exit")
        try:
            select = int(input("Enter your choice (1-5): "))
            if select == 1:
                print("\nDoctor Details:", doctor_list)
            elif select == 2:
                print("\nPatient Details:")
                if patients:
                    for id, details in patients.items():
                        print(f"ID {id}: {details}")
                else:
                    print("No patients added yet.")
            elif select == 3:
                print("\nMedicine Details:", medicine if medicine else "No medicines added yet.")
            elif select == 4:
                view_appointments()
            elif select == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice! Please select 1, 2, 3, 4, or 5.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
def add_medicine():
    try:
        name = input("Enter the name of the medicine: ")
        price = int(input("Enter the medicine price: "))
        medicine[name] = price  # Store dynamically
        print(f"{name} added successfully with price Rs {price}")
    except ValueError:
        print("Invalid input! Please try again.")
def bill_of_medicine():
    if not medicine:
        print("No medicine has been added yet.")
        return
    print("Medicine Bill:")
    total_bill = sum(medicine.values())
    for med, price in medicine.items():
        print(f"{med}: Rs {price}")
    print(f"Total Bill: Rs {total_bill}")
def book_appointment():
    doctor_name = input("Enter the doctor's name: ")
    doctor_department = input("Enter the department name: ")
    if doctor_list["name"].lower() == doctor_name.lower() and doctor_list["health_department"].lower() == doctor_department.lower():
        print(f"Yes, Dr. {doctor_name} is available in {doctor_department} department.")
        try:
            patient_id = int(input("Enter your Patient ID: "))
            if patient_id not in patients:
                print("Patient not found! Please register first.")
                return
            appointments[patient_id] = {"doctor": doctor_name, "department": doctor_department}
            print(f"Appointment booked successfully with Dr. {doctor_name} ({doctor_department} department).")
        except ValueError:
            print("Invalid Patient ID! Please enter a number.")
    else:
        print("Sorry, the doctor is not available.")
def view_appointments():
    print("\nAppointments List:")
    if not appointments:
        print("No appointments booked yet.")
        return
    for patient_id, details in appointments.items():
        print(f"Patient ID {patient_id}: Dr. {details['doctor']} ({details['department']} department)")
while True:
    try:
        select_option=("1.add_patient\n2.book_appointment\n3.view_appointments\n4.bill_of_medicine\n5.add_medicine\n6.see patient\n7.exit")
        print(select_option)
        select_option = int(input("Enter your choice (1-6): "))
        if select_option == 1:
            add_patient()
        elif select_option == 2:
            book_appointment()
        elif select_option == 3:
            view_appointments()
        elif select_option == 4:
            bill_of_medicine()
        elif select_option == 5:
            add_medicine()
        elif select_option==6:
            see()
        elif select_option == 7:
            print("Exiting")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")
    except ValueError:
        print("Invalid input! Please enter a number.")