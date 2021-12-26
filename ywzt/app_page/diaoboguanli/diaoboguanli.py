import os
from time import sleep

from ywzt.base.app_bace_page import AppBace


class DiaoBoGuanLi(AppBace):
    case_path = r'E:\job\test\ywzt\app_page\diaoboguanli\pda_diaoboguanli.yaml'
    data_path = r'E:\job\test\ywzt\data_files\wms\diaoboguanli\diaobodan_data.yaml'

    def diaobo_jianhuo(self, *args):
        # self.click('xpath', '//*[@text="调拨拣货"]')
        # # self.input('id', 'com.rantion.ns.pda:id/edt_code', odd)
        # # self.click('xpath', '//*[@text="确认"]')
        # os.system('adb shell am broadcast -a my_broadcast_service -p com.rantion.ns.pda --es scannerdata %s' % odd)
        # text = self.find("id", 'com.rantion.ns.pda:id/code').text
        # print(text)
        # # os.system('adb connect 127.0.0.1:11509')
        # # sleep(1)
        # os.system('adb shell am broadcast -a my_broadcast_service -p com.rantion.ns.pda --es scannerdata %s' % text)
        # self.click('id', 'com.rantion.ns.pda:id/btn_pickbysku')
        # self.input('id', 'com.rantion.ns.pda:id/edt_code', 'HY1719')
        # self.click('xpath', '//*[@text="确认"]')
        # self.input('id', 'com.rantion.ns.pda:id/edit_qty', '1')
        # self.click('id', 'com.rantion.ns.pda:id/btn_sure')
        # self.click('id', 'com.rantion.ns.pda:id/tv_popup_window_ok')
        # self.click('id', 'com.rantion.ns.pda:id/btn')
        self.app_yaml_operation(self.case_path, *args)
