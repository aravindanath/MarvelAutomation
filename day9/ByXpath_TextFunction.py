from day8 import LaunchBrowser as lp
import time
from selenium.webdriver.common.keys import Keys

lp.driver.get("https://www.amazon.in")


lp.driver.find_element_by_xpath("//span[text()='Hello. Sign in']").click()

time.sleep(4)
lp.driver.back()

time.sleep(4)
lp.driver.quit()