-- 코드를 입력하세요
SELECT YEAR(sales_date) as YEAR, MONTH(sales_date) as MONTH, COUNT(DISTINCT sale.user_id) as PURCHASED_USERS , round(COUNT(DISTINCT sale.user_id) / (
    select count(*) from user_info where YEAR(joined) = '2021'
), 1) as PUCHASED_RATIO
from USER_INFO as info
join ONLINE_SALE as sale
on info.user_id = sale.user_id
where YEAR(joined) = '2021'
group by YEAR(sales_date), MONTH(sales_date)
order by YEAR(sales_date), MONTH(sales_date)