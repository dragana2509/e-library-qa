from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_config import ADMIN_USERNAME, ADMIN_PASSWORD
import os
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # LOGIN AS ADMIN
    driver.get("http://localhost/libraryVUTP/")

    driver.find_element(By.NAME, "username").send_keys(ADMIN_USERNAME)
    driver.find_element(By.NAME, "pass").send_keys(ADMIN_PASSWORD)
    driver.find_element(By.NAME, "submit_login").click()

    wait.until(EC.url_contains("admin.php"))

    print("PASS: Admin login successful.")

    # OPEN ADD BOOKS
    driver.get(
        "http://localhost/libraryVUTP/admin.php?action=add_books"
    )

    wait.until(
        EC.presence_of_element_located(
            (By.NAME, "title")
        )
    )

    # CREATE UNIQUE TEST DATA
    timestamp = str(int(time.time()))

    title = "QA Test Book " + timestamp
    isbn = "9" + timestamp[-9:]

    # TITLE
    driver.find_element(
        By.NAME, "title"
    ).send_keys(title)

    # AUTHOR
    driver.find_element(
        By.NAME, "author"
    ).send_keys("Test Author")

    # PUBLISHER
    publisher_select = Select(
        driver.find_element(
            By.NAME, "cbx_publisher"
        )
    )

    for option in publisher_select.options:
        if option.get_attribute("value") != "0":
            publisher_select.select_by_value(
                option.get_attribute("value")
            )
            break

    # PUBLISHED DATE
    driver.find_element(
        By.NAME, "published_on"
    ).send_keys("2026-10-01")

    # GENRE
    genre_select = Select(
        driver.find_element(
            By.NAME, "cbx_genre"
        )
    )

    for option in genre_select.options:
        if option.get_attribute("value") != "0":
            genre_select.select_by_value(
                option.get_attribute("value")
            )
            break

    # ISBN
    driver.find_element(
        By.NAME, "isbn"
    ).send_keys(isbn)

    # NUMBER OF PAGES
    driver.find_element(
        By.NAME, "number_of_pages"
    ).send_keys("100")

    # NUMBER OF COPIES
    driver.find_element(
        By.NAME, "number_of_copies"
    ).send_keys("3")

    # BOOK IMAGE
    image_path = r"C:\xampp\htdocs\libraryVUTP\test-book.jpg"

    assert os.path.exists(image_path), (
        "Book image not found: " + image_path
    )

    driver.find_element(
        By.NAME, "avatar"
    ).send_keys(image_path)

    # SUBMIT FORM WITH THE REAL SUBMIT BUTTON
    add_button = driver.find_element(
        By.CSS_SELECTOR,
        "input[name='submit_add'][value='Add book into library']"
    )

    driver.execute_script(
        "arguments[0].form.requestSubmit(arguments[0]);",
        add_button
    )

    # VERIFY SUCCESS MESSAGE
    wait.until(
        EC.text_to_be_present_in_element(
            (By.TAG_NAME, "body"),
            "Book successfully added into library!"
        )
    )

    print("PASS: Book added successfully.")
    print("PASS: Admin Add Book test successful.")

finally:
    driver.quit()