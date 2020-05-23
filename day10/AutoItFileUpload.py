from browserLaunch import launchChrome as lp
import subprocess
import time

lp.driver.get("http://www.tinyupload.com/")
element = lp.driver.find_element_by_xpath("//input[@name='uploaded_file']")
lp.driver.execute_script("arguments[0].click();",element)

#lp.driver.execute_script("C:\Users\91965\PycharmProjects\Target2020PyAuto\Target2020PyAuto\SeleniumBuiltins\fileupload.exe")
subprocess.Popen("C:\\Users\\91965\\PycharmProjects\\Target2020PyAuto\\Target2020PyAuto\\SeleniumBuiltins\\fileupload.exe")