from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#from selenium.webdriver.common.keys import Keys

class Automail:
    """Class Automail inits driver and functions login and mail """
    def __init__(self):
        self.driver = webdriver.Firefox('geckodriver.exe')

    def registry(self):
        """Зарегистрировать новую электронную почту в любом почтовом сервисе"""

    def login(self, email, password):
        """ Login function sigh in googlemail with email and password as arguments"""
        self.driver.get('https://accounts.google.com/signin/v2/identifier')
        self.driver.find_element(By.ID, "identifierId").send_keys(email)
        self.driver.find_element(By.ID, "identifierNext").click()
        time.sleep(3) #We use time sleep to give the page enoght time to load
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.ID, "passwordNext").click()

    def mail(self, email, theame, context):
        """Mail functions receives email, theames and context for sending """
        self.driver.get('https://mail.google.com')
        time.sleep(3) #We use time sleep to give the page enoght time to load
        self.driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]'
                                           '/div[1]/div/div/div/div[1]/div/div').click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '#\:fw').send_keys(email)# Вот здесь проблема!

if __name__ == '__main__':
    main = Automail()