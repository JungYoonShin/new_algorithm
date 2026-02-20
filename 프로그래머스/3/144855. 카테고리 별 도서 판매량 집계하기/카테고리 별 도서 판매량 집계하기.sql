-- 코드를 입력하세요
SELECT category, sum(sales) as TOTAL_SALES
from book
join book_sales
on book.book_id = book_sales.book_id
where YEAR(book_sales.SALES_DATE) = '2022' and MONTH(book_sales.SALES_DATE) = '1'
group by category 
order by category