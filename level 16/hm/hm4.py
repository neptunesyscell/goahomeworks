correct_password = "password123"
entered_password = ""

while entered_password != correct_password:
    entered_password = input("შეიტანეთ პაროლი: ")
    if entered_password == correct_password:
        print("მომხმარებელი დაშვებულია!")
    else:
        print("არასწორი პაროლი. სცადეთ ისევ.")

