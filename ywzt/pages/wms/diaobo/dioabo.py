from time import sleep

from ywzt.base.base_page import PageBase
from ywzt.pages.wms.diaobo.diaobodan import DiaoBoDan
from ywzt.pages.wms.diaobo.zancun import ZanCun


class DiaoBo(PageBase):
    def zancun(self):
        self.click("css", '#app-wms>section>aside>div>ul>li:nth-child(4)>ul>li:nth-child(4)>a')
        return ZanCun(self.driver)

    def diaobodan(self):
        self.click("css", '#app-wms>section>aside>div>ul>li:nth-child(4)>ul>li:nth-child(1)>a')
        return DiaoBoDan(self.driver)