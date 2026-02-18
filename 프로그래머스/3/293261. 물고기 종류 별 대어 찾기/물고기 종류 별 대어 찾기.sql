-- 코드를 작성해주세요
select ID, FISH_NAME, LENGTH
from FISH_INFO as info
join fish_name_info as name
on name.fish_type = info.fish_type
where (info.fish_type, info.length) in (select fish_type, max(length) from fish_info group by fish_type)