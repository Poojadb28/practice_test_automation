import pytest
from pages.login_page import LoginPage
import time

@pytest.mark.smoke
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    time.sleep(2)
    login_page.login("student", "Password123")
    assert "Practice Test Automation" in driver.title
