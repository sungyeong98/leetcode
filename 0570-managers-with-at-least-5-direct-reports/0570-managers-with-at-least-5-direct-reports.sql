with count_num as (
    select managerId
    from Employee
    group by managerId
    having count(managerId)>=5
)
select name
from Employee
where id in (select * from count_num)