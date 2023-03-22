from common.configHttp import RunMain
from common.getexcel import *
from common.get_token import get_token
from common.logger import logger
from common.readconfig import ReadConfig
import json


class RunTestCase:
    def __init__(self):
        self.Runmain = RunMain()  # 实例化调用get/post请求基类
        self.data = HandleExcel()  # 实例化操作excel文件类
        self.ReadConfig = ReadConfig()  # 实例化操作config文件类

    def go_run(self):
        rows_count = self.data.get_rows()  # 获取excel行数
        schema = self.ReadConfig.get_http("schema")
        schema_url = self.ReadConfig.get_http("schema_url")
        port = self.ReadConfig.get_http("port")
        path = schema + "://" + schema_url + ":" + port
        for i in range(1, rows_count):  # 利用行数进行迭代处理每个接口
            url = path + self.data.get_value(i, get_url())  # 循环获取url的值
            method = self.data.get_value(i, get_method())  # 循环获取method的值
            expect = self.data.get_value(i, get_expect_value())  # 循环获取expect的值
            if self.data.get_value(i, get_params()) == '':
                data = None
            else:
                data = json.loads(self.data.get_value(i, get_params()))  # 循环获取请求参数，并将得到的数据反序列
            is_run = self.data.get_value(i, get_is_run())  # 通过标识循环获取该用例事是否运行
            if is_run == 'Y':
                headers = {'Content-Type': 'application/json;charset=UTF-8'}
                res = self.Runmain.run_main(method, url, data, headers=headers)
                logger.debug(f"响应结果：{res}")
                try:
                    if res['token']:
                        print('登陆成功')
                        self.data.write_value(i, get_result_value(), 'pass')
                    else:
                        print('测试失败')
                        self.data.write_value(i, get_result_value(), 'fail')
                except:
                    if res['message'] == '用户或者密码不正确':
                        print('登陆失败')
                        self.data.write_value(i, get_result_value(), 'pass')
                    else:
                        print("测试失败")
                        self.data.write_value(i, get_result_value(), 'fail')
            elif is_run == "YT":
                headers = {'Content-Type': 'application/json;charset=UTF-8', "token": get_token()}
                res = self.Runmain.run_main(method, url, data, headers=headers)
                logger.debug(f"响应结果：{res}")
                try:
                    if res['code'] == 200:
                        print('发送成功')
                        self.data.write_value(i, get_result_value(), 'pass')
                    else:
                        print('发送失败')
                        self.data.write_value(i, get_result_value(), 'fail')
                except:
                    if res in expect:
                        print('测试成功')
                        self.data.write_value(i, get_result_value(), 'pass')
                    else:
                        print('测试失败')
                        self.data.write_value(i, get_result_value(), 'fail')
            else:
                print("服务器繁忙，请联系管理员")
                self.data.write_value(i, get_result_value(), '用例阻塞')


if __name__ == '__main__':
    run = RunTestCase()
    run.go_run()
