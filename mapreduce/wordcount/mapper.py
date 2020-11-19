#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/19 14:59
# @Author : way
# @Site : 
# @Describe:

import sys

for line in sys.stdin:
    for word in line.strip().split():
        print(word + '\t' + '1')