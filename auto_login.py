from selenium import webdriver
from getpass import getpass

#username/pw variables
username = 'username'
password = 'pw'

driver = webdriver.Chrome('C:\\Users\\dario\\Documents\\Projects\\chromedriver.exe')    # web driver path
driver.get('https://thetagang.com/login')   # site login page

username_textbox = driver.find_element_by_id('Username')
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id('Password')
password_textbox.send_keys(password)

login_button = driver.find_element_by_xpath('//button[text()="Sign In"]')
login_button.click()