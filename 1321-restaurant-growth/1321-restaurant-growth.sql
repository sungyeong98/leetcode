with temp as (
    select distinct
        c2.visited_on
    from Customer c1
    inner join Customer c2 on
        datediff(c2.visited_on,c1.visited_on)=6
)
select
    t.visited_on,
    (select sum(amount) from Customer c where c.visited_on<=t.visited_on and datediff(t.visited_on,c.visited_on)<=6) as amount,
    round((select sum(amount) from Customer c where c.visited_on<=t.visited_on and datediff(t.visited_on,c.visited_on)<=6)/7,2) as average_amount
from temp t