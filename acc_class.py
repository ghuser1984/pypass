import re

def check_email(email):
    '''function checks if passed email corresponds to overall email syntax'''
    pass

class Acc(object):
    #account class constructor 
    def __init__(self,page,email,psswd):
        assert type(page)==str, 'Incorrect email type, should be string'
        assert type(email)==str, 'Incorrect email type should be string'
        self.page=page
        self.email=[] #using list here in case there is more than one email associated with this page
        self.psswd=psswd
        self.email.append(email)

    @property
    def psswd(self):
        return self.__psswd
    
    @psswd.setter
    def psswd(self, psswd):
        assert len(psswd)>=8, "password must be at least 8 characters long"
        self.__psswd=psswd

    def __repr__(self):
        return("Account for {} at {}".format(self.email[0],self.page))
    def __str__(self):
        return("{}, {}, {}".format(self.page,self.email[0],self.psswd))
    
    #some small class methods
    def get_page(self):
        return(self.page)
        
    def get_email(self):
        assert len(self.email)>=1, 'No email provided'
        if len(self.email)==1:
            return(self.email[0])
        else:
            if len(self.email)==2:
                return("{}, {}".format(self.email[0],self.email[1]))
            elif len(self.email)==3:
                return("{}, {}, {}".format(self.email[0],self.email[1],self.email[2]))
    
    def get_psswd(self):
        return(self.psswd)

    @property
    def accnt(self):
        return(self.email[0],self.page)
    
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

    def chng_email(self,email,primary=True):
        assert type(email)==str, 'Wrong email type'
        if primary==True:
            #need to add re check here!!!
            self.email[0]=email
        else:
            if len(self.email)>3:
                print('This account already has three email adresses, canot add more')
            else:
                self.email.append(email)
            




tst=Acc("github.com","someone@mail.tr","12345678")
print(tst.get_page(), tst.get_email())
print(tst.accnt)
print(str(tst))
print(repr(tst))
tst2=Acc("github.com","someone@mail.tr","12345678")

print(tst.comp_accs(tst2))
tst.chng_psswd("")
tst.chng_psswd(1234)
newpass="newpass123"
tst.chng_psswd(newpass)

print(tst.get_psswd())

tst.chng_email('some1else@mail.com')
print(tst.get_email())
tst.chng_email('anotheremail@mail.hz',primary=False)
print(tst.get_email())
tst.chng_email('andonemore@mail.hh',primary=False)
print(tst.get_email())