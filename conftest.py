# conftest.py
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # Setup: runs before the test function
    browser = webdriver.Chrome()
    browser.maximize_window()

    # Hand the browser instance to the test
    yield browser

    # Teardown: runs after the test finishes, even if the test fails
    browser.quit()