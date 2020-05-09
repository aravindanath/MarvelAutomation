from day8 import LauchBrowserUsingWM as op
import time
from day10 import Generic as gs
from selenium.webdriver.common.keys import Keys
from datetime import datetime

op.driver.get("https://www.amazon.in/")

op.driver.find_element_by_id("twotabsearchtextbox").send_keys("Apple iPhone XR (128GB)",Keys.ENTER)


op.driver.save_screenshot("./demo.png")
time.sleep(3)


# dt = str(time.strftime("%x")).replace("/","_")
now = str(datetime.now()).replace("-","_").replace(" ","_").replace(":","_").split(".")[0]

file = "./demo"+now+".png"



print(file)
op.driver.get("https://www.myntra.com")
gs.takeScreenShot(op.driver,file)
op.driver.quit()


