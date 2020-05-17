from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

browser ="chrome"
ops = ChromeOptions()
ops.add_argument("--disable-notifications")
global driver
if browser == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=ops)
elif browser == 'firefox':
    driver = webdriver.Firefox(GeckoDriverManager().install())

# driver.get("https://www.google.com")