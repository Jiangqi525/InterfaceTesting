import requests
from common.readconfig import ReadConfig
import json


def get_token():
    url = eval(ReadConfig().get_token('url'))
    headers = json.loads(ReadConfig().get_token('headers'))
    data = json.loads(ReadConfig().get_token('data'))
    res = requests.post(url=url, headers=headers, json=data)
    token = res.json()['token']
    return token
