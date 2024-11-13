import json, os,time as t
import shutil as sh
# Base directory for employee files
BASE_DIR = "employee_file"
if not os.path.exists(BASE_DIR):
    os.mkdir(BASE_DIR)
print(45 * "_")
print("OFFICE MANAGEMENT SYSTEM".center(45))
print(45 * "_")
# Departments with initial employee data
departments = {
    "HR": {
        1: {"id": 23, "name": "SP Bhasker", "position": "HR Manager", "address": "Gurugram"},
        2: {"id": 20, "name": "Kimmy Sha", "position": "Training Manager", "address": "Barnala"},
    },
    "Software Testing": {
        1: {"id": 11, "name": "Anurag", "position": "Automation Testing", "address": "Mandi Gobindgarh"},
    },
    "Data": {
        1: {"id": 1, "name": "Lakshme", "position": "Data Engineer", "address": "Panipat"},
    },
    "Development": {
        1: {"id": 15, "name": "Ankit", "position": "Back-end Developer", "address": "Bhagalpur"},
    },
}
# Save and load data functions
def save_data(data, filename='employee_data.json'):
    with open(filename, 'w') as file:
        json.dump(data, file)
    print("Data saved successfully!")

def load_data(filename='employee_data.json'):
    if os.path.exists(filename):
        with open(filename) as file:
            return json.load(file)
    print("Data not found, using default data.")
    return departments
# View employees by department
def view_department(dept_name):
    # Convert the department name to uppercase for a consistent lookup
    dept = departments.get(dept_name.upper())
    if dept:
        print(f"Employees in {dept_name}:")
        for key, emp in dept.items():
            print(f"ID: {emp['id']}, Name: {emp['name']}, Position: {emp['position']}, Address: {emp['address']}")
    else:
        print(f"Department '{dept_name}' not found.")
# Add new employee
def add_employee():
    dept_name = input("Enter department (HR, Software Testing, Data, Development): ").title()
    if dept_name in departments:
        emp_id = int(input("Enter new ID: "))
        name = input("Enter employee name: ")
        position = input("Enter employee position: ")
        address = input("Enter employee address: ")
        departments[dept_name][len(departments[dept_name]) + 1] = {
            "id": emp_id, "name": name, "position": position, "address": address
        }
        print(f"Employee added to {dept_name}.")
    else:
        print("Department not found.")
# Update employee information
def update_employee():
    dept_name = input("Enter department to update: ").title()
    if dept_name in departments:
        emp_id = int(input("Enter employee ID: "))
        emp = departments[dept_name].get(emp_id)
        if emp:
            print(f"Current details: {emp}")
            field = input("Field to update (name, position, address): ").lower()
            if field in emp:
                emp[field] = input(f"Enter new {field}: ")
                print("Update successful.")
            else:
                print("Invalid field.")
        else:
            print("Employee not found.")
    else:
        print("Department not found.")
# Delete employee
def delete_employee():
    dept_name = input("Enter department to delete from: ").title()
    if dept_name in departments:
        emp_id = int(input("Enter employee ID: "))
        if emp_id in departments[dept_name]:
            del departments[dept_name][emp_id]
            print("Employee deleted successfully.")
        else:
            print("Employee not found.")
    else:
        print("Department not found.")
# File management functions
def upload_file(employee_id, dept_name):
    dept_dir = os.path.join(BASE_DIR, dept_name)
    os.makedirs(dept_dir, exist_ok=True)
    employee_dir = os.path.join(dept_dir, f"emp_{employee_id}")
    os.makedirs(employee_dir, exist_ok=True)
    file_path = input("Enter file path to upload: ")
    if os.path.isfile(file_path):
        sh.copy(file_path, employee_dir)
        print(f"File uploaded to Employee {employee_id} in {dept_name}.")
    else:
        print("Invalid file path.")
def download_file(employee_id, dept_name):
    employee_dir = os.path.join(BASE_DIR, dept_name, f"emp_{employee_id}")
    if os.path.exists(employee_dir):
        files = os.listdir(employee_dir)
        print("Files available for download:", files)
        file_choice = int(input("Enter file number to download: ")) - 1
        if 0 <= file_choice < len(files):
            dest_path = os.path.join(os.getcwd(), files[file_choice])
            sh.copy(os.path.join(employee_dir, files[file_choice]), dest_path)
            print(f"Downloaded to {dest_path}.")
        else:
            print("Invalid choice.")
    else:
        print("No files available.")
# Project Assignment classes
class Project:
    def __init__(self, project_id, name, deadline, assigned_to=None):
        self.project_id = project_id
        self.name = name
        self.deadline = deadline
        self.assigned_to = assigned_to
    def __str__(self):
        return f"Project ID: {self.project_id}, Name: {self.name}, Deadline: {self.deadline}, Assigned To: {self.assigned_to}"
class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.projects = []
    def assign_project(self, project):
        self.projects.append(project)
        print(f"Project '{project.name}' assigned to {self.name}.")
    def view_projects(self):
        if not self.projects:
            print(f"{self.name} has no assigned projects.")
        else:
            print(f"Projects assigned to {self.name}:")
            for project in self.projects:
                print(project)
    def __str__(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}"
# Project assignment functions
def assign_project_to_employee(employees, projects):
    emp_id = int(input("Enter the Employee ID: "))
    project_id = int(input("Enter the Project ID: "))
    employee = next((emp for emp in employees if emp.employee_id == emp_id), None)
    project = next((proj for proj in projects if proj.project_id == project_id), None)
    if employee and project:
        employee.assign_project(project)
        print("Project assigned successfully!")
    else:
        print("Invalid Employee ID or Project ID.")
def view_employee_projects(employee):
    employee.view_projects()
# Main function
def main():
    employees = [Employee(1, "Alice"), Employee(2, "Bob")]
    projects = [Project(101, "Website Development", "2024-12-31"),
                Project(102, "Database Migration", "2024-11-15")]
    while True:
        print("\n1. Assign Project to Employee")
        print("2. View Employee Projects")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            assign_project_to_employee(employees, projects)
        elif choice == '2':
            emp_id = int(input("Enter Employee ID to view projects: "))
            employee = next((emp for emp in employees if emp.employee_id == emp_id), None)
            if employee:
                view_employee_projects(employee)
            else:
                print("Invalid Employee ID.")
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main()
while True:
    try:
    # Display options to the user
        print("Choose an option:")
        print("1. View Department \n2. Add Employee\n3. Update Employee\n4. Delete Employee\n5. Exit")
        chose_option = int(input("Enter your choice: "))
        if chose_option == 1:
            dept_name = input("Enter department name (HR, Software Testing, Data, Development): ").title()
            view_department(dept_name)
        elif chose_option == 2:
              add_employee()
        elif chose_option == 3:
            update_employee()
        elif chose_option == 4:
            delete_employee()
        elif chose_option == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")
    except ValueError :
        print("invalde choice try again")