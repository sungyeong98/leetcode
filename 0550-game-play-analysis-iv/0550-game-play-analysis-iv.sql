with temp as (
    select
        player_id,
        event_date,
        row_number() over (partition by player_id order by event_date) as rn
    from Activity
), temp1 as (
    select
        player_id,
        max(case when rn=1 then event_date end) as first_val,
        max(case when rn=2 then event_date end) as second_val
    from temp
    where rn<=2
    group by player_id
)
select
    round(sum(if(second_val is not null and datediff(second_val,first_val)=1,1,0)) /count(player_id) , 2) as fraction
from temp1