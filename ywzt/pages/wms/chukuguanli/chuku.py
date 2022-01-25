from ywzt.base.base_page import BasePage
from ywzt.case.wms.chukuguanli.chukudan import ChuKuDan
from ywzt.config.get_path import pages_path


class ChuKu(BasePage):
    path = pages_path + '/wms/chukuguanli/chuku.yaml'

    def chukudan(self):
        self.yaml_operation(self.path)
        return ChuKuDan(self.driver)
