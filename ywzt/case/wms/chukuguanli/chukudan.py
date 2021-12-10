from ywzt.base.base_page import BasePage
from ywzt.config.get_path import data_files_path


class ChuKuDan(BasePage):
    case_path = data_files_path + '/wms/chukuguanli/chukudan_case.yaml'

    def get_ob_odd(self):
        print(self.yaml_operation(self.case_path))
        # return self.yaml_operation(self.case_path)
