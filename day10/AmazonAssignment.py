from day8 import LauchBrowserUsingWM as op
import time
from day10 import Generic as gs
from selenium.webdriver.common.keys import Keys

op.driver.get("https://www.amazon.in/")



op.driver.find_element_by_id("twotabsearchtextbox").send_keys("Apple iPhone XR (128GB)",Keys.ENTER)

time.sleep(3)
phones = op.driver.find_elements_by_xpath("//div[@class='a-section aok-relative s-image-fixed-height']/img")
print("Total no of mobiles:", len(phones))
phones[7].click()

win1 = op.driver.current_window_handle;
print("Parent windows id", win1)
print("Parent page Title", op.driver.title)
windows = op.driver.window_handles
for win in windows:
    print(win)
    op.driver.switch_to.window(win)


price = op.driver.find_element_by_xpath("(//span[contains(text(),'₹')])[1]")
print("Child page Title"+ op.driver.title)
print("Price of Xr is ", price.text)
time.sleep(3)
op.driver.close()
op.driver.switch_to.window(win1)
search = op.driver.find_element_by_id("twotabsearchtextbox")
search.clear()
search.send_keys("Moongdal",Keys.ENTER)
time.sleep(3)
op.driver.quit()


