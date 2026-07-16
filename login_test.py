from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import time

driver = webdriver.Chrome()

driver.get("http://da.adlynk.in:8000/login")

wait = WebDriverWait(driver, 10)

email = ''.join(random.choices(string.ascii_lowercase, k=8)) + "@gmail.com"
password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

wait.until(EC.presence_of_element_located((By.NAME, "email_address"))).send_keys(email)
driver.find_element(By.NAME, "password").send_keys(password)

time.sleep(5)

driver.quit()
