1.赋予执行权限

```shell
chmod 755 mapper.py
chmod 755 reducer.py
```

2.本地测试

```shell
echo ' ' |./mapper.py |sort|./reducer.py 

echo 'python c++ c java hive python sql sql c c++ c c java' |./mapper.py |sort|./reducer.py 
```

3.通过 hadoop-streaming 启动 map-reduce
>input 和 output 都是 hdfs 的文件和文件夹

```shell
hadoop jar /opt/cloudera/parcels/CDH/jars/hadoop-streaming-2.6.0-cdh5.16.1.jar \
-mapper /root/mapper.py \
-file /root/mapper.py \
-reducer /root/reducer.py \
-file /root/reducer.py \
-input /tmp/test.txt \
-output /tmp/out \
-numReduceTasks 1
```