import random

symbols_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

symbols_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

characters_groups = [symbols_letters, symbols_digits]

def passCreateRandom() -> str:
    length_password = _input_length_password()
    password = ""
    for i in range(length_password):
        choice_characters_group = random.randint(0, 1)
        if choice_characters_group == 0:
            choice_symbol = random.choice(symbols_letters)
        elif choice_characters_group == 1:
            choice_symbol = random.choice(symbols_digits)
        choice_symbol = choice_symbol.upper() if random.randint(0, 1) else choice_symbol
        password += choice_symbol
    return password


def _input_length_password() -> int:
    while True:
        try:
            length_password = int(input("Enter please length of your password: "))
        except ValueError:
            print("Enter please number of length in format \"integer digits\"!")
        else:
            if length_password > 0:
                return length_password
            else:
                print("Length of password don't be less then 0! Please enter number more than 0.")
                continue
