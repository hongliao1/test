import inspect
import json
import logging
from time import sleep

import yaml
from appium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from ywzt.base.read_yaml import ReadYaml


class AppBace(object):
    def __init__(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '7.1.2',
                        'deviceName': '127.0.0.1-11509',
                        'appPackage': 'com.rantion.ns.pda',
                        'appActivity': 'com.rantion.ns_pda.ui.main.activity.WelcomActivity',
                        'automationName': 'uiautomator2'}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def quit(self):
        self.driver.quit()

    def max_window(self):
        self.driver.maximize_window()

    def min_window(self):
        self.driver.minimize_window()

    # def open(self):
    #     self.driver.get(self.url)

    # @handle_black
    def find(self, key, value: str = None):
        if isinstance(key, tuple):
            return self.driver.find_element(*key)
        else:
            self.sleep(1)
            if key == "css":
                return self.driver.find_element(By.CSS_SELECTOR, value)
            elif key == "xpath":
                return self.driver.find_element(By.XPATH, value)
            elif key == "id":
                return self.driver.find_element(By.ID, value)
            elif key == "class":
                return self.driver.find_element(By.CLASS_NAME, value)
            elif key == 'some_text':
                return self.driver.find_element(By.PARTIAL_LINK_TEXT, value)
            else:
                return self.driver.find_element(key, value)

    # @handle_black
    def finds(self, key, value):
        try:
            WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located((key, value)))
            self.sleep(1)
            if key == "css":
                return self.driver.find_elements(By.CSS_SELECTOR, value)
            elif key == "xpath":
                return self.driver.find_elements(By.XPATH, value)
            elif key == "id":
                return self.driver.find_elements(By.ID, value)
            elif key == "class":
                return self.driver.find_elements(By.CLASS_NAME, value)
            else:
                return self.driver.find_elements(key, value)
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
                    data['by'] = By.CSS_SELECTOR
                elif data['by'] == 'xpath':
                    data['by'] = By.XPATH
                elif data['by'] == 'id':
                    data['by'] = By.ID
                elif data['by'] == 'class':
                    data['by'] = By.CLASS_NAME
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
