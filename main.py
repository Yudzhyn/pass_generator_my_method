from logo import show_logo as logo
from random import randint

# the site for which the password is generated
class Password():

    pass_methods = ("My own method", "Random method")

    #for my own method
    keyword_stardart = "plusultra"

    #for random method

    symbols_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    symbols_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    characters_groups = [symbols_letters, symbols_digits]

    def __init__(self, method, site):
        self.method = Password.pass_methods[method]
        self.site = site                         # назва сайту, для якого треба згенерувати пароль
        self.password = ""                      # сам пароль
        self.keyword = Password.keyword_stardart                 # ключове слово, по якому буде створений пароль    
        self.length_password = None

    def passCreate(self):
        if self.method == Password.pass_methods[0]:
            Password.passCreateMyOwn(self)
        else:
            Password.passCreateRandom(self)
        

    def passShow(self):
        print(f"Site: {self.site}, password: {self.password}")
        return None

    def passCreateMyOwn(self):
        '''
           Функція створення паролю для сайту по ключовому слову
           Принцип створення паролю:
           1)      {16+len(domain_name)}
           2) +    {last_character_from_name_site_that_are_not_in_keyword_uppercase}
           3) +    {characters_of_keyword_that_are_not_in_site_name}
           4) +    {first_character_from_name_site_that_are_not_in_keyword_uppercase}
           5) +    {18+len(site_name)}
          
        '''
        full_name_site_input = self.site
        full_name_site_input = full_name_site_input.split(".")
        
        # site name
        if len(full_name_site_input) > 2:
            site_name = "".join(word for word in full_name_site_input[0 : len(full_name_site_input) - 1])
        else:
            site_name = full_name_site_input[0]
        
        # domain name
        domain_name = full_name_site_input[-1]

        # STEP 1
        # 16 + length of domain name of the site
        self.password += str(16 + len(domain_name))
        #--------------------------------------------------------

        # STEP 2
        # uppercase last characters from the site name that are not in the keyword 
        for letter_site_name in site_name[::-1]:
            if letter_site_name not in self.keyword:
                self.password += letter_site_name.upper()
                break
        #--------------------------------------------------------

        # STEP 3
        # characters of the keyword that are not in the site name
        for letter_site_name in self.keyword:
            if letter_site_name not in site_name:
                self.password += letter_site_name

        #********************************************************
        # characters of the site name that are not in the keyword
        #for letter in name_site[0]:
        #    if letter not in word_key:
        #        self.password += letter
        #********************************************************
        #--------------------------------------------------------

        # STEP 4
        # uppercase first characters from the site name that are not in the keyword 
        for letter_site_name in site_name:
            if letter_site_name not in self.keyword:
                self.password += letter_site_name.upper()
                break
        #--------------------------------------------------------

        # STEP 5
        self.password += str(18 + len(site_name))
        #--------------------------------------------------------

    def passCreateRandom(self):
        length_password = Password.input_length_password()
        for i in range(length_password):
            choice_characters_group = randint(0, 1)
            if choice_characters_group == 0:
                choice_symbol = Password.symbols_letters[randint(0, 23)]
            elif choice_characters_group == 1:
                choice_symbol = Password.symbols_digits[randint(0, 9)]
            self.password += choice_symbol

    
    def input_length_password():
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


def quit():
    '''
        Quit from program
    '''
    while(True):
        input_key = input("Do you want to exit to program (y/n):  ")
        if input_key == 'y' or input_key == 'Y':
            exit(0)
        elif input_key == 'n' or input_key == 'N':
            return None
        else:
            continue

def loop():
    site = input("Please, enter site's name: ")
    method = int(input("Please, enter method (0 -- my own, 1 -- random): "))
    password = Password(method, site)
    password.passCreate()
    password.passShow()

def _main():
    logo()
    while True:
        loop()
        quit()


if __name__ == "__main__":
    _main()
