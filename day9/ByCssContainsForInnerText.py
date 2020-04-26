from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys

lp.driver.get("https://www.google.com/")

lp.driver.find_element_by_css_selector("input[class*='gs']").send_keys("ipad pro 2019",Keys.ENTER)
time.sleep(5)

lp.driver.quit()

# //button[text()='Sign Up' and starts-with(@id,'u_0')]//preceding::div[@class='_1lch']