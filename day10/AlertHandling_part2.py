from day8 import LauchBrowserUsingWM as op
import time
from day10 import Generic as gs

op.driver.get("http://the-internet.herokuapp.com/javascript_alerts")

op.driver.find_element_by_xpath("//button[text()='Click for JS Alert']").click()

gs.acceptAlert(op.driver)
time.sleep(4)
result = op.driver.find_element_by_css_selector("#result").text
print("Result: ",result)
time.sleep(4)
op.driver.find_element_by_xpath("//button[text()='Click for JS Confirm']").click()
time.sleep(4)
gs.dismissAlert(op.driver)
result = op.driver.find_element_by_css_selector("#result").text
print("Result: ",result)
time.sleep(4)
op.driver.find_element_by_xpath("//button[text()='Click for JS Prompt']").click()
time.sleep(4)
gs.sendValToAlert(op.driver,"Hello all")
result = op.driver.find_element_by_css_selector("#result").text
print("Result: ",result)
time.sleep(2)
op.driver.quit()


