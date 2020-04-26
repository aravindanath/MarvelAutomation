from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys

lp.driver.get("https://www.amazon.com/")

lp.driver.find_element_by_css_selector("input[id='twotabsearchtextbox'][type='text']").send_keys("iphone 11 pro",Keys.ENTER)
time.sleep(3)
lp.driver.quit()