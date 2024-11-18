from fpdf import FPDF

print("HOSPITAL MANAGEMENT SYSTEM")

class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.staff = []
        self.inventory = []

    def add_patient(self):
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        disease = input("Enter patient disease: ")
        patient = Patient(name, age, disease)
        self.patients.append(patient)

    def add_doctor(self):
        name = input("Enter doctor name: ")
        specialization = input("Enter doctor specialization: ")
        doctor = Doctor(name, specialization)
        self.doctors.append(doctor)

    def add_staff(self):
        name = input("Enter staff name: ")
        role = input("Enter staff role (e.g., Nurse, Receptionist): ")
        staff_member = Staff(name, role)
        self.staff.append(staff_member)

    def add_inventory_item(self):
        name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        item = InventoryItem(name, quantity)
        self.inventory.append(item)

    def display_patients(self):
        print("\nPatients:")
        for patient in self.patients:
            print(f"Name: {patient.name}, Age: {patient.age}, Disease: {patient.disease}")

    def display_doctors(self):
        print("\nDoctors:")
        for doctor in self.doctors:
            print(f"Name: {doctor.name}, Specialization: {doctor.specialization}")

    def display_staff(self):
        print("\nStaff:")
        for member in self.staff:
            print(f"Name: {member.name}, Role: {member.role}")

    def display_inventory(self):
        print("\nInventory:")
        for item in self.inventory:
            print(f"Name: {item.name}, Quantity: {item.quantity}")

    def display_all_info(self):
        self.display_patients()
        self.display_doctors()
        self.display_staff()
        self.display_inventory()

    def generate_pdf_report(self):
        pdf = FPDF()
        pdf.add_page()

        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, "HOSPITAL REPORT", 0, 1, 'C')

        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Patients:", 0, 1)

        pdf.set_font("Arial", '', 12)
        for patient in self.patients:
            pdf.cell(0, 10, f"Name: {patient.name}, Age: {patient.age}, Disease: {patient.disease}", 0, 1)

        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Doctors:", 0, 1)

        pdf.set_font("Arial", '', 12)
        for doctor in self.doctors:
            pdf.cell(0, 10, f"Name: {doctor.name}, Specialization: {doctor.specialization}", 0, 1)

        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Staff:", 0, 1)

        pdf.set_font("Arial", '', 12)
        for member in self.staff:
            pdf.cell(0, 10, f"Name: {member.name}, Role: {member.role}", 0, 1)

        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Inventory:", 0, 1)

        pdf.set_font("Arial", '', 12)
        for item in self.inventory:
            pdf.cell(0, 10, f"Name: {item.name}, Quantity: {item.quantity}", 0, 1)

        pdf.output("hospital_report.pdf")  # Save the PDF file
        print("PDF report generated successfully: hospital_report.pdf")

hospital = Hospital()

while True:
    print("\nHospital Management System")
    print("1. Add Patient")
    print("2. Add Doctor")
    print("3. Add Staff")
    print("4. Add Inventory Item")
    print("5. Display Patients")
    print("6. Display Doctors")
    print("7. Display Staff")
    print("8. Display Inventory")
    print("9. Display All Information")
    print("10. Generate PDF Report")
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        hospital.add_patient()
    elif choice == 2:
        hospital.add_doctor()
    elif choice == 3:
        hospital.add_staff()
    elif choice == 4:
        hospital.add_inventory_item()
    elif choice == 5:
        hospital.display_patients()
    elif choice == 6:
        hospital.display_doctors()
    elif choice == 7:
        hospital.display_staff()
    elif choice == 8:
        hospital.display_inventory()
    elif choice == 9:
        hospital.display_all_info()
    elif choice == 10:
        hospital.generate_pdf_report()
    elif choice == 11:
        break
    else:
        print("Invalid choice")