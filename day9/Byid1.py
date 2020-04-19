from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(ChromeDriverManager().install())

data = "iphone xr"
driver.get("https://www.amazon.com")
driver.find_element_by_id("twotabsearchtextbox").send_keys(data,Keys.ENTER)
time.sleep(4)
driver.quit()

