#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/1/10 10:24
# @Author : way
# @Site :
# @Describe: doris 数据导入

from DorisClient import DorisSession, DorisLogger, Logger

# DorisLogger.setLevel('ERROR')  # default:INFO

doris_cfg = {
    'fe_servers': ['10.211.7.131:8030', '10.211.7.132:8030', '10.211.7.133:8030'],
    'database': 'testdb',
    'user': 'test',
    'passwd': '123456',
}
doris = DorisSession(**doris_cfg)

# append
data = [
    {'id': '1', 'shop_code': 'sdd1', 'sale_amount': '99'},
    {'id': '2', 'shop_code': 'sdd2', 'sale_amount': '5'},
    {'id': '3', 'shop_code': 'sdd3', 'sale_amount': '3'},
]
doris.streamload('streamload_test', data)

# delete
data = [
    {'id': '1'},
]
doris.streamload('streamload_test', data, merge_type='DELETE')

# merge
data = [
    {'id': '10', 'shop_code': 'sdd1', 'sale_amount': '99', 'delete_flag': 0},
    {'id': '2', 'shop_code': 'sdd2', 'sale_amount': '5', 'delete_flag': 1},
    {'id': '3', 'shop_code': 'sdd3', 'sale_amount': '3', 'delete_flag': 1},
]
doris.streamload('streamload_test', data, merge_type='MERGE', delete='delete_flag=1')

# Sequence append
data = [
    {'id': '1', 'shop_code': 'sdd1', 'sale_amount': '99', 'source_sequence': 11, },
    {'id': '1', 'shop_code': 'sdd2', 'sale_amount': '5', 'source_sequence': 2},
    {'id': '2', 'shop_code': 'sdd3', 'sale_amount': '3', 'source_sequence': 1},
]
doris.streamload('streamload_test', data, sequence_col='source_sequence')

# Sequence merge
data = [
    {'id': '1', 'shop_code': 'sdd1', 'sale_amount': '99', 'source_sequence': 100, 'delete_flag': 0},
    {'id': '1', 'shop_code': 'sdd2', 'sale_amount': '5', 'source_sequence': 120, 'delete_flag': 0},
    {'id': '2', 'shop_code': 'sdd3', 'sale_amount': '3', 'source_sequence': 100, 'delete_flag': 1},
]
doris.streamload('streamload_test', data, sequence_col='source_sequence', merge_type='MERGE',
                 delete='delete_flag=1')


# streamload default retry config:  max_retry=3, retry_diff_seconds=3
# if you don't want to retry, "_streamload" can help you
doris._streamload('streamload_test', data)

# if you want to changed retry config, follow code will work
from DorisClient import DorisSession, Retry

max_retry = 5
retry_diff_seconds = 10


class MyDoris(DorisSession):

    @Retry(max_retry=max_retry, retry_diff_seconds=retry_diff_seconds)
    def streamload(self, table, dict_array, **kwargs):
        return self._streamload(table, dict_array, **kwargs)


doris = MyDoris(**doris_cfg)
doris.streamload('streamload_test', data)
