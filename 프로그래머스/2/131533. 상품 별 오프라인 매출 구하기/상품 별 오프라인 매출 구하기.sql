-- 코드를 입력하세요
SELECT pd.PRODUCT_CODE, sum(sale.SALES_AMOUNT) * pd.PRICE as SALES
from product as pd
join offline_sale as sale
on pd.product_id = sale.product_id
group by pd.product_code
order by SALES desc, pd.PRODUCT_CODE