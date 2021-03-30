#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/5/27 14:48
# @Author : way
# @Site : 
# @Describe:  操作 hdfs

from hdfs import Client

HDFS_ClIENT = "http://172.16.122.21:50070;http://172.16.122.24:50070"

file_dir = '/tmp/way'
file_name = '/tmp/way/test.txt'
file_name2 = '/tmp/way/test123.txt'
loacl_file_name = 'test.txt'

client = Client(HDFS_ClIENT)

# 创建文件夹
client.makedirs(file_dir)

# 返回目标信息
info = client.status(file_name, strict=False)
print(info)

# 写入文件(覆盖)
client.write(file_name, data="hello hdfs !", overwrite=True)

# 写入文件(追加)
client.write(file_name, data="hello way !", overwrite=False, append=True)

# 读取文件内容
with client.read(file_name, encoding='utf-8') as f:
    print(f.read())

# 文件下载
client.download(file_name, loacl_file_name, overwrite=True)

# 文件上传
client.upload(file_name + '111', loacl_file_name, cleanup=True)

# 删除文件
client.delete(file_name2)

# 文件重命名
client.rename(file_name, file_name2)

# 文件夹底下文件
files = client.list(file_dir, status=False)
for file in files:
    print(file)

# 删除文件夹(递归删除、谨慎)
# client.delete(file_dir, recursive=True)
