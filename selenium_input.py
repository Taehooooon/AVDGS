import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



driver = webdriver.Chrome("./chromedriver")
driver.get("https://dgw.daebogroup.com")

login_id="lilliiliil"
login_pw='thth9880!'

pyperclip.copy(login_id)

driver.find_element_by_xpath('//*[@id="userId"]').send_keys(pyperclip.paste())


pyperclip.copy(login_pw)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(pyperclip.paste())

time.sleep(1)

driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
