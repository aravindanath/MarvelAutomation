from day8 import LauchBrowserUsingWM as op
import time
from day10 import Generic as gs
from selenium.webdriver.common.keys import Keys

header ="TC001"
url =gs.readData(header,"url")


op.driver.get(url)

op.driver.find_element_by_css_selector("#src").send_keys(gs.readData(header,"src"))
time.sleep(2)
src = op.driver.find_elements_by_xpath("//ul[@class='autoFill']/li")
print("Total no of pickup points" ,len(src))

for x in src:
    # print(x.text)
    if x.text == gs.readData(header,"pickup"):
        x.click()
        break

op.driver.find_element_by_id("dest").send_keys(gs.readData(header,"dest"))
time.sleep(2)

src = op.driver.find_elements_by_xpath("//ul[@class='autoFill']/li")
print("Total no of Drop points" ,len(src))

for x in src:
    # print(x.text)
    if x.text == gs.readData(header,"droppoint"):
        x.click()
        break

op.driver.find_element_by_css_selector(".fl.icon-calendar_icon-new.icon-onward-calendar.icon").click()
time.sleep(2)

onWardCal = op.driver.find_elements_by_xpath("//div[@id='rb-calendar_onward_cal']/table/tbody/tr/td")

for x in onWardCal:
    if x.text == "May 2020":
        op.driver.find_element_by_xpath("(//button[text()='>'])[2]").click()
        break

time.sleep(2)
juneCal = op.driver.find_elements_by_xpath("//div[@id='rb-calendar_onward_cal']/table/tbody/tr/td")
for x in juneCal:
    if x.text == "9":
        x.click()
        break

time.sleep(2)
op.driver.find_element_by_css_selector(".fl.icon-calendar_icon-new.icon-return-calendar.icon").click()

juneCalReturn = op.driver.find_elements_by_xpath("//div[@id='rb-calendar_return_cal']/table/tbody/tr/td")
for x in juneCal:
    if x.text == "11":
        x.click()
        break

time.sleep(2)

op.driver.find_element_by_xpath("//button[text()='Search Buses']").click()

time.sleep(5)
op.driver.quit()


