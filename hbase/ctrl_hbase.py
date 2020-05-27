#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/27 10:29
# @Author : way
# @Site : 
# @Describe: 操作 hbase

import happybase


class CtrlHbase:

    def __init__(self, host, port):
        self.connection = happybase.Connection(host=host, port=port, timeout=120000)  # 默认2分钟超时

    def __del__(self):
        self.connection.close()

    @property
    def tables(self):
        """
        :return: 所有表名
        """
        return [tb.decode() for tb in self.connection.tables()]

    def create_table(self, name, families):
        """
        :param name:  表名
        :param families:  列族 {'cf':dict(),'cf2':dict(),}
        :return:
        """
        self.connection.create_table(name, families)

    def delete_table(self, name, disable=True):
        self.connection.delete_table(name, disable)

    def enable_table(self, name):
        self.connection.enable_table(name)

    def disable_table(self, name):
        self.connection.disable_table(name)

    def is_table_enabled(self, name):
        return self.connection.is_table_enabled(name)

    def insert_many(self, name, items):
        """
        :param name: 表名
        :param items:  [(keyid, {'cf:key1': 'value1', 'cf:key2': 'value2'}),]
        :return:
        """
        table = self.connection.table(name)
        bat = table.batch()
        for item in items:
            bat.put(*item)
        bat.send()

    def insert(self, name, item):
        """
        :param name: 表名
        :param item:  (keyid, {'cf:key1': 'value1', 'cf:key2': 'value2'})
        :return:
        """
        table = self.connection.table(name)
        table.put(*item)

    def delete(self, name, keyid):
        """
        :param name: 表名
        :param keyid:
        :return:
        """
        table = self.connection.table(name)
        table.delete(keyid)

    def read(self, name, **kwargs):
        """
        :param name: 表名
        :param kwargs:
        :return:
        """
        table = self.connection.table(name)
        rows = table.scan(**kwargs)
        return rows


if __name__ == "__main__":
    HBASE_HOST = '172.16.122.21'
    HBASE_PORT = 9090
    hb = CtrlHbase(host=HBASE_HOST, port=HBASE_PORT)
    print(hb.tables)  # 打印所有表

    # tbname = 'test'
    # hb.create_table(tbname, {'cf': dict()})  # 新建表

    # item = ('row1', {'cf:name': 'test', 'cf:age': '0'})
    # hb.insert(tbname, item)   # 写入单条记录

    # items = [
    #     ('row1', {'cf:name': 'way', 'cf:age': '29'}),
    #     ('row2', {'cf:name': 'mutou', 'cf:age': '28'}),
    # ]
    # hb.insert_many(tbname, items)  # 写入多条记录

    # rows = hb.read(tbname)  # 读取记录
    # for row in rows:
    #     keyid = row[0].decode()
    #     value = {key.decode(): value.decode() for key, value in row[1].items()}
    #     print(keyid, value)

    # hb.delete(tbname, 'row1') # 删除记录

    # hb.delete_table(tbname)   # 删除表
