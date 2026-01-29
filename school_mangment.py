student_recoud={}
def add():
    student_recoud["id"]=int(input("enter the id number of student"))
    student_recoud['name']=input("enter the name of students")
    student_recoud['class']=int(input("enter the class"))
    student_recoud['age']=int(input("enter the the age"))
    student_recoud['course']=input("enter the course ")
    student_recoud["Fee"]=int(input("enter the fee"))
    print(student_recoud)
def fees():
    id_no = int(input("\nEnter the student ID to check fee: "))
    if id_no == student_recoud.get("id"):
        if student_recoud["Fee"] == 5000:
            print("fee is paid")
        else:
            print("fee is not fully paid")
    else:
        print("invalde student")
def exam():
    global subject
    subject = {}
    number_of_subject = int(input("Enter number of subjects: "))

    for i in range(number_of_subject):
        sub_name = input(f"Enter subject {i+1} name: ")
        marks = float(input(f"Enter marks of {sub_name}: "))
        subject[sub_name] = marks
def result():
    id_no=int(input("enter the id"))
    if id_no in student_recoud.get("id"):
        if student_recoud["Fee"]==5000:
            print("you are elgible for exam")
        else:
            print("need to pay the fees")
    else:
        print("ivalde id")
def mark_sheet():
    print("="*45)
    print("MARK SHEET".center(45))
    print("="*45)
    total=0
    for sub,mark in subject.items():
        print(sub,":",mark)
        total+=1
    percentage = total / len(subject)
    print("Total Marks:", total)
    print("Percentage:", percentage)

    if percentage >= 40:
        print("Result: PASS ")
    else:
        print("Result: FAIL")
def see():
    id_no=int(input("enter the id number"))
    if id_no in student_recoud.get(id):
        print(student_recoud)
print("1.Add the new student \n 2.Fee status \n 3.result \n 4.mark_sheet \n see")
select_choice=int(input("Enter the choice of the user"))
if select_choice==1:
    add()
elif select_choice==2:
    fees()
elif select_choice==3:
    result()
elif select_choice==4:
    mark_sheet()
elif select_choice==5:
    see()
else:
    print("invade choice")