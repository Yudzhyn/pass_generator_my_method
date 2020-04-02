from random import randint

symbols_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

symbols_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

characters_groups = [symbols_letters, symbols_digits]



# This function input length future password that need to be integer and more than 0
def input_length_of_password():
    while True:
        try:
            length_of_password = int(input("Enter please length of your password: "))
        except ValueError:
            print("Enter please number of length in format \"integer digits\"!")
        else:
            if length_of_password > 0:
                return length_of_password
            else:
                print("Length of password don't be less then 0! Please enter number more than 0.")
                continue

# This function create password used random
def create_password(length_of_password):
    password = ""
    for i in range(length_of_password):
        choice_characters_group = randint(0, 1)
        if choice_characters_group == 0:
            choice_symbol = symbols_letters[randint(0, 23)]
        elif choice_characters_group == 1:
            choice_symbol = symbols_digits[randint(0, 9)]
        password += choice_symbol
    return password

#if __name__ == "__main__":
#    print("Creater password")
#    while True:
#        length_of_password = input_length_of_password()
#        print("Created password: " + create_password(length_of_password))
#        end_program = input("Do you want to continue? (y/n)")
#        if end_program == 'n':
#            print("Good bye")
#            break
#        elif end_program == 'y':
#            continue
