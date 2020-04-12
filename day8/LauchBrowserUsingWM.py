from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

browser ="chrome"
global driver
if browser == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browser == 'firefox':
    driver = webdriver.Firefox(GeckoDriverManager().install())

driver.get("https://www.google.com")