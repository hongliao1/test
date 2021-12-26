from ywzt.base.base_page import BasePage
from ywzt.case.wms.diaoboguanli.diaobodan.diaobodan import DiaoBoDan
from ywzt.case.wms.diaoboguanli.zancunquguanli.zancun import ZanCun
from ywzt.config.get_path import pages_path


class DiaoBo(BasePage):
    case_path = pages_path + '/wms/diaoboguanli/diaoboguanli.yaml'

    def diaobodan(self):
        self.yaml_operation(self.case_path)
        return DiaoBoDan(self.driver)

    def zancunquguanli(self):
        self.yaml_operation(self.case_path)
        return ZanCun(self.driver)

