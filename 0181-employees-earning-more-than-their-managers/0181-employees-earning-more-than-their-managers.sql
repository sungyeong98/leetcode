select name as 'Employee'
from Employee e1
where 
    managerId is not null and
    salary>(select salary from Employee e2 where e1.managerId=e2.id)