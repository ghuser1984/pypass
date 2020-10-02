import re

class Acc(object):
    def __init__(self,page,email,psswd):
        self.page=page
        self.email=email
        self.psswd=psswd

    def __repr__(self):
        return("Account for {} at {}".format(self.email,self.page))
    def __str__(self):
        return("{}, {}, {}".format(self.page,self.email,self.psswd))
    
    def get_page(self):
        return(self.page)
    def get_email(self):
        return(self.email)
    def get_psswd(self):
        return(self.psswd)
    
    
    def chng_psswd(self,psswd):
        pswwd=str(psswd)
        if len(pswwd)==0:
            print("No password provided")
        elif len(pswwd)<=6:
            print("Password too short")
        else:
            self.psswd=pswwd

tst=Acc("github.com","someone@mail.tr","123")
print(tst.get_page(), tst.get_email())
print(str(tst))
print(repr(tst))

dir(tst)

tst.chng_psswd("")
tst.chng_psswd(1234)
newpass="newpass123"
tst.chng_psswd(newpass)

print(tst.get_psswd())
