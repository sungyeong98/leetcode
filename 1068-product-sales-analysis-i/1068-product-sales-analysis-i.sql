select
    product_name, year, price
from Sales
join Product using(product_id)