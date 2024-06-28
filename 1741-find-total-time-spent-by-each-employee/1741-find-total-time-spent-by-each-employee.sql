select
    event_day as 'day',
    emp_id,
    sum(time) as total_time
from (
    select emp_id, event_day, out_time-in_time as 'time'
    from Employees
) t
group by event_day, emp_id