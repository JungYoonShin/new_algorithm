# -- 코드를 입력하세요
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
from rest_info
where FAVORITES in (select max(FAVORITES) from rest_info group by food_type)
group by food_type
order by food_type desc;

# select *
# from rest_info;