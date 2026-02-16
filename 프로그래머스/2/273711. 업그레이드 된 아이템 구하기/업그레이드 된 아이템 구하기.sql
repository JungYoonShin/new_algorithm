-- 코드를 작성해주세요
select b.item_id as ITEM_ID, a.item_name as ITEM_NAME, a.RARITY
from ITEM_INFO as a
join ITEM_TREE as b
on a.item_id = b.item_id
where b.parent_item_id in (
    select item_id
    from item_info
    where rarity = 'RARE'
)
order by a.item_id desc
