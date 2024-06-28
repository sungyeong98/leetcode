with target_order as (
    select buyer_id, count(buyer_id) as cnt
    from Orders
    where year(order_date)=2019
    group by buyer_id
)
select
    u.user_id as buyer_id,
    u.join_date,
    ifnull(t.cnt,0) as orders_in_2019
from target_order as t
right join Users as u on
    t.buyer_id=u.user_id