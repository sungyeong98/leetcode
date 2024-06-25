with temp as (
    select
        product_id,
        min(year) as year
    from Sales
    group by product_id
)
select
    t.product_id,
    t.year as first_year,
    s.quantity,
    s.price
from temp as t
inner join Sales as s on
    t.product_id=s.product_id and
    t.year=s.year