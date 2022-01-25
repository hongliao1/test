import inspect
import json
import logging
import os
from time import sleep

import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from ywzt.app_config.app_handle_black import app_handle_black
from ywzt.app_config.app_config import page_name

from ywzt.base.read_yaml import ReadYaml


class AppBace():
    data_path = ''

    def __init__(self, driver: WebDriver = None):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '7.1.2',
                        'deviceName': '127.0.0.1-11509',
                        'appPackage': 'com.rantion.ns.pda',
                        'noReset': True,
                        'donotStopAppOnReset': True,
                        'appActivity': 'com.rantion.ns_pda.ui.main.activity.WelcomActivity',
                        'automationName': 'uiautomator2'
                        }
        if driver is None:
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        else:
            self.driver = driver
        self.driver.implicitly_wait(5)

    def max_window(self):
        self.driver.maximize_window()

    def min_window(self):
        self.driver.minimize_window()

    def element(self, key):
        if key == "css":
            return MobileBy.CSS_SELECTOR
        elif key == "xpath":
            return MobileBy.XPATH
        elif key == "id":
            return MobileBy.ID
        elif key == "class":
            return MobileBy.CLASS_NAME
        elif key == 'some_text':
            return MobileBy.PARTIAL_LINK_TEXT
        elif key == 'accessibility_id':
            return MobileBy.ACCESSIBILITY_ID
        else:
            return '定位方法错误'

    @app_handle_black
    def find(self, key, value: str = None):
        try:
            if isinstance(key, tuple):
                return self.driver.find_element(*key)
            else:
                self.wait_for_click((self.element(key), value))
                return self.driver.find_element(self.element(key), value)
        except Exception as f:
            print('查找元素失败：%s' % f)
            return None

    def finds(self, key, value: str = None):
        self.sleep(0.5)
        try:
            # self.sleep(0.2)
            self.wait_for_click((self.element(key), value))
            return self.driver.find_elements(self.element(key), value)
        except Exception as f:
            logging.info("查找元素失败：%s" % f)
            return None

    def input(self, key, value, txt):
        self.find(key, value).send_keys(txt)

    def click(self, key, value):
        self.find(key, value).click()

    # @handle_black
    def sleep(self, txt):
        sleep(txt)

    def wait_for_click(self, key, time=10):
        WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(key))

    def app_yaml_operation(self, case_path, *args):
        with open(case_path, encoding='utf-8') as f:
            name = inspect.stack()[1].function
            location = yaml.safe_load(f)[name]
        raw = json.dumps(location)
        data_1 = ReadYaml().readyaml(self.data_path, args)
        for key, value in data_1.items():
            raw = raw.replace(f'${{{key}}}', value)
        location = json.loads(raw)
        list_1 = []
        for data in location:
            if data['operation'] == 'get_kuwei':
                text = self.find(data['by'], data['location']).text
                list_1 = [text]
            if data['operation'] == 'scan_code':
                self.scan_code(data['odd'], list_1)
                list_1.clear()
            if data['operation'] == 'input':
                self.input(data['by'], data['location'], data['input'])
            if data['operation'] == 'click':
                self.click(data['by'], data['location'])
            if data['operation'] == 'sleep':
                self.sleep(data['time'])

    # 模拟键盘操作
    # def action(self):
    #     return ActionChains(self.selfdriver)
    # action.send_keys(Keys.F5)

    # pda扫码
    def scan_code(self, odd, list=None):
        # 连接联想模拟器
        # os.system('adb connect 127.0.0.1:11509')
        # 运行扫码
        self.sleep(1)
        if odd != '':
            os.system('adb shell am broadcast -a my_broadcast_service -p %s --es scannerdata %s' % (page_name, odd))
        else:
            os.system('adb shell am broadcast -a my_broadcast_service -p %s --es scannerdata %s' % (page_name, list[0]))

    # 滑动到元素直至元素可见
    def sliding(self, key, value):
        element = self.find(key, value)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", element)

    def quit(self):
        self.driver.quit()
