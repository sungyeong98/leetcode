with temp as (
    select 
        p.product_id,
        p.price*u.units as Price
    from Prices as p
    cross join UnitsSold as u on 
        p.product_id=u.product_id and
        u.purchase_date between p.start_date and p.end_date
), temp1 as (
    select
        product_id,
        sum(Price) as sum_price
    from temp
    group by product_id
), cnt as (
    select
        product_id,
        sum(units) as cnt
    from UnitsSold
    group by product_id
)
select
    t.product_id as product_id,
    round(sum_price/cnt,2) as average_price
from temp1 as t, cnt as c
where t.product_id=c.product_id