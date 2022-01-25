from ywzt.base.base_page import BasePage


class DingCangOperation(BasePage):

    def dingcang_case(self, case_path, data_path, *args):
        self.yaml_operation(case_path, data_path, *args)

    def dingcang_case_1(self, case_path, data_path):
        self.yaml_operation(case_path, data_path)

    def dingcang_case_2(self, case_path, data_path):
        self.yaml_operation(case_path, data_path)

    def dingcang_case_3(self, case_path, data_path):
        self.yaml_operation(case_path, data_path)

    def dingcang_case_4(self, case_path, data_path):
        self.yaml_operation(case_path, data_path)

    def dingcang_case_5(self, case_path, data_path):
        self.yaml_operation(case_path, data_path)

    def dingcang_get_odd(self, case_path, data_path):
        return self.yaml_operation(case_path, data_path)