

data ={"url":"https://www.google.com","browser":"chrome","search":"Selenium jobs"}

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

if data["browser"]=="chrome":
    path ="../driver/chromedriver"
    driver = Chrome(executable_path=path)

driver.fullscreen_window()
driver.get(data["url"])
driver.find_element_by_name("q").send_keys(data["search"],Keys.ENTER)


