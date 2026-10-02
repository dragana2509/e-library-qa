from selenium import webdriver
from selenium.webdriver.common.by import By
from test_config import USER_USERNAME, USER_PASSWORD
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost/libraryVUTP/")

    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "pass")
    login_button = driver.find_element(By.NAME, "submit_login")

    username.send_keys(USER_USERNAME)
    password.send_keys(USER_PASSWORD)
    login_button.click()

    time.sleep(2)

    assert "You are logged in as:" in driver.page_source
    print("PASS: Login successful.")

finally:
    driver.quit()