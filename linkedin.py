from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://www.linkedin.com")

username = driver.find_element_by_class_name('input__message hidden')
username.send_keys('josh.farmer.atx@gmail.com')

# password = driver.find_element_by_name('session_password')
# password.send_keys('Ghosts4513')

# log_in_button = driver.find_element_by_class_name('sign-in-form__submit-btn')
# log_in_button.click()

