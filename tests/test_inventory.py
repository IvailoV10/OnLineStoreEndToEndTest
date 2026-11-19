from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_add_backpack_to_cart(driver):
    LoginPage(driver).open().login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded()

    inventory_page.add_backpack_to_cart()

    assert inventory_page.get_cart_count() == 1


def test_remove_backpack_from_cart(driver):
    LoginPage(driver).open().login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded()

    inventory_page.add_backpack_to_cart()
    inventory_page.remove_backpack_from_cart()

    assert not inventory_page.is_cart_badge_visible()