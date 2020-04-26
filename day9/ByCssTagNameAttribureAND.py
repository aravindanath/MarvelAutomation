
from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys

lp.driver.get("https://www.google.com/")

lp.driver.find_element_by_css_selector("input[name='q'][type='text']").send_keys("ipad pro",Keys.ENTER)
lp.driver.quit()