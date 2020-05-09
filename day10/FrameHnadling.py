from day8 import LauchBrowserUsingWM as op
import time
from day10 import Generic as gs
from selenium.webdriver.common.keys import Keys


op.driver.get("https://www.selenium.dev/selenium/docs/api/java/")


op.driver.switch_to.frame("packageListFrame")

op.driver.find_element_by_link_text("com.thoughtworks.selenium").click()

op.driver.switch_to.default_content()

op.driver.switch_to.frame("packageFrame")

op.driver.find_element_by_link_text("Wait").click()

op.driver.switch_to.default_content()
op.driver.switch_to.frame("classFrame")

op.driver.find_element_by_link_text("Wait.WaitTimedOutException").click()

time.sleep(3)
op.driver.quit()