# ლუწი ან კენტი
number = int(input("შეიყვანეთ რიცხვი: "))
if number % 2 == 0:
    print("რიცხვი ლუწია.")
else:
    print("რიცხვი კენტია.")

# ხმის მიცემის მარტივი უფლება
age = int(input("შეიყვანეთ თქვენი ასაკი: "))
if age >= 18:
    print("თქვენ გაქვთ ხმის მიცემის უფლება.")
else:
    print("თქვენ არ გაქვთ ხმის მიცემის უფლება.")

# ტემპერატურის შემოწმება
temperature = float(input("შეიყვანეთ ტემპერატურა (°C): "))
if temperature < 15:
    print("ცივი")
elif 15 <= temperature <= 25:
    print("თბილი")
else:
    print("ცხელი")

# პაროლი
password = input("შეიყვანეთ პაროლი: ")
if password == "python123":
    print("Access Granted")
else:
    print("Access Denied")

