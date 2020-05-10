from selenium.webdriver.support.select import Select

from day8 import LauchBrowserUsingWM as op
import time
from day10 import Generic as gs
from selenium.webdriver.common.action_chains import ActionChains



op.driver.get("https://www.wikipedia.org/")


lang = op.driver.find_element_by_xpath("//select[@id='searchLanguage']")

sel = Select(lang)
sel.select_by_visible_text("हिन्दी")
time.sleep(4)
sel.select_by_index(45)
time.sleep(4)
sel.select_by_value("nan")

time.sleep(3)
op.driver.quit()


