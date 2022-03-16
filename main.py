import os
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


#main.login('sometestname12341234@gmail.com', 'sometest1234')
#main.mail(emails_list, topic, *massage)
print(emails_list, topic, *massage)