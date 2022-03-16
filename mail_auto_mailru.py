from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import mail_password_gen as gen
import os
#from selenium.webdriver.common.keys import Keys

class Automail:
    """Class Automail inits driver and functions login and mail """
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.driver = webdriver.Chrome()
    def registry(self, name, surname, birthdate, sex, telephone):
        """Зарегистрировать новую электронную почту в любом почтовом сервисе"""
        #We choose mailru server
        mail_registration = 'https://account.mail.ru/signup'
        self.driver.get(mail_registration)
        # Вводим имя
        self.driver.find_element(By.XPATH, '//*[@id="fname"]').send_keys(name)
        # Вводим фамилию
        self.driver.find_element(By.XPATH, '//*[@id="lname"]').send_keys(surname)
        birthdate = birthdate.split('.')
        # Вводим день рождения







        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/div/form/div[5]/'
                                           'div[2]/div/div[1]/div/div/div/div/div[1]/span').send_keys(birthdate[0])
        # Вводим месяц рождения
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/div/form/div[5]/'
                                           'div[2]/div/div[3]/div/div/div/div[1]').send_keys(birthdate[1])
        # Вводим год рождения
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/div/form/div[5]/'
                                           'div[2]/div/div[5]/div/div/div/div/div[1]').send_keys(birthdate[2])
        # Выбираем пол
        if sex == 'M':
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[3]/div[4]/div/div/'
                                               'div/div/form/div[8]/div[2]/div/label[1]').click()
        elif sex == 'Ж':
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/div/'
                                               'form/div[8]/div[2]/div/label[2]/div[2]/span').click()
        #вызываем функцию генерации адреса эл почты
        email_address = gen.create_mail(name, surname, birthdate)
        #Вводим сгенерированный адрес эл. почты
        self.driver.find_element(By.XPATH, '//*[@id="aaa__input"]').send_keys(email_address)
        #вызываем функцию генерации пароля
        password = gen.create_password()
        #вводим сгенерированный пароль
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        # вводим сгенерированный пароль для подтверждения
        self.driver.find_element(By.XPATH, '//*[@id="repeatPassword"]').send_keys(password)
        #Нажимаем кнопку создать
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[3]/div[4]/div/div/div/div/form/button/span').click()
        time.sleep(3)  # We use time sleep to give the page enoght time to load
        # Нажимаем кнопку далее
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()
        time.sleep(3)  # We use time sleep to give the page enoght time to load
        # Принимаем условия конфиденциальности
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[3]").click()
        time.sleep(3)  # We use time sleep to give the page enoght time to load

    def log_in(self, email, password):
        """ Login function sigh in googlemail with email and password as arguments"""
        self.driver.get('https://accounts.google.com/signin/v2/identifier')
        self.driver.find_element(By.ID, "identifierId").send_keys(email)
        self.driver.find_element(By.ID, "identifierNext").click()
        time.sleep(3) #We use time sleep to give the page enoght time to load
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.ID, "passwordNext").click()

    def send_mail(self, email, topic, message):
        """Mail functions receives email, theames and context for sending """
        self.driver.get('https://mail.google.com')
        time.sleep(3) #We use time sleep to give the page enoght time to load
        self.driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]'
                                           '/div[1]/div/div/div/div[1]/div/div').click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '#\:fw').send_keys(email)# Вот здесь проблема!

if __name__ == '__main__':
    result = Automail()
    email, password = result.registry('Andey', 'Makarov', '12.12.1976', 'М','(914)193-98-90')
    #result.log_in(email, password)
    #result.send_mail(email, topic, message)
