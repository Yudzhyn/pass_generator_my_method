from logo_menu import logo, menu
from passClass import Password
from SQLite import SQL_init, SQL_close, SQL_select_one, SQL_select_all
import os

def select_menu():
    """
        Select submenu from main menu
    """
    while True:
        select_item = int(input("\n  Run: "))
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
    print("""
  ===================================
  === Create password for website ===
  ===================================
    """)
    site_name = input("  Please, enter site's name: ")
    print("""\n  Methods:\n
  ------------------------------------
  [0] Senchuk's method
  ------------------------------------
  [1] Random
  ------------------------------------
  """)
    method = int(input("\n  Please, select method:"))
    password_obj = Password(site_name, method)
    password_obj.passCreate()
    password_obj.passShow()
    return 0


def select_password_from_database():
    """
        ITEM 2
    """
    os.system('cls')
    print("""
  =====================================
  === Select password from database ===
  =====================================
    """)
    site_name = input("  Please, enter site's name: ")
    password_ = SQL_select_one(site_name)
    password_obj = Password(site_name, password = password_)
    password_obj.passShow()
    return 0

def show_all_passwords_form_database():
    """
        ITEM 3
    """
    os.system('cls')
    print("""
  ==========================================
  ||| Select all passwords from database |||
  ==========================================
    """)
    data = SQL_select_all()
    for key in data.keys():
        print(f"\n  Site: {key} --> Password: {data[key]}")
    input("\n  Please press Enter for continue...")

def _main():
    """
        Loop main program
    """
    while True:
        os.system('cls')
        logo()
        menu()
        select_menu()


if __name__ == "__main__":
    SQL_init()
    _main()
