import requests

class RunMethod:
    #定义post请求
    def post_method(self,url,data,header=None,token = None):
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header)
        else:
            res = requests.post(url=url,data=data)

        return res

    #定义get请求
    def get_method(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header)
        else:
            res = requests.get(url=url, data=data)

        return res

    #定义主函数
    def run_main(self,method,url,data,header):
        if method == 'POST':
            res = self.post_method(url,data,header)
        else:
            res = self.get_method(url,data,header)

        return res

if __name__ == '__main__':
    run = RunMethod()
