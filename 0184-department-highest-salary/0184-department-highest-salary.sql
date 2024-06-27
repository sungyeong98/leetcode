with temp as (
    select
        d.name as Department, 
        e.name as Employee,
        e.salary as Salary,
        rank() over (partition by departmentId order by salary desc) as rk 
    from Employee e
    inner join Department d on e.departmentId=d.id
)
select Department, Employee, Salary
from temp
where rk=1