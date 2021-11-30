from time import sleep

from ywzt.base.base_page import PageBase


class ZanCun(PageBase):
    def add(self):
        self.click("css", '.ant-layout-content>div>div:nth-child(2)>button')
        self.input("css", '#app-wms > div:nth-child(5) > div > div.ant-modal-wrap.ant-modal-centered > div > '
                          'div.ant-modal-content > div.ant-modal-body > form > div > div:nth-child(2) > div > '
                          'div.ant-col.ant-col-15.ant-form-item-control-wrapper > div > span > input', '11')
        self.input("css", "#app-wms > div:nth-child(5) > div > div.ant-modal-wrap.ant-modal-centered > div > "
                          "div.ant-modal-content > div.ant-modal-body > form > div > div:nth-child(3) > div > "
                          "div.ant-col.ant-col-15.ant-form-item-control-wrapper > div > span > input", "11")
        self.click('css', '#app-wms > div:nth-child(5) > div > div.ant-modal-wrap.ant-modal-centered > div > '
                          'div.ant-modal-content > div.ant-modal-footer > div > button.ant-btn.ant-btn-primary')
        sleep(5)
