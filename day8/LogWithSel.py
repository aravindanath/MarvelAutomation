# print("Hello is a report")

# https://docs.python.org/3/library/logging.html
import logging
from browser import openChrome as oc
from selenium.webdriver.common.keys import Keys
import time

def log():
    logger = logging.getLogger("Demo log")
    fileHandler = logging.FileHandler("logFile.log")
    logger.addHandler(fileHandler)
    formater = logging.Formatter("%(asctime)s :%(levelname)s: %(name)s :%(message)s")
    fileHandler.setFormatter(formater)
    logger.setLevel(logging.DEBUG)
    return logger

l = log()

oc.driver.get("https://www.amazon.com")
l.info("User is on "+ oc.driver.current_url)
l.info("User is on "+ oc.driver.title)
try:
    oc.driver.find_element_by_name("q").send_keys("Covid 19 in india",Keys.ENTER)
    l.info("User is on "+ oc.driver.current_url)
    l.info("User is on "+ oc.driver.title)
except:
    l.error("Element not found")

finally:
    oc.driver.quit()








