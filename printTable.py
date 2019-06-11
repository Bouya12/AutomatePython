"""
program     : printTable.py
chapterNo   : 6.7
description : 文字列のリストのリストを入力すると各行を右揃えに
              整形して表示する
created     : 2019/06/04
"""

def print_table(table_data):
    col_num = len(table_data)
    row_num = len(table_data[0])
    col_widths = [0] * col_num
    for i in range(col_num):
        col_widths[i] = len(max(table_data[i], key=len))
        
    lines = ''
    for i in range(row_num):
        for j in range(col_num):
            lines += table_data[j][i].rjust(col_widths[j]) + ' '
            if j == col_num - 1:
                lines += ('\n')
    
    print(lines)


table_data = [['apple', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]
print_table(table_data)