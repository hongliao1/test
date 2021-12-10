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

from ywzt.base.read_yaml import ReadYaml


class AppBace():
    url = ''
    data_path = ''

    def __init__(self, driver: WebDriver = None):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '7.1.2',
                        'deviceName': '127.0.0.1-11509',
                        'appPackage': 'com.rantion.ns.pda',
                        'noReset': True,
                        # 'donotStopAppOnReset': True,
                        'appActivity': 'com.rantion.ns_pda.ui.main.activity.WelcomActivity',
                        'automationName': 'uiautomator2'}
        if driver is None:
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        else:
            self.driver = driver
        self.driver.implicitly_wait(5)

    def max_window(self):
        self.driver.maximize_window()

    def min_window(self):
        self.driver.minimize_window()

    # def open(self):
    #     self.driver.get(self.url)
    def a(self, key):
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
        # elif key == "wait":
        #     pass
        else:
            return '定位方法错误'

    # @handle_black
    def find(self, key, value: str = None):
        if isinstance(key, tuple):
            return self.driver.find_element(*key)
        else:
            self.sleep(0.2)
            self.wait_for_click((self.a(key), value))
            return self.driver.find_element(self.a(key), value)

    # @handle_black
    def finds(self, key, value: str = None):
        try:
            self.sleep(0.2)
            self.wait_for_click((self.a(key), value))
            return self.driver.find_elements(self.a(key), value)
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

    def yaml_operation(self, case_path):
        with open(case_path, encoding='utf-8') as f:
            # 获取调用yaml文件的函数【0】表示第一层：class名，【1】表示第二层逐级类推。
            name = inspect.stack()[1].function
            location = yaml.safe_load(f)[name]
        # 将读取的yaml（字典形式）转成json格式（字符串）
        raw = json.dumps(location)
        # 读取配置文件
        data1: dict = ReadYaml().readyaml(self.data_path)
        # 遍历配置文件中的值
        for by, value in data1.items():
            # 替换值。固定格式。前面带f的两个{}才相当于一个{}
            raw = raw.replace(f'${{{by}}}', value)
        # 转回字典格式
        location = json.loads(raw)
        for data in location:
            if "click" == data['operation']:
                self.click(data['by'], data['location'])
            if 'input' == data['operation']:
                self.input(data['by'], data['location'], data['input'])
            if 'wait' == data['operation']:
                if data['by'] == 'css':
                    data['by'] = MobileBy.CSS_SELECTOR
                elif data['by'] == 'xpath':
                    data['by'] = MobileBy.XPATH
                elif data['by'] == 'id':
                    data['by'] = MobileBy.ID
                elif data['by'] == 'class':
                    data['by'] = MobileBy.CLASS_NAME
                self.wait_for_click((data['by'], data['location']))
            if 'sleep' == data['operation']:
                # self.sleep(data['time'])
                pass
            # if "action" == data['operation']:
            #     self.action().send_keys(Keys.F5)
            if 'sliding' == data['operation']:
                self.sliding(data['by'], data['location'])

    # 模拟键盘操作
    # def action(self):
    #     return ActionChains(self.selfdriver)
    # action.send_keys(Keys.F5)

    # 滑动到元素直至元素可见
    def sliding(self, key, value):
        element = self.find(key, value)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", element)

    def quit(self):
        self.driver.quit()
