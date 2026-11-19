# tests/test_smoke.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_login_page_loads(driver):
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, timeout=10)

    # Wait until the page title is exact, then assert
    wait.until(EC.title_is("Swag Labs"))
    assert driver.title == "Swag Labs"

    # Wait until the login button is in the DOM and visible
    login_button = wait.until(
        EC.visibility_of_element_located((By.ID, "login-button"))
    )
    assert login_button.is_displayed()