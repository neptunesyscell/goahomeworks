import random

def guess_the_number():
    number = random.randint(1, 100)
    print("გამოიცანით რიცხვი 1-დან 100-მდე.")
    while True:
        try:
            guess = int(input("შეიყვანეთ თქვენი ვარაუდი: "))
            if guess < number:
                print("რიცხვი უფრო დიდია.")
            elif guess > number:
                print("რიცხვი უფრო პატარაა.")
            else:
                print(f"გილოცავთ! რიცხვი არის {number}")
                break
        except ValueError:
            print("გთხოვთ, შეიყვანეთ მხოლოდ ციფრი.")

guess_the_number()

