#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/27 19:55
# @Author : way
# @Site : 
# @Describe: 操作 elasticsearch  官方文档 https://elasticsearch-py.readthedocs.io/en/master/

from elasticsearch import Elasticsearch

es = Elasticsearch(["127.0.0.1:9200"])

index_name = 'test'
type_name = 'human'

"""
print(es.ping())  # 测试es是否启动
print(es.info())  # 打印es信息
print(es.cluster.health())  # 打印集群健康信息
print(es.cluster.client.info())  # 当前节点信息
print(es.cat.indices())  # 索引信息 实例es的 cat 属性可以得到更多信息
"""

# 创建index  新增数据时，索引不存在时，也会被自动创建
response = es.indices.create(index=index_name, ignore=400)  # 已存在则ignore
print(response)

data = {'name': '肥仔', 'age': 28}

# 新增数据(指定id, id已存在则报错)
response = es.create(index=index_name, doc_type=type_name, body=data, id=1)
print(response)

# 新增数据(自动生成id)
response = es.index(index=index_name, doc_type=type_name, body=data)
print(response)

# 新增/修改数据(id存在则更新，不存在则新增)
response = es.index(index=index_name, doc_type=type_name, body=data, id=1)
print(response)

# 查指定index、type、id数据
response = es.get(index=index_name, doc_type=type_name, id=1)
print(response['_source'])

# 条件查询
query = {
    'query': {'match': {'age': 28}}
}
response = es.search(index=index_name, doc_type=type_name, body=query)
# response = es.search()   # 也可以不加任何条件..
print(response['hits'])

# 删除指定id数据
response = es.delete(index=index_name, doc_type=type_name, id=1, ignore=404)  # id不存在则ignore
print(response)

# 删除指定index、type下的所有数据
query_all = {'query': {'match_all': {}}}  # 查询所有数据
response = es.delete_by_query(index=index_name, doc_type=type_name, body=query_all, ignore=409)  # 查询为空则ignore
print(response)

# 删除index
response = es.indices.delete(index=index_name, ignore=404)  # 索引不存在则ignore
print(response)
