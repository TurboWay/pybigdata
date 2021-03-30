#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/3 23:43
# @Author : way
# @Site : 
# @Describe: 根据 ，炸开所有字段

import sys

if __name__ == '__main__':
    for line in sys.stdin:
        cols = line.replace('\n', '').split('\t')
        for col in cols:
            for son in col.split('，'):
                sys.stdout.write(son + '\n')