from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.extensions.android.gsm import GsmCallActions
from selenium.webdriver.common.by import By


class TestAppDriver():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = '127.0.0.1-11509'
        # desired_caps['avd'] = 'app_123'
        desired_caps['appPackage'] = 'com.rantion.ns.pda'
        desired_caps['appActivity'] = 'com.rantion.ns_pda.ui.main.activity.WelcomActivity'
        desired_caps['automationName'] = 'uiautomator2'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(15)

    def teardown(self):
        self.driver.quit()

    def tounch_1(self):
        pass

    def test_search(self):
        # sleep(5)
        self.driver.find_element(By.ID, 'com.rantion.ns.pda:id/userEditText').send_keys('廖宏')
        self.driver.find_element(By.ID, 'com.rantion.ns.pda:id/passwordEditText').send_keys('000000')
        self.driver.find_element(By.ID, 'com.rantion.ns.pda:id/btn_setting').click()
        self.driver.find_element(By.XPATH, '//*[@text="测试环境"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="确定"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="登录"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="盘点管理"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="扫描盘点单"]').click()
        self.driver.find_element(By.ID, 'com.rantion.ns.pda:id/edt_code').send_keys("12345656")
        # self.driver.make_gsm_call('15879758076', GsmCallActions.CALL)
        self.driver.send_sms('19179081239', 'hello sb')
        # self.driver.set_network_connection(1)
        # sleep(5)
        # self.driver.set_network_connection(4)
        sleep(5)