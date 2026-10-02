from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_config import USER_USERNAME, USER_PASSWORD

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # LOGIN
    driver.get("http://localhost/libraryVUTP/")

    driver.find_element(By.NAME, "username").send_keys(USER_USERNAME)
    driver.find_element(By.NAME, "pass").send_keys(USER_PASSWORD)
    driver.find_element(By.NAME, "submit_login").click()

    wait.until(EC.url_contains("home.php"))

    # CHECK INITIAL AVAILABILITY
    driver.get(
        "http://localhost/libraryVUTP/home.php?action=gallery_selection"
    )

    anatomy_row = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[@href='rent-input.php?bookId=1']/ancestor::tr")
        )
    )

    cells = anatomy_row.find_elements(By.TAG_NAME, "td")
    available_before = int(cells[8].text.strip())

    print("Available before renting:", available_before)

    # OPEN RENT PAGE
    driver.get(
        "http://localhost/libraryVUTP/home.php?action=rent"
    )

    # SELECT ANATOMY
    book_select = Select(
        wait.until(
            EC.presence_of_element_located(
                (By.ID, "cbx_books")
            )
        )
    )

    book_select.select_by_value("1")

    # ENTER QUANTITY
    number_books = wait.until(
        EC.presence_of_element_located(
            (By.NAME, "number_books")
        )
    )

    driver.execute_script(
        "arguments[0].value = '1';",
        number_books
    )

    print("Quantity entered:", number_books.get_attribute("value"))

    assert number_books.get_attribute("value") == "1"

    # SUBMIT FORM WITH THE SUBMIT BUTTON INCLUDED
    rent_button = driver.find_element(
        By.CSS_SELECTOR,
        "input[name='submit'][value='Rent a book']"
    )

    driver.execute_script(
        "arguments[0].form.requestSubmit(arguments[0]);",
        rent_button
    )

    # CHECK AVAILABILITY AFTER RENT
    driver.get(
        "http://localhost/libraryVUTP/home.php?action=gallery_selection"
    )

    anatomy_row = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[@href='rent-input.php?bookId=1']/ancestor::tr")
        )
    )

    cells = anatomy_row.find_elements(By.TAG_NAME, "td")
    available_after_rent = int(cells[8].text.strip())

    assert available_after_rent == available_before - 1

    print("PASS: Book rented successfully.")
    print("PASS: Available copies decreased correctly.")

    # CHECK MY PROFILE
    driver.get(
        "http://localhost/libraryVUTP/home.php?action=user_profile"
    )

    wait.until(
        EC.text_to_be_present_in_element(
            (By.TAG_NAME, "body"),
            "Anatomy"
        )
    )

    print("PASS: Anatomy appears in My Profile.")

    # OPEN RETURN PAGE
    driver.get(
        "http://localhost/libraryVUTP/home.php?action=return"
    )

    # SELECT ANATOMY
    return_select = Select(
        wait.until(
            EC.presence_of_element_located(
                (By.ID, "cbx_books")
            )
        )
    )

    return_select.select_by_value("1")

    # ENTER RETURN QUANTITY
    number_books = wait.until(
        EC.presence_of_element_located(
            (By.NAME, "number_books")
        )
    )

    driver.execute_script(
        "arguments[0].value = '1';",
        number_books
    )

    print(
        "Return quantity entered:",
        number_books.get_attribute("value")
    )

    assert number_books.get_attribute("value") == "1"

    # SUBMIT RETURN FORM WITH SUBMIT BUTTON INCLUDED
    return_button = driver.find_element(
        By.CSS_SELECTOR,
        "input[name='submit'][value='Return books']"
    )

    driver.execute_script(
        "arguments[0].form.requestSubmit(arguments[0]);",
        return_button
    )

    # CHECK FINAL AVAILABILITY
    driver.get(
        "http://localhost/libraryVUTP/home.php?action=gallery_selection"
    )

    anatomy_row = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[@href='rent-input.php?bookId=1']/ancestor::tr")
        )
    )

    cells = anatomy_row.find_elements(By.TAG_NAME, "td")
    available_after_return = int(cells[8].text.strip())

    assert available_after_return == available_before

    print("PASS: Book returned successfully.")
    print("PASS: Available copies restored correctly.")
    print("PASS: Complete rent and return test successful.")

finally:
    driver.quit()