-- 코드를 작성해주세요
select YEAR(DIFFERENTIATION_DATE) as YEAR, 
(select max(size_of_colony) from ecoli_data where YEAR(DIFFERENTIATION_DATE) = YEAR) - size_of_colony as YEAR_DEV, ID
from ecoli_data as d
order by YEAR asc, YEAR_DEV asc

