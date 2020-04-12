from selenium import webdriver
path = "../driver/chromedriver"
driver =webdriver.Chrome(executable_path=path)
driver.get("https://www.google.com")