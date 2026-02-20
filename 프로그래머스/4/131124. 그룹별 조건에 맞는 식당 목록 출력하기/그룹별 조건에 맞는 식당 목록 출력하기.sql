-- 코드를 입력하세요
SELECT profile.member_name, review.review_text, date_format(review.review_date, '%Y-%m-%d')
from member_profile as profile
join rest_review as review
on profile.member_id = review.member_id
where review.member_id = (select member_id from rest_review group by member_id order by count(review_score) desc limit 1)
order by review.review_date asc

