temp1 = input("შეიყვანეთ F, C ან K : ")
temp2 = input("შეიყვანეთ მეორე ერთეული, რომელშიც გსურთ პირველის კონვერტირება: ")

if temp1.upper() == "K" and temp2.upper() == "F":
    try:
        fahrenheit = float(input(
            f"შეიყვანეთ თქვენი ციფრი, რომელიც გსურთ რომ იქნეს კონვერტირებული {temp1.upper()}-დან {temp2.upper()}-ში: "))
        print(f"{fahrenheit} {temp1.upper()}, {temp2.upper()}-ში არის", (9 / 5 * (fahrenheit - 273) + 32).__round__(),
              temp2.upper())
    except:
        print("აუცილებლად შეიყვანეთ რიცხვი და არა რაიმე სხვა ასო!")


elif temp1.upper() == "F" and temp2.upper() == "K":
    try:
        fahrenheit = float(input(
            f"შეიყვანეთ თქვენი ციფრი, რომელიც გსურთ რომ იქნეს კონვერტირებული {temp1.upper()}-დან {temp2.upper()}-ში: "))
        print(f"{fahrenheit} {temp1.upper()}, {temp2.upper()}-ში არის", (5 / 9 * (fahrenheit - 32) + 273).__round__(),
              temp2.upper())
    except:
        print("აუცილებლად შეიყვანეთ რიცხვი და არა რაიმე სხვა ასო!")


elif temp1.upper() == "C" and temp2.upper() == "F":
    try:
        celsius = float(input(
            f"შეიყვანეთ თქვენი ციფრი, რომელიც გსურთ რომ იქნეს კონვერტირებული {temp1.upper()}-დან {temp2.upper()}-ში: "))
        print(f"{celsius} {temp1.upper()}, {temp2.upper()}-ში არის", (celsius * 9 / 5 + 32).__round__(), temp2.upper())
    except:
        print("აუცილებლად შეიყვანეთ რიცხვი და არა რაიმე სხვა ასო!")


elif temp1.upper() == "F" and temp2.upper() == "C":
    try:
        celsius = float(input(
            f"შეიყვანეთ თქვენი ციფრი, რომელიც გსურთ რომ იქნეს კონვერტირებული {temp1.upper()}-დან {temp2.upper()}-ში: "))
        print(f"{celsius} {temp1.upper()}, {temp2.upper()}-ში არის", (5 / 9 * (celsius - 32)).__round__(),
              temp2.upper())
    except:
        print("აუცილებლად შეიყვანეთ რიცხვი და არა რაიმე სხვა ასო!")


elif temp1.upper() == "K" and temp2.upper() == "C":
    try:
        kelvin = float(input(
            f"შეიყვანეთ თქვენი ციფრი, რომელიც გსურთ რომ იქნეს კონვერტირებული {temp1.upper()}-დან {temp2.upper()}-ში: "))
        print(f"{kelvin} {temp1.upper()}, {temp2.upper()}-ში არის", (kelvin - 273).__round__(), temp2.upper())
    except:
        print("აუცილებლად შეიყვანეთ რიცხვი და არა რაიმე სხვა ასო!")


elif temp1.upper() == "C" and temp2.upper() == "K":
    try:
        kelvin = float(input(
            f"შეიყვანეთ თქვენი ციფრი, რომელიც გსურთ რომ იქნეს კონვერტირებული {temp1.upper()}-დან {temp2.upper()}-ში: "))
        print(f"{kelvin} {temp1.upper()}, {temp2.upper()}-ში არის", (kelvin + 273).__round__(), temp2.upper())
    except:
        print("აუცილებლად შეიყვანეთ რიცხვი და არა რაიმე სხვა ასო!")


else:
    print("აუცილებელია, რომ იქნეს F,C ან K მითითებული")
