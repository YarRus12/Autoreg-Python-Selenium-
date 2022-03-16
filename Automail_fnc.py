from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#from selenium.webdriver.common.keys import Keys

class Automail:
    """Class Automail inits driver and functions login and mail """
    def __init__(self):
        self.driver = webdriver.Firefox('geckodriver.exe')

    def registry(self, name, surname, birthdate, s):
        """Зарегистрировать новую электронную почту в любом почтовом сервисе"""
        #We choose gmail server
        mail_registration = 'https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=SignUp'
        # Вводим имя
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]"
                                           "/div/form/span/section/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div[1]/input").send_keys(name)
        # Вводим фамилию
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]"
                                           "/div/form/span/section/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/input").send_keys(surname)
        #вызываем функцию генерации адреса эл почты
        email_address = create_mail(name,surname,birthdate)
        #Вводим сгенерированный адрес эл. почты
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]"
                                           "/div/form/span/section/div/div/div[2]/div[1]/div/div[1]/div/div[1]/input").send_keys(email_address)
        #вызываем функцию генерации пароля
        password = create_password()
        #вводим сгенерированный пароль
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/"
                                           "div/form/span/section/div/div/div[3]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(password)
        # вводим сгенерированный пароль для подтверждения
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/"
                                           "div/form/span/section/div/div/div[3]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(password)
        #Нажимаем кнопку далее
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()
        time.sleep(3)  # We use time sleep to give the page enoght time to load
        birthdate = birthdate.split('.')
        #Вводим день рождения
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/"
                                           "div/form/span/section/div/div/div[3]/div[1]/div/div/div[1]/div/div[1]/input").send_keys(birthdate[0])
        # Вводим месяц рождения
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]"
                                           "/div/form/span/section/div/div/div[3]/div[2]/div/div/div[2]/select").send_keys(birthdate[1])
        # Вводим год рождения
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]"
                                           "/div/form/span/section/div/div/div[3]/div[2]/div/div/div[2]/select").send_keys(birthdate[1])
        # Выбираем пол
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]"
                                           "/div/form/span/section/div/div/div[4]/div[1]/div/div[2]/select").send_keys(s)
        # Нажимаем кнопку далее
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()
        time.sleep(3)  # We use time sleep to give the page enoght time to load
        # Принимаем условия конфиденциальности
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[3]").click()
        time.sleep(3)  # We use time sleep to give the page enoght time to load

    def login(self, email, password):
        """ Login function sigh in googlemail with email and password as arguments"""
        self.driver.get('https://accounts.google.com/signin/v2/identifier')
        self.driver.find_element(By.ID, "identifierId").send_keys(email)
        self.driver.find_element(By.ID, "identifierNext").click()
        time.sleep(3) #We use time sleep to give the page enoght time to load
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.ID, "passwordNext").click()

    def send_mail(self, email, theame, context):
        """Mail functions receives email, theames and context for sending """
        self.driver.get('https://mail.google.com')
        time.sleep(3) #We use time sleep to give the page enoght time to load
        self.driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]'
                                           '/div[1]/div/div/div/div[1]/div/div').click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '#\:fw').send_keys(email)# Вот здесь проблема!

if __name__ == '__main__':
    main = Automail()