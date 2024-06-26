with max_user as (
    select m.user_id, u.name
    from MovieRating as m
    inner join Users as u on
        m.user_id=u.user_id
    group by m.user_id
    order by count(m.rating) desc, u.name
    limit 1
), top_movie as (
    select m.title
    from MovieRating as r
    inner join Movies as m on
        r.movie_id=m.movie_id
    where year(r.created_at)=2020 and month(r.created_at)=2
    group by r.movie_id
    order by avg(r.rating) desc, m.title
    limit 1
)
select name as results
from max_user
union all
select title as results
from top_movie