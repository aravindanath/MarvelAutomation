
from browserLaunch import launchChrome as lp
import time
from selenium.webdriver.common.keys import Keys

lp.driver.get("https://app.hubspot.com/login?loginPortalId=&loginRedirectUrl=https%3A%2F%2Fapp.hubspot.com%2Fhome-beta")
time.sleep(10)
lp.driver.find_element_by_css_selector("input#username.form-control.private-form__control.login-email").send_keys("dummy@testmail.com",Keys.ENTER)
time.sleep(5)


lp.driver.get("https://www.google.com")

lp.driver.find_element_by_css_selector("input.gLFyf.gsfi").send_keys("Selenium jobs",Keys.ENTER)
time.sleep(5)

lp.driver.quit()

# //button[text()='Sign Up' and starts-with(@id,'u_0')]//preceding::div[@class='_1lch']