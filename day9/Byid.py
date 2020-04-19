from day8 import LaunchBrowser as lp
import time
from selenium.webdriver.common.keys import Keys

lp.driver.get("https://www.amazon.com")

time.sleep(3)
lp.driver.find_element_by_id("twotabsearchtextbox").send_keys("ipad pro 2020",Keys.ENTER)
time.sleep(3)

lp.driver.close()