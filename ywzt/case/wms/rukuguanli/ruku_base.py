from ywzt.base.base_page import BasePage
from ywzt.config.get_path import data_files_path


class RuKuBase(BasePage):
    case_path = data_files_path + '/wms/rukuguanli/ruku_case.yaml'
    data_path = data_files_path + '/wms/rukuguanli/ruku_data.yaml'

    def createrukudan(self):
        self.yaml_operation(self.case_path, self.data_path)

    def get_ib_odd(self):
        return self.yaml_operation(self.case_path, self.data_path)

    def shouhuo(self, *args):
        self.yaml_operation(self.case_path, self.data_path, *args)

    def yijianruku(self):
        self.yaml_operation(self.case_path, self.data_path)