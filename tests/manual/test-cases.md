# Manual Test Cases – e-Library

## TC-01 – Login with valid credentials

**Precondition:** A registered user exists.
**Steps:**

1. Open the login page.
2. Enter valid username and password.
3. Click Login.

**Expected result:** User is successfully logged in and redirected to the appropriate page.

---

## TC-02 – Login with invalid credentials

**Precondition:** Login page is open.
**Steps:**

1. Enter an invalid username or password.
2. Click Login.

**Expected result:** Login is rejected and an appropriate error message is displayed.

---

## TC-03 – User registration

**Precondition:** Registration page is open.
**Steps:**

1. Enter valid registration data.
2. Submit the registration form.

**Expected result:** A new user account is created successfully.

---

## TC-04 – Search for a book

**Precondition:** User is logged in.
**Steps:**

1. Open the book search/gallery.
2. Enter an existing book title or keyword.
3. Start the search.

**Expected result:** Matching books are displayed.

---

## TC-05 – View book details

**Precondition:** Books are displayed.
**Steps:**

1. Select a book.
2. Open its details.

**Expected result:** The book details are displayed correctly, including title, author and availability.

---

## TC-06 – Check book availability

**Precondition:** A book exists in the library.
**Steps:**

1. Open the book details.
2. Check the number of available copies.

**Expected result:** The displayed available quantity matches the actual availability.

---

## TC-07 – Rent a book

**Precondition:** User is logged in and the selected book is available.
**Steps:**

1. Select an available book.
2. Rent the book.

**Expected result:** The book is successfully rented and the available quantity is updated.

---

## TC-08 – Return a book

**Precondition:** User has rented a book.
**Steps:**

1. Open the rented books section.
2. Select the rented book.
3. Return the book.

**Expected result:** The book is returned successfully and the available quantity is updated.

---

## TC-09 – Admin adds a book

**Precondition:** Admin user is logged in.
**Steps:**

1. Open the admin book management.
2. Enter valid book data.
3. Add the book.

**Expected result:** The new book is created and appears in the library.

---

## TC-10 – Admin deletes a user

**Precondition:** Admin user is logged in and a test user exists.
**Steps:**

1. Open use
