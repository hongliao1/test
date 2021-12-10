from ywzt.app_page.rukuguanli.rukuguanli import RuKuGuanLi
from ywzt.base.app_bace_page import AppBace


class PdaFirstPage(AppBace):
    def setup(self):
        self.input('id', 'com.rantion.ns.pda:id/userEditText', '廖宏')
        self.input('id', 'com.rantion.ns.pda:id/passwordEditText', "000000")
        self.click('id', 'com.rantion.ns.pda:id/btn_setting')
        self.click('xpath', '//*[@text="测试环境"]')
        self.click('xpath', '//*[@text="确定"]')
        self.click('xpath', '//*[@text="登录"]')

    def rukuguanli(self):
        self.setup()
        self.click('xpath', '//*[@text="入库管理"]')
        return RuKuGuanLi(self.driver)

    def gongchangguanli(self):
        self.setup()
        self.click('xpath', '//*[@text="工厂管理"]')

    def chukuguanli(self):
        self.setup()
        self.click('xpath', '//*[@text="出库管理"]')

    def diaoboguanli(self):
        self.setup()
        self.click('xpath', '//*[@text="调拨管理"]')

    def pandianguanli(self):
        self.setup()
        self.click('xpath', '//*[@text="盘点管理"]')