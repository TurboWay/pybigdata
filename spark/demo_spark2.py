#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/4/14 9:25
# @Author : way
# @Site : 
# @Describe:

import os
from datetime import datetime, date
import pandas as pd
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession, Row

spark = SparkSession\
.builder \
.appName('test') \
.enableHiveSupport() \
.getOrCreate()

df = spark.createDataFrame([
    ['red', 'banana', 1, 10], ['blue', 'banana', 2, 20], ['red', 'carrot', 3, 30],
    ['blue', 'grape', 4, 40], ['red', 'carrot', 5, 50], ['black', 'carrot', 6, 60],
    ['red', 'banana', 7, 70], ['red', 'grape', 8, 80]], schema=['color', 'fruit', 'v1', 'v2'])
df.show()
df.write.csv('hdfs://nameservice1/user/foo.csv')
spark.read.csv('hdfs://nameservice1/user/foo.csv').show()



