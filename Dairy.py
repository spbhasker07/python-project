print("_"*45)
print("DAIRY MANAGEMENT SYSTEM".center(45))
print("_"*45)
dec_dairy = {"Milk": 64, "Curd": 10, "Ghee": 600, "Butter": 55, "Paneer": 100, "Khoya": 120}
bag = []
def see():
    try:
        with open("Dairy.txt", "r") as file:
            print("Available products:")
            for line in file:
                product, price = line.strip().split(":")
                print(f"{product}: Rs {price}")
    except FileNotFoundError as err:
        print(err)
def add():
    while True:
        add_dairy = input("Enter the product you want to buy: ").capitalize()
        if add_dairy in dec_dairy:
            print(f"{add_dairy} is available for Rs {dec_dairy[add_dairy]}")
        else:
            print("Invalid choice. Please select a valid product.")
            continue
        ch = input("Do you want to add it to the basket? (yes/no): ").lower()
        if ch == "yes":
            buy(add_dairy)
        else:
            print(f"{add_dairy} not added to the basket.")
        count = input("Do you want to buy more products? (yes/no): ").lower()
        if count == "no":
            break
        elif count != "yes":
            print("Invalid input, please enter 'yes' or 'no'.")
def buy(product):
    bag.append(product)
    print(f"{product} has been added to your cart.")
def checkout():
    if not bag:
        print("Your cart is empty.")
        return   
    print("\nItems in your cart:")
    total = 0
    for item in bag:
        print(f"{item}: Rs {dec_dairy[item]}")
        total += dec_dairy[item]
    print(f"\nTotal amount to pay: Rs {total}")
    print("Thank you for shopping!")
def write():
    with open("Dairy.txt", "w") as file:  
        for product, price in dec_dairy.items():
            file.write(f"{product}:{price}\n")  
write()
while True:
    try:
        select = int(input("Select an option (1: See, 2: Buy, 3: Checkout): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue  
    if select == 1:
        see()
    elif select == 2:
        add()
    elif select == 3:
        checkout()
    else:
        print("Invalid option.") 
    ch = input("Do you want to continue using the system? (y/n): ").lower()
    if ch != 'y':
        print("Exiting the program.")
        break
