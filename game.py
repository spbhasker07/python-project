import random as ram
print("rules of games:n\"  "+ "papaer vs rock = paper win"+"papaer vs scissor = scissor win" + "rock vs scissor = rock win")
while True:
    print("select: \n 1.rock \n 2.papaer \n 3.scissors")
    human=int(input("enter the choice"))
    while human >3 or human<1:
        human=int(input("invalde choice "))
    if human==1:
        human_select="rock"
    elif human==2:
        human_select="papaer"
    else:
        human_select="scissors"
    print("human choice",human_select)
    ai=ram.randint(1,3)
    if ai==1:
        ai_choice="rock"
    elif ai==2:
        ai_choice="papaer"
    else:
        ai_choice="scissors"
    print("AI CHOICE",ai_choice)
    if(human_select==ai_choice):
        print("draw")
    elif(human_select == "Rock" and  ai_choice== "Scissors") or \
         (human_select == "Paper" and  ai_choice== "Rock") or \
         (human_select == "Scissors" and  ai_choice== "Paper"):
        print("You win!")
    else:
        print("AI WIN")