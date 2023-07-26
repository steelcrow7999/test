from datetime import date
today = date.today()

birthYear = int(input("your birthyear "))
age = today.year - birthYear
if 15 <= age >= 20:
    print("teenager")
