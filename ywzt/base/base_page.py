"""
    打开浏览器。关键字驱动封装了定位，等待、退出等多种方法
"""
import inspect
import json
import logging
from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from ywzt.base.read_yaml import ReadYaml
from ywzt.handle_black import handle_black
from ywzt.config.config import driver_type


# 无页面运行
# def browser(value):
#     opt = webdriver.ChromeOptions()  # 创建Chrome参数对象
#     opt.headless = True     # 把Chrome设置成可视化无界面模式，windows/Linux 皆可
#     try:
#         return getattr(webdriver, value)(options=opt)
#     except Exception as i:
#         print(i)
#         # webdriver.Firefox
#         return webdriver.Chrome(options=opt)

#     有页面运行
def browser(value):
    try:
        return getattr(webdriver, value)()
    except Exception as i:
        print(i)
        # webdriver.Firefox
        return webdriver.Chrome()


class BasePage(object):
    url = ''
    # case_path = ''
    data_path = ''

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self.driver = browser(driver_type)
        else:
            self.driver = driver
        self.max_window()
        self.driver.implicitly_wait(20)

    def max_window(self):
        self.driver.maximize_window()

    def min_window(self):
        self.driver.minimize_window()

    def open(self):
        self.driver.get(self.url)

    def by_object(self, key):
        if key == "css":
            return By.CSS_SELECTOR
        elif key == "xpath":
            return By.XPATH
        elif key == "id":
            return By.ID
        elif key == "class":
            return By.CLASS_NAME
        elif key == 'some_text':
            return By.PARTIAL_LINK_TEXT
        elif key == 'all_text':
            return By.LINK_TEXT
        elif key == 'name':
            return By.NAME
        elif key == 'tag_name':
            return By.TAG_NAME
        else:
            return '定位方法错误'

    @handle_black
    def find(self, key, value: str = None):
        if isinstance(key, tuple):
            return self.driver.find_element(*key)
        else:
            self.wait_for_click((self.by_object(key), value))
            return self.driver.find_element(self.by_object(key), value)

    @handle_black
    def finds(self, key, value: str = None):
        try:
            self.sleep(0.2)
            self.wait_for_click((self.by_object(key), value))
            return self.driver.find_elements(self.by_object(key), value)
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

    def yaml_operation(self, case_path, data_path='', *args):
        with open(case_path, encoding='utf-8') as f:
            # 获取调用yaml文件的函数【0】表示第一层：class名，【1】表示第二层逐级类推。
            name = inspect.stack()[1].function
            location = yaml.safe_load(f)[name]
        # 将读取的yaml（字典形式）转成json格式（字符串）
        raw = json.dumps(location)
        # 读取配置文件
        data: dict = ReadYaml().readyaml(data_path, args)
        # 遍历配置文件中的值
        for by, value in data.items():
            # 替换值。固定格式。前面带f的两个{}才相当于一个{}
            raw = raw.replace(f'${{{by}}}', value)
        # 转回字典格式
        location = json.loads(raw)
        list_1 = []
        list_2 = []
        # 先获得该用例中调用get_odd的总个数，用于下面作比较
        for data1 in location:
            data1: dict
            if data1['operation'] == 'get_odd':
                list_2.append(data1['operation'])
        for data1 in location:
            data1: dict
            for key in data1.keys():
                if 'txt' not in key:
                    pass
                else:
                    logging.info('正在执行：%s ' % data1['txt'])
            if "click" == data1['operation']:
                self.click(data1['by'], data1['location'])
                continue
            if 'input' == data1['operation']:
                self.input(data1['by'], data1['location'], data1['input'])
                continue
            if 'wait' == data1['operation']:
                if data1['by'] == 'css':
                    data1['by'] = By.CSS_SELECTOR
                elif data1['by'] == 'xpath':
                    data1['by'] = By.XPATH
                elif data1['by'] == 'id':
                    data1['by'] = By.ID
                elif data1['by'] == 'class':
                    data1['by'] = By.CLASS_NAME
                self.wait_for_click((data1['by'], data1['location']))
                continue
            if 'sleep' == data1['operation']:
                self.sleep(data1['time'])
                continue
            if "action" == data1['operation']:
                self.action(data1['key'])
                continue
            if 'sliding' == data1['operation']:
                self.sliding(data1['by'], data1['location'])
                continue
            if data1['operation'] == 'get_odd':
                text = self.find(data1['by'], data1['location']).text
                if text is None:
                    text = self.find(data1['by'], data1['location']).get_attribute('textContent')
                    if text is None:
                        text = self.find(data1['by'], data1['location']).get_attribute('innerHTML')
                list_1.append(text)
                if len(list_1) == len(list_2):
                    return tuple(list_1)

    def keys(self, key):
        if key == 'backspace':
            return Keys.BACK_SPACE
        elif key == 'enter':
            return Keys.ENTER

    # 模拟键盘操作
    def action(self, key):
        action = ActionChains(self.driver)
        action.send_keys(self.keys(key)).perform()

    # 滑动到元素直至元素可见
    def sliding(self, key, value):
        element = self.find(key, value)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", element)

    def quit(self):
        self.driver.quit()
