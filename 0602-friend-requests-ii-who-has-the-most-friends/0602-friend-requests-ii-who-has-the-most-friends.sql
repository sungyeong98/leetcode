with q1 as (
    select
        requester_id as id,
        count(distinct accepter_id) as cnt1
    from RequestAccepted
    group by requester_id
), q2 as (
    select
        accepter_id as id,
        count(distinct requester_id) as cnt2
    from RequestAccepted
    group by accepter_id
), temp as (
    select id, cnt1
    from q1
    union all
    select id, cnt2
    from q2
)
select id, sum(cnt1) as num
from temp
group by id
order by sum(cnt1) desc
limit 1