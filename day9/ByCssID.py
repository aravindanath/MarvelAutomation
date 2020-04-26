from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys

lp.driver.get("https://www.amazon.com/")

"""
# hash represents the id in CSS
"""

lp.driver.find_element_by_css_selector("#twotabsearchtextbox").send_keys("ipad pro",Keys.ENTER)


time.sleep(5)

lp.driver.quit()

# //button[text()='Sign Up' and starts-with(@id,'u_0')]//preceding::div[@class='_1lch']