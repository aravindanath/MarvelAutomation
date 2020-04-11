from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
from browser import openChrome as oc

def writeToIni(filePath,header,key,value):
    config = ConfigParser()
    config.add_section(header)
    config.set(header, key, value)
    with open(filePath, 'a') as dt:
        config.write(dt)

def readData(header,key):
    config = ConfigParser()
    config.read("../testdata/data.ini")
    val = config.get(header,key)
    return val



url = readData("Tc01",'url')
search = readData("Tc01",'search')
oc.driver.get(url)
oc.driver.find_element_by_name('q').send_keys(search,Keys.ENTER)





