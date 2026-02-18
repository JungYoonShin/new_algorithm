-- 코드를 작성해주세요
select YEAR(data.DIFFERENTIATION_DATE) as YEAR, 
(select max(size_of_colony) from ecoli_data where YEAR(DIFFERENTIATION_DATE) = YEAR(data.DIFFERENTIATION_DATE)) - size_of_colony as YEAR_DEV, ID
from ECOLI_DATA as data
order by YEAR asc, YEAR_DEV asc