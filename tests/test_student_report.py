from pages.login_page import LoginPage
from pages.student_report_page import StudentReportPage
import pytest

@pytest.mark.order(5)
def test_student_report(driver):
    login = LoginPage(driver)
    student_report = StudentReportPage(driver)

    login.open()
    login.login("Sanskruthi School - Nalgonda", "8247282479")

    student_report.open_student_report()
    student_report.select_grade_and_student()

    assert student_report.verify_sections()
    assert student_report.toggle_assessment()

    driver.quit()
    
    