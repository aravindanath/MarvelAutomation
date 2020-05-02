from selenium.webdriver import ActionChains


def acceptAlert(driver):
    al = driver.switch_to.alert
    print("Title:", al.text)
    al.accept()

def dismissAlert(driver):
    al = driver.switch_to.alert
    print("Title:", al.text)
    al.dismiss()

def sendValToAlert(driver,value):
    al = driver.switch_to.alert
    al.send_keys(value)
    acceptAlert(driver)

def mouseHover(driver,element):
    act = ActionChains(driver)
    act.move_to_element(element).perform()

def actionClick(driver,element):
    act = ActionChains(driver)
    act.click(element).perform()

def actionClickAndHold(driver,element):
    act = ActionChains(driver)
    act.click_and_hold(element).perform()

def rightClick(driver, element):
    act = ActionChains(driver)
    act.context_click(element).perform()

def dragAndDrop(driver, src, tgt):
    act = ActionChains(driver)
    act.drag_and_drop(src,tgt).perform()

def doubleClick(driver, element):
    act = ActionChains(driver)
    act.double_click(element).perform()