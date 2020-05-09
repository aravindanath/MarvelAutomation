from day8 import LauchBrowserUsingWM as op
import time
from day10 import Generic as gs
from selenium.webdriver.common.keys import Keys


op.driver.get("http://the-internet.herokuapp.com/iframe")


op.driver.switch_to.frame("mce_0_ifr")
time.sleep(3)
textarea = op.driver.find_element_by_xpath("//*[@id='tinymce']")
textarea.clear()
textarea.send_keys("Happy learning python selenium")
time.sleep(3)
op.driver.quit()