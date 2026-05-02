from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class StudentManagementPage(BasePage):

    MANAGEMENT_TAB = (By.XPATH, "//span[contains(text(),'Management')]")

    ADD_BTN = (By.XPATH, "//button[contains(.,'Add')]")
    NAME_INPUT = (By.XPATH, "//input[@placeholder='Student Name']")
    SAVE_BTN = (By.XPATH, "//button[contains(.,'Save')]")

    APPROVAL_TAB = (By.XPATH, "//span[contains(text(),'Approval')]")
    APPROVAL_LIST = (By.XPATH, "//div[contains(@class,'student')]")

    EDIT_BTN = (By.XPATH, "//button[contains(.,'Edit')]")
    DELETE_BTN = (By.XPATH, "//button[contains(.,'Delete')]")

    DROPDOWN = (By.XPATH, "//div[@tabindex='0']")
    OPTIONS = (By.XPATH, "//div[@role='dialog']//div")

    def open_management(self):
        self.click(self.MANAGEMENT_TAB)
        time.sleep(1)

    def register_student(self, name):
        self.click(self.ADD_BTN)
        self.send_keys(self.NAME_INPUT, name)
        self.click(self.SAVE_BTN)
        print(f"Registered: {name}")

    def check_approvals(self):
        self.click(self.APPROVAL_TAB)
        approvals = self.find_elements(self.APPROVAL_LIST)
        print(f"Approvals: {len(approvals)}")
        self.open_management()

    def edit_student(self):
        dropdowns = self.find_elements(self.DROPDOWN)
        self.driver.execute_script("arguments[0].click();", dropdowns[0])

        students = self.find_elements(self.OPTIONS)

        for s in students:
            name = s.text.lower()
            if "qa" in name or "test" in name:
                self.driver.execute_script("arguments[0].click();", s)
                self.click(self.EDIT_BTN)
                print(f"Edited: {name}")
                break

        self.open_management()

    def delete_student(self):
        dropdowns = self.find_elements(self.DROPDOWN)
        self.driver.execute_script("arguments[0].click();", dropdowns[0])

        students = self.find_elements(self.OPTIONS)

        for s in students:
            name = s.text.lower()
            if "qa" in name or "test" in name:
                self.driver.execute_script("arguments[0].click();", s)
                self.click(self.DELETE_BTN)
                print(f"Deleted: {name}")
                break

        self.open_management()