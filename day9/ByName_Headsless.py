from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

ops = webdriver.ChromeOptions()
# ops.add_argument('--ignore-certificate-errors')
ops.add_argument("--disable-notifications")
ops.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(),options=ops)

data = "Selenium jobs in bangalore"
driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys(data,Keys.ENTER)
print("Page title ",driver.title)
time.sleep(4)

driver.quit()

