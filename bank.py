import pickle as pic
import os
print(45 * "-")
print("BANK".center(45))
print(45 * "-")
def load_data():
    if os.path.exists("bank.pkl"):
        with open("bank.pkl", "rb") as file:
            return pic.load(file)
    return {}  
def save_data(bank):
    with open("bank.pkl", "wb") as file:
        pic.dump(bank, file)
def see():
    bank = load_data()
    if bank:
        for key, record in bank.items():
            print(f"id: {key} and {record}")
    else:
        print("No records found.")
def add():
    bank = load_data() 
    new_id = max(bank.keys(), default=0) + 1  
    dynamic_dict = {}
    dynamic_dict["Account number"] = int(input("Enter the account number: "))
    dynamic_dict["Name"] = input("Enter the name: ")
    dynamic_dict["age"] = int(input("Enter the age: "))
    dynamic_dict["city"] = input("Enter the city: ")
    dynamic_dict["phone number"] = input("Enter the phone number: ")
    dynamic_dict["proof id"] = int(input("Enter the proof ID number: "))
    bank[new_id] = dynamic_dict  
    save_data(bank)  
    print(f"{dynamic_dict} added successfully.")
def search():
    bank = load_data()
    account_search = int(input("Enter the account number to search: "))
    found = False
    for record in bank.values():
        if record["Account number"] == account_search:
            print(f"Record found: {record}")
            found = True
            break
    if not found:
        print("Record not found.")
def remove():
    bank = load_data()
    account_remove = int(input("Enter the account number to remove: "))
    found = False
    for key, record in list(bank.items()):
        if record["Account number"] == account_remove:
            del bank[key]
            found = True
            break
    if found:
        save_data(bank)
        print(f"Record with account number {account_remove} removed.")
    else:
        print(f"Record with account number {account_remove} not found.")
while True:
    print("\n1. See all records\n2. Add a record\n3. Search for a record\n4. Remove a record\n5 Exit")
    select = int(input("Select an option (1-7): "))
    if select == 1:
        see()
    elif select == 2:
        add()
    elif select == 3:
        search()
    elif select == 4:
        remove()
    elif select == 5:
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")
    ch = input("Do you want to continue (y/n): ").lower()
    if ch != 'y':
        print("Exiting the program.")
        break