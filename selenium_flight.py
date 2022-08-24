import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_elem(path_value):
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, path_value)))
    elem = browser.find_element(By.XPATH, path_value)
    elem.click()

browser = webdriver.Chrome("./chromedriver")

url = "http://flight.naver.com"
browser.get(url)


click_elem('//button[text() = "가는 날"]')

#begin_date = browser.find_element(By.XPATH, '//button[text() = "가는 날"]')
#begin_date.click()

time.sleep(1)
# WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//b[text() = "26"]')))    
from_day = browser.find_elements(By.XPATH, '//b[text() = "26"]')
from_day[1].click()

time.sleep(1)
to_day = browser.find_elements(By.XPATH, '//b[text() = "29"]')
to_day[1].click()



click_elem('//b[text() = "도착"]')
# click_elem('//button[contains(text(), "동남아")]')
click_elem('//button[text() = "동남아"]')
click_elem('//i[text() = "싱가포르"]')
# click_elem('//i[contains(text(), "싱가포르")]')
click_elem('//button[contains(text(), "직항만")]')

click_elem('//span[contains(text(), "항공권 검색")]')


elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[6]/div/div[3]/div[2]')))
print(elem.text)
