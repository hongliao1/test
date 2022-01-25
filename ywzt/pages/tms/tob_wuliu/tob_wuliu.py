from ywzt.base.base_page import BasePage
from ywzt.pages.tms.tob_wuliu.dingcangguanli.dingcangguanli import DingCangGuanLi


class TobWuLiu(BasePage):
    case_path = r'E:\job\test\ywzt\pages\tms\tob_wuliu\tob_wuliu.yaml'

    def dingcangguanli(self):
        self.yaml_operation(self.case_path)
        return DingCangGuanLi(self.driver)
