import os
import mail_auto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
(os.listdir(BASE_DIR+'/Data'))

emails_list = []
with open(BASE_DIR+'/Data/Emails_list', 'r', encoding='utf-8') as emails:
    for line in emails:
        emails_list.append(line)
topic = 'Задание 1. На вакансию Junior Python developer'
massage = ''
with open(BASE_DIR+'/Data/Message', 'r', encoding='utf-8') as text:
    massage = [x for x in text]

with open(BASE_DIR+'/Data/Info_for_new_eboxes', 'r', encoding='utf-8') as info:
    """Считывание файла с данными и преобразование его 
    в переменные выполнено для обеспечения масштабируемости проекта"""
    for line in info:
        full_name, sex, birthdate = line.split(', ')
        name = full_name.split()[1]
        surname = full_name.split()[0]

result = mail_auto.Automail()
email, password = result.registry(name, surname, birthdate, s)
result.log_in(email, password)
result.send_mail(email, topic, message)
print()

##print(emails_list, topic, *massage)
