from browser import openChrome as lp
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

import time



lp.driver.get("https://www.expedia.co.in/")
lp.driver.find_element_by_xpath("//span[contains(text(),'Flights')]").click()
lp.driver.find_element_by_css_selector("label[id='flight-type-one-way-label-hp-flight']").click()
lp.driver.find_element_by_css_selector("input[id='flight-origin-hp-flight']").send_keys("Bengaluru, India (BLR-Kempegowda Intl.)",Keys.TAB)

lp.driver.find_element_by_css_selector("input[id='flight-destination-hp-flight']").send_keys("Boston, United States of America (BOS-All Airports)",Keys.TAB)

lp.driver.find_element_by_css_selector("input[id='flight-departing-single-hp-flight']").send_keys("20/10/2020",Keys.ENTER)



button = lp.driver.find_element_by_xpath("(//button[@type='button' and starts-with(@class,'btn-secondary btn-action t-select-btn')])[1]")

# driver, max time, polling,ignoreExceptions
wait = WebDriverWait(lp.driver,60,poll_frequency=2,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])

element = wait.until(EC.element_to_be_clickable((By.XPATH,"(//button[@type='button'])[34]")))
element.click()


thanks = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'No thanks')]")))
thanks.click()


time.sleep(3)
lp.driver.quit()