from day8 import LauchBrowserUsingWM as op
import time
from day10 import Generic as gs
from selenium.webdriver.common.action_chains import ActionChains


op.driver.get("https://www.myntra.com/")


women = op.driver.find_element_by_xpath("(//a[text()='Women'])[1]")

gs.mouseHover(op.driver,women)
time.sleep(3)
shrug = op.driver.find_element_by_xpath("(//a[text()='Shrugs'])[1]")
gs.actionClick(op.driver,shrug)
time.sleep(3)

op.driver.get("http://demo.guru99.com/test/drag_drop.html")

src = op.driver.find_element_by_xpath("(//*[@id='fourth']/a)[1]")
tgt = op.driver.find_element_by_xpath("//*[@id='amt7']/li")

gs.dragAndDrop(op.driver,src,tgt)
time.sleep(3)
op.driver.quit()


