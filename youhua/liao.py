import inspect
import logging
import time

# class TestLiao():
# def liao():
#     logging.basicConfig(level=logging.INFO)
#     log = logging.getLogger('111')
#     list = [1, 2, 3]
#     list_1 = [1,1213, 3]
#     for key in list:
#         log.info(key)
#     for value in list_1:
#         log.info(value)
# def test_liao_2():
#     return liao()
#
# def test_2():
#     logging.basicConfig(level=logging.INFO)
#     log = logging.getLogger('test_2')
#     time.sleep(1)
#     log.debug('after 1 sec')
#     time.sleep(1)
#     log.debug('after 2 sec')
#     time.sleep(1)
#     log.debug('after 3 sec')
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from ywzt.base.base_page import BasePage

# def test_1():
#     logging.basicConfig(level=logging.DEBUG)
#     log = logging.getLogger('test_1')
#     time.sleep(1)
#     log.debug('after 1 sec')
#     time.sleep(1)
#     log.debug('after 2 sec')
#     time.sleep(1)
#     log.debug('after 3 sec')
#     assert 1, 'should pass'


# def test_2():
#     log = logging.getLogger('test_2')
#     time.sleep(1)
#     log.debug('after 1 sec')
#     time.sleep(1)
#     log.debug('after 2 sec')
#     time.sleep(1)
#     log.debug('after 3 sec')
#     assert 0, 'failing for demo purposes'
# TestLiao().test_liao_2()
# test_2()
# test_1()
# [pytest]
# log_cli = 1
# log_cli_level = INFO
# log_cli_format = %(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)
# log_cli_date_format=%Y-%m-%d %H:%M:%S
option = Options()
option.debugger_address = 'localhost:9222'

driver = webdriver.Chrome(options=option)
driver.find_element(By.CSS_SELECTOR, '#props-tags>main>div>div>div>div>div>label:nth-child(2)>span:nth-child(2)').click()
driver.find_element(By.CSS_SELECTOR, '"#props-tags>main>div>div>div>div:nth-child(2)>form>div>div>div>div:nth-child(2)>div>span>div>div>div"').click()
driver.find_element(By.CSS_SELECTOR, '#props-tags>main>div>div>div>div:nth-child(2)>form>div>div>div>div:nth-child(2)>div>span>div>div>div>div:nth-child(2)>div>input').send_keys('美西仓')
# BasePage.yaml_operation(r'E:\job\test\ywzt\pages\wms\baosunguanli\baosun_pass.yaml')
# with open(r'E:\job\test\youhua\baosun_pass.yaml', encoding='utf-8') as f:
#     # 获取调用yaml文件的函数【0】表示第一层：class名，【1】表示第二层逐级类推。
#     # name = inspect.stack()[1].function
#     location = yaml.safe_load(f)
# # print(location)
# for data in location:
#     if "click" == data['operation']:
#         selfdriver.find_element(data['by'], data['location']).click()
#     if 'input' == data['operation']:
#         selfdriver.find_element(data['by'], data['location']).send_keys(data['input'])
#     # if 'wait' == data['operation']:
#     #     WebDriverWait(selfdriver, 10).until(expected_conditions.element_to_be_clickable((data['by'], data['location'])))
#     if 'sleep' == data['operation']:
#         time.sleep(data['time'])
#     # if "action" == data['operation']:
#     #     self.action().send_keys(Keys.F5)
#     # if 'sliding' == data['operation']:
#     #     element = selfdriver.find_element(data['by'], data['location'])
#     #     selfdriver.execute_script("arguments[0].scrollIntoView(false);", element)
driver.find_element()
