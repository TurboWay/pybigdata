#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/27 14:30
# @Author : way
# @Site : 
# @Describe:

import json
from kafka import KafkaConsumer

servers = ['172.16.122.17:9092', ]
consumer = KafkaConsumer(bootstrap_servers=servers,
                         auto_offset_reset='earliest', # 重置偏移量 earliest移到最早的可用消息，latest最新的消息，默认为latest
                         key_deserializer=lambda m: m.decode('utf-8'),
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))
consumer.subscribe(topics=['test', ])
for msg in consumer:
    print(msg.key, msg.value)
