select YEAR(DIFFERENTIATION_DATE) as YEAR, (
    select max(SIZE_OF_COLONY) from ecoli_data where YEAR(DIFFERENTIATION_DATE) = YEAR
) - SIZE_OF_COLONY as YEAR_DEV, ID
from ecoli_data
order by YEAR, YEAR_DEV
