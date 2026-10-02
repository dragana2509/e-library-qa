# e-Library – QA Portfolio Project

This is an older version of a PHP/MySQL library application that I originally developed myself and later revisited as a QA project.

I tested the existing functionality, identified and fixed several issues, and created automated Selenium and Playwright tests for important user and admin workflows.

The main focus was on practical QA work — creating test cases, reproducing and documenting bugs, verifying fixes and automating repeatable tests.

## QA Testing

The project includes:

* Manual test cases
* Bug reports
* Selenium automated tests
* Playwright automated tests
* End-to-end testing of user and admin workflows

## Manual Testing

10 manual test cases covering:

* User login
* Invalid login
* User registration
* Book search
* Book details
* Book availability
* Renting a book
* Returning a book
* Admin adding a book
* Admin deleting a user

See:

`tests/manual/test-cases.md`

## Bug Reports

Three bugs were identified, documented, fixed and retested:

* User deletion SQL error
* Incorrect available book count
* PHP 8.5 deprecation warning

See:

`tests/bug-reports/bug-reports.md`

## Automated Testing

The project includes automated UI tests using both Selenium and Playwright.

### Selenium

Selenium tests cover:

* Valid login
* Invalid login
* Book search
* Book rental and return
* Admin adding a book

Tests are located in:

`tests/selenium/`

### Playwright

Playwright tests cover:

* Valid login
* Book search

Tests are located in:

`tests/playwright/`

The automated tests were written in Python using Selenium WebDriver and Playwright.

## Technologies

* PHP
* MySQL
* HTML / CSS
* Python
* Selenium
* Playwright
* Git / GitHub
* XAMPP

## Project Purpose

This project demonstrates practical QA skills including:

* Test case design
* Bug reporting
* Bug reproduction
* Debugging
* Regression testing
* UI test automation
* End-to-end testing
* Git/GitHub workflow
