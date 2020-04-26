from day8 import LaunchBrowser as lp
import time
from selenium.webdriver.common.keys import Keys

lp.driver.get("https://www.amazon.in")


lp.driver.find_element_by_xpath("//span[contains(text(),'Hello')]").click()

time.sleep(4)
lp.driver.back()
try:
    lp.driver.find_element_by_xpath("//a[contains(text(),'Customer Service') and @tabindex=30]").click()
except:
    # raise
    print("Element not found")

lp.driver.get("https://www.amazon.com")
lp.driver.find_element_by_xpath("//span[contains(text(),'Hello')]").click()
time.sleep(4)
lp.driver.back()
time.sleep(4)
try:
    lp.driver.find_element_by_xpath("//a[contains(text(),'Customer Service') and @tabindex=30 or @tabindex=48]").click()
except:
    # raise
    print("Element not found")

lp.driver.quit()