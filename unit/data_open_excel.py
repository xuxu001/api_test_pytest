import xlrd
from xlutils.copy import copy
import unittest

class OpemExcel:

    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = 'C:/Users/daiba/PycharmProjects/api_test_pytest/test_file/case/class.xlsx'
            self.sheet_id = 0

        self.data = self.get_data()
    #获取excel内容
    def get_data(self,):

        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]

        return tables
    #获取行数
    def get_data_line(self):
        tables = self.get_data()
        print('_____')
        print(tables.nrows)
        print('_____')
        return tables.nrows

    #获取单元格的内容
    def get_cell_value(self,row,col):
        res = None
        res = self.data.cell_value(row,col)
        # print(res)
        # print(type(res))
        return res

    def write_value(self,row,col,value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)



if __name__ == '__main__':
    ope = OpemExcel()
    ope.get_cell_value(0,0)




