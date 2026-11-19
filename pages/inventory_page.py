from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:
    PAGE_TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    ADD_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=timeout)

    def is_loaded(self) -> bool:
        title = self.wait.until(EC.visibility_of_element_located(self.PAGE_TITLE))
        return title.text == "Products"

    def add_backpack_to_cart(self):
        button = self.wait.until(EC.element_to_be_clickable(self.ADD_BACKPACK_BUTTON))
        button.click()
        return self

    def remove_backpack_from_cart(self):
        button = self.wait.until(EC.element_to_be_clickable(self.REMOVE_BACKPACK_BUTTON))
        button.click()
        return self

    def get_cart_count(self) -> int:
        badge = self.wait.until(EC.visibility_of_element_located(self.CART_BADGE))
        return int(badge.text)

    def is_cart_badge_visible(self) -> bool:
        elements = self.driver.find_elements(*self.CART_BADGE)
        return len(elements) > 0 and elements[0].is_displayed()

    def open_cart(self):
        link = self.wait.until(EC.element_to_be_clickable(self.CART_LINK))
        link.click()