from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost/libraryVUTP/")

    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "pass")
    login_button = driver.find_element(By.NAME, "submit_login")

    username.send_keys("wrong_user")
    password.send_keys("wrong_password")
    login_button.click()

    time.sleep(2)

    assert "You are logged in as:" not in driver.page_source
    print("PASS: Invalid login rejected.")

finally:
    driver.quit()