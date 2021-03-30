#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/27 14:24
# @Author : way
# @Site : 
# @Describe:

import json
from kafka import KafkaProducer
from random import choice

servers = ['172.16.122.17:9092', ]
producer = KafkaProducer(bootstrap_servers=servers,
                         key_serializer=lambda m: m.encode('utf-8'),
                         value_serializer=lambda m: json.dumps(m).encode('utf-8'))
topic = 'test'
key = 'hi'
value = 'way'
partitions = producer.partitions_for(topic) # 获取所有分区，均匀地写到分区中
for i in range(10000):
    producer.send(topic=topic, partition=choice(list(partitions)), key=key, value=value).get(timeout=10)
