with temp as (
    select
        customer_id, 
        min(order_date) as date1, 
        min(customer_pref_delivery_date) as date2
    from Delivery
    group by customer_id
)
select
    round(sum(if(date1=date2,1,0))/count(customer_id)*100,2) as immediate_percentage
from temp