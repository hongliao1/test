from ywzt.base.base_page import BasePage
from ywzt.case.wms.rukuguanli.ruku_base import RuKuBase
from ywzt.config.get_path import pages_path


class RuKuGuanLi(BasePage):
    path = pages_path + '/wms/rukuguanli/rukudan.yaml'

    def rukudan(self):
        self.yaml_operation(self.path)
        return RuKuBase(self.driver)

    def shouhuo(self):
        self.yaml_operation(self.path)
        return RuKuBase(self.driver)

    def tuopanguanli(self):
        self.yaml_operation(self.path)
