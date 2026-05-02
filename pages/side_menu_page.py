from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SideMenuPage(BasePage):

    DASHBOARD = (By.XPATH, "//span[contains(text(),'Dashboard')]")
    PROFILE = (By.XPATH, "//span[contains(text(),'Profile')]")
    TEST = (By.XPATH, "//span[contains(text(),'Test')]")
    UNLOCK_TOPICS = (By.XPATH, "//span[contains(text(),'Unlock Topics')]")
    ZOOM_TRAINING = (By.XPATH, "//span[contains(text(),'Zoom Training')]")
    LOGOUT = (By.XPATH, "//span[contains(text(),'Logout')]")

    def open_dashboard(self):
        self.wait.until(lambda d: d.find_element(*self.DASHBOARD)).click()

    def open_profile(self):
        self.wait.until(lambda d: d.find_element(*self.PROFILE)).click()

    def open_test(self):
        self.wait.until(lambda d: d.find_element(*self.TEST)).click()

    def open_unlock_topics(self):
        self.wait.until(lambda d: d.find_element(*self.UNLOCK_TOPICS)).click()

    def open_zoom_training(self):
        self.wait.until(lambda d: d.find_element(*self.ZOOM_TRAINING)).click()

    def logout(self):
        self.wait.until(lambda d: d.find_element(*self.LOGOUT)).click()