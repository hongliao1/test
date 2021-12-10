from ywzt.pages.login import LoginPage
from time import sleep

import pytest
import yaml

from ywzt.base.connect_mysql import connect_mysql_1



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

    @connect_mysql_1(int(
        yaml.safe_load(open(r'E:\job\test\ywzt\data_files\wms\baosunguanli\baosun_data.yaml', encoding='utf-8'))[0][
            'num']))
    # @pytest.mark.run(order=2)
    def test_shenhe_pass(self):
        self.login.wms_click().kucun().kuweikucun().kuwei_baosun()
        self.login.wms_click().baosunguanli().baosun().shenhe_tongguo()
        sleep(2)
        self.login.quit()

    def test_ruku(self):
        # 创建入单
        self.login.wms_click().rukuguanli().rukudan().createrukudan()
        # 获取入库单号，固定格式
        ib_odd = self.login.wms_click().rukuguanli().rukudan().get_ib_odd()
        data = {'ib': ib_odd}
        # 完成收货
        self.login.wms_click().rukuguanli().shouhuo().shouhuo(data)
        # 点击一键入库
        self.login.wms_click().rukuguanli().rukudan().yijianruku()

        sleep(2)
        self.login.quit()

    def test_chuku(self):
        # self.login.wms_click().chukuguanli().chukudan()
        self.login.wms_click().chukuguanli().chukudan().get_ob_odd()
        self.login.quit()
