import requests
import json


class RunMain():
    def send_get(self, url, data, headers):
        try:
            r = requests.get(url, params=data, headers=headers)
            r.encoding = 'utf-8'
            json_r = r.json()
            print("Test执行结果：", json_r)
            return json_r
        except BaseException as e:
            print("请求失败！", str(e))

    def send_post(self, url, data, headers):
        try:
            data = json.dumps(data)
            r = requests.post(url, data=data, headers=headers)
            r.encoding = 'utf-8'
            json_r = r.json()
            print("Test执行结果：", json_r)
            return json_r
        except BaseException as e:
            print("请求失败！", str(e))

    def run_main(self, method, url, data, headers):
        result = None
        if method == 'get':
            result = self.send_get(url, data, headers)
        elif method == 'post':
            result = self.send_post(url, data, headers)
        else:
            print("method值错误！！！")
        return result


if __name__ == '__main__':
    result1 = RunMain().run_main('post', 'http://139.186.xxx.xx:8080/login',
                                 {"username": "admin", "password": "xxx"},
                                 {"Content-Type": "application/json;charset=UTF-8"})
    print(result1)
