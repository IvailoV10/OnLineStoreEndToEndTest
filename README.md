# OnLineStoreEndToEndTest
# Sauce Demo E2E Test Automation (Selenium + Pytest)

An end-to-end UI test automation framework built with **Python**, **Pytest**, and **Selenium WebDriver**, implementing the **Page Object Model (POM)** design pattern against [Sauce Demo](https://www.saucedemo.com/).

## Tech Stack
* **Language:** Python 3.10+
* **Browser Automation:** Selenium WebDriver
* **Test Runner:** Pytest
* **Design Pattern:** Page Object Model (POM)

## Project Structure
```text
saucedemo-selenium/
├── pages/                  # Page Object classes encapsulating locators and page actions
│   ├── base_page.py        # Shared WebDriver helpers and explicit wait wrappers
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/                  # Pytest test suites grouped by feature/flow
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_checkout.py
├── conftest.py             # Shared Pytest fixtures (WebDriver setup and teardown)
├── pytest.ini              # Pytest configuration and custom markers
├── requirements.txt        # Project dependencies
└── README.md
