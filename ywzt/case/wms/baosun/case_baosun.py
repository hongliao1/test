from ywzt.base.base_page import BasePage
from ywzt.config.get_path import data_files_path


class BaoSunCase(BasePage):
    path = data_files_path + r'\wms\baosunguanli\baosun_pass.yaml'
    data_path = r'E:\job\test\ywzt\data_files\wms\baosunguanli\baosun_data.yaml'

    def shenhe_tongguo(self):
        self.yaml_operation(self.path, self.data_path)
