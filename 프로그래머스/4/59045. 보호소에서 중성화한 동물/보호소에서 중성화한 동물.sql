-- 코드를 입력하세요
SELECT ins.animal_id, ins.animal_type, ins.name
from animal_ins as ins
join animal_outs as outs
on ins.animal_id = outs.animal_id
where ins.sex_upon_intake IN ('Intact Male', 'Intact Female') and outs.SEX_UPON_OUTCOME IN ('Neutered Male', 'Spayed Female')