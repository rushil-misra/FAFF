from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://myaadhaar.uidai.gov.in/genricDownloadAadhaar/en")

time.sleep(5)


aadhar_number = driver.find_element(By.NAME,"uid")
aadhar_number.send_keys('681993142042')

First_name = 'rushil'
yob = '2004'
# while True:
#     time.sleep(2)

#     captcha = driver.find_element(By.NAME,"button_btn__HeAxz")
#     captcha.click()

#     try:
        
while True:
    try:
        captcha = driver.find_element(By.NAME,"captcha")
        captcha.click()
        break
    except:
        time.sleep(5)


while True:
    try:
        otp = driver.find_element(By.NAME,"button_btn__HeAxz")
        otp.click()
        break
    except:
        time.sleep(5)

password = First_name[:4] + yob

print("password is - ",password)


time.sleep(10)

driver.quit()