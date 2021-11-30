"""
    登录页面
"""

from ywzt.base.base_page import PageBase
from ywzt.pages.pms.pms_module import PmsModule
from ywzt.pages.wms.wms_module import WmsModule
from ywzt.config.config import base_url
from ywzt.config.get_path import pages_path


class LoginPage(PageBase):
    url = base_url
    path = pages_path + '\login.yaml'
    data_path = r'E:\job\test\ywzt\config\login.yaml'

    def login(self):
        self.open()
        self.yaml_operation(self.path)

    def pms_click(self):
        self.login()
        self.yaml_operation(self.path)
        return PmsModule(self.driver)

    def wms_click(self):
        self.login()
        self.yaml_operation(self.path)
        return WmsModule(self.driver)

    def oms_click(self):
        self.login()
        self.yaml_operation(self.path)
        return WmsModule(self.driver)

    def tms_click(self):
        self.login()
        self.yaml_operation(self.path)
        return WmsModule(self.driver)

# path =str(pages_path + '\login.yaml')
# E:\job\test\ywzt\pages\login.yaml
# print(path)
