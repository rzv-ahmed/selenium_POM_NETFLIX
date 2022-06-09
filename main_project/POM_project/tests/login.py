import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.ID , "txtUsername").send_keys("Admin")
time.sleep(2)
driver.find_element(By.ID , "txtPassword").send_keys("admin123")
time.sleep(2)
driver.find_element(By.ID , "btnLogin").click()
time.sleep(2)
driver.find_element(By.ID,"welcome").click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="welcome-menu"]/ul/li[3]/a').click()
time.sleep(2)

print ("u r success")
driver.close()
driver.quit()