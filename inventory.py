#program     : make_grid.py
#chapterNo   : 4.10.2
#description : 引数としてxy座標で文字で絵を描くリストを渡し、関数で描画する
#makeDate    : 2019/06/04

def display_inventory(inventory):
    print('持ち物リスト:')
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total += v
    print('アイテム総数: ' + str(item_total))
    
    
stuff = {'ロープ': 1, 'たいまつ': 6, '金貨': 42, '手裏剣': 1, '矢': 12}
display_inventory(stuff)