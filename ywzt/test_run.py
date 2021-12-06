from time import sleep

import pytest
import yaml

from ywzt.base.connect_mysql import connect_mysql_1
from ywzt.pages.login import LoginPage


class Testrun:
    def setup(self):
        self.login = LoginPage()
    
    # @connect_mysql
    # @pytest.mark.run(order=1)
    # def test_baoshun(self):
    #     # a.wms_cllick().diaobo().zancun().add()
    #     # a.wms_cllick().diaobo().diaobodan().crea_diaobodan()
    #     # a.wms_cllick().lingyong().add_lingyongdan()
    #     # a.wms_cllick().cangku().cangku().create_cangku()
    #     self.login.wms_click().kucun().kuweikucun().kuwei_baosun()
    #     sleep(2)
    #     self.login.quit()

    @connect_mysql_1(int(yaml.safe_load(open(r'E:\job\test\ywzt\data_files\wms\baosunguanli\baosun_data.yaml', encoding='utf-8'))[0]['num']))
    # @pytest.mark.run(order=2)
    def test_shenhe_pass(self):
        self.login.wms_click().kucun().kuweikucun().kuwei_baosun()
        self.login.wms_click().baosunguanli().baosun().shenhe_tongguo()
        sleep(2)
        self.login.quit()