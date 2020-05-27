#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/27 17:23
# @Author : way
# @Site : 
# @Describe: 操作 hive , windows 下可能会有环境问题，参考 https://www.aitolearn.com/article/9a06a8e1ff5e4252aa2373eb3cc4fed8

from impala.dbapi import connect


class CtrlHive:

    def __init__(self, host, port):
        self.connection = connect(host=host, port=port, auth_mechanism='PLAIN')

    def __del__(self):
        self.connection.close()

    def execute(self, sql):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            try:
                rows = cursor.fetchall()
                return rows
            except:
                pass


if __name__ == "__main__":
    host = '172.16.122.20'
    port = 10000
    hv = CtrlHive(host, port)
    sql = "show databases"
    rows = hv.execute(sql)
    print(rows)
