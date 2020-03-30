from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time


path ="../driver/chromedriver"
driver = Chrome(executable_path=path)

driver.get("https://www.hdfcbank.com/")

try:
    driver.find_element_by_xpath("//a[@id='popupBoxClose']").click()

    driver.find_element_by_xpath("(//button[@type='button' and text()='Login'])[2]").click()
except:
    print("popup did  not appear")

finally:
    driver.quit()

