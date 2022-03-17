import re
import random

def create_mail(name,surname,birthdate):
    birthdate = birthdate.split('.')
    return f'{name}.{surname}{(int(birthdate[0])*random.randint(1,9)*random.randint(1,9))//random.randint(1,100)}{int(birthdate[1])*random.randint(1,9)}'

def create_password():
    length = random.randint(10, 20)
    varchar = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_!@#$%^&*()_!@#$%^&*()_!@#$%^&*()_!@#$%^&*()')
    flag = 'False'
    while flag != "True":
        password = ''.join([random.choice(varchar) for _ in range(length)])
        if re.findall(r'[A-Za-z0-9@#$%^&+=]', password):
            flag = 'True'
    return password

#print(create_password())
#print(create_mail('Anton','Groznyi','12.11.1990'))



