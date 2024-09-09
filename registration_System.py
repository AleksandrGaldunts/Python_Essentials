import re
import string_Problems
def validate_username(registrate_user):
    def inner(**kwargs):
        if len(kwargs['username']) < 5 or len(kwargs['username']) > 20:
            raise ValueError("invalid username")
        if not kwargs['username'].isalpha():
            raise ValueError("invalid username")
        if kwargs['username'].lower() == "admin" or kwargs['username'].lower() == 'root' or kwargs['username'].lower() == 'user':
            raise ValueError("invalid username")
        registrate_user(**kwargs)
    return inner
def validate_email(registrate_user):
    def inner(**kwargs):
        email_pattern = r'^[a-zA-Z]{1,}.*\@[a-z]{1,}\.[a-zA-Z]{2,}$'
        if not (re.search(email_pattern, kwargs['email'])):
            raise ValueError("invalid email")
        return registrate_user(**kwargs)
    return inner
def validate_phone(registrate_user):
    def inner(**kwargs):
        pattern = r'^\d{9}$'
        if re.search(pattern , kwargs['phone']):
            return registrate_user(**kwargs)
        pattern = r'^\+\d{11}$'
        if re.search(pattern, kwargs['phone']):
            return registrate_user(**kwargs)
        raise ValueError("not valid phone")
    return inner
def validate_pass(registrate_user):
    def inner(**kwargs):
        up_statement = False
        low_statement = False
        special_statement = False
        num_statement = False
        specials = ['/', '+', '*']
        up_letters = set(string.ascii_uppercase)
        low_letters = set(string.ascii_lowercase)
        for i in kwargs['pwd']:
            if i in low_letters:
                low_statement = True
            if i in up_letters:
                up_statement = True
            if i in specials:
                special_statement = True
            if i.isnumeric():
                num_statement = True
        if not (low_statement and up_statement and special_statement and num_statement):
            raise ValueError("invalid password")
        return registrate_user(**kwargs)
    return inner
def pass_repeat(registrate_user):
    def inner(**kwargs):
        if not (kwargs['pwd'] == kwargs['rep_pwd']):
            raise ValueError("not valid repitition of password")
        return registrate_user(**kwargs)
    return inner
@pass_repeat
@validate_pass
@validate_phone
@validate_email
@validate_username
def registrate_user(username = '', email = '', phone = '', pwd = '', rep_pwd = ''):
    return True
while True:
    try:
        usrname = input()
        email = input()
        phone = input()
        pwd = input()
        rep_pwd = input()
        print(registrate_user(username = usrname,email= "d9@mail.com",phone= "+37491111111",pwd= "qwertT+1",rep_pwd= "qwertT+1"))
        break
    except ValueError as e:
        print(e)