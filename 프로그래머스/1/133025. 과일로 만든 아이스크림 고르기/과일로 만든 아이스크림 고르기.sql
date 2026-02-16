-- 코드를 입력하세요
SELECT a.FLAVOR
from ICECREAM_INFO as a
join FIRST_HALF as b
on a.flavor = b.flavor
where b.total_order > 3000 and  a.ingredient_type = 'fruit_based'
order by b.total_order desc