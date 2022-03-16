from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import mail_password_gen as gen
import os

class Automail:
    """Class Automail inits driver and functions login and mail """
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.driver = webdriver.Firefox()

    def registry(self, name, surname, birthdate, sex, telephone):
        """Зарегистрировать новую электронную почту в любом почтовом сервисе"""
        #We choose gmail server
        mail_registration = 'https://account.mail.ru/signup'
        self.driver.get(mail_registration)


if __name__ == '__main__':
    result = Automail()
    result.registry('Andey', 'Makarov', '12.12.1976', 'М','(914)193-98-90')


#https://russianblogs.com/article/856680849/