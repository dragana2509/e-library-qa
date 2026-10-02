from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from test_config import USER_USERNAME, USER_PASSWORD
import time

driver = webdriver.Chrome()

try:
    # Open application
    driver.get("http://localhost/libraryVUTP/")

    # Login
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "pass")
    login_button = driver.find_element(By.NAME, "submit_login")

    username.send_keys(USER_USERNAME)
    password.send_keys(USER_PASSWORD)
    login_button.click()

    time.sleep(2)

    print("PASS: Login successful.")

    # Open book search
    driver.get(
        "http://localhost/libraryVUTP/home.php?action=search"
    )

    time.sleep(1)

    # Select "Select all"
    search_type = Select(
        driver.find_element(By.NAME, "column")
    )
    search_type.select_by_visible_text("Select all")

    # Click Search
    search_button = driver.find_element(
        By.NAME, "search_book"
    )

    driver.execute_script(
        "arguments[0].form.requestSubmit(arguments[0]);",
        search_button
    )

    time.sleep(2)

    # Verify search results
    assert "Anatomy" in driver.page_source

    print("PASS: Book search successful.")

finally:
    driver.quit()