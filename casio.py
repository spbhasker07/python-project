def add(number1,number2):
    return number1 + number2
def subtract(number1,number2):
    return number1 - number2
def multiply(number1,number2):
    return number1 * number2
def divide(number1,number2):
    return number1 / number2
print("plse select operation-\n"\
      "1.add\n"\
        "2.subtract\n"\
            "3.multiply\n"\
                "4.divide")
select = float(input("select any b/w 1,2,3,4"))
number1=float(input("enter the number"))
number2=float(input("enter the number"))
if select ==1:
    print(number1,"+",number2,"=",
          add(number1,number2))
elif select ==2:
    print(number1,"-",number2,"=",
          subtract(number1,number2))
elif select ==3:
    print(number1,"*",number2,"=",
          multiply(number1,number2))
elif select ==4:
    print(number1,"/",number2,"=",
          divide(number1,number2))
else:
    print("error")