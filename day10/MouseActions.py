from day8 import LauchBrowserUsingWM as op
import time
from day10 import Generic as gs
from selenium.webdriver.common.action_chains import ActionChains


op.driver.get("https://www.myntra.com/")


women = op.driver.find_element_by_xpath("(//a[text()='Women'])[1]")

act = ActionChains(op.driver)
act.move_to_element(women).perform()

time.sleep(3)
shrug = op.driver.find_element_by_xpath("(//a[text()='Shrugs'])[1]")
act.click(shrug).perform()
time.sleep(3)
op.driver.quit()


