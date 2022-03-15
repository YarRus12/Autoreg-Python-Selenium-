from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#from selenium.webdriver.common.keys import Keys


class Automail:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def login(self, email, password):
        self.driver.get('https://accounts.google.com/signin/v2/identifier')
        self.driver.find_element(By.ID, "identifierId").send_keys(email)
        self.driver.find_element(By.ID, "identifierNext").click()
        time.sleep(3)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.ID, "passwordNext").click()

    def mail(self, email, theme, context):
        self.driver.get('https://mail.google.com')
        time.sleep(3)
        self.driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div').click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '#\:fw').send_keys(email)


if __name__ == '__main__':
    main = Automail()
    main.login('sometestname12341234@gmail.com', 'sometest1234')
    main.mail('yaroslav.russu@mail.ru', 'test', 'Hi!')
