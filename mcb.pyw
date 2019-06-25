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
"""

import shelve
import pyperclip
import sys

mcb_shelf = shelve.open('mcb')

# クリップボードの内容を保存
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # TODO: キーワードの一覧と、内容の読み込み

mcb_shelf.close()