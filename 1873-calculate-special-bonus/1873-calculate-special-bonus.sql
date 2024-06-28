select
    employee_id,
    case
        when substring(name,1,1)='M' or employee_id%2=0 then 0
        else salary
    end as bonus
from Employees
order by employee_id