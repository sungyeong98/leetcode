with temp as (
    select
        *,
        id-row_number() over (order by id) as num
    from Stadium
    where people>=100
), temp1 as (
    select
        *,
        count(*) over (partition by num) as cnt
    from temp
)
select id, visit_date, people
from temp1
where cnt>=3
order by visit_date