-- 코드를 입력하세요
SELECT product.PRODUCT_ID, product.PRODUCT_NAME, sum(orders.amount) * product.price as TOTAL_SALES
from food_product as product
join food_order as orders
on product.product_id = orders.product_id
where YEAR(orders.produce_date) = 2022 and MONTH(orders.produce_date) = 5
group by product_id
order by TOTAL_SALES desc, product.product_id