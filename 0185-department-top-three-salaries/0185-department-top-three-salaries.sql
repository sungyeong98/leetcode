with temp as (
    select
        name,
        salary,
        departmentId,
        dense_rank() over (partition by departmentId order by salary desc) as rk
    from Employee
)
select
    d.name as Department,
    t.name as Employee,
    t.salary as Salary
from temp t
inner join Department d on
    t.departmentId=d.id
where rk<=3