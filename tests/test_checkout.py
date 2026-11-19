import time

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_complete_checkout_with_single_item(driver):
    LoginPage(driver).open().login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded()
    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page = CartPage(driver)
    assert cart_page.is_loaded()
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(driver)
    assert checkout_page.is_info_page_loaded()
    checkout_page.fill_customer_info("Ivo", "Tester", "1000")
    checkout_page.continue_to_overview()
    checkout_page.finish_order()

    assert checkout_page.get_complete_header() == "Thank you for your order!"
    time.sleep(30)