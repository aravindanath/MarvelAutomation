from day8 import LauchBrowserUsingWM as op
import time
from day10 import Generic as gs
from selenium.webdriver.common.keys import Keys
from datetime import datetime

op.driver.get("https://www.amazon.in/")

time.sleep(3)
backtoTop = op.driver.find_element_by_xpath("//span[text()='Back to top']")

op.driver.execute_script("arguments[0].scrollIntoView();",backtoTop)
time.sleep(3)
backtoTop = op.driver.find_element_by_xpath("//span[text()='Back to top']")
time.sleep(3)
gs.highlightElement(op.driver,backtoTop,"yellow")
backtoTop.click()

time.sleep(3)
op.driver.find_element_by_id("twotabsearchtextbox").send_keys("mens wrist watch",Keys.ENTER)



time.sleep(3)
op.driver.quit()


