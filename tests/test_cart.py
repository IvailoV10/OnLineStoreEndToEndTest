from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_added_item_appears_in_cart(driver):
    LoginPage(driver).open().login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded()
    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page = CartPage(driver)
    assert cart_page.is_loaded()
    assert "Sauce Labs Backpack" in cart_page.get_item_names()


def test_remove_item_from_cart_page(driver):
    LoginPage(driver).open().login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded()
    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page = CartPage(driver)
    assert cart_page.is_loaded()
    cart_page.remove_backpack()

    assert "Sauce Labs Backpack" not in cart_page.get_item_names()