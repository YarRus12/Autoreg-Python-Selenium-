import os
import Regist as reg

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

emails_list = []
with open(BASE_DIR+'/Data/Emails_list', 'r', encoding='utf-8') as emails:
    for line in emails:
        emails_list.append(line)
    print(f'Адреса рассылок считаны!')

topic = 'Задание 1. На вакансию Junior Python developer'
massage = ''
with open(BASE_DIR+'/Data/Message', 'r', encoding='utf-8') as text:
    massage = [x for x in text]
    print(f'Сообщение считано')


with open(BASE_DIR + '/Data/Info_for_new_eboxes', 'r', encoding='utf-8') as info:
    """Считывание файла с данными и преобразование его 
    в переменные выполнено для обеспечения масштабируемости проекта"""
    for line in info:
        full_name, sex, birthdate, phone_num = line.split(', ')
        surname, name = full_name.split()[0], full_name.split()[1]

print(name, surname, birthdate, sex, phone_num)
