from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(ChromeDriverManager().install())

data = "iphone SE2"
driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys(data,Keys.ENTER)
time.sleep(4)
driver.quit()

