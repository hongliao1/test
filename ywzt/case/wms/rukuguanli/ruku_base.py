from ywzt.base.base_page import BasePage
from ywzt.config.get_path import data_files_path


class RuKuBase(BasePage):
    case_path = data_files_path + '/wms/rukuguanli/ruku_case.yaml'
    data_path = data_files_path + '/wms/rukuguanli/ruku_data.yaml'

    def createrukudan(self):
        self.yaml_operation(self.case_path)

    def get_ib_odd(self):
        return self.yaml_operation(self.case_path)

    def shouhuo(self, data):
        self.yaml_operation(self.case_path, data)

    def yijianruku(self):
        self.yaml_operation(self.case_path)