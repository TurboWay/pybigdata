add file /home/getway/sum_all.py;

with tt as (
select '1' as dt, '2' as test
union all select '1' as dt, '2' as test
union all select '1' as dt, '2' as test
union all select '1' as dt, '3' as test
)
SELECT transform(dt, test)
USING 'python3 sum_all.py' AS (total)
FROM tt;