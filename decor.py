def show_logo():
    print("""
                             ####          ###      ######
                            ######       ######   ##
                          ###   ###     ##    ## ##
                         ###    ##     ##    ###  ##
                        ###           ##    ##     ###
                       ###           #######         ##
                      ###           ##                ##
                      ###          ##                 ##
                       ###  ###   ##                ##
                        #####   ####           ######
                                                        by Yudzhyn
        """)

def show_menu():
    print("""
  ====================================
        Select one of the items:
  ====================================
  [1] Create password for website
  ------------------------------------
  [2] Select password from database
  ------------------------------------
  [3] Show all passwords from database
  ------------------------------------
  [0] Exit
  ------------------------------------
            """)

###   ITEM 1

def show_create_top_text():
    print("""
  ===================================
  === Create password for website ===
  ===================================
    """)

def show_create_methods():
   print("""\n  Methods:\n
  ------------------------------------
  [0] Senchuk's method
  ------------------------------------
  [1] Random
  ------------------------------------
  """)

###   ITEM 2
def show_select_one():
    print("""
  =====================================
  === Select password from database ===
  =====================================
    """)

###   ITEM 3
def show_select_all():
    print("""
  ==========================================
  ||| Select all passwords from database |||
  ==========================================
    """)
