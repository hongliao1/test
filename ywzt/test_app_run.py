from ywzt.app_page.pda_login import PdaFirstPage
import os

class TestAppRun():
    def setup(self):
        self.login = PdaFirstPage()

    def test_ruku(self):
        # self.login.rukuguanli().qianshou()
        self.login.rukuguanli().shouhuo()
        self.login.rukuguanli().shangjia()

    def test_chuku(self):
        self.login.chukuguanli()

