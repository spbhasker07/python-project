import pandas as pd
recoud = []

no_of_opration = int(input("enter the number of the opration: "))

for i in range(no_of_opration):
    bill = {}
    bill["name"] = input("enter the name of the item: ")
    bill["price"] = int(input("enter the amount of the item: "))
    bill["qty"] = int(input("enter the qty of the item: "))
    bill["total"] = bill["price"] * bill["qty"]
    recoud.append(bill)

df = pd.DataFrame(recoud)

print("\n" + "-"*45)
print("FINAL BILL".center(45))
print("-"*45)
print(f"{'Item':<15}{'Price':<10}{'Qty':<8}{'Total':<10}")
print("-"*45)
from datetime import datetime
date = datetime.now().strftime("%d-%m-%Y")
print("Date :", date)
datetime.now().strftime("%d-%m-%Y %H:%M")
grand_total = 0
for i in recoud:
    print(f"{i['name']:<15}{i['price']:<10}{i['qty']:<8}{i['total']:<10}")
    grand_total += i["total"]

print("-"*45)
print(f"{'Grand Total':<33}{grand_total}")
print("-"*45)
