from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage:
    PAGE_TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=timeout)

    def is_info_page_loaded(self) -> bool:
        return self.wait.until(
            EC.text_to_be_present_in_element(
                self.PAGE_TITLE, "Checkout: Your Information"
            )
        )

    def fill_customer_info(self, first_name: str, last_name: str, postal_code: str):
        first = self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_INPUT))
        first.clear()
        first.send_keys(first_name)

        last = self.wait.until(EC.visibility_of_element_located(self.LAST_NAME_INPUT))
        last.clear()
        last.send_keys(last_name)

        postal = self.wait.until(EC.visibility_of_element_located(self.POSTAL_CODE_INPUT))
        postal.clear()
        postal.send_keys(postal_code)

    def continue_to_overview(self):
        button = self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON))
        button.click()

    def finish_order(self):
        button = self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON))
        button.click()

    def get_complete_header(self) -> str:
        header = self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER))
        return header.text