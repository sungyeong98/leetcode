with not_target as (
    select product_id
    from Sales
    where sale_date<'2019-01-01' or sale_date>'2019-03-31'
), target as (
    select product_id
    from Sales
    where sale_date between '2019-01-01' and '2019-03-31'
)
select product_id, product_name
from Product
where 
    product_id not in (select distinct product_id from not_target) and
    product_id in (select product_id from target)