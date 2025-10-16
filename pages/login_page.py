from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.submit_button = (By.ID, "submit")
        self.error_message = (By.ID, "error")

    def open(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.submit_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text
