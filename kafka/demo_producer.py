#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/27 14:24
# @Author : way
# @Site : 
# @Describe:

import json
from kafka import KafkaProducer

servers = ['172.16.122.17:9092', ]
producer = KafkaProducer(bootstrap_servers=servers,
                         key_serializer=lambda m: m.encode('utf-8'),
                         value_serializer=lambda m: json.dumps(m).encode('utf-8'))
topic = 'test'
key = 'hi'
value = 'way'
producer.send(topic=topic, key=key, value=value).get(timeout=10)
