#program     : inventory.py
#chapterNo   : 5.6.1
#description : 持ち物リストを引数として、各アイテムの数と全アイテムの総数を表示する
#makeDate    : 2019/06/09

def display_inventory(inventory):
    print('持ち物リスト:')
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total += v
    print('アイテム総数: ' + str(item_total))
    
    
stuff = {'ロープ': 1, 'たいまつ': 6, '金貨': 42, '手裏剣': 1, '矢': 12}
display_inventory(stuff)