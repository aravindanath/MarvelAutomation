from day8 import LaunchBrowser as lp
import time
from selenium.webdriver.common.keys import Keys

lp.driver.get("https://www.facebook.com")


radio =  lp.driver.find_elements_by_xpath("//input[@type='radio']")

print("Total count of radio",len(radio))

for r in radio:

    r.click()
    time.sleep(2)

if not radio[0].is_selected():
    radio[0].click()

# lp.driver.find_element_by_xpath("(//input[@type='radio'])[2]").click()


time.sleep(4)


lp.driver.quit()