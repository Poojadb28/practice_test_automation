from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.mark.smoke
def test_login_page_title():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()            
    assert "Practice Test Automation" in driver.title
    driver.quit()
