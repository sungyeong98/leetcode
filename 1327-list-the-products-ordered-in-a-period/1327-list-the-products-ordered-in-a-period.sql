with temp as (
    select
        product_id,
        sum(unit) as sum_num
    from Orders
    where year(order_date)=2020 and month(order_date)=2
    group by product_id
)
select
    p.product_name,
    t.sum_num as unit
from temp as t
inner join Products as p on
    t.product_id=p.product_id
where t.sum_num>=100