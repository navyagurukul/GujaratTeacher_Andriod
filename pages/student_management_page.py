from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (StaleElementReferenceException, TimeoutException)
from pages.base_page import BasePage
import time


class StudentManagementPage(BasePage):

    # ================= LOCATORS =================

    MANAGEMENT_TAB = (By.XPATH, "//span[normalize-space(text())='Management']/parent::a")
    MANAGEMENT_HEADER = (
        By.XPATH,
        "//*[@role='heading' and normalize-space()='Student Management']"
    )

    REGISTER_CARD = (
        By.XPATH,
        "//div[@tabindex='0'][.//div[normalize-space()='Student Registration']]"
    )

    APPROVAL_CARD = (
        By.XPATH,
        "//div[@tabindex='0'][.//div[normalize-space()='Student Approval']]"
    )

    EDIT_CARD = (
        By.XPATH,
        "//div[@tabindex='0'][.//div[normalize-space()='Edit Student']]"
    )

    DELETE_CARD = (
        By.XPATH,
        "//div[@tabindex='0'][.//div[normalize-space()='Delete Student']]"
    )

    STUDENT_NAME_INPUT = (By.XPATH, "//input[@placeholder='Student Name']")
    FATHER_NAME_INPUT = (By.XPATH, "//input[@placeholder=\"Father's Name\"]")
    MOBILE_INPUT = (By.XPATH, "//input[@placeholder='Mobile Number']")

    # 🔥 FIXED DROPDOWNS (no absolute xpath)
    GENDER_DROPDOWN = (By.XPATH, "//div[contains(text(),'Gender')]/following::div[@tabindex='0'][1]")
    GRADE_OPTIONS = (
        By.XPATH,
        "//div[@tabindex='0']//div[starts-with(normalize-space(),'Grade')]"
    )
    LANGUAGE_DROPDOWN = (
        By.XPATH, "//div[contains(text(),'Language')]/following::div[@tabindex='0'][1]"
    )

    SUBMIT_REVIEW_BTN = (By.XPATH, "//div[normalize-space(.)='Submit & Review']")
    
    CONFIRM_BTN = (
        By.XPATH,
        "//div[normalize-space()='Confirm']"
    )
    
    REGISTER_ALL_BTN = (
        By.XPATH,
        "//div[@tabindex='0'][.//div[normalize-space()='Register All Students']]"
    )
    
    BACK_BTN = (
        By.XPATH,
        "//div[contains(@class,'r-lrvibr') and .//img]"
    )
    
    REGISTER_STUDENT_BTN = (By.XPATH, "//button[contains(.,'Register Student') or contains(.,'Register')]")

    APPROVAL_LIST = (By.XPATH, "//div[contains(@class,'student')]")
    NO_PENDING_TEXT = (By.XPATH, "//*[contains(normalize-space(.), 'No pending students')]")

    # ================= COMMON METHODS =================
    def wait_for_management_screen(self):
        self.wait.until(EC.visibility_of_element_located(self.MANAGEMENT_HEADER))
    
    def open_management(self):
        print("Opening Management tab...")
        self.click(self.MANAGEMENT_TAB)
        self.wait_for_management_screen()
        print("✅ Management screen loaded")
        
    def safe_click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)  # 🔥 re-fetch (fix stale)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)
        
    def open_card(self, locator, name):
        print(f"Opening {name}...")
        self.wait_for_management_screen()

        cards = self.driver.find_elements(*locator)
        for card in cards:
            if card.is_displayed():
                self.driver.execute_script("arguments[0].click();", card)
                return

        raise Exception(f"❌ {name} card not found")
        
    def get_visible_back_button(self):
        buttons = self.driver.find_elements(*self.BACK_BTN)

        for btn in buttons:
            if btn.is_displayed():
                return btn

        raise Exception("❌ No visible back button found")

    def go_back_to_management(self):
        print("🔙 Clicking Back...")

        try:
            back_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.BACK_BTN)
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", back_btn
            )

            self.driver.execute_script("arguments[0].click();", back_btn)

            # ✅ STRICT VALIDATION
            self.wait.until(
                EC.visibility_of_element_located(self.MANAGEMENT_HEADER)
            )

            print("✅ Back to Management")

        except Exception as e:
            print(f"⚠️ Back failed → fallback: {str(e)[:80]}")

            # 🔥 FALLBACK (VERY IMPORTANT)
            self.open_management()
            
    def safe_back_to_management(self):
        print("🔙 Navigating back...")

        try:
            back_btn = WebDriverWait(self.driver, 8).until(
                EC.element_to_be_clickable(self.BACK_BTN)
            )

            self.driver.execute_script("arguments[0].click();", back_btn)

            self.wait_for_management_screen()
            print("✅ Back to Management")

        except Exception:
            print("⚠️ Back failed → fallback")
            self.open_management()
        
    #  UNIVERSAL DROPDOWN HANDLER
    def select_dropdown_option(self, dropdown_locator, option_text):
        print(f"Selecting {option_text}...")

        dropdown = self.wait.until(
            EC.presence_of_element_located(dropdown_locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", dropdown
        )

        self.driver.execute_script("arguments[0].click();", dropdown)

        option = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                f"//*[self::div or self::li or self::span][normalize-space()='{option_text}']")))
        
        self.driver.execute_script("arguments[0].click();", option)
        
    def select_any_option(self, dropdown_locator):
        print("Selecting available option...")
        dropdown = self.wait.until( EC.presence_of_element_located(dropdown_locator)
                                )
        self.driver.execute_script( "arguments[0].scrollIntoView({block:'center'});", dropdown )
        self.driver.execute_script("arguments[0].click();", dropdown) # 🔥 WAIT FOR OPTIONS (FIXED)
        options = self.wait.until( EC.presence_of_all_elements_located((
            By.XPATH, "//div[@tabindex='0']//div[starts-with(normalize-space(),'Grade')]" )))
        if not options:
            raise Exception("❌ No grade options found")
        
        option = options[1]
        print(f"Selected: {option.text}")
        self.driver.execute_script("arguments[0].click();", option)
        time.sleep(1)
        
    def click_submit_review(self):
        submit_btn = self.wait.until(
            EC.presence_of_element_located(self.SUBMIT_REVIEW_BTN)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", submit_btn)
        self.driver.execute_script("arguments[0].click();", submit_btn)
        
    def click_confirm(self):
        print("Clicking Confirm...")

        btn = self.wait.until(
            EC.element_to_be_clickable(self.CONFIRM_BTN)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", btn
        )

        # RN Web → always safer with JS click
        self.driver.execute_script("arguments[0].click();", btn)
        
    def click_register_all_students(self):
        print("Clicking Register All Students...")

        btn = self.wait.until(
            EC.element_to_be_clickable(self.REGISTER_ALL_BTN)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", btn
        )

        self.driver.execute_script("arguments[0].click();", btn)
        
    def debug_pause(self, seconds=2):
        if getattr(self, "DEBUG_MODE", True):
            time.sleep(seconds)
    # ================= MAIN FLOWS =================

    def register_student(self):
        self.click(self.REGISTER_CARD)

        self.send_keys(self.STUDENT_NAME_INPUT, "qa test")
        self.send_keys(self.FATHER_NAME_INPUT, "test")
        self.send_keys(self.MOBILE_INPUT, "9876543210")

        self.select_dropdown_option(self.GENDER_DROPDOWN, "Female")
        time.sleep(0.6)
        self.select_any_option(self.GRADE_OPTIONS)
        time.sleep(1.5)
        self.select_dropdown_option(self.LANGUAGE_DROPDOWN, "English")

        self.click(self.SUBMIT_REVIEW_BTN)
        self.click_confirm()
        self.click_register_all_students()

        print("Registered student successfully")
        # 🔥 SINGLE LINE instead of big block
        self.safe_back_to_management()

    def open_student_approval(self):
        self.safe_click(self.APPROVAL_CARD)
        print("Student Approval page opened")
        
        self.safe_back_to_management()

    def edit_student(self):
        self.safe_click(self.EDIT_CARD)
        print("Edit Student page opened")

        self.safe_back_to_management()
        
    def delete_student(self):
        self.safe_click(self.DELETE_CARD)
        print("Delete Student page opened")

        self.safe_back_to_management()