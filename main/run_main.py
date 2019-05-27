from commit.runmethod import RunMethod
from commit.get_data import GetData
from main.com import CommonUtil
from unit.send_email import SengEmail

class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.commit = CommonUtil()
        self.send = SengEmail()


    def go_on_run(self):
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            data = self.data.get_request_data(i)
            header = self.data.is_header(i)
            expect = int(self.data.get_request_expcet(i))
            # depend_case = self.data.is_depend(i)
            token = self.data.get_request_token(i)
            # print(url)
            # print(method)
            # print(data)
            # print('-------')
            # print(header)
            # print('-------')

            res = self.run_method.run_main(method,url,data,header).status_code
            print(res)
            print(int(expect))

            if self.commit.is_contain(expect, res):
                self.data.write_result(i, 'pass')
                pass_count.append(i)


            else:
                self.data.write_result(i, 'fail')
                fail_count.append(i)

        self.send.send_main(pass_count, fail_count)

if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()