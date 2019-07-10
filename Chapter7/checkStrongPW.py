"""
program     : checkStrongPW.py
chapterNo   : 7.18.1
description : 引数として渡されたパスワード文字列が強いかどうかを
              正規表現を用いて確認する
created     : 2019/06/17
"""

import re


def check_password(pw):
    num_regex = re.compile(r'\d')
    lower_regex = re.compile(r'[a-z]')
    upper_regex = re.compile(r'[A-Z]')
    num_mo = num_regex.search(pw)
    lower_mo = lower_regex.search(pw)
    upper_mo = upper_regex.search(pw)
    
    if len(pw) < 8:
        print('強いパスワードは文字数が8文字以上である必要があります。')
    elif num_mo == None:
        print('強いパスワードは数字を1つ以上含む必要があります。')
    elif lower_mo == None:
        print('強いパスワードは小文字を1つ以上含む必要があります。')
    elif upper_mo == None:
        print('強いパスワードは大文字を1つ以上必要があります。')
    else:
        print('このパスワードは強いパスワードです！')
        
        
pw = input('確認したいパスワードを入力してください：')
check_password(pw)