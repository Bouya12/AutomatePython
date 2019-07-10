#! python3
"""
program     : mcb.pyw
chapterNo   : 8.7
description : クリップボードのテキストを保存・復元
created     : 2019/06/25
usage       : 
    py.exe mcb.pyw save <keyword> - クリップボードにキーワードを紐づけて保存
    py.exe mcb.pyw <keyword> - キーワードに紐付けられたテキストをクリップボードにコピー
    py.exe mcb.pyw list - 全キーワードをクリップボードにコピー
    py.exe mcb.pyw delete <keyword> - シェルフから指定したキーワードを削除
    py.exe mcb.pyw delete --all - シェルフからすべてのキーワードを削除
========================================================
Moddify
========================================================
2019/07/04 : Chapter 8.10.1  マルチクリップボードを拡張する
・delete でキーワードを削除する機能を追加
"""

import shelve
import pyperclip
import sys

mcb_shelf = shelve.open('mcb')

# クリップボードの内容を保存
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()

# シェルフのキーワードを削除
elif sys.argv[1].lower() == 'delete':
    if sys.argv[2].lower() == '--all':
        mcb_shelf.clear()
    else:
        del mcb_shelf[sys.argv[2]]

elif len(sys.argv) == 2:
    
    # キーワードの一覧と、内容の読み込み
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()