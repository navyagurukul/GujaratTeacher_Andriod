import pytest
from pages.side_menu_page import SideMenuPage
from pages.login_page import LoginPage
from pages.class_report_page import ClassReportPage


@pytest.fixture
def setup(driver):
    login = LoginPage(driver)
    page = ClassReportPage(driver)

    login.open()
    login.login("Sanskruthi School - Nalgonda", "8247282479")
    page.open_class_report()

    return page
def side_menu(driver):
    
    return SideMenuPage(driver)


def test_dashboard(side_menu):
    side_menu.open_dashboard()
    print("Dashboard opened")


def test_profile(side_menu):
    side_menu.open_profile()
    print("Profile opened")


def test_test_page(side_menu):
    side_menu.open_test()
    print("Test opened")


def test_unlock_topics(side_menu):
    side_menu.open_unlock_topics()
    print("Unlock Topics opened")


def test_zoom_training(side_menu):
    side_menu.open_zoom_training()
    print("Zoom Training opened")


def test_logout(side_menu):
    side_menu.logout()
    print("Logout clicked")