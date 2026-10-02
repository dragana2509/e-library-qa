from pathlib import Path
import importlib.util

from playwright.sync_api import sync_playwright


# Load test_config.py from selenium folder
config_path = Path(__file__).resolve().parents[1] / "selenium" / "test_config.py"

spec = importlib.util.spec_from_file_location("test_config", config_path)
test_config = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_config)

USER_USERNAME = test_config.USER_USERNAME
USER_PASSWORD = test_config.USER_PASSWORD


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    try:
        # Open application
        page.goto("http://localhost/libraryVUTP/")

        # Login
        page.locator('input[name="username"]').fill(USER_USERNAME)
        page.locator('input[name="pass"]').fill(USER_PASSWORD)
        page.locator('input[name="submit_login"]').click()

        page.wait_for_load_state("networkidle")

        # Open book search
        page.goto("http://localhost/libraryVUTP/home.php?action=search")

        # Select "Select all"
        page.locator('select[name="column"]').select_option("select")

        # Enter search term
        page.locator('input[name="key_word"]').fill("Anatomy")

        # Click Search
        page.locator('input[name="search_book"]').click()

        page.wait_for_load_state("networkidle")

        # Verify search result
        assert "Anatomy" in page.content()

        print("PASS: Playwright book search successful.")

    finally:
        browser.close()