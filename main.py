import decor
from passClass import Password
from SQLite import SQL_init, SQL_close, SQL_select_one, SQL_select_all
import os



def select_menu():
    """
        Select submenu from main menu
    """
    while True:
        select_item = clear_input("\n  Run: ")
        if select_item in range(0, 5):
            break
        else:
            print("\n  Select digit from correct diapason!")

    if select_item == 1:
        create_password()
    elif select_item == 2:
        select_password_from_database()
    elif select_item == 3:
        show_all_passwords_form_database()
    elif select_item == 0:
        SQL_close()
        os._exit(0)

def create_password():
    """
        ITEM 1
    """
    os.system('cls')

    create_mode = 1

    decor.show_create_top_text()

    site_name = input("  Please, enter site's name: ")

    if Password.check_password_in_db(site_name):
        print("  Do you want to update old password? [y/n]")
        if input("  ") == 'n':
            return 0
        create_mode = 0
        os.system('cls')
        decor.show_create_top_text()      # from logo_menu.py


    decor.show_create_methods()

    method = int(input("\n  Please, select method:"))
    password_obj = Password(site_name, method)

    if create_mode == 1:
        password_obj.passCreate()
        password_obj.insert_into_db()
    elif create_mode == 0:
        password_obj.passCreate()
        password_obj.update_password_in_db()

    password_obj.passShow()
    return 0


def select_password_from_database():
    """
        ITEM 2
    """
    os.system('cls')
    decor.show_select_one()
    site_name = input("  Please, enter site's name: ")
    password_ = SQL_select_one(site_name)
    password_obj = Password(site_name)
    password_obj.password = password_
    password_obj.passShow()
    return 0

def show_all_passwords_form_database():
    """
        ITEM 3
    """
    os.system('cls')
    decor.show_select_all()
    data = SQL_select_all()
    show_data_in_table(data)
    input("\n  Please press Enter for continue...")

############### helpful functions #################

def show_data_in_table(data):
    longest_site_string = max(map(len, data.keys()))
    longest_pass_string = max(map(len, data.values()))
    for key in data.keys():
        output_sep = "=" * (longest_site_string * 2 + 12)
        print("  " + output_sep)
        output_site = "|| " + key + " " * (longest_site_string - len(key)) + " | "
        output_password = data[key] + " " * (longest_pass_string - len(data[key])) + " ||"
        print("  " + output_site + output_password)
    print("  " + output_sep)
    return 0

def clear_input(text):
    while True:
        try:
            return_data = int(input(text))
        except ValueError:
            continue
        return return_data

###################### main functions #######################

def _main():
    """
        Loop main program
    """
    while True:
        os.system('cls')
        decor.show_logo()
        decor.show_menu()
        select_menu()


if __name__ == "__main__":
    SQL_init()
    _main()
