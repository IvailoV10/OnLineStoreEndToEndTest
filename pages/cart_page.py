from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    PAGE_TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    ITEM_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=timeout)

    def is_loaded(self) -> bool:
        return self.wait.until(
            EC.text_to_be_present_in_element(self.PAGE_TITLE, "Your Cart")
        )

    def get_item_names(self) -> list[str]:
        items = self.driver.find_elements(*self.ITEM_NAMES)
        return [item.text for item in items if item.is_displayed()]

    def remove_backpack(self):
        button = self.wait.until(EC.element_to_be_clickable(self.REMOVE_BACKPACK_BUTTON))
        button.click()

    def proceed_to_checkout(self):
        button = self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON))
        button.click()