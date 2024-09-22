print("-"*45)
print("BANK MANGMENT SYSTEM".center(45))
print("-"*45)
print("Plese chose any option")
Account_type_option=["s","c"]
my_dic={1:{"Acount number":123,"Name":"Sp bhasker","age":23,"city":"barnla","phone number":23456743,"proof id":2345},
        2:{"Acount number":133,"Name":"kimmy","age":23,"city":"samrala","phone number":5678903,"proof id":2315},
       3:{"Acount number":153,"Name":"lalu","age":43,"city":"nodia","phone number":5126703,"proof id":2378},
       4:{"Acount number":154,"Name":"papu","age":33,"city":"dholakpur","phone number":5190890,"proof id":2348} 
       }
def see():
    a = int(input("Enter the account number: "))
    found = False
    for key, customer in my_dic.items():
        if customer["Acount number"] == a:  # Check the customer's account number
            print(f"Account details: {customer}")
            found = True
            break
    if not found:  # Move this out of the loop
        print("Account not found.")
def add():
   # Initialize an empty dictionary
    dynamic_dict = {}
    dynamic_dict["name"] = input("Enter the name")
    dynamic_dict["age"] = int(input("enter the age"))
    dynamic_dict["city"] = input("enter the city")
    dynamic_dict["Phone number"] = int(input("Enter the phone number"))
    dynamic_dict["Enter id"] = int(input("enter id proof number"))
    Account_type=input("enter the type (s/c):")
    if Account_type not in Account_type_option:
        print("wrong choice")
        return
    if Account_type == "s":
        dynamic_dict["deposit"]=int(input("enter the ammount"))
    elif Account_type=="c":
        dynamic_dict["fix deposit"]=int(input("enter the amount"))
        new_id=max(my_dic.keys())+1
        my_dic[new_id]=dynamic_dict
    print("details add succefully")
    print(dynamic_dict)
while True:
    print("\n1. New customer\n2. Existing customer\n3. Exit")
    select = int(input("Select any option (1, 2, or 3): "))

    if select == 1:
        add()
    elif select == 2:
        see()
    elif select == 3:
        print("Exiting the system...")
        break
    else:
        print("Invalid option, please try again.")