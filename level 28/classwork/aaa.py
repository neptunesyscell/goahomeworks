
def add_numbers(a, b):
    return a + b

def is_even(number):
    return number % 2 == 0


def find_max(a, b):
    return a if a > b else b


def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    return sum(1 for char in text.lower() if char in 'aeiou')


def is_divisible(a, b):
    return a % b == 0
