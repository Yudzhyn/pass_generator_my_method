from randomMethod import passCreateRandom as randomMethod
from myMethod import passCreateMyOwn as myMethod
from SQLite import SQL_insert, SQL_select_one, SQL_update_one
import clipboard as cp

# the site for which the password is generated
class Password():

    pass_methods = ("My own method", "Random method", None)

    #for my own method
    keyword_standart = "plusultra"

    def __init__(self, site, method = 2):
        self.method = self.pass_methods[method]
        self.site = site                                     # назва сайту, для якого треба згенерувати пароль
        self.password = ""                                   # пароль
        self.keyword = self.keyword_standart                 # ключове слово, по якому буде створений пароль    
        self.length_password = None
        #Password.passCreate(self)

    def passCreate(self):
        if self.method == self.pass_methods[0]:
            self.passCreateMyOwn(self)
        else:
            self.passCreateRandom(self)
        self.copy_to_clipboard(self)


    def passShow(self):
        print(f"\n  Site: {self.site}, password: {self.password}")
        input("\n  Please press Enter for continue...")
        return None

    #########Methods##########

    @staticmethod
    def passCreateMyOwn(self):
        self.password = myMethod(self.site, self.keyword)

    @staticmethod
    def passCreateRandom(self):
        self.password = randomMethod()

    #########clipboard##########

    @staticmethod
    def copy_to_clipboard(self):
        '''
            Created password immediately is coping to clipboard
        '''
        cp.copy(self.password)

    ##########SQLite##########

    def insert_into_db(self):
        SQL_insert(self.site, self.password, self.method)

    def check_password_in_db(site_name):
        password_from_db = SQL_select_one(site_name)
        if password_from_db != None:
            print(f"""\n  This site already exists in the database.\n
  Its password is: {password_from_db}\n""")
            return 1
        return 0

    def update_password_in_db(self):
        SQL_update_one(self.site, self.password, self.method)
        return 0


