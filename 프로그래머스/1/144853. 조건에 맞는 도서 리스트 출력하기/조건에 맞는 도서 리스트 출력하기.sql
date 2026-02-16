-- 코드를 입력하세요
SELECT BOOK_ID, date_format(PUBLISHED_DATE, '%Y-%m-%d') 
from book
where category = '인문' and YEAR(PUBLISHED_DATE) = 2021
order by PUBLISHED_DATE asc;