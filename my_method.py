'''
Pass-generator by my own method
'''

import clipboard

class password():

    def __init__(self):
        self.site = ""                         # назва сайту, для якого треба згенерувати пароль
        self.keyword = "plusultra"                 # ключове слово, по якому буде створений пароль    
        self.password = ""                      # сам пароль


    def pass_creat(self, full_name_site_input):
        '''
           Функція створення паролю для сайту по ключовому слову
           Принцип створення паролю:
           1)      {16+len(domain_name)}
           2) +    {last_character_from_name_site_that_are_not_in_keyword_uppercase}
           3) +    {characters_of_keyword_that_are_not_in_site_name}
           4) +    {first_character_from_name_site_that_are_not_in_keyword_uppercase}
           5) +    {18+len(site_name)}
           
        '''
        self.site = full_name_site_input
        full_name_site_input = full_name_site_input.split(".")
        self.password = ""
        site_name = full_name_site_input[0]
        domain_name = full_name_site_input[1]

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
    
    def show_created_password(self):
        '''
            Show password that was been creating for site
        '''
        print(f"Password for \"{self.site}\":  {self.password}")

    def copy_to_clipboard(self):
        '''
            Created password immediately is coping to clipboard
        '''
        clipboard.copy(self.password)



def quit():
    '''
        Quite from program
    '''
    while(True):
        input_key = input("Do you want to exit to program (y/n):  ")
        if input_key == 'y' or input_key == 'Y':
            exit(0)
        elif input_key == 'n' or input_key == 'N':
            return None
        else:
            continue

if __name__ == "__main__":
    while(True):
        password_object = password()
        input_site_name = input("Please enter the site name in (for example -> \"google.com\"): ")
        password_object.pass_creat(input_site_name)
        password_object.show_created_password()
        password_object.copy_to_clipboard()
        quit()
