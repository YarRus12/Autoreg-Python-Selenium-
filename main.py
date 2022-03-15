from selenium import webdriver
import time
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys


class Automail:

    def __init__(self):
        self.driver = driver = webdriver.Firefox()

    def login(self, email, password):
        self.driver.get('https://accounts.google.com/signin/v2/identifier')
        self.driver.find_element_by_id("identifierId").send_keys(email)
        self.driver.find_element_by_id("identifierNext").click()
        time.sleep(3)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_id("passwordNext").click()

#    def mail(self):


if __name__ == '__main__':
    mail = Automail()
    mail.login('sometestname12341234@gmail.com', 'sometest1234')