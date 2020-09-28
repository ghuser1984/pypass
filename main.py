def enter_creds():
    mail=input("Your email: ")
    acct=input("Your account: ")
    pssw=input("Your password: ")
    return(mail,acct,pssw)

creds= enter_creds()
print("mail: {}\nacct: {}\npassw: {}\n".format(creds[0],creds[1],creds[2]))