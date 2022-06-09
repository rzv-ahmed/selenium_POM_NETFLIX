import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test_loginValue(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        time.sleep(2)
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        time.sleep(2)
        self.driver.find_element(By.ID, "btnLogin").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "welcome").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="welcome-menu"]/ul/li[3]/a').click()
        time.sleep(2)
    @classmethod
    def tearDownClass(cls) :
        cls.driver.close()
        cls.driver.quit()
        print("u r success")

        #self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
