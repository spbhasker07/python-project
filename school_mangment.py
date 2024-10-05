print("_"*45)
print("STUDENT MANGMENT SYSTEM".center(45))
print("_"*45)
student_list=["aman","rohit","puja","pinky"]
def see():
    try:
          with open("student.txt", "r") as file:
              print("cureent student fron list")
              for line in file:
                  print(line.strip())
    except FileNotFoundError:
        print("No students found in the file.")
def add():
    dynamic_dict = {}  # Initialize the dictionary outside the file block
    dynamic_dict["name"] = input("Enter the name of the student: ")
    dynamic_dict["age"] = int(input("Enter the age: "))
    dynamic_dict["city"] = input("Enter the city: ")
    dynamic_dict["number"] = input("Enter the phone number: ")  # Changed to string to avoid number issues
    dynamic_dict["id"] = input("Enter the ID proof number: ")

    with open("student.txt", "a") as file:  # Open the file here and append the details
        file.write(f"{dynamic_dict['name']},{dynamic_dict['age']},{dynamic_dict['city']},{dynamic_dict['number']},{dynamic_dict['id']}\n")
    print(f"{dynamic_dict['name']} has been added successfully!")

def remove():
    try:
        student_to_remove = input("Enter the name of the student to remove: ")
        with open("student.txt", "r") as file:
            lines = file.readlines()
        found = False
        with open("student.txt", "w") as file:
            for line in lines:
                if not line.startswith(student_to_remove):
                    file.write(line)
                else:
                    found=True
            if found:
                print(f"{student_to_remove} removed")
            else:
                print(f"{student_to_remove} not found")
    except FileNotFoundError:
        print("plese add student first")

def serch():
    try:
        student_serch = input("Enter the name of the student to search: ")
        with open("student.txt", "r") as file:
            found = False
            for line in file:
                if line.startswith(student_serch):
                    print(f"{student_serch} found in the list: {line.strip()}")
                    found = True
                    break
        if not found:
            print(f"{student_serch} not found in the list.")
    except FileNotFoundError:
        print("Student file not found, please add a student first.")
while True:
    print("1. To see student list\n2. To add data\n3. To remove data\n4. To serch list\n5. Exit")
    select=int(input("select  option b/w in 1,2,3,4,5"))
    if select == 1:
        see()
    elif select == 2:
        add()
    elif select == 3:
        remove()
    elif select == 4:
        serch()
    elif select == 5:
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")

    ch = input("Do you want to continue (y/n): ").lower()
    if ch != 'y':
        print("Exiting the program.")
        break