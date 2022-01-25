from ywzt.base.base_page import BasePage


class YuDingCangOperation(BasePage):
    def create_dingcang(self, case_path, data_path):
        self.yaml_operation(case_path, data_path)
