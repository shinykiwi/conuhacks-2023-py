import random
import string


def generate_password(complexity: int):
    letters_lower = set(string.ascii_lowercase)
    letters_upper = set(string.ascii_uppercase)
    digits = string.digits
    symbols = string.hexdigits
    print("Welcome to the PyPassword Generator!")
    num_letters = int(input("How many letters would you like in your password?\n"))
    num_symbols = int(input(f"How many symbols would you like?\n"))
    num_digits = int(input(f"How many numbers would you like?\n"))
    password_list = []
    for char in range(1, num_letters + 1):
        password_list.append(random.choice(letters_lower))
    for char in range(1, num_symbols + 1):
        password_list += random.choice(symbols)
    for char in range(1, num_digits + 1):
        password_list += random.choice(digits)

    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char
    print(f"Your password is: {password}")

generate_password()