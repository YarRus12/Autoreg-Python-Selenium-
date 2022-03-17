from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import mail_password_gen as gen

class MailReg:
    """Class Automail inits driver and functions login and mail """
    def __init__(self, BASE_DIR):
        self.driver = webdriver.Firefox()
        with open(BASE_DIR + '/Data/Info_for_new_eboxes', 'r', encoding='utf-8') as info:
            """Считывание файла с данными и преобразование его 
            в переменные выполнено для обеспечения масштабируемости проекта"""
            for line in info:
                full_name, self.sex, self.birthdate, self.phone_num = line.split(', ')
                self.surname, self.name = full_name.split()[0], full_name.split()[1]

    def yandex_registation(self, BASE_DIR):
        """Зарегистрировать новую электронную почту в любом почтовом сервисе"""
        #We choose yandex mailserver
        mail_service_address = 'https://passport.yandex.ru/registration/'
        self.driver.get(mail_service_address)
        # Вводим имя
        self.driver.find_element(By.XPATH, '//*[@id="firstname"]').send_keys(self.name)
        # Вводим фамилию
        self.driver.find_element(By.XPATH, '//*[@id="lastname"]').send_keys(self.surname)
        #вызываем функцию генерации логина
        email_address = gen.create_mail(self.name, self.surname, self.birthdate)
        #Вводим сгенерированный адрес эл. почты
        self.driver.find_element(By.XPATH, '//*[@id="login"]').send_keys(email_address)
        #вызываем функцию генерации пароля
        password = gen.create_password()
        #вводим сгенерированный пароль
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        #вводим сгенерированный пароль для подтверждения
        self.driver.find_element(By.XPATH, '//*[@id="password_confirm"]').send_keys(password)

        #Вводим номер телефона
        #self.driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(self.phone_num)
        #time.sleep(3)  # We use time sleep to give the page enoght time to load
        #  Нажимаем кнопку подтвердить номер телефона
        #self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[2]/div/div[2]/button').click()
        #time.sleep(5)  # We use time sleep to give the page enoght time to load
        # Вводим проверочный номер
        # telephone_code = input('Проверочный код, который назвал Вам оператор по номеру телефона или в СМС: ')
        # self.driver.find_element(By.XPATH, '//*[@id="phoneCode"]').send_keys(telephone_code)
        #time.sleep(1)  # We use time sleep to give the page enoght time to load

        #Нажимаем кнопку у меня нет номер телефона
        self.driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[2]/div/div[1]/span').click()
        time.sleep(3)
        # Вводим ответ на вопрос
        self.driver.find_element(By.XPATH, '//*[@id="hint_answer"]').send_keys('Кроваво-красное ничто')
        # Вводим capture
        answer = input("Введите символы:  ")
        self.driver.find_element(By.XPATH, '//*[@id="captcha"]').send_keys(answer)
        time.sleep(1)  # We use time sleep to give the page enoght time to load
        # Нажимаем кнопку зарегистрироваться
        self.driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/main/div/div/div/form/div[4]/span/button').click()
        # Нажимаем кнопку пропустить
        time.sleep(5)  # We use time sleep to give the page enoght time to load
        self.driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[2]/main/div/div/div/div[3]/span/a').click()
        written_line = f'{email_address}:{password}\n'
        """По завершению выполенния функции программа записывает сведения о логине и пароле 
        для дальнейшего использования. Скрипт можно улучшить и предусмотреть возможность дозаписывания новых логинов ('a').
        Но сейчас это не актуально"""
        with open(BASE_DIR + '/Data/Created_accounts.txt', 'w', encoding='utf-8') as f:
            f.write(written_line)
    def mailru_registation(self, BASE_DIR):
        """Данная функция оставлена для будущей возможности масштабирования класса с другими платформати """
        pass

if __name__ == '__main__':
    main = MailReg()
