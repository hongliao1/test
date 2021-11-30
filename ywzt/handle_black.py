import logging

import allure
from selenium.webdriver.common.by import By


def handle_black(func):
    def wrapper(*args, **kwargs):
        # 设置日志级别（因为pytest.int已定义级别所以这里不用设置级别了）
        # logging.basicConfig(level=logging.INFO)
        from ywzt.base.base_page import PageBase
        _black_list = [(By.XPATH, '//*[@text="请求异常"]'),
                       (By.XPATH, '//*[@text="创建失败"]'),
                       (By.XPATH, '//*[@text="报损失败，报损数量不能大于库存数量"]'),
                       (By.XPATH, '//*[@text="111"]')]
        # _black_list = []
        _max_num = 3
        _error_num = 0
        # 调用self
        instance: PageBase = args[0]
        try:
            # 打印info等级日志，【1：】表示分割，repr为把数组字典转为字符
            logging.info("run" + func.__name__ + "\n args:\n" + repr(args[1:]) + "\n" + repr(kwargs)+"\n")
            element = func(*args, **kwargs)
            _error_num = 0
            instance.driver.implicitly_wait(10)
            return element
        except Exception as e:
            # 如果异常就截图
            instance.driver.save_screenshot('png.png')
            with open('png.png', 'rd') as f:
                content = f.read()
            allure.attach(content, attachment_type=allure.attachment_type.PNG)
            # 打印日志
            logging.info('error:element not found,handle black list')
            instance.driver.get_screenshot_as_png()
            instance.driver.implicitly_wait(1)
            if _error_num > _max_num:
                raise e
            _error_num += 1
            for ele in _black_list:
                elelist = instance.finds(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    return wrapper(*args, **kwargs)
        #     raise e

    return wrapper
