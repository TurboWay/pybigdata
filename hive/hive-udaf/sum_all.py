#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/3 23:31
# @Author : way
# @Site : 
# @Describe: 对所有列求和

import sys

if __name__ == '__main__':
    total = 0
    for line in sys.stdin:
        cols = line.split('\t')
        total += sum([int(col) for col in cols])
    sys.stdout.write(str(total) + '\n')