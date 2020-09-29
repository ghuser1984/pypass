class Acc(object):
    def __init__(self,page,email,psswd):
        self.page=page
        self.email=email
        self.psswd=psswd

    def get_page(self):
        return(self.page)
    def get_email(self):
        return(self.email)
    def get_psswd(self):
        return(self.psswd)
    
    def __str__(self):
        return("{}, {}, {}".format(self.page,self.email,self.psswd))

    def chng_psswd(self,psswd):
        if type(psswd)==str:
            self.psswd=psswd
        else:
            pass

tst=Acc("github.com","someone@mail.tr","123")
print(tst.get_page(), tst.get_email())
print(str(tst))

tst.chng_psswd("newpass11")
print(tst.get_psswd())
