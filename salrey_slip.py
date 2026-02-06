from datetime import date

# ---------------- Employee Details ----------------
org = "ABC Technologies Pvt. Ltd."
name = "Rahul Sharma"
emp_id = "EMP1023"
designation = "Software Trainee"
department = "IT"
pay_period = "January 2026"
generated_date = date.today().strftime("%d-%m-%Y")

# ---------------- Earnings ----------------
basic_salary = 25000
house_rent = 10000
medical_allowance = 3000
travel_allowance = 2000

# ---------------- Deductions ----------------
pf = 1800
professional_tax = 200
income_tax = 1500

# ---------------- Calculations ----------------
total_earnings = basic_salary + house_rent + medical_allowance + travel_allowance
total_deductions = pf + professional_tax + income_tax
net_salary = total_earnings - total_deductions

# ---------------- Amount in Words (simple) ----------------
amount_in_words = "Thirty Six Thousand Five Hundred Rupees Only"

# ---------------- Print Salary Slip ----------------
print("=" * 70)
print("SALARY SLIP".center(70))
print("=" * 70)

print(f"Organization   : {org}")
print(f"Employee Name  : {name}")
print(f"Employee ID    : {emp_id}")
print(f"Designation    : {designation}")
print(f"Department     : {department}")
print(f"Pay Period     : {pay_period}")
print(f"Date Generated : {generated_date}")

print("-" * 70)

print(f"{'EARNINGS':<35}{'DEDUCTIONS':<35}")
print("-" * 70)

print(f"{'Basic Salary':<25} ₹{basic_salary:<8}{'Provident Fund (PF)':<25} ₹{pf}")
print(f"{'House Rent Allowance':<25} ₹{house_rent:<8}{'Professional Tax':<25} ₹{professional_tax}")
print(f"{'Medical Allowance':<25} ₹{medical_allowance:<8}{'Income Tax':<25} ₹{income_tax}")
print(f"{'Travel Allowance':<25} ₹{travel_allowance:<8}")

print("-" * 70)

print(f"{'Total Earnings':<25} ₹{total_earnings:<8}{'Total Deductions':<25} ₹{total_deductions}")

print("-" * 70)

print(f"NET SALARY (IN HAND) : ₹{net_salary}")
print("-" * 70)

print("Amount in words :")
print(amount_in_words)

print("-" * 70)
print("This is a system-generated salary slip and does not require signature.")
print("=" * 70)
