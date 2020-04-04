from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pyjavaproperties import Properties

prop = Properties()
# path for win c:\\Users\\Marvel\\testData\\config.properties
prop.load(open("../testData/config.properties"))

if prop.getProperty("browser") == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif prop.getProperty("browser") == 'firefox':
    driver = webdriver.Firefox(GeckoDriverManager().install())



driver.get(prop.getProperty("url"))





