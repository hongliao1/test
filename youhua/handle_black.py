import logging

from selenium.webdriver.common.by import By


def handle_black(func):
    # 设置日志级别
    logging.basicConfig(level=logging.INFO)

    def wrapper(*args, **kwargs):
        from ywzt.base.base_page import BasePage
        _black_list = [(By.XPATH, '//*[@text="确认"]'),
                       (By.XPATH, '//*[@text="创建失败"]')]
        _max_num = 3
        _error_num = 0
        instance: BasePage = args[0]
        try:
            logging.info("run" + func.__name__ + "\n args:\n" + repr(args) + "\n kwargs:" + repr(kwargs))
            element = func(*args, **kwargs)
            _error_num = 0
            instance.driver.implicitly_wait(10)
            return element
        except Exception as e:
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
            raise e
