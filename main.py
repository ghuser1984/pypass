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


creds= enter_creds()
check_creds(creds)