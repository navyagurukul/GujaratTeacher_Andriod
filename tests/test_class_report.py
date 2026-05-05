import pytest
from pages.login_page import LoginPage
from pages.class_report_page import ClassReportPage


@pytest.mark.order(4)
@pytest.mark.smoke
@pytest.mark.regression
def test_class_report(driver):

    login = LoginPage(driver)
    class_report = ClassReportPage(driver)

    login.open()

    assert login.login("24070609203-NAVA VATAVA PRI. SCH.", "8247208247")

    print("Login successful")

    class_report.run_full_class_report_flow()
    