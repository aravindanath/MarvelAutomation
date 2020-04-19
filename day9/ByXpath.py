from day8 import LaunchBrowser as lp
import time
from selenium.webdriver.common.keys import Keys

lp.driver.get("https://www.google.com")

lp.driver.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div/div/div/div[2]/input").send_keys("Selenium jobs",Keys.ENTER)

lp.driver.back();

"""
 Relative
 //TAGNAME[ @ Attribute = 'VALUE']"""

lp.driver.find_element_by_xpath("//input[@name='q']").send_keys("Appium jobs in bangalore",Keys.ENTER)

lp.driver.back()

time.sleep(4)
lp.driver.quit()