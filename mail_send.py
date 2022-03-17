from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import mail_password_gen as gen


class MailSend:
    """Class MailSend inits driver and functions to send mails """
    def __init__(self, BASE_DIR):
        self.driver = webdriver.Firefox()
        with open(BASE_DIR + '/Data/Created_accounts.txt', 'r', encoding='utf-8') as f:
            for line in f:
                self.login, self.password = line.split(':')[0], line.split(':')[1]
    def log_in_yandex(self):
        """ Login function sigh in googlemail with email and password as arguments"""
        #авторизация в почте Яндекса
        #self.driver.get('https://passport.yandex.ru/auth')
        #Ввод логина
        self.driver.find_element(By.ID, 'passp-field-login').send_keys(self.login)
        self.driver.find_element(By.ID, "passp:sign-in").click()
        time.sleep(3)  # We use time sleep to give the page enoght time to load
        #Ввод пароля
        self.driver.find_element(By.ID, "passp-field-passwd").send_keys(self.password)
        self.driver.find_element(By.ID, "passp:sign-in").click()

    def send_mail(self, BASE_DIR):
        """Mail functions receives email, theames and context for sending """
        self.driver.get('https://mail.yandex.ru')
        time.sleep(1)  # We use time sleep to give the page enoght time to load
        self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[4]/a[2]').click()
        try:
            self.driver.find_element(By.XPATH,
                                     '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[1]/div[2]/button').click()
        except:
            self.log_in_yandex()
            time.sleep(5)
            #Нажимаем написать письмо
            self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[7]/div/div[3]/div[2]/div[1]/div/div/div/a/span').click()
            time.sleep(3)  # We use time sleep to give the page enoght time to load
            emails_list = []
            with open(BASE_DIR + '/Data/Emails_list', 'r', encoding='utf-8') as emails:
                for line in emails:
                    emails_list.append(line)
            topic = 'Задание 1. На вакансию Junior Python developer'
            massage = ''
            with open(BASE_DIR + '/Data/Message', 'r', encoding='utf-8') as text:
                massage = [x for x in text]
            self.driver.find_element(By.CSS_SELECTOR, '.composeTextField').send_keys(topic)
            self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[10]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div[2]/div[1]/div/div/div').send_keys(massage)
            # Вставляем список рассылки
            for i in range(len(emails_list)):
                self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[10]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div/div').send_keys(emails_list[i])
            #Прикрепляем архив
            self.driver.find_element(By.CSS_SELECTOR,'input[type=file]').send_keys(file)
            #Нажимаем отправить
            self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[10]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/div[5]/span/span/div/input').click()

if __name__ == '__main__':
    MailSend()

