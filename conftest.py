import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    # Optional stability fixes
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless=new")

    # ✅ Selenium Manager will auto-handle chromedriver
    driver = webdriver.Chrome(options=options)
    

    driver.implicitly_wait(5)

    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    login = LoginPage(driver)
    login.open()
    login.login("Sanskruthi School - Nalgonda", "8247282479")

    return driver


def take_screenshot(driver, name="error"):
    driver.save_screenshot(f"{name}.png")