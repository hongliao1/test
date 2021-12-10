from ywzt.base.base_page import BasePage
from ywzt.pages.wms.baosun.baosunshenhe import BaoSunShenHe
from ywzt.pages.wms.cangku.cangku import Test_CangKu
from ywzt.pages.wms.chukuguanli.chuku import ChuKu
from ywzt.pages.wms.diaobo.dioabo import DiaoBo
from ywzt.pages.wms.kucun.kucun import KunCun
from ywzt.pages.wms.lingyong.lingyongdan import LingYongDan
from ywzt.config.get_path import pages_path
from ywzt.pages.wms.rukuguanli.rukudan import RuKuGuanLi


class WmsModule(BasePage):
    case_path = pages_path + r'\wms\wms_module.yaml'

    def rukuguanli(self):
        self.yaml_operation(self.case_path)
        return RuKuGuanLi(self.driver)

    def diaobo(self):
        self.yaml_operation(self.case_path)
        return DiaoBo(self.driver)

    def lingyong(self):
        self.yaml_operation(self.case_path)
        return LingYongDan(self.driver)

    def cangku(self):
        self.yaml_operation(self.case_path)
        return Test_CangKu(self.driver)

    def kucun(self):
        self.yaml_operation(self.case_path)

        return KunCun(self.driver)

    def baosunguanli(self):
        self.yaml_operation(self.case_path)
        return BaoSunShenHe(self.driver)

    def chukuguanli(self):
        self.yaml_operation(self.case_path)
        return ChuKu(self.driver)
