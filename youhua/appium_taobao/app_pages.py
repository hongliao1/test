from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestAppDriver():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = '127.0.0.1-11509'
        desired_caps['appPackage'] = 'com.taobao.taobao'
        desired_caps['appActivity'] = 'com.taobao.tao.welcome.Welcome'
        desired_caps['automationName'] = 'uiautomator2'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(15)

    def teardown(self):
        self.driver.quit()

    def tounch_1(self):
        pass

    def test_search(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='同意']").click()
        self.driver.find_element(MobileBy.ID, "com.taobao.taobao:id/searchEdit").send_keys('内裤被风吹走了')
        sleep(5)
