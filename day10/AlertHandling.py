from day8 import LauchBrowserUsingWM as op
import time

op.driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

op.driver.find_element_by_xpath("//input[@name='proceed']").click()
time.sleep(2)
al = op.driver.switch_to.alert
title = al.text
print("Alert title ",title)
al.accept()
time.sleep(4)
op.driver.find_element_by_css_selector("#login1").send_keys("arvind")

time.sleep(2)

op.driver.quit()


