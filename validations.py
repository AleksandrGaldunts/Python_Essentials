def validate_username(func):
    def wrapper(*args,**kwargs):
        if 5<=len(args[0])<=20 and args[0].lower()!= 'admin' and args[0].lower()!= 'root':
            if args[0].isalnum():
                return func(*args,**kwargs)
        raise ValueError('Registration failed')
    return wrapper


def validate_email(func):
    def wrapper(*args, **kwargs):
        if '@' not in args[0] and '.' not in args[0]:
            raise ValueError("Invalid email")

        len_1 = args[0].split('@')
        if len(len_1) == 2:
            if len_1[0].isalnum() and not len_1[0][0].isdigit():
                len_1 = len_1[1].split('.')
                if len(len_1) > 1:
                    if len(len_1[0]) >= 2:
                        return func(*args, **kwargs)
        raise ValueError("Invalid email")

    return wrapper


def validate_phone(func):
    def wrapper(*args,**kwargs):
        if len(args[0])==12 and args[0][0]=='+' and args[0][1:].isdigit() or (len(args[0])==9 and args[0][0]=='0' and args[0].isdigit()):
            return func(*args,**kwargs)
        raise Exception
    return wrapper


def validate_password(func):
    def wrapper(*args,**kwargs):
        if len(args[0])<8:
            raise Exception
        characters = {'!', '@', '#', '$', '%', '&', '*'}
        if any(char in characters for char in args[0]):
            if any(c.isupper() for c in args[0]):
                if any(c.isdigit() for c in args[0]):
                    if any(c.islower() for c in args[0]):
                        return func(*args, **kwargs)
        raise Exception
    return wrapper


def password_repeat(func):
    def wrapper(*args,**kwargs):
        if args[0]==args[1]:
            return func(*args,**kwargs)
        raise Exception
    return wrapper

@validate_username
def check_username(username):
    try :
        Username=username
    except ValueError as f:
        print(f"{f}")

@validate_email
def check_email(email):
    try:
        email=email
    except Exception as e:
        print(e)
@validate_phone
def check_phone(phone):
    try:
        phone=phone
    except Exception as e:
        print(e)
@validate_password
def check_password(password):
    try:
        password = password
    except Exception as e:
        print(e)
@password_repeat
def check_repass(repeat_password,password):
    try:
        repeat_password = repeat_password
        password=password
    except Exception as e:
        print(e)




username = input("Enter your username:  ")
check_username(username)

email = input("Enter your email: ")
check_email(email)

phone = input("Enter your phone number:   ")
check_phone(phone)

password = input("Enter your password:       ")
check_password(password)

password_repeat = input("Repeat your password:    ")
check_repass(password_repeat,password)


