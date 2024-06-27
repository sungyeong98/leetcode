with temp as (
    select 
        request_at,
        case when status='completed' then 0 else 1 end as status
    from Trips
    where 
        client_id not in (select users_id from Users where banned='Yes') and
        driver_id not in (select users_id from Users where banned='Yes') and
        request_at between "2013-10-01" and "2013-10-03"
)
select
    request_at as Day,
    round(sum(status)/count(status),2) as 'Cancellation Rate'
from temp
group by request_at