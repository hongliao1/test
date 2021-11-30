"""
    查看读取excel表格
"""
import openpyxl


class ReadEx(object):
    def __init__(self, ex_path):
        self.excel = openpyxl.load_workbook(ex_path)

    def read_excel(self):
        for sheets in self.excel.sheetnames:
            sheet = self.excel[sheets]
            for value in sheet.values:
                if type(value[0]) is int:
                    data = {"key": value[1], "value": value[2], "txt": value[3]}
                    return data
