import re

# name validation
def NameValidation(name):
    ptr = "[a-zA-Z]+$"
    if re.match(ptr,name):
        return name
    else:
        return False
def UserNameValidation(username):
    ptr = "^[a-zA-Z]+[0-9]+[a-zA-Z]+$"
    if re.match(ptr,username):
        return True
    else:
        return False
    
def EmailValidation(Email):
    ptr = "^[a-z0-9\_\.]+@[a-z]+\.+[com|in|org]+$"
    if re.match(ptr,Email):
        return True
    else:
        return False

def ContactValidation(contact):
    ptr="(0|91)?[6-9][0-9]{9}$"
    if re.match(ptr,contact):
        return True
    else:
        return False
    
def PasswordValidation(pass1,pass2):
    if len(pass1) >= 8 and pass1 == pass2:
        return True
    else:
        return False
    
def dpvalidation(id):
    ptr = r"\d{1}:\d{2}:\d{3}:\d{4}:\d{5}:\d{6}:\d{7}:"
    if re.match(ptr,id):
        return True
    else:
        return False
