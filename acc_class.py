import re

class Acc(object):
    def __init__(self,page,email,psswd):
        self.page=page
        self.email=email
        self.psswd=psswd

    @property
    def psswd(self):
        return self.__psswd
    
    @psswd.setter
    def psswd(self, psswd):
        assert len(psswd)>5, "password must be at least 6 characters long"
        self.__psswd=psswd

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

    @property
    def accnt(self):
        return(self.email,self.page)
    
    def comp_accs(self,other):
        if not isinstance (other, Acc):
            return NotImplemented
        else:
            return(self.email==other.email and self.page==other.page)
    
    def chng_psswd(self,psswd):
        pswwd=str(psswd)
        if len(pswwd)==0:
            print("No password provided")
        elif len(pswwd)<8:
            print("Password too short")
        else:
            self.psswd=pswwd

    def chng_email(self,email):
        if type(email)==str:
            #need to add re-check here!!!
            self.email=email
        else:
            pass

tst=Acc("github.com","someone@mail.tr","123456")
print(tst.get_page(), tst.get_email())
print(tst.accnt)
print(str(tst))
print(repr(tst))
tst2=Acc("github.com","someone@mail.tr","123456")

print(tst.comp_accs(tst2))
tst.chng_psswd("")
tst.chng_psswd(1234)
newpass="newpass123"
tst.chng_psswd(newpass)

print(tst.get_psswd())
