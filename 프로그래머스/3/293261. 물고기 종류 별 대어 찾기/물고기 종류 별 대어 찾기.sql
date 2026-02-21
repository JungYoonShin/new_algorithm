select info.ID, name.FISH_NAME, info.length as LENGTH
from fish_info as info
join fish_name_info as name
on info.fish_type = name.fish_type
where (info.fish_type, info.length) in (select fish_type, max(length) from fish_info group by fish_type)
order by info.id
