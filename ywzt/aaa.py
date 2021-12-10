import os
from time import sleep
from selenium import webdriver

# sleep(3)
# os.system("kill MEmu")
# os.system("MEmu")
os.system("adb devices")
os.system('MEmu')
sleep(1)
os.system('adb connect 127.0.0.1:11509')
os.system('appium')
sleep(1)
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# print(driver.current_url)
# print(driver.title)
# print(driver.page_source)

# element = driver.find_element(By.ID, 'su')
# print(element.text)
# driver.quit()