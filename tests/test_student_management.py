from pages.login_page import LoginPage
from pages.student_management_page import StudentManagementPage
import pytest

@pytest.mark.order(6)
def test_student_management(driver):

    login = LoginPage(driver)
    sm = StudentManagementPage(driver)

    login.open()
    login.login("Sanskruthi School - Nalgonda", "8247282479")

    sm.open_management()   # MUST ADD

    sm.register_student("QA Test Student")
    sm.check_approvals()
    sm.edit_student()
    sm.delete_student()

    driver.quit()