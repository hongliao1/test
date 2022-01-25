from ywzt.base.base_page import BasePage
from ywzt.pages.tms.tob_wuliu.tob_wuliu import TobWuLiu


class TmsModule(BasePage):
    case_path = r'E:\job\test\ywzt\pages\tms\tms_module.yaml'

    def tob_wuliu(self):
        self.yaml_operation(self.case_path)
        return TobWuLiu(self.driver)

