add file /home/getway/explode_all.py;

with tt as (
select '肥仔，圆圆' as dt, '哈利，赫敏' as test
union all select '罗恩，邓布利多' as dt, '金妮，马尔福' as test
)
SELECT transform(dt, test)
USING 'python3 explode_all.py' AS (total)
FROM tt;