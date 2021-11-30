from time import sleep

from ywzt.base.base_page import PageBase


class DiaoBoDan(PageBase):
    def crea_diaobodan(self):
        self.click("css", '.table-top>button')
        self.click("css", '#app-wms > div:nth-child(2) > div > div.ant-modal-wrap > div > div.ant-modal-content > '
                          'div.ant-modal-body > form > div > div:nth-child(1) > div > '
                          'div.ant-col.ant-col-18.ant-form-item-control-wrapper > div > span > div > div > span > i > '
                          'svg')
        self.input("css", "#app-wms > div:nth-child(2) > div > div.ant-modal-wrap > div > div.ant-modal-content > "
                          "div.ant-modal-body > form > div > div:nth-child(1) > div > "
                          "div.ant-col.ant-col-18.ant-form-item-control-wrapper > div > span > div > div > div > div", "自营调拨")

        sleep(5)
