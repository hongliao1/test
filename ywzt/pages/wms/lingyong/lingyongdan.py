from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from ywzt.base.base_page import BasePage


class LingYongDan(BasePage):
    def add_lingyongdan(self):
        sleep(2)
        # 点击领用单
        self.click('css', '#app-wms > section > aside > div > ul > li:nth-child(8)>ul>li>a')
        # 点击新增
        self.click("css", '#props-tags > main > div > div.table-top > button:nth-child(1)')
        # 点击来源仓库
        sleep(1)
        self.click('css', '#app-wms>div>div>div:nth-child(2)>div>div:nth-child(2)>div:nth-child('
                          '3)>form>div>div>div>div:nth-child(2)>div>span>div>div>div')
        # 等待
        sleep(1)
        # 点击最后一个花都仓
        self.click('css', '.ant-select-dropdown-placement-bottomLeft>div> ul > li:nth-last-child(1)')
        # 输入领用人
        self.input("xpath", '//*[@id="app-wms"]/div[1]/div/div[2]/div/div[2]/div[2]/form[1]/div/div[2]/div/div['
                            '2]/div/span/input', "廖宏")
        # 输入领用原因
        self.input('css', '#app-wms > div:nth-child(2) > div > div.ant-modal-wrap > div > div.ant-modal-content > '
                          'div.ant-modal-body > form:nth-child(2) > div > div:nth-child(3) > div > '
                          'div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > input', '就是测试下')
        # 输入地址
        self.input('css', '#app-wms > div:nth-child(2) > div > div.ant-modal-wrap > div > div.ant-modal-content > '
                          'div.ant-modal-body > form:nth-child(2) > div > div:nth-child(4) > div > '
                          'div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > input', '广州')
        # 输入电话
        self.input('css', '#app-wms > div:nth-child(2) > div > div.ant-modal-wrap > div > div.ant-modal-content > '
                          'div.ant-modal-body > form:nth-child(2) > div > div:nth-child(5) > div > '
                          'div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > input', '123456789')
        # 选择主体
        self.click('css', '#app-wms > div:nth-child(2) > div > div.ant-modal-wrap > div > div.ant-modal-content > '
                          'div.ant-modal-body > form:nth-child(2) > div > div:nth-child(6) > div > '
                          'div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > div')
        sleep(2)
        # self.click('xpath', '/html/body/div/section/div[3]/div/div/div[4]/div/div/div/ul/li[2]')
        self.click('css', '#app-wms>div:nth-child(5)>div>div>div>ul>li:nth-child(1)')
        # self.click('css', '.ant-select-dropdown-menu-item-active')
        sleep(5)
