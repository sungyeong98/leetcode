with recursive temp as (
    select
        person_name,
        weight,
        turn
    from Queue
    where turn=1

    union all

    select
        q.person_name,
        t.weight+q.weight as weight,
        q.turn
    from temp t
    inner join Queue q on
        t.turn+1=q.turn
    where t.weight+q.weight<=1000
)
select person_name
from temp
order by weight desc
limit 1