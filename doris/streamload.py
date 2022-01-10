#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/1/10 10:24
# @Author : way
# @Site : 
# @Describe: doris 数据导入

import base64
import json
from requests import Session

"""
支持两种格式数据导入，json/csv(默认\t \n)
curl -u user:pwd -T test.csv --retry-delay 1 --retry 20 --location-trusted http://127.0.0.1:8030/api/database/table/_stream_load
"""


class DorisSession:

    def __init__(self, host, port, database, table, user, pwd):
        self.Authorization = base64.b64encode((user + ':' + pwd).encode('utf-8')).decode('utf-8')
        self.url = f'http://{host}:{port}/api/{database}/{table}/_stream_load'
        self.sesson = Session()
        self.sesson.headers = {
            'Expect': '100-continue',
            'Authorization': 'Basic ' + self.Authorization,
            'format': 'json',
        }

    def send(self, data, url=None):
        if url is None:
            url = self.url
        response = self.sesson.put(url, data, allow_redirects=False)
        if response.status_code == 307:
            url = response.headers['Location']
            self.send(data, url)
        elif response.status_code == 200:
            res = response.json()
            if res['Status'] == 'Success':
                return True
            else:
                print(f"fail: {res['Message']}")
                return False
        else:
            print(f"error: {response.text}")
            return False


if __name__ == "__main__":
    doris = DorisSession(
        host='',
        port=8030,
        database='',
        table='',
        user='',
        pwd=''
    )
    json_data = {
        'dateid': '20211014', 'shop_code': 'sdd', 'sale_amount': '1'
    }
    json_data = json.dumps(json_data)
    doris.send(json_data)

