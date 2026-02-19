-- 코드를 입력하세요
SELECT outs.ANIMAL_ID, outs.NAME
from animal_ins as ins
right outer join animal_outs as outs
on ins.animal_id = outs.animal_id
where outs.animal_id not in (select animal_id from animal_ins)
