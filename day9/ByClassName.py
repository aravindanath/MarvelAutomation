from selenium.webdriver import ChromeOptions,Chrome

from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

ops = ChromeOptions()
# ops.add_argument('--ignore-certificate-errors')
ops.add_argument("--disable-notifications")
driver = Chrome(executable_path=ChromeDriverManager().install(),options=ops)

driver.get("https://www.icicibank.com/")
driver.find_element_by_class_name("pl-login-ornage-box").click()
time.sleep(4)
driver.quit()

