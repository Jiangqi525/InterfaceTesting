import xlrd
from xlutils.copy import copy
from testcase.getpathInfo import get_path


class HandleExcel:
    """封装操作excel的方法"""
    def __init__(self, file=get_path(), sheet_id=0):
        self.file = file
        self.sheet_id = sheet_id
        self.data = self.get_data()

    # 获取某一页sheet对象
    def get_data(self):
        data = xlrd.open_workbook(self.file)
        sheet = data.sheet_by_index(self.sheet_id)
        return sheet

    # 获取excel数据行数
    def get_rows(self):
        rows = self.data.nrows
        return rows

    # 获取某个单元格数据
    def get_value(self, row, col):
        value = self.data.cell_value(row, col)
        return value

    # 向某个单元格写入数据
    def write_value(self, row, col, value):
        data = xlrd.open_workbook(self.file)  # 打开文件
        data_copy = copy(data)  # 复制原文件
        sheet = data_copy.get_sheet(0)  # 取得复制文件的sheet对象
        sheet.write(row, col, value)  # 在某一单元格写入value
        data_copy.save(self.file)  # 保存文件


# 封装excel的列名常量
def get_caseseq():
    """获取编号"""
    caseSeq = 0
    return caseSeq


def get_mode():
    """获取模块"""
    mode = 1
    return mode


def get_apiName():
    """获取标题"""
    apiName = 2
    return apiName


def get_method():
    """获取请求方式"""
    method = 3
    return method


def get_url():
    """获取接口地址"""
    url = 4
    return url


def get_params():
    """获取请求参数"""
    params = 5
    return params


def get_expect_value():
    """获取预期输出"""
    expect = 6
    return expect


def get_is_run():
    """获取是否运行"""
    is_run = 7
    return is_run


def get_result_value():
    """获取实际输出"""
    result = 8
    return result

