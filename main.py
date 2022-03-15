from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys


name='sometestname12341234@gmail.com'
password='sometest1234'

driver = webdriver.Firefox()
driver.get('https://accounts.google.com/signin/v2/identifier')
driver.find_element_by_id("identifierId").send_keys(name)
driver.find_element_by_id("identifierNext").click()
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("passwordNext").click()


#driver.get("https://github.com/login")
#driver.find_element_by_id("login_field").send_keys(name)
#driver.find_element_by_id("password").send_keys(password)