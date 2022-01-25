from ywzt.base.base_page import BasePage


class DiaoBoPiCiOperation(BasePage):
    def diaobopici_case(self, case_path):
        self.yaml_operation(case_path)

    def diaobopici_case_1(self, case_path):
        self.yaml_operation(case_path)

    def diaobopici_case_2(self, case_path):
        self.yaml_operation(case_path)

    def diaobopici_case_3(self, case_path):
        self.yaml_operation(case_path)

    def diaobopici_get_odd(self, case_path, *args):
        return self.yaml_operation(case_path, *args)
