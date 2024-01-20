import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class User(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_click_button_on_index_page(self):
        driver = self.driver
        driver.get('http://127.0.0.1:5000/')
        index_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'index-button'))
        )
        index_button.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()