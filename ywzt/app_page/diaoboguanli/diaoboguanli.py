import os
from time import sleep

from ywzt.base.app_bace_page import AppBace


class DiaoBoGuanLi(AppBace):
    case_path = r'E:\job\test\ywzt\app_page\diaoboguanli\pda_diaoboguanli.yaml'
    data_path = r'E:\job\test\ywzt\data_files\wms\diaoboguanli\diaobodan_data.yaml'

    def diaobo_jianhuo(self, *args):
        self.app_yaml_operation(self.case_path, *args)

    def diaobo_pici_fayun(self, *args):
        self.app_yaml_operation(self.case_path, *args)