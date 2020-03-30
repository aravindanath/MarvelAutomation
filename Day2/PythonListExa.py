from selenium.webdriver import Chrome

import time
path ="../driver/chromedriver"
driver = Chrome(executable_path=path)
driver.fullscreen_window()
driver.get("https://www.wikipedia.org/")


listOfLang = driver.find_elements_by_xpath("//select[@id='searchLanguage']/option")


print("Total no of lang: ",len(listOfLang))

empty=[]

for ref in listOfLang:
    # print(ref.text)
    empty.append(ref.text)

print("Before sort:",empty)
empty.sort()
print("After sort:", empty)

time.sleep(2)
driver.close()