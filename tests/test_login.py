# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pytest
# import time

# @pytest.mark.smoke
# def test_login_page_title():
#     driver = webdriver.Chrome()
#     driver.get("https://practicetestautomation.com/practice-test-login/")
#     time.sleep(2)

#     driver.find_element(By.ID, "username").send_keys("student")
#     driver.find_element(By.ID, "password").send_keys("Password123")
#     driver.find_element(By.ID, "submit").click()            
#     assert "Practice Test Automation" in driver.title
#     driver.quit()

import tempfile
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

@pytest.fixture
def driver():
    # Create a unique temporary directory for Chrome user data
    user_data_dir = tempfile.mkdtemp(prefix="chrome-user-data-")

    options = Options()
    # Run in headless mode for GitHub Actions; comment this line if debugging locally
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument(f"--user-data-dir={user_data_dir}")
    options.add_argument("--remote-allow-origins=*")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver

    # Cleanup
    try:
        driver.quit()
    except:
        pass
    shutil.rmtree(user_data_dir, ignore_errors=True)

@pytest.mark.smoke
def test_login_page_title(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    time.sleep(1)
    assert "Practice Test Automation" in driver.title

