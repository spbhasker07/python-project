def see():
    for student in my_list:
        print(student)
def remove():
    list=input("enter the namer ")
    if list in my_list:
        my_list.remove(list)
        print(f"it is remove by {my_list}")
    else:
        print("it is not prasent in list")
def add():
    student= int(input("Enter the number of student add"))
    for _ in range(student):
        name = input("Enter the name")
        my_list.append(name)
    print(f"Updated list: {my_list}")
def serch():
   name = input("Enter the name: ")
   if name in my_list:
        print(f"{name} is present in the list.")
   else:
        print(f"{name} is not present in the list.")
while True:
    print("_"*45)
    print("WELCOME".center(45))
    print("_"*45)
    print("Plsese chose an option")
    print("plse select operation-\n"\
      "1.To see student list\n"\
        "2.to remove data\n"\
            "3.To serch data\n"\
            "4.To add new list\n"\
                "5.exit")
    select=int(input("select  option b/w in 1,2,3,4,5"))
    my_list=["aman","bhasker","ravi","soraj","abhijeet","rohan"]
    if select==1:
        see()
    elif select==2:
        remove()
    elif select==3:
        add()
    elif select==4:
        serch()
    elif select==5:
        exit
    else:
        print("invalde option")
    ch = input("Do you want to continue (y/n): ").lower()
    if ch != 'y':
        print("Exiting the program.")
        break