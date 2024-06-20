select
    s.student_id as student_id,
    s.student_name as student_name,
    sub.subject_name as subject_name,
    count(e.student_id) as attended_exams
from Students as s
cross join Subjects as sub
left join Examinations as e
    on s.student_id=e.student_id and
        sub.subject_name=e.subject_name
group by s.student_id, s.student_name, sub.subject_name
order by student_id, subject_name