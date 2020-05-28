import json
import requests
from typing import Union  # 支持函数传参或返值多种类型

from setting import ENVDICT


class XCBResponse:
    def __init__(self, resp: requests.Response):
        self.status_code = resp.status_code
        j = resp.json()
        self.code = j['code']
        self.msg = j['message']
        if self.code == 0 and 'data' in j:
            self.data = j['data']
            #self.data = json.loads(self.data)


class XCBRequest:
    def __init__(self, env: str):
        """
        :param env: 请求环境
        """
        env_dict = ENVDICT
        if env_dict.get(env):
            pass
        else:
            env = 'test'
        self.ip = env_dict[env]['ip']

    def change_env(self, d: dict):
        if d.get('ip'):
            self.ip = d.get('ip')

    def put(self, api: str, data=None, headers=None):
        """
        :param api: 接口地址
        :param data: 请求参数
        :return: 接口返回json数据
        """
        # url 参数
        url = self.ip + api
        # params = {
        #     'data': data
        # }
        # 保持登录状态
        r = requests.put(url, json=data, headers=headers)
        return XCBResponse(r)

    def get(self, api: str, data=None, headers=None):
        """
        :param api: 接口地址
        :param data: 请求参数
        :return: 接口返回json数据
        """
        url = self.ip + api
        # params = {
        #     'data': data
        # }
        # 保持登录状态
        r = requests.get(url, params=data, headers=headers)
        return XCBResponse(r)

    def post(self, api: str, data=None, headers=None):
        """
        :param api: 接口地址
        :param data: 请求参数
        :return: 接口返回json数据
        """
        url = self.ip + api
        # params = {
        #     'data': data
        # }
        # 保持登录状态
        r = requests.post(url, json=data, headers=headers)
        return XCBResponse(r)

    def delete(self, api: str, data=None, headers=None):
        """
        :param api: 接口地址
        :param data: 请求参数
        :return: 接口返回json数据
        """
        url = self.ip + api
        # params = {
        #     'data': data
        # }
        # 保持登录状态
        r = requests.delete(url, json=data, headers=headers)
        return XCBResponse(r)
