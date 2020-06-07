from browser import openChrome as lp
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select

import time



lp.driver.get("https://plugins.krajee.com/dependent-dropdown/demo#basic-usage")
time.sleep(4)
cat = lp.driver.find_element_by_css_selector("#cat-id")
sel = Select(cat)
sel.select_by_visible_text("Home & Kitchen")
time.sleep(5)
wait = WebDriverWait(lp.driver,20,poll_frequency=1,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
ele =wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#subcat-id.form-control")))
sel = Select(ele)
sel.select_by_index(2)

time.sleep(10)
lp.driver.quit()