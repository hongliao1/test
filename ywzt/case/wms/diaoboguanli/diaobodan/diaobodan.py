from time import sleep

from ywzt.base.base_page import BasePage
from ywzt.config.get_path import data_files_path


class DiaoBoDan(BasePage):
    case_path = data_files_path + '/wms/diaoboguanli/diaobodan.yaml'
    data_path = data_files_path + '/wms/diaoboguanli/diaobodan_data.yaml'

    def create_ziying_diaobodan(self):
        self.yaml_operation(self.case_path)

    def get_pd_odd(self):
        text = self.yaml_operation(self.case_path)
        return text
