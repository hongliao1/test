from ywzt.base.base_page import BasePage
from ywzt.case.tms.tob_wuliu.dingcangguanli.gongcangzhenggui.gz_case import GZ_case
from ywzt.pages.tms.tob_wuliu.dingcangguanli.ziyingsanhuo.ziyingsanhuo import ZiYingSanHuo


class DingCangGuanLi(BasePage):
    case_path = r'E:\job\test\ywzt\pages\tms\tob_wuliu\dingcangguanli\dingcangguanli.yaml'

    def gongcangzhenggui(self):
        self.yaml_operation(self.case_path)
        return GZ_case(self.driver)

    def ziyingsanhuo(self):
        self.yaml_operation(self.case_path)
        return ZiYingSanHuo(self.driver)