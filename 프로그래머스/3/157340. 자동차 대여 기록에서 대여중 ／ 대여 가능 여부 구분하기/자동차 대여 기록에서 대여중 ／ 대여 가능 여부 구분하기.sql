-- 코드를 입력하세요
SELECT CAR_ID, (
    case when car_id in (select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY where start_date <= '2022-10-16'  and
                       '2022-10-16' <= end_date) THEN '대여중' ELSE '대여 가능' END
) as AVALIABLITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
order by car_id desc