from logo import show_logo as logo
from passClass import Password

def loop():
    site = input("Please, enter site's name: ")
    method = int(input("Please, enter method (0 -- my own, 1 -- random): "))
    password = Password(method, site)
    password.passShow()

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

def _main():
    logo()
    while True:
        loop()
        quit()

if __name__ == "__main__":
    _main()
