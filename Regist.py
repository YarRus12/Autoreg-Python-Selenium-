from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import mail_password_gen as gen

class MailReg:
    """Class Automail inits driver and functions login and mail """
    def __init__(self):
        self.driver = webdriver.Firefox()

    def yandex_registation(self, name, surname, birthdate, sex, telephone):
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
        time.sleep(1)  # We use time sleep to give the page enoght time to load
        #  Нажимаем кнопку подтвердить номер телефона
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

    def mailru_registation(self, name, surname, birthdate, s, telephone):
        """Зарегистрировать новую электронную почту в любом почтовом сервисе"""
        pass

if __name__ == '__main__':
    main = MailReg()
