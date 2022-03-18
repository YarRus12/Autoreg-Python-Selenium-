from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import mail_password_gen as gen
from selenium.webdriver.support.ui import WebDriverWait


class MailboxReg:
    """Класс задает аргументы для регистрации наследуемым классам"""
    def __init__(self, base_directory):
        self.driver = webdriver.Firefox()
        self.base_directory = base_directory
        with open(self.base_directory + '/Data/Info_for_new_eboxes', 'r', encoding='utf-8') as info:
            """Считывание файла с данными и преобразование его 
            в переменные выполнено для обеспечения масштабируемости проекта"""
            for line in info:
                full_name, self.sex, self.birthdate, self.phone_num = line.split(', ')
                self.surname, self.name = full_name.split()[0], full_name.split()[1]


class YandexReg(MailboxReg):
    """Наследуемый класс для регистрации почтового ящика в сервисе яндекса с родительскими аргументами """
    def yandex_registation(self):
        """Функция регистрации почтового ящика в почтовом сервисе яндекса"""
        while True:
            try:
                # Создаем переменную с адресом регистрации в почтовом сервисе
                mail_service_address = 'https://passport.yandex.ru/registration/'
                # Подключаемся к адрессу регистрации
                self.driver.get(mail_service_address)
                # Вводим имя
                self.driver.find_element(By.ID, 'firstname').send_keys(self.name)
                # Вводим фамилию
                self.driver.find_element(By.ID, 'lastname').send_keys(self.surname)
                # Вызываем функцию генерации логина и передаем ее результаты в виде кортежа в переменную
                self.email_address = gen.create_mail(self.name, self.surname, self.birthdate)
                # Вводим сгенерированный логин в поле
                self.driver.find_element(By.ID, 'login').send_keys(self.email_address)
                # Вызываем функцию генерации пароля и передаем ее результаты в переменную
                self.password = gen.create_password()
                # Вводим сгенерированный пароль в поле
                self.driver.find_element(By.ID, 'password').send_keys(self.password)
                # Вводим сгенерированный пароль для подтверждения
                self.driver.find_element(By.ID, 'password_confirm').send_keys(self.password)

                """ Ниже приведенный код сохраняем на случай изменения политики 
                    безопасности сервиса и оперативного перевода       
                    #Вводим номер телефона
                    self.driver.find_element(By.ID, 'phone').send_keys(self.phone_num)
                    # Нажимаем кнопку подтвердить номер телефона
                    self.driver.find_element(By.XPATH, 
                    '/html/body/div/div/div[2]/div/main/div/div/div/form/div[3]/div/div[2]/div/div[2]/button').click()
                    time.sleep(5)  # We use time sleep to give the page enoght time to load
                    # Вводим проверочный номер
                    telephone_code = input('Проверочный код, который назвал Вам оператор по номеру телефона или в СМС: ')
                    self.driver.find_element(By.XPATH, '//*[@id="phoneCode"]').send_keys(telephone_code)
                    time.sleep(1)  # We use time sleep to give the page enoght time to load
                """
                try:
                    # Нажимаем кнопку у меня нет номер телефона
                    self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/main/div/div/'
                                                       'div/form/div[3]/div/div[2]/div/div[1]/span').click()
                except:
                    print('Похоже кнопка ввода данных без номера телефона отсутсвует. '
                          'Продолжение выполнения скрипта не даст результаты. '
                          'Нужно начинать заново')
                    break
                # Вводим ответ на вопрос
                self.driver.find_element(By.ID, 'hint_answer').send_keys('Кроваво-красное ничто')
                # Вводим capture
                answer = input("Введите символы:  ")
                self.driver.find_element(By.ID, 'captcha').send_keys(answer)
                time.sleep(1)  # We use time sleep to give the page enoght time to load
                # Нажимаем кнопку зарегистрироваться
                self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/main/div/div/'
                                                      'div/form/div[4]/span/button').click()
                # Нажимаем кнопку пропустить
                time.sleep(3)  # We use time sleep to give the page enoght time to load
                self.driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[2]/main/div/div/div/div[3]/span/a').click()
                """По завершению выполенния функции программа записывает сведения о логине и пароле 
                        для дальнейшего использования. Скрипт можно улучшить и предусмотреть возможность дозаписывания новых логинов ('a').
                        Но сейчас это не актуально"""
                try:
                    written_line = f'{self.email_address}:{self.password}\n'
                    with open(self.base_directory + '/Data/Created_accounts.txt', 'w', encoding='utf-8') as f:
                        f.write(written_line)
                    print(f"Почта создана! Данные об аккаунте сохранены в файл {self.base_directory}/Data/Created_accounts.txt'")
                except:
                    print(f"Ошибка {EOFError}")
                    break
                break
            except:
                pass

class Mailru(MailboxReg):

    def mailru_registation(self):
        """Данная функция оставлена для будущей возможности масштабирования класса с другими платформати """
        pass

if __name__ == '__main__':
    main = MailReg()
