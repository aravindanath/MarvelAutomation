from day8 import LaunchBrowser as lp
import time
from selenium.webdriver.common.keys import Keys

lp.driver.get("https://www.google.com")

links = lp.driver.find_elements_by_tag_name("a")

print("Total count of the links",len(links))

for l in links:
    print(l.text," ----> ",l.get_attribute("href"))


time.sleep(3)
lp.driver.quit()