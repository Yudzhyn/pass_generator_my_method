from randomMethod import passCreateRandom as randomMethod
from myMethod import passCreateMyOwn as myMethod
from SQLite import SQL_insert
import clipboard as cp

# the site for which the password is generated
class Password():

    pass_methods = ("My own method", "Random method", None)

    #for my own method
    keyword_standart = "plusultra"

    def __init__(self, site, method=2, password=""):
        self.method = self.pass_methods[method]
        self.site = site                                     # назва сайту, для якого треба згенерувати пароль
        self.password = password                             # пароль
        self.keyword = self.keyword_standart                 # ключове слово, по якому буде створений пароль    
        self.length_password = None
        #Password.passCreate(self)

    def passCreate(self):
        if self.method == self.pass_methods[0]:
            self.passCreateMyOwn(self)
        else:
            self.passCreateRandom(self)
        self.copy_to_clipboard(self)
        self.insert_into_db(self)


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

    @staticmethod
    def insert_into_db(self):
        SQL_insert(self.site, self.password, self.method)
