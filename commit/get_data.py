from unit.data_open_excel import OpemExcel
from commit import dataconfig

class GetData:
    def __init__(self):
        self.opemexcel = OpemExcel()


    #获取行数
    def get_case_lines(self):
        cow = int(self.opemexcel.get_data_line())
        return cow

    # 是否携带header
    # def is_header(self,row):
    #     col = int(dataconfig.get_header())
    #     header = self.opemexcel.get_cell_value(row,col)
    #     if header == '2':
    #         return dataconfig.get_header()
    #     else:
    #         return None
    #     print(header)

    #获取请求方式
    def get_request_method(self,row):
        col = int(dataconfig.get_method())
        request_method = self.opemexcel.get_cell_value(row,col)
        return request_method

    #获取请求地址
    def get_request_url(self,row):
        col = int(dataconfig.get_url())
        request_url = self.opemexcel.get_cell_value(row,col)
        return request_url

    #获取请求数据
    def get_request_data(self,row):
        col = int(dataconfig.get_data())
        request_data = self.opemexcel.get_cell_value(row,col)
        if request_data =='':
            return None
        return request_data

    #获取预期结果

    def get_request_expcet(self,row):
        col  = int(dataconfig.get_expect())
        request_expect = self.opemexcel.get_cell_value(row,col)
        return request_expect


    #获取token
    def get_request_token(self,row):
        col = int(dataconfig.get_token())
        request_token = self.opemexcel.get_cell_value(row,col)
        if request_token == '':
            return None
        return request_token

    def is_header(self,row):
        col = int(dataconfig.get_header())
        request_header = self.opemexcel.get_cell_value(row,col)
        if request_header == 'yes':
            return dataconfig.get_header_value()
        else:
            return dataconfig.get_header_value_two()

    def write_result(self,row,value):
        col = int(dataconfig.get_result())
        self.opemexcel.write_value(row,col,value)
        # return res
