select customer_id
from (
    select 
        case
            when count(distinct product_key)=(select count(product_key) from Product)
                then customer_id 
        end as customer_id
    from Customer c
    group by customer_id
) temp
where customer_id is not null