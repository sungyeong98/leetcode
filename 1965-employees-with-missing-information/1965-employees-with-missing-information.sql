with temp1 as (
    select employee_id
    from Employees
    where employee_id not in (select employee_id from Salaries)
), temp2 as (
    select employee_id
    from Salaries
    where employee_id not in (select employee_id from Employees)
)
select employee_id
from temp1
union
select employee_id
from temp2
order by employee_id