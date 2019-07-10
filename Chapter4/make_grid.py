#program     : make_grid.py
#chapterNo   : 4.10.2
#description : 引数としてxy座標で文字で絵を描くリストを渡し、関数で描画する
#makeDate    : 2019/06/04

def draw_charpict(grid):
    x_len = len(grid)
    y_len = len(grid[0])
    pict = ''
    
    for i in range(y_len):
        row = ''
        
        for j in range(x_len):
            row += grid[j][i]
            
        pict += row + '\n'
        
    return pict


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
print(draw_charpict(grid))