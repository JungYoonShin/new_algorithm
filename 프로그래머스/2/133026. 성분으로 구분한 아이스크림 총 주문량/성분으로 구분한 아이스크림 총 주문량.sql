-- 코드를 입력하세요
SELECT INGREDIENT_TYPE, sum(total_order) as TOTAL_ORDER
from FIRST_HALF as a
join icecream_info as b
on a.flavor = b.flavor
group by INGREDIENT_TYPE