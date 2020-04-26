from day8 import LaunchBrowser as lp
import time
from selenium.webdriver.common.keys import Keys

lp.driver.get("http://the-internet.herokuapp.com/tables")

name ="Tim"

web = lp.driver.find_element_by_xpath("//table[@id='table1']/tbody/tr/td[2][contains(text(),'NAME')]//following::td[3]".replace("NAME",name)).text

print(web)


table =lp.driver.find_element_by_xpath("//table[@id='table1']/tbody/tr/td[2][contains(text(),'NAME')]//preceding-sibling::td".replace("NAME",name)).text
print(table)


time.sleep(2)
lp.driver.quit()