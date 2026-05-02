from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time
import random

class StudentReportPage(BasePage):

    STUDENT_REPORT_TAB = (By.XPATH, "//span[contains(text(),'Student Report')]")

    DROPDOWN = (By.XPATH, "//div[@tabindex='0']")
    OPTIONS = (By.XPATH, "//div[@role='dialog']//div[@tabindex='0']")

    STORIES = (By.XPATH, "//*[contains(text(),'Stories')]")
    WORDFUN = (By.XPATH, "//*[contains(text(),'Word')]")
    FUNLEARN = (By.XPATH, "//*[contains(text(),'Fun')]")

    ASSESSMENT = (By.XPATH, "//button[contains(.,'Assessment')]")

    def open_student_report(self):
        self.click(self.STUDENT_REPORT_TAB)
        time.sleep(1)

    def select_grade_and_student(self):
        dropdowns = self.find_elements(self.DROPDOWN)

        if len(dropdowns) < 2:
            raise Exception("Dropdowns not found properly")

        # Grade
        self.driver.execute_script("arguments[0].click();", dropdowns[0])
        options = self.find_elements(self.OPTIONS)
        self.driver.execute_script("arguments[0].click();", options[0])

        time.sleep(1)

        # Student
        self.driver.execute_script("arguments[0].click();", dropdowns[1])
        if students:= self.find_elements(self.OPTIONS):
            self.driver.execute_script("arguments[0].click();", random.choice(students))

        return True

    # ADD THIS
    def verify_sections(self):
        return (
            self.is_visible(self.STORIES) and
            self.is_visible(self.WORDFUN) and
            self.is_visible(self.FUNLEARN)
        )

    # ADD THIS
    def toggle_assessment(self):
        self.click(self.ASSESSMENT)
        return True