from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import mail_password_gen as gen
from datetime import datetime

class MailSend:
    """Class MailSend inits driver and functions to send mails """
    def __init__(self, base_direction):
        self.base_direction = base_direction
        self.driver = webdriver.Firefox()
        with open(self.base_direction + '/Data/Created_accounts.txt', 'r', encoding='utf-8') as f:
            for line in f:
                self.login, self.password = line.split(':')[0], line.split(':')[1]


class YandexMailSend(MailSend):
    def log_in_yandex(self):
        """ Login function sigh in yandexmail with email and password as arguments"""
        #авторизация в почте Яндекса
        #Ввод логина
        self.driver.find_element(By.ID, 'passp-field-login').send_keys(self.login)
        self.driver.find_element(By.ID, "passp:sign-in").click()
        self.driver.implicitly_wait(5)
        #Ввод пароля
        self.driver.find_element(By.ID, "passp-field-passwd").send_keys(self.password)
        self.driver.find_element(By.ID, "passp:sign-in").click()
        print(f'Вход в аккаунт {self.login} выполнен успешно!')

    def yand_send_mail(self):
        """Функция по отправке писем, принимает в себя сведения о текущем расположении проекта"""
        self.driver.get('https://mail.yandex.ru')
        self.driver.implicitly_wait(1) # We use wait to give the page enough time to load
        #Нажатие кнопки "Войти"
        self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div/div[4]/a[2]').click()
        # У Яндекса рамдомно выпадает два варианта входа. Попробуем более редкий через исключения
        try:
            self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[1]/div[2]/button').click()
        except:
            pass
        #Используем функция входа в аккаунта яндекс почты
        self.log_in_yandex()
        time.sleep(10)
        # При добавлении новой почты Яндекc предлагает добавить дополнительную почту. Обработаем как исключение
        self.driver.implicitly_wait(5) # We use wait to give the page enough time to load
        try:
            self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/form/div[3]/button').click()
        except:
            pass
            # Либо при добавлении новой почты Яндекc предлагает подтвердить номер телефона. Обработаем как исключение
        try:
            self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[2]/button').click()
            telephone_code = input('Проверочный код, который назвал Вам оператор по номеру телефона или в СМС: ')
            self.driver.find_element(By.XPATH, '//*[@id="passp-field-phoneCode"]').send_keys(telephone_code)
            self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[2]/form/div[2]/button').click()
            self.driver.implicitly_wait(5) # We use wait to give the page enough time to load
        except:
           pass
        self.driver.implicitly_wait(3) # We use wait to give the page enough time to load
        # Может встплыть окно "С красивым адресом почты"
        try:
            self.driver.find_element(By.XPATH, '/html/body/div[13]/div[2]/div/div/div/article/span/button').click()
        except:
            pass
        #Нажимаем написать письмо
        try:
            self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[7]/div/div[3]/div[2]/div[1]/div/div/div/a/span').click()
            self.driver.implicitly_wait(5) # We use wait to give the page enough time to load
        except:
            self.driver.find_element(By.XPATH,
                                     '/html/body/div[2]/div[2]/div[7]/div/div[3]/div[2]/div[1]/div/div/div/a/span').click()

        #Вставляем тему
        topic = 'Задание 1. На вакансию Junior Python developer'
        self.driver.find_element(By.CSS_SELECTOR, '.composeTextField').send_keys(topic)

        #Вставляем сообщение
        with open(self.base_direction + '/Data/Message', 'r', encoding='utf-8') as text:
                massage = [x for x in text]
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[10]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div[2]/div[1]/div/div/div').send_keys(massage)
        self.driver.implicitly_wait(5) # We use wait to give the page enough time to load

        # Вставляем список рассылки
        emails_list = []
        with open(self.base_direction + '/Data/Emails_list', 'r', encoding='utf-8') as emails:
            for line in emails:
                emails_list.append(line)
        for i in range(len(emails_list)):
            self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[10]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div/div').send_keys(emails_list[i])
        self.driver.implicitly_wait(5)  # We use wait to give the page enough time to load
        #Прикрепляем архив
        path = self.base_direction + '\Data\Selenium_JPD.rar'
        self.driver.find_element(By.CSS_SELECTOR,'input[type=file]').send_keys(path)
        time.sleep(20) # We use time.sleep to give the page enough time to load
        while True:
            try:
                # Нажимаем отправить
                self.driver.find_element(By.CSS_SELECTOR, 'button.Button2_view_default').click()
                print("Нажата кнопка отправить")

                # Если время загрузки архива недостаточно то откроется окно с соответствующей записью
                # обрабатываем его как исключение
                try:
                    self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[10]/div/div/div[2]/div/div[2]/div/div[1]/div[3]/div/div/div/div/div[3]/button').click()
                    print("Нажата кнопка продолжить загрузку")
                    continue
                except:
                    pass
                break
            except:
                pass
            # После нажатия кнопки отправить сервис может проверить нас на спам
            # Обрабатываем как исключение
        try:
            print("Сканирование проверки на спам")
            spam_sec = self.driver.find_element(By.XPATH,
                        '/html/body/div[2]/div[2]/div[10]/div/div/div[2]/div/div[2]/div/div[1]/div[3]/div/div/div/div/div[2]/div/div/div[2]/input')
            if spam_sec is not None:
                print("Обнаружена защита от спама")
                check = input('Введите символы на картинке: ')
                spam_sec.send_keys(check)
                self.driver.find_element(By.XPATH,
                        '/html/body/div[2]/div[2]/div[10]/div/div/div[2]/div/div[2]/div/div[1]/div[3]/div/div/div/div/div[3]/button').click()
                time.sleep(10)
            print(f'Письмо отправлено в {datetime.now()}')
        except:
            print(f'Письмо отправлено в {datetime.now()}')
        self.driver.implicitly_wait(1)
        self.driver.quit()

if __name__ == '__main__':
    MailSend()

