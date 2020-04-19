from day8 import LaunchBrowser as lp
import time
from selenium.webdriver.common.keys import Keys

data = "Bangalore during carona"
lp.driver.get("https://www.google.com")
lp.driver.find_element_by_partial_link_text("Ima").click()
time.sleep(4)
lp.driver.find_element_by_name('q').send_keys(data,Keys.ENTER)
time.sleep(4)
lp.driver.quit()

