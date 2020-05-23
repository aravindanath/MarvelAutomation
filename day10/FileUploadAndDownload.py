from day8 import LauchBrowserUsingWM as op
import time
from day10 import Generic as gs

op.driver.get("http://the-internet.herokuapp.com/upload")

op.driver.find_element_by_id("file-upload").send_keys("/Users/aravindanathdm/PycharmProjects/MarvelAutomation/testData/data.ini")
time.sleep(4)
op.driver.find_element_by_id("file-submit").click()
time.sleep(4)
op.driver.get("http://the-internet.herokuapp.com/download")
time.sleep(4)
op.driver.find_element_by_link_text("data.ini").click()
time.sleep(4)
op.driver.quit()


