from ywzt.base.base_page import BasePage
from ywzt.pages.tms.tob_wuliu.dingcangguanli.ziyingsanhuo.dingcang_operation.dingcang_operation import DingCangOperation
from ywzt.pages.tms.tob_wuliu.dingcangguanli.ziyingsanhuo.yudingcang_operation.yudingcangoperation import YuDingCangOperation


class ZiYingSanHuo(BasePage):
    case_path = r'E:\job\test\ywzt\pages\tms\tob_wuliu\dingcangguanli\ziyingsanhuo\ziyingsanhuo.yaml'

    def yudingcang(self):
        self.yaml_operation(self.case_path)
        return YuDingCangOperation(self.driver)

    def dingcang(self):
        self.yaml_operation(self.case_path)
        return DingCangOperation(self.driver)
