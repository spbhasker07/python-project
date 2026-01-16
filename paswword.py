print("_" * 45)
print("PASSWORD MANAGEMENT SYSTEM".center(45))
print("_" * 45)
password = input("Enter your password: ")
upper = lower = digit = special = 0
special_chars = "!@#$%^&*()-_=+[]{}|;:',.<>?/"
if " " in password:
    print(" Password should not contain spaces")
else:
    for char in password:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digit += 1
        elif char in special_chars:
            special += 1
    if len(password) < 8:
        print(" Weak Password (Minimum 8 characters required)")

    elif upper >= 1 and lower >= 1 and digit >= 1 and special >= 1:
        print(" Strong Password")

    elif (upper + lower + digit + special) >= 3:
        print("Medium Password")

    else:
        print(" Weak Password")
