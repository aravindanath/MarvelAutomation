from day8 import LaunchBrowser as lp
import time
from selenium.webdriver.common.keys import Keys

lp.driver.get("https://www.google.in")


lp.driver.find_element_by_xpath("//input[starts-with(@class,'gLF')]").send_keys("Appium jobs in bangalore",Keys.ENTER)

time.sleep(4)


lp.driver.quit()