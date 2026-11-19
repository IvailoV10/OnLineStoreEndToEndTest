# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=timeout)

    def open(self):
        self.driver.get(self.URL)
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_BUTTON))
        return self

    def enter_username(self, username: str):
        field = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        )
        field.clear()
        field.send_keys(username)
        return self

    def enter_password(self, password: str):
        field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        field.clear()
        field.send_keys(password)
        return self

    def submit(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        button.click()

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.submit()

    def is_login_button_visible(self) -> bool:
        button = self.wait.until(
            EC.visibility_of_element_located(self.LOGIN_BUTTON)
        )
        return button.is_displayed()

    def get_error_message(self) -> str:
        error = self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return error.text