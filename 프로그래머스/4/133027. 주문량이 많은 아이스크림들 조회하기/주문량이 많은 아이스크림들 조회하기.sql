-- 코드를 입력하세요
SELECT july.FLAVOR
from first_half as half
join july
on half.flavor = july.flavor
group by july.flavor
order by sum(july.total_order) + half.total_order desc
limit 3;