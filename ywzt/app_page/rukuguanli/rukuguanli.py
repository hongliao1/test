import os
import shlex

from paramiko.proxy import subprocess

from ywzt.base.app_bace_page import AppBace


class RuKuGuanLi(AppBace):
    def qianshou(self):
        self.click('xpath', '//*[@text="签收"]')
        # cmd = shlex.split("adb shell am broadcast -a my_broadcast_service -p com.rantion.ns.pda --es scannerdata "
        #                   "IB2112070L-A")
        # subprocess.popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        os.system("adb shell am broadcast -a my_broadcast_service -p com.rantion.ns.pda --es scannerdata IB2112060I-A")
        self.click('xpath', "//*[@text='签收']")
        # self.quit()

    def zhuangxiang(self):
        self.click('xpath', '//*[@text="装箱"]')

    def zhuangban(self):
        self.click('xpath', '//*[@text="装板"]')

    def shouhuo(self):
        self.click('xpath', '//*[@text="收货"]')
        os.system("adb shell am broadcast -a my_broadcast_service -p com.rantion.ns.pda --es scannerdata IB2112060I-A")
        self.click('xpath', '//*[@text="完成收货"]')
        # self.quit()

    def shangjia(self):
        self.click('xpath', '//*[@text="上架"]')
        os.system("adb shell am broadcast -a my_broadcast_service -p com.rantion.ns.pda --es scannerdata SS1A01010101")
        self.click('xpath', '//*[@text="扫描产品条码上架"]')
        os.system("adb shell am broadcast -a my_broadcast_service -p com.rantion.ns.pda --es scannerdata IB2112060I-A")
        os.system("adb shell am broadcast -a my_broadcast_service -p com.rantion.ns.pda --es scannerdata HY1719")
        self.click('xpath', '//*[@text="确定"]')
        self.click('xpath', '//*[@text="上架"]')
        # self.quit()

    def tuijianqianshou(self):
        self.click('xpath', '//*[@text="退件签收"]')