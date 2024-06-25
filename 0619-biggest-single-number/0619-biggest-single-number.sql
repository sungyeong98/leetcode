select num
from (
    select coalesce(num,null) as num
    from MyNumbers
    group by num
    having count(num)=1
    order by num desc
) temp
union all
select null
where not exists (
    select 1
    from MyNumbers
    group by num
    having count(num)=1
)
limit 1