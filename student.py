print("_"*45)
print("WELCOME".center(45))
print("_"*45)
print("Plsese chose an option")
my_list=["aman","bhasker","ravi","soraj","abhijeet","rohan"]
def see():
    print(my_list)
def remove():
    list=input("enter the namer ")
    if list in my_list:
        my_list.remove(list)
        print(f"it is remove by {my_list}")
    else:
        print("it is not prasent in list")
def add():
    for _ in range(int(input("enter the number of student"))):
        my_list.append(input("enter the name"))
    print(f"see new list \n {my_list}")
def search():
    name = input("Enter the name: ")
    print(f"{name} is {'present' if name in my_list else 'not present'} in the list.")
while True:
    print("1. To see student list\n2. To remove data\n3. To search data\n4. To add new list\n5. Exit")
    select=int(input("select  option b/w in 1,2,3,4,5"))
    if select==1:
        see()
    elif select==2:
        remove()
    elif select==3:
        add()
    elif select==4:
        search()
    elif select==5:
        exit
    else:
        print("invalde option")
    ch = input("Do you want to continue (y/n): ").lower()
    if ch != 'y':
        print("Exiting the program.")
        break
