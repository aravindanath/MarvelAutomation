from day8 import LaunchBrowser as lp
import time
from selenium.webdriver.common.keys import Keys

data = "Bangalore during carona"
lp.driver.get("https://www.google.com")
im = lp.driver.find_elements_by_partial_link_text("Imag")
print("COunt",len(im))
lp.driver.quit()

