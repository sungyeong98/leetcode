with temp as(
    select i1.pid, i1.tiv_2016
    from Insurance i1
    where
        i1.tiv_2015 in (select i2.tiv_2015 from Insurance i2 where i1.pid!=i2.pid) and
        (i1.lat,i1.lon) not in (select i2.lat,i2.lon from Insurance i2 where i1.pid!=i2.pid)
)
select sum(tiv_2016) as tiv_2016 from temp