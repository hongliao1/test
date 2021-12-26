from ywzt.app_page.diaoboguanli.diaoboguanli import DiaoBoGuanLi
from ywzt.app_page.rukuguanli.rukuguanli import RuKuGuanLi
from ywzt.base.app_bace_page import AppBace


class PdaFirstPage(AppBace):
    case_path = r'E:\job\test\ywzt\app_page\pda_lodin.yaml'
    data_path = r'E:\job\test\ywzt\config\login.yaml'

    def setup_class(self):
        self.app_yaml_operation(self.case_path)

    def rukuguanli(self):
        self.setup_class()
        self.click('xpath', '//*[@text="入库管理"]')
        return RuKuGuanLi(self.driver)

    def gongchangguanli(self):
        self.setup_class()
        self.click('xpath', '//*[@text="工厂管理"]')

    def chukuguanli(self):
        self.setup_class()
        self.click('xpath', '//*[@text="出库管理"]')

    def diaoboguanli(self):
        self.setup_class()
        self.click('xpath', '//*[@text="调拨管理"]')
        return DiaoBoGuanLi(self.driver)

    def pandianguanli(self):
        self.setup_class()
        self.click('xpath', '//*[@text="盘点管理"]')
