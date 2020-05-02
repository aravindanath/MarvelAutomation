from day8 import LauchBrowserUsingWM as op
from selenium.webdriver.common.keys import Keys
import time
op.driver.get("https://www.google.com")

op.driver.find_element_by_name('q').send_keys("Selenium appium jobs in bangalore",Keys.ENTER)
time.sleep(5)
pgTitle = op.driver.title
print("Page title -->", pgTitle)

op.driver.back()
pgTitle = op.driver.title
print("Page title -->", pgTitle)
time.sleep(5)
op.driver.forward()

op.driver.quit()





