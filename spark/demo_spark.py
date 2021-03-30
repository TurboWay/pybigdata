#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/6/3 14:47
# @Author : way
# @Site : 
# @Describe: 操作 spark

from pyspark import SparkContext
from operator import add

# 每个程序只能有一个 SparkContext
sc = SparkContext("local", "test")
# sc = SparkContext("yarn", "test")   # 提交到 yarn 执行

words = sc.parallelize(
    ["scala",
     "java",
     "hadoop",
     "spark",
     "akka",
     "spark vs hadoop",
     "pyspark",
     "pyspark and spark"
     ])

# count
counts = words.count()
print("Number of elements in RDD -> %i" % counts)

# collect
coll = words.collect()
print("Elements in RDD -> %s" % coll)

# foreach
fore = words.foreach(lambda x: print(x) if 'spark' in x else ...)

# filter
words_filter = words.filter(lambda x: 'spark' in x)
filtered = words_filter.collect()
print("Fitered RDD -> %s" % (filtered))

# map
words_map = words.map(lambda x: 'hello ' + x)
mapping = words_map.collect()
print("Key value pair -> %s" % (mapping))

# reduce
nums = sc.parallelize([i for i in range(100)])
adding = nums.reduce(add)
print("Adding all the elements -> %i" % (adding))

# join
x = sc.parallelize([("spark", 1), ("hadoop", 4)])
y = sc.parallelize([("spark", 2), ("hadoop", 5)])
joined = x.join(y)
final = joined.collect()
print("Join RDD -> %s" % (final))
