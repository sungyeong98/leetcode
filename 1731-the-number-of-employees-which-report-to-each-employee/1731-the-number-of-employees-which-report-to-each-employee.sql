with temp as (
    select
        reports_to as id,
        count(reports_to) as cnt,
        round(avg(age)) as age
    from Employees
    group by reports_to
    having reports_to is not null
)
select 
    t.id as employee_id,
    e.name,
    t.cnt as reports_count,
    t.age as average_age
from temp as t
inner join Employees as e on
    t.id=e.employee_id
order by employee_id