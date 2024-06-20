select
    b.id
from Weather as a, Weather as b
where 
    datediff(b.recordDate, a.recordDate)=1 and
    b.temperature>a.temperature