-- 코드를 입력하세요
SELECT BOOK_ID, AUTHOR_NAME, date_format(PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
from book 
join author
on book.author_id = author.author_id
where book.category = '경제'
order by PUBLISHED_DATE