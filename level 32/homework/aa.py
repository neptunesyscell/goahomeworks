# 1. ორი string-ის შეერთება და დაპრინტვა
def concatenate_strings(str1, str2):
    print(str1 + str2)

concatenate_strings("Hello, ", "World!")

# 2. სიის მე-3 და მე-4 ელემენტის ჯამი
def sum_third_and_fourth(numbers):
    if len(numbers) >= 4:
        print(numbers[2] + numbers[3])

sum_third_and_fourth([1, 2, 3, 4, 5])

# 3. კილომეტრების მეტრებად გადაყვანა
def km_to_meters(km):
    print(km * 1000)

km_to_meters(5)

# 4. ორი რიცხვიდან უფრო დიდის დაპრინტვა
def print_larger_number(num1, num2):
    print(max(num1, num2))

print_larger_number(10, 25)

# 5. სტრინგის შებრუნება
def reverse_string(text):
    print(text[::-1])

reverse_string("Python")
