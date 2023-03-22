import os
import configparser


path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(path + '/config.ini')
config = configparser.ConfigParser()
config.read(config_path, encoding='utf-8')


class ReadConfig():
    def get_http(self, name):
        value = config.get('HTTP', name)
        return value

    def get_token(self, name):
        token = config.get("token", name)
        return token


if __name__ == '__main__':
    schema = ReadConfig().get_http("schema")
    schema_url = ReadConfig().get_http("schema_url")
    port = ReadConfig().get_http("port")
    url = schema + "://" + schema_url + ":" + port
    print('HTTP中的baseurl值为：', url)
