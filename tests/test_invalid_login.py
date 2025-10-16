import pytest
from pages.login_page import LoginPage
import time

@pytest.mark.smoke
def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    time.sleep(2)
    login_page.login("admin", "Password123")
    time.sleep(1)
    assert login_page.get_error_message() == "Your username is invalid!"
