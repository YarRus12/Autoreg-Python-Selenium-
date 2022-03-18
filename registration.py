import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import mail_password_gen as gen
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


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
        # Вызываем функцию генерации логина и пароля. Передаем ее результаты в виде кортежа в переменную
        self.email_address = gen.create_mail(self.name, self.surname, self.birthdate)
        # Вызываем функцию генерации пароля и передаем ее результаты в переменную
        self.password = gen.create_password()


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
                # Вводим сгенерированный логин в поле
                self.driver.find_element(By.ID, 'login').send_keys(self.email_address)
                # Вводим сгенерированный пароль в поле
                self.driver.find_element(By.ID, 'password').send_keys(self.password)
                # Вводим сгенерированный пароль для подтверждения
                self.driver.find_element(By.ID, 'password_confirm').send_keys(self.password)
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
                self.driver.find_element(By.ID, 'hint_answer').send_keys('Карлсон')
                time.sleep(2)
                self.driver.find_element(By.ID, 'hint_answer').click()
                # Вводим capture
                answer = input("Введите символы:  ")
                self.driver.find_element(By.ID, 'captcha').send_keys(answer)
                self.driver.implicitly_wait(1)  # We use wait to give the page enough time to load
                # Нажимаем кнопку зарегистрироваться
                self.driver.find_element(By.CSS_SELECTOR, '.Button2_view_action').click()
                # Нажимаем кнопку пропустить
                self.driver.implicitly_wait(3)  # We use wait to give the page enough time to load
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
        self.driver.quit()

class GMailReg(MailboxReg):

    def gmail_registation(self):
        """Данная функция оставлена для будущей возможности масштабирования класса с другими платформати """
        # Создаем переменную с адресом регистрации в почтовом сервисе
        mail_service_address = 'https://accounts.google.com/signup/v2'
        # Подключаемся к адрессу регистрации
        self.driver.get(mail_service_address)
        # Вводим имя
        self.driver.find_element(By.ID, 'firstName').send_keys(self.name)
        # Вводим фамилию
        self.driver.find_element(By.ID, 'lastName').send_keys(self.surname)
        # Вводим сгенерированный логин в поле
        self.driver.find_element(By.ID, 'username').send_keys(self.email_address)
        # Вводим сгенерированный пароль в поле
        self.driver.find_element(By.NAME, 'Passwd').send_keys(self.password)
        # Вводим сгенерированный пароль для подтверждения
        self.driver.find_element(By.NAME, 'ConfirmPasswd').send_keys(self.password)
        # Нажимаем кнопку "Далее"
        self.driver.find_element(By.ID, 'accountDetailsNext').click()
        # Gmail борется со спамом через номер телефона, поэтому вводим заготовленный номер
        self.driver.find_element(By.ID, 'phoneNumberId').send_keys(self.phone_num)
        # Нажимаем кнопку "Далее"
        self.driver.find_element(By.CSS_SELECTOR, '.VfPpkd-LgbsSe-OWXEXe-k8QpJ').click()
        # Оператору придется ввести код подтверждения
        while True:
            try:
                code = input("Введите код подтверждения: ")
                self.driver.find_element(By.ID, 'code').send_keys(code)
                break
            except:
                pass
        # Нажимаем кнопку "Далее"
        self.driver.find_element(By.CSS_SELECTOR, '.VfPpkd-LgbsSe-OWXEXe-k8QpJ > span:nth-child(4)').click()
        # Готовим данные о дате рождения для ввода в поля
        day, month, year = str(self.birthdate).split('.')
        # Вводим день рождения
        self.driver.find_element(By.ID, 'day').send_keys(day)
        # Выбираем в выпадающем списке месяц рождения
        select_m = Select(self.driver.find_element(By.ID, 'month'))
        select_m.select_by_value(month)
        # Вводим год рождения
        self.driver.find_element(By.ID, 'year').send_keys(year)
        # Выбираем в выпадающем списке пол неуказан, так как нам это не принципиально
        select_g = Select(self.driver.find_element(By.ID, 'gender'))
        select_g.select_by_value('Не указан')
        # Нажимаем кнопку "Далее"
        self.driver.find_element(By.CSS_SELECTOR, '.VfPpkd-LgbsSe-OWXEXe-k8QpJ > span:nth-child(4)').click()
        # Нажимаем кнопку "Пропустить"
        self.driver.find_element(By.CSS_SELECTOR, '.kDmnNe > div:nth-child(1) > button:nth-child(1) > span:nth-child(4)').click()
        # Нажимаем кнопку "Принимаю"
        self.driver.find_element(By.CSS_SELECTOR, '.VfPpkd-LgbsSe-OWXEXe-k8QpJ > div:nth-child(3)').click()
        print(f"Почта создана! Данные об аккаунте сохранены в файл {self.base_directory}/Data/Created_accounts.txt'")

class MailruReg(MailboxReg):

    def mailru_registation(self):
        """Данная функция оставлена для будущей возможности масштабирования класса с другими платформати """
        # Создаем переменную с адресом регистрации в почтовом сервисе
        mail_service_address = 'https://account.mail.ru/signup'
        # Подключаемся к адрессу регистрации
        self.driver.get(mail_service_address)
        time.sleep(1)
        # Вводим имя
        self.driver.find_element(By.ID, 'fname').send_keys(self.name)
        time.sleep(1)

        # Вводим фамилию
        self.driver.find_element(By.ID, 'lname').send_keys(self.surname)
        time.sleep(1)

        # Вводим сгенерированный логин в поле
        self.driver.find_element(By.ID, 'aaa__input').send_keys(self.email_address)
        time.sleep(1)

        # Вводим сгенерированный пароль в поле
        self.driver.find_element(By.ID, 'password').send_keys(self.password)
        time.sleep(1)

        # Вводим сгенерированный пароль для подтверждения
        self.driver.find_element(By.ID, 'repeatPassword').send_keys(self.password)
        time.sleep(1)

        # Ставим галочку выбора пола аккаунта
        if self.sex.islower() == "м":
            self.driver.find_element(By.CLASS_NAME,
                                     'radio-0-2-139').click()
        elif self.sex.islower() == "ж":
            self.driver.find_element(By.CSS_SELECTOR, 'label.label-0-2-138:nth-child(3) > div:nth-child(2) > span:nth-child(1)').click()
        time.sleep(1)

        #нажимаем поле "укажите резервный почтовый ящик" и вводим его
        self.driver.find_element(By.CSS_SELECTOR, 'span.styles__rightTopLink--3tzHt:nth-child(2) > a:nth-child(1)').click()
        time.sleep(1)

        """

        self.driver.find_element(By.ID, 'extra-email').send_keys('yaroslav.russu@mail.ru')
        # нажимаем "Создать"
        self.driver.find_element(By.CSS_SELECTOR,'button.base-0-2-6:nth-child(21) > span:nth-child(1)').click()

        
        # Нажимаем кнопку "Далее"
        self.driver.find_element(By.ID, 'accountDetailsNext').click()
        # Gmail борется со спамом через номер телефона, поэтому вводим заготовленный номер
        self.driver.find_element(By.ID, 'phoneNumberId').send_keys(self.phone_num)
        # Нажимаем кнопку "Далее"
        self.driver.find_element(By.CSS_SELECTOR, '.VfPpkd-LgbsSe-OWXEXe-k8QpJ').click()
        # Оператору придется ввести код подтверждения
        while True:
            try:
                code = input("Введите код подтверждения: ")
                self.driver.find_element(By.ID, 'code').send_keys(code)
                break
            except:
                pass
        # Нажимаем кнопку "Далее"
        self.driver.find_element(By.CSS_SELECTOR, '.VfPpkd-LgbsSe-OWXEXe-k8QpJ > span:nth-child(4)').click()
        # Готовим данные о дате рождения для ввода в поля
        day, month, year = str(self.birthdate).split('.')
        # Вводим день рождения
        self.driver.find_element(By.ID, 'day').send_keys(day)
        # Выбираем в выпадающем списке месяц рождения
        select_m = Select(self.driver.find_element(By.ID, 'month'))
        select_m.select_by_value(month)
        # Вводим год рождения
        self.driver.find_element(By.ID, 'year').send_keys(year)
        # Выбираем в выпадающем списке пол неуказан, так как нам это не принципиально
        select_g = Select(self.driver.find_element(By.ID, 'gender'))
        select_g.select_by_value('Не указан')
        # Нажимаем кнопку "Далее"
        self.driver.find_element(By.CSS_SELECTOR, '.VfPpkd-LgbsSe-OWXEXe-k8QpJ > span:nth-child(4)').click()
        # Нажимаем кнопку "Пропустить"
        self.driver.find_element(By.CSS_SELECTOR, '.kDmnNe > div:nth-child(1) > button:nth-child(1) > span:nth-child(4)').click()
        # Нажимаем кнопку "Принимаю"
        self.driver.find_element(By.CSS_SELECTOR, '.VfPpkd-LgbsSe-OWXEXe-k8QpJ > div:nth-child(3)').click()
        print(f"Почта создана! Данные об аккаунте сохранены в файл {self.base_directory}/Data/Created_accounts.txt'")

"""

if __name__ == '__main__':
    main = MailReg()
