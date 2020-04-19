from day8 import LaunchBrowser as lp
import time
from selenium.webdriver.common.keys import Keys

lp.driver.get("https://www.google.com")

links = lp.driver.find_elements_by_tag_name("a")


print("Total count of the links",len(links))

for l in links:
    if l.text == "Stay home to thank those who are helping us":
        l.click()
        break


lp.driver.back()

time.sleep(4)
lp.driver.quit()