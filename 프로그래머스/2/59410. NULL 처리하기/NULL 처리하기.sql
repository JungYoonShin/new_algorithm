-- 코드를 입력하세요
SELECT ANIMAL_TYPE, (
    case when name is null then "No name" ELSE name end
) as "NAME", SEX_UPON_INTAKE
from animal_ins
order by animal_id 