from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import mail_password_gen as gen
#from selenium.webdriver.common.keys import Keys

class Automail:
    """Class Automail inits driver and functions login and mail """
    def __init__(self):
        self.driver = webdriver.Firefox()

    def registry(self, name, surname, birthdate, s, telephone):
        """Зарегистрировать новую электронную почту в любом почтовом сервисе"""
        #We choose yandex mailserver
        mail_registration = 'https://passport.yandex.ru/registration/'
        self.driver.get(mail_registration)
        # Вводим имя
        self.driver.find_element(By.XPATH, '//*[@id="firstname"]').send_keys(name)
        # Вводим фамилию
        self.driver.find_element(By.XPATH, '//*[@id="lastname"]').send_keys(surname)
        #вызываем функцию генерации логина
        email_address = gen.create_mail(name,surname,birthdate)
        #Вводим сгенерированный адрес эл. почты
        self.driver.find_element(By.XPATH, '//*[@id="login"]').send_keys(email_address)
        #вызываем функцию генерации пароля
        password = gen.create_password()
        #вводим сгенерированный пароль
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        #вводим сгенерированный пароль для подтверждения
        self.driver.find_element(By.XPATH, '//*[@id="password_confirm"]').send_keys(password)
        #Вводим номер телефона
        self.driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(telephone)
        #  Нажимаем кнопку далее
        self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[2]/div/div[2]/button').click()
        time.sleep(3)  # We use time sleep to give the page enoght time to load
        # Вводим проверочный номер
        telephone_code = input('Проверочный код, который назвал Вам оператор по номеру телефона или в СМС: ')
        self.driver.find_element(By.XPATH, '//*[@id="phoneCode"]').send_keys(telephone_code)
        time.sleep(1)  # We use time sleep to give the page enoght time to load
        # Нажимаем кнопку зарегистрироваться
        self.driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/main/div/div/div/form/div[4]/span/button').click()
        # Нажимаем кнопку пропустить
        time.sleep(3)  # We use time sleep to give the page enoght time to load
        self.driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[2]/main/div/div/div/div[3]/span/a').click()
        return email_address, password

    def log_in(self, email, password):
        """ Login function sigh in googlemail with email and password as arguments"""
        self.driver.get('https://mail.yandex.ru')
        self.driver.find_element(By.ID, "identifierId").send_keys(email)
        self.driver.find_element(By.ID, "identifierNext").click()
        time.sleep(3) #We use time sleep to give the page enoght time to load
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.ID, "passwordNext").click()

    def send_mail(self, email, topic, message):
        """Mail functions receives email, theames and context for sending """
        self.driver.get('https://mail.google.com')
        time.sleep(1) #We use time sleep to give the page enoght time to load
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[7]/div/div[3]/div[2]/div[1]/div/div/div/a/span').click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '#\:fw').send_keys(email)# Вот здесь проблема!

if __name__ == '__main__':
    result = Automail()
    #email_address_password = result.registry('Andey', 'Makarov', '12.12.1976', 'М','(924)214-03-96')
    #print(email_address_password)
    #result.log_in(email, password)
    #result.send_mail(email, topic, message)
