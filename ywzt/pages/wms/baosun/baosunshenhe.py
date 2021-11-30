from ywzt.base.base_page import PageBase
from ywzt.case.wms.baosun.case_baosun import BaoSunCase
from ywzt.config.get_path import pages_path


class BaoSunShenHe(PageBase):
    path = pages_path + r'\wms\baosun\baosunshenhe.yaml'

    def baosun(self):
        self.yaml_operation(self.path)
        return BaoSunCase(self.driver)
