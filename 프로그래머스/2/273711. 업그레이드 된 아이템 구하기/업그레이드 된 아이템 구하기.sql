select tree.ITEM_ID, info.ITEM_NAME, info.RARITY
from item_info as info
join item_tree as tree
on info.item_id = tree.item_id
where tree.parent_item_id in (select item_id from item_info where rarity = 'RARE')
order by info.ITEM_ID desc

