# tests/test_login.py
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver).open()
    login_page.login("standard_user", "secret_sauce")

    WebDriverWait(driver, timeout=10).until(EC.url_contains("/inventory.html"))
    assert "/inventory.html" in driver.current_url


def test_invalid_login_shows_error(driver):
    login_page = LoginPage(driver).open()
    login_page.login("standard_user", "wrong_password")

    error_text = login_page.get_error_message()
    assert "Username and password do not match" in error_text