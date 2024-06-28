select u.name, ifnull(t.dis,0) as travelled_distance
from (
    select user_id, sum(distance) as dis
    from Rides
    group by user_id
) t
right join Users u on
    t.user_id=u.id
order by travelled_distance desc, name