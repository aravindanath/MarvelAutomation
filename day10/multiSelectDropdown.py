from selenium.webdriver.support.select import Select

from day8 import LauchBrowserUsingWM as op
import time
from day10 import Generic as gs
from selenium.webdriver.common.action_chains import ActionChains



op.driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")


city = op.driver.find_element_by_xpath("//select[@id='multi-select']")

# sel = Select(city)
# sel.select_by_visible_text("California")
# time.sleep(4)
# sel.select_by_index(3)
# time.sleep(4)
# sel.select_by_value("Texas")

for i in range(8):
    gs.selectDropdownByindex(city,i)
time.sleep(3)
gs.deSelectDropdownByindex(city,3)
time.sleep(3)
gs.deSelectDropdownByVal(city,"California")
time.sleep(3)
gs.deSelectAllValues(city)
time.sleep(3)
op.driver.quit()


