import pytest
from pages.login_page import LoginPage

@pytest.mark.order(1)
@pytest.mark.smoke
@pytest.mark.regression
def test_login(driver):
    login = LoginPage(driver)
    login.open()
    assert login.login("24070609203-NAVA VATAVA PRI. SCH.", "8247208247")