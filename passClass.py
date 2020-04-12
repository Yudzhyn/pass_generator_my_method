from randomMethod import passCreateRandom as randomMethod
from myMethod import passCreateMyOwn as myMethod
import clipboard

# the site for which the password is generated
class Password():

    pass_methods = ("My own method", "Random method")

    #for my own method
    keyword_standart = "plusultra"

    def __init__(self, method, site):
        self.method = self.pass_methods[method]
        self.site = site                                     # назва сайту, для якого треба згенерувати пароль
        self.password = ""                                   # сам пароль
        self.keyword = self.keyword_standart                 # ключове слово, по якому буде створений пароль    
        self.length_password = None
        Password.passCreate(self)

    def passCreate(self):
        if self.method == self.pass_methods[0]:
            self.passCreateMyOwn(self)
        else:
            self.passCreateRandom(self)
        self.copy_to_clipboard(self)

    def passShow(self):
        print(f"Site: {self.site}, password: {self.password}")
        return None

    @staticmethod
    def passCreateMyOwn(self):
        self.password = myMethod(self.site, self.keyword)

    @staticmethod
    def passCreateRandom(self):
        self.password = randomMethod()

    @staticmethod
    def copy_to_clipboard(self):
        '''
            Created password immediately is coping to clipboard
        '''
        clipboard.copy(self.password)

