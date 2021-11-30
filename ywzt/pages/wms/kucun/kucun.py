from ywzt.base.base_page import PageBase
from ywzt.case.wms.kuweikucun.kuweikucun import KuWeiKuCun
from ywzt.config.get_path import pages_path


class KunCun(PageBase):
    path = pages_path + r"\wms\kucun\kucun.yaml"

    def kucun(self):
        self.yaml_operation(self.path)

    def kuweikucun(self):
        self.yaml_operation(self.path)
        return KuWeiKuCun(self.driver)
