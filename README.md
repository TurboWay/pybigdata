# pybigdata
![](https://img.shields.io/badge/python-3.6%2B-brightgreen)

做大数据应用需要学习什么编程语言，一定要学 java 吗，不，python 也是一个很好的选择

所以，一起用 python 来玩转大数据吧



# install

```shell
pip install -r requirements.txt
pip install --no-deps thrift-sasl==0.2.1
```



# list

| 大数据组件    |  python 操作示例 | 文档 |
| ------------- | ------------ | --------------- |
| hadoop        |  [ctrl_hdfs.py](hadoop/ctrl_hdfs.py)             | [hdfs](https://hdfscli.readthedocs.io/en/latest/) |
| hadoop-mapreduce        |  [mapreduce](hadoop/mapreduce/wordcount)             | [mapreduce.md](hadoop/mapreduce/wordcount/wordcount.md)    |
| hive          |  [ctrl_hive.py](hive/ctrl_hive.py) <br> [一进一出 udf](hive/hive-udf) <br> [多进一出 udaf](hive/hive-udaf) <br> [一进多出 udtf](hive/hive-udtf)             | [impyla](https://github.com/cloudera/impyla)                |
| impala        |  [ctrl_impala.py](impala/ctrl_impala.py)            | [impyla](https://github.com/cloudera/impyla) |
| hbase         |  [ctrl_hbase.py](hbase/ctrl_hbase.py)             | [happybase](https://happybase.readthedocs.io/en/latest/user.html#retrieving-data) |
| kafka         |  [demo_producer.py](kafka/demo_producer.py) <br> [demo_consumer.py](kafka/demo_consumer.py)        | [kafka](https://kafka-python.readthedocs.io/en/master/) |
| elasticsearch |  [ctrl_elasticsearch.py](elasticsearch/ctrl_elasticsearch.py)              | [elasticsearch](https://elasticsearch-py.readthedocs.io/en/7.7.1/) |
| spark         |  [demo_spark.py](spark/demo_spark.py)              | [spark](http://spark.apache.org/examples.html)                |
| flink         |  [flink-sql](flink/flink-sql)           |  [flink 实践系列2-flinksql](http://blog.turboway.top/article/flinksql/)                |
