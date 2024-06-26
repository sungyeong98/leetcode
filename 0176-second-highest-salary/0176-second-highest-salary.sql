select
    ifnull(
            (
                select
                    salary
                from (
                    select distinct
                        salary,
                        dense_rank() over (order by salary desc) as rk
                    from Employee
                ) temp
                where rk=2
            ),
    null) as SecondHighestSalary 