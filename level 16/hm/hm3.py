import random

# შემთხვევითი რიცხვის არჩევა 1-დან 10-მდე
secret_number = random.randint(1, 10)
guess = None

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 10: "))  # შეცვალეთ ეს ნაწილი ქართულით
    if guess < secret_number:
        print("თქვენი რიცხვი მცირეა. სცადეთ კვლავ.")
    elif guess > secret_number:
        print("თქვენი რიცხვი დიდი არის. სცადეთ კვლავ.")
    else:
        print("გილოცავთ! თქვენ სწორად გამოიცანით!")

