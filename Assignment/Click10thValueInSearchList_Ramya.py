from day8 import LaunchBrowser as lp
import time
from selenium.webdriver.common.keys import Keys

lp.driver.get("https://www.amazon.in")

"""lp.driver.find_element_by_id("twotabsearchtextbox").send_keys("wrist watches for women", Keys.ENTER)
lp.driver.back()"""

lp.driver.find_element_by_id("twotabsearchtextbox").send_keys("wrist watches for women")
lp.driver.find_element_by_xpath("//input[@type='submit' and @value ='Go']").click()
time.sleep(3)
lp.driver.find_element_by_xpath("//div[@class='s-result-list s-search-results sg-row']/div[10]").click()
time.sleep(4)

