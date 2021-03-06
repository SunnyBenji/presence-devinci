import os

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

emailFile= open("email_env.txt", 'r')
email = emailFile.read()

passwordFile= open("password_env.txt", 'r')
password = passwordFile.read()

os.environ['email'] = email
os.environ['password'] = password
#lancement
driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
driver.maximize_window()
driver.get('https://www.leonard-de-vinci.net/');

#connexion
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login"]'))).send_keys(os.environ['email'])
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btn_next"]'))).click()
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordInput"]'))).send_keys(os.environ['password'])
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submitButton"]'))).click()


# présence à partir du menu principale
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div[2]/div/ul/div/a'))).click()

for x in range(1, 5):
    boutton_xpath = '//*[@id="body_presences"]/tr['
    boutton_xpath += str(x)
    boutton_xpath += ']/td[4]/a/span'

    if driver.find_element(By.XPATH, boutton_xpath) :
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, boutton_xpath))).click()
        if driver.find_elements(By.ID, "set-presence") :
            WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'set-presence'))).click()
        driver.back()

    else :
        break
driver.quit





