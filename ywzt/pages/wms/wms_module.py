from ywzt.base.base_page import PageBase
from ywzt.pages.wms.baosun.baosunshenhe import BaoSunShenHe
from ywzt.pages.wms.cangku.cangku import Test_CangKu
from ywzt.pages.wms.diaobo.dioabo import DiaoBo
from ywzt.pages.wms.kucun.kucun import KunCun
from ywzt.pages.wms.lingyong.lingyongdan import LingYongDan
from ywzt.config.get_path import pages_path


class WmsModule(PageBase):
    path = pages_path + r'\wms\wms_module.yaml'

    def diaobo(self):
        self.yaml_operation(self.path)
        return DiaoBo(self.driver)

    def lingyong(self):
        self.yaml_operation(self.path)
        return LingYongDan(self.driver)

    def cangku(self):
        self.yaml_operation(self.path)
        return Test_CangKu(self.driver)

    def kucun(self):
        self.yaml_operation(self.path)

        return KunCun(self.driver)

    def baosunguanli(self):
        self.yaml_operation(self.path)
        return BaoSunShenHe(self.driver)
