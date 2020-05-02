from selenium.webdriver import Chrome,ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
ops = ChromeOptions()
ops.add_argument("--disable-notifications")
driver = Chrome(ChromeDriverManager().install(),options=ops)
driver.implicitly_wait(30)
driver.fullscreen_window()
driver.get("https://www.icicibank.com/")
driver.find_element_by_css_selector(".pl-login-ornage-box").click()

