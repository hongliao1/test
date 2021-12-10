from time import sleep

import pytest
import yaml




# a = ReadYaml()
# print(a.get_value())
from ywzt.base.base_page import BasePage
from ywzt.base.read_yaml import ReadYaml


class Test_CangKu(BasePage):

    def cangku(self):
        # 点击仓库管理
        self.click('css', '#app-wms > section > aside > div > ul > li>ul>li>a')
        return self

    # @pytest.mark.parametrize("name,num,type,type_1,action,sheng,city,fuzeren,lianxiren,phone,phone_1,"
    #                          "email,address,"
    #                          "body", list(ReadYaml().get_value()))
    def create_cangku(self):
        list_1 = ReadYaml().get_value()
        for i in range(len(list_1)):
            data = list_1[i]
            # 点击创建
            self.click('xpath', '//div[@id="props-tags"]/main/div/div[2]/button')
            # 输入仓库名
            self.input('xpath', '//div[@class="ant-modal-content"]/div[2]/form/div/div//input', data['name'])
            # 输入仓库编号
            self.input('xpath', '//div[@class="ant-modal-content"]/div[2]/form/div/div[2]//input', data['num'])
            # 选择类型
            self.click('xpath', '//div[@class="ant-modal-content"]/div[2]/form/div/div[3]//span/div/div/div')
            self.click('css', '#app-wms>div:nth-child(3)>div>div>div>ul>li:nth-child(%s)' % data['type'])
            # 选择状态
            self.click('xpath', '//*[@id="app-wms"]/div[1]/div/div[2]/div/div[2]/div[2]/form/div/div[4]/div/div['
                                '2]/div/span/div/div/div')
            self.click('xpath', '//*[@id="app-wms"]/div[3]/div/div/div/ul/li[%s]' % data['type_1'])
            # 点击国家并输入
            self.click('css', '#app-wms > div:nth-child(2) > div > div.ant-modal-wrap > div > div.ant-modal-content > '
                              'div.ant-modal-body > form > div > div:nth-child(5) > div > '
                              'div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > div')
            self.input('xpath', '//*[@id="app-wms"]/div[1]/div/div[2]/div/div[2]/div[2]/form/div/div[5]/div/div['
                                '2]/div/span/div/div/div/div[3]/div/input', data['action'])

            # 选择交易主体
            self.click('css', '#app-wms > div:nth-child(2) > div > div.ant-modal-wrap > div > div.ant-modal-content > '
                              'div.ant-modal-body > form > div > div:nth-child(14) > div > '
                              'div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > div')
            self.input('css', '#app-wms > div:nth-child(2) > div > div.ant-modal-wrap > div > div.ant-modal-content > '
                              'div.ant-modal-body > form > div > div:nth-child(14) > div > '
                              'div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > div > '
                              'ul > '
                              'li.ant-select-search.ant-select-search--inline > div > input', data['body'])
            self.click('css', '#app-wms > div > div > div.ant-modal-wrap > div > div.ant-modal-content > '
                              'div.ant-modal-body > form > div > div:nth-child(11) > div > '
                              'div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > input')
            # 点击并输入负责人
            self.click("css", '#app-wms > div:nth-child(2) > div > div.ant-modal-wrap > div > div.ant-modal-content > '
                              'div.ant-modal-body > form > div > div:nth-child(8) > div > '
                              'div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > div')
            self.input('xpath', '//*[@id="app-wms"]/div[1]/div/div[2]/div/div[2]/div[2]/form/div/div[8]/div/div['
                                '2]/div/span/div/div/div/div[3]/div/input', data['fuzeren'])
            # 点击省份并输入
            self.click('css', '#app-wms > div:nth-child(2) > div > div.ant-modal-wrap > div > div.ant-modal-content > '
                              'div.ant-modal-body > form > div > div:nth-child(6) > div > '
                              'div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > div')
            self.input('css', '#app-wms > div:nth-child(2) > div > div.ant-modal-wrap > div > div.ant-modal-content > '
                              'div.ant-modal-body > form > div > div:nth-child(6) > div > '
                              'div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > div > '
                              'div.ant-select-search.ant-select-search--inline > div > input', data['sheng'])
            # 输入联系人
            self.input('css', '#app-wms > div:nth-child(2) > div > div.ant-modal-wrap > div > div.ant-modal-content > '
                              'div.ant-modal-body > form > div > div:nth-child(9) > div > '
                              'div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > input',
                       data['lianxiren'])
            # 输入手机号码
            self.input('css', '#app-wms > div:nth-child(2) > div > div.ant-modal-wrap > div > div.ant-modal-content > '
                              'div.ant-modal-body > form > div > div:nth-child(10) > div > '
                              'div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > input',
                       data['phone'])
            # 输入固定电话
            self.input('css', '#app-wms > div:nth-child(2) > div > div.ant-modal-wrap > div > div.ant-modal-content > '
                              'div.ant-modal-body > form > div > div:nth-child(11) > div > '
                              'div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > input',
                       data['phone_1'])
            # 输入邮箱
            self.input('css', '#app-wms > div > div > div.ant-modal-wrap > div > div.ant-modal-content > '
                              'div.ant-modal-body > form > div > div:nth-child(12) > div > '
                              'div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > input',
                       data['email'])
            # 点击并输入城市
            self.click('css', '#app-wms > div:nth-child(2) > div > div.ant-modal-wrap > div > div.ant-modal-content > '
                              'div.ant-modal-body > form > div > div:nth-child(7) > div > '
                              'div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > div')
            self.input('css', '#app-wms > div:nth-child(2) > div > div.ant-modal-wrap > div > div.ant-modal-content > '
                              'div.ant-modal-body > form > div > div:nth-child(7) > div > '
                              'div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > div > '
                              'div.ant-select-search.ant-select-search--inline > div > input', data['city'])
            # 输入地址
            self.input('css', '#app-wms > div > div > div.ant-modal-wrap > div > div.ant-modal-content > '
                              'div.ant-modal-body > form > div > div:nth-child(13) > div > '
                              'div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > input',
                       data['address'])

            # 点击确定
            sleep(1)
            self.click('css', '#app-wms>div>div>div:nth-child(2)>div>div>div:nth-child(3)>div>button:nth-child(2)')
            sleep(1)
            txt = self.driver.page_source
            if data['assert'] in txt:
                assert True
            else:
                assert False
            # assert_1 = self.find('xpath', '/html/body/div[2]/div/div/div/div/div/div[2]')
            # if assert_1:
            #     assert data['assert'] in assert_1.get_attribute("textContent")
            #           # assertTextPresent(data['assert'])
            # else:
            #     element_1 = self.find('css', '.ant-modal-content')
            #     assert data['assert'] in element_1.text
            #
            try:
                element = self.find('css', '#app-wms > div:nth-child(2) > div > div.ant-modal-wrap > div > '
                                           'div.ant-modal-content > button > span > i')
                if element:
                    self.click('css', '#app-wms > div:nth-child(2) > div > div.ant-modal-wrap > div > '
                                      'div.ant-modal-content > button > span > i')
            except Exception as f:
                print(f)
            print("执行 %s 用例成功" % data['explain'])

    # def go_assert(self):
    #     if assertTextPresent(self.data['assert']):
