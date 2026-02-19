# -- 코드를 입력하세요
SELECT pf.MEMBER_NAME, review.REVIEW_TEXT, date_format(review.REVIEW_DATE, "%Y-%m-%d") as REVIEW_DATE
from member_profile as pf
join rest_review as review
on pf.member_id = review.member_id
where pf.member_id = (select member_id from rest_review group by member_id order by count(review_score) desc limit 1)
ORDER BY REVIEW_DATE, REVIEW_TEXT
