add file hdfs:/user/hive/udf/dateformatUDF.py;

with tt as (
select '20181025' as dt, '测试1' as test
union all select '2018-10-25' as dt, '测试2' as test
union all select '26/10/2018' as dt, '测试3' as test
union all select '2018.10.25' as dt, '测试4' as test
union all select '二零一八年十月二十五日' as dt, '测试5'  as test
union all select '二〇一八年十月二十五日' as dt, '测试6'  as test
union all select '201810' as dt, '测试7' as test
union all select '2018-10' as dt, '测试8' as test
union all select '10/2018' as dt, '测试9' as test
union all select '2018.10' as dt, '测试10' as test
union all select '二零一八年十月' as dt, '测试11' as  test
union all select '二〇一八年十月' as dt, '测试12' as  test
union all select '不合法输入' as dt, '测试13' as test
union all select '2018.10.32' as dt, '测试14' as test
union all select '2018-02-29' as dt, '测试15' as test
union all select '32/10/2018' as dt, '测试16' as test
union all select '二零一八年十月三十二日' as dt, '测试17' as test
union all select '13/2018' as dt, '测试18' as test
union all select '2018-13' as dt, '测试19' as test
union all select '二零一八年十三月' as dt, '测试20' as  test
union all select '二〇一八年' as dt, '测试21' as test
union all select '二零一八' as dt, '测试22' as test
union all select '2018' as dt, '测试23' as test
union all select '' as dt, '测试24' as test
union all select NULL as dt, '测试25' as test
union all select '00050203' as dt, '测试26' as test
union all select '2018-11-19 19:13:51' as dt, '测试27'  as test
union all select '2018-1-15' as dt, '测试28' as test
union all select '2018-7-9' as dt, '测试29' as test
union all select '18.5.6' as dt, '测试30' as test
union all select '69.12.6' as dt, '测试31' as test
union all select '201111' as dt, '测试32' as test
union all select '195901' as dt, '测试33' as test
union all select '170203' as dt, '测试34' as test
union all select '560203' as dt, '测试35' as test
union all select '2018年11月28日' as dt, '测试36' as  test
union all select '2018年11月' as dt, '测试37' as test
union all select '2018年11月28' as dt, '测试38' as test
union all select '2018年11' as dt, '测试39' as test
union all select '2018年13月' as dt, '测试40' as test
)
SELECT transform(dt, concat('UDF',dt), test)
USING 'python3 dateformatUDF.py' AS (dt, newdt, test)
FROM tt;