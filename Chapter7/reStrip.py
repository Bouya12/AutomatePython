"""
program     : reStrip.py
chapterNo   : 7.18.2
description : 正規表現を用いてstrip()と同様の動作を行う
created     : 2019/06/17
"""

import re


def re_strip(strings, cut='\s'):
    head_regex = re.compile('^' + cut + '*')
    tail_regex = re.compile(cut + '*$')
    mo1 = head_regex.sub('', strings)
    mo2 = tail_regex.sub('', mo1)
    print(mo2)
    

# 引数2を省略した場合、前後のスペースをカット
strings = '  asdasda  '
re_strip(strings)

# 引数2に文字を入れた場合、該当文字をカット
strings = 'asdasda'
re_strip(strings, 'a')