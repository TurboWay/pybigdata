#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/19 14:59
# @Author : way
# @Site : 
# @Describe:

import sys

cur_word = None
cur_count = 0

for line in sys.stdin:
    word, count = line.strip().split('\t', 1)
    count = int(count)
    if cur_word == word:
        cur_count += count
    else:
        if cur_word:
            print(cur_word + '\t' + str(cur_count))
        cur_word = word
        cur_count = count

# 最后一个
if cur_word:
    print(cur_word + '\t' + str(cur_count))
