-- 코드를 입력하세요
SELECT CAR_TYPE, count(*) as CARS
from car_rental_company_car
WHERE OPTIONS LIKE '%통풍시트%'
   OR OPTIONS LIKE '%열선시트%'
   OR OPTIONS LIKE '%가죽시트%'
group by car_type
order by car_type