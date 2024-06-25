with temp1 as (
    select employee_id, department_id
    from Employee
    where primary_flag='Y'
), temp2 as (
    select employee_id, department_id
    from Employee
    group by employee_id
    having count(employee_id)=1
)
select *
from temp1
union all
select *
from temp2