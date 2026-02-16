-- 코드를 입력하세요
SELECT ROUND(sum(daily_fee) / count(*)) as AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
where car_type = 'SUV';