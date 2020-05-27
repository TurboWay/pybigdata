#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/27 13:38
# @Author : way
# @Site : 
# @Describe: 操作 impala

from impala.dbapi import connect


class CtrlImpala:

    def __init__(self, host, port):
        self.connection = connect(host=host, port=port)

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
    port = 25004
    im = CtrlImpala(host, port)
    sql = "show databases;"
    rows = im.execute(sql)
    print(rows)
