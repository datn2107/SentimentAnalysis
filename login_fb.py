from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome("chromedriver.exe")

browser.get("https://www.facebook.com/")
txt_user = browser.find_element_by_id("email")
txt_user.send_keys("")
txt_pass = browser.find_element_by_id("pass")
txt_pass.send_keys("")
txt_pass.send_keys(Keys.ENTER)

sleep(5)
browser.close()