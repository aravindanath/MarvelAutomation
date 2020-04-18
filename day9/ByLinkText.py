from day8 import LaunchBrowser as lp
import time
from selenium.webdriver.common.keys import Keys

data = "iphone SE2"
lp.driver.get("https://www.google.com")
lp.driver.find_element_by_link_text("తెలుగు").click()

lp.driver.find_element_by_name('q').send_keys("news",Keys.ENTER)
time.sleep(4)
lp.driver.quit()

