import random
import string


def generate_password(lengthpassword: int):

    letters_lower = list(string.ascii_lowercase)
    letters_upper = list(string.ascii_uppercase)
    digits = string.digits
    symbols = string.hexdigits

    x = lengthpassword
    while True:
        pick = random.sample(range(2, x), 4)
        if sum(pick) == x:
            break
    result = pick

    numofletterlower, numofletterupper, numofsymbols, numofdigits = result

    num_letterlower = int(numofletterlower)
    num_letterupper = int(numofletterupper)
    num_symbols = int(numofsymbols)
    num_digits = int(numofdigits)

    password_list = []
    for char in range(1, num_letterlower + 1):
        password_list.append(random.choice(letters_lower))
    for char in range(1, num_letterupper + 1):
        password_list.append(random.choice(letters_upper))
    for char in range(1, num_symbols + 1):
        password_list += random.choice(symbols)
    for char in range(1, num_digits + 1):
        password_list += random.choice(digits)

    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char
    print(f"Your password is: {password}")


generate_password(16)
