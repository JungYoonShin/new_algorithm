-- 코드를 작성해주세요
select info.ITEM_ID, info.ITEM_NAME, info.RARITY
from item_tree as tree
join item_info as info
on tree.item_id = info.item_id
where tree.parent_item_id in (select item_id from item_info where rarity = 'RARE')
order by tree.item_id desc