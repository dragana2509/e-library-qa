# Bug Reports – e-Library

## BUG-01 – User deletion fails with SQL error

**Severity:** High
**Priority:** High
**Status:** Fixed

**Description:**
Deleting a user from the admin panel caused a database error.

**Steps to reproduce:**

1. Log in as administrator.
2. Open user management.
3. Select an existing user.
4. Click delete.

**Expected result:**
The selected user is deleted successfully.

**Actual result:**
The application displayed the error:
`SQLSTATE[HY093]: Invalid parameter number`

**Root cause:**
The SQL query used an incorrect parameter binding.

**Fix:**
The query was changed to use a named parameter correctly with PDO.

**Retest:**
User deletion was tested again after the fix and worked successfully.

---

## BUG-02 – Incorrect available book count

**Severity:** Medium
**Priority:** High
**Status:** Fixed

**Description:**
The book gallery displayed the total number of copies instead of the currently available copies.

**Steps to reproduce:**

1. Log in as a user.
2. Open the book gallery.
3. Find a book with rented copies.
4. Check the displayed availability.

**Expected result:**
The number of currently available copies should be displayed.

**Actual result:**
The total number of copies was displayed instead.

**Root cause:**
The gallery displayed `Number_of_copies` instead of `Avaliable_books`.

**Fix:**
The displayed value was changed to `Avaliable_books`.

**Retest:**
The availability was checked again after the fix and the displayed number was correct.

---

## BUG-03 – PHP 8.5 deprecation warning during registration

**Severity:** Low
**Priority:** Medium
**Status:** Fixed

**Description:**
User registration generated a PHP deprecation warning when running the application with PHP 8.5.

**Steps to reproduce:**

1. Open the registration page.
2. Enter valid registration data.
3. Submit the form.
4. Check the PHP output/log.

**Expected result:**
Registration should work without PHP deprecation warnings.

**Actual result:**
A deprecation warning related to `FILTER_SANITIZE_STRING` was displayed.

**Root cause:**
`FILTER_SANITIZE_STRING` is deprecated in newer PHP versions.

**Fix:**
The deprecated filter was removed from the affected input fields.

**Retest:**
Registration was tested again with PHP 8.5
