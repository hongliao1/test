from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By


class TestAppDriver():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = '127.0.0.1-11509'
        desired_caps['appPackage'] = 'com.rantion.ns.pda'
        desired_caps['appActivity'] = 'com.rantion.ns_pda.ui.main.activity.WelcomActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def tounch_1(self):
        pass

    def test_search(self):
        self.driver.find_element(By.ID, 'com.rantion.ns.pda:id/userEditText').send_keys('廖宏')
        self.driver.find_element(By.ID, 'com.rantion.ns.pda:id/passwordEditText').send_keys('000000')
        self.driver.find_element(By.ID, 'com.rantion.ns.pda:id/btn_setting').click()
        self.driver.find_element(By.XPATH, '//*[@text="测试环境"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="确定"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="登录"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="盘点管理"]').click()
        self.driver.find_element(By.XPATH, '//*[@text="扫描盘点单"]').click()
        self.driver.find_element(By.ID, 'com.rantion.ns.pda:id/edt_code').send_keys("12345656")
        # self.driver.find_element_by_android_uiautomator('new UiSelector().resourcreId("com.rantion.ns.pda:id/edt_code")').send_keys('12345')
        sleep(5)

# class AppDriver():
#     def __init__(self):
#         selfdriver =webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# from appium import webdriver

# 1\准备参数：告诉appium，你要打开哪个设备上的哪个app。
# desired_caps = {
#     "automationName": "UiAutomator2",  # 使用哪个自动化引擎,appium1.x可以不用写
#     "platformName": "Android",  # 使用哪个移动操作系统平台
#     "platformVersion": '7.1.2',  # 移动操作系统版本
#     "deviceName": "emulator-5554",  # 使用的移动设备或模拟器的种类,需要在cmd命令下，敲adb devices查看
#     "appPackage": "com.lemon.lemonban",  # 所要测试的app的包名，获取命令：aapt dump badging apk路径，查看package: name=
#     "appActivity": "com.lemon.lemonban.activity.WelcomeActivity",
#     # 所要测试app的入口页面，获取命令：aapt dump badging apk路径，查看launchable-activity: name='
#     "noReset": True  # 在此会话之前，请勿重置应用程序状态
# }
#
# # 2、连接appium server，把启动参数发送
# selfdriver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 要讲源代码里提供的端口号改成4723
