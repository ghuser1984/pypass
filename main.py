import random, string

def enter_creds():
    mail=input("Your email: ")
    acct=input("Your account: ")
    pssw=input("Your password: ")
    return(mail,acct,pssw)

def check_creds(lst):
    if len(lst)==3:
        print("mail: {}\nacct: {}\npassw: {}\n".format(lst[0],lst[1],lst[2]))
    else:
        print("Only {} credential featurs provided".format(len(lst)))

def gen_psswd():
    tmpl=list(string.ascii_letters+string.digits)
    pswd=''.join(random.sample(tmpl,k=random.randint(8,12)))
    return(pswd)

def chk_psswd(psswd):
    pass

#creds= enter_creds()
#check_creds(creds)
for i in range(10):
    print(gen_psswd())