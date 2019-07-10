#! python3
"""
program     : phoneAndEmail.py
chapterNo   : 7.15
description : クリップボードから電話番号とメールアドレスを検索する
created     : 2019/06/17
"""

import re
import pyperclip


# 電話番号用の正規表現
phone_regex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?              # 市外局番
        (\s|-|\.)?                      # 区切り
        (\d{3})                         # 3桁の番号
        (\s|-|\.)                       # 区切り
        (\d{4})                         # 4桁の番号
        (\s*(ext|x|ext.)\s*(\d{2,5}))?  # 内線番号
        )''', re.VERBOSE)

# 電子メール用の正規表現
email_regex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+  # ユーザー名
        @                  # ＠記号
        [a-zA-Z0-9.-]+     # ドメイン名
        (\.[a-zA-Z]{2,4})  # ドットなんとか
        )''', re.VERBOSE)

# クリップボードのテキストを検索
text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])
    
# 検索結果をクリップボードに貼り付け
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('クリップボードにコピーしました:')
    print('\n'.join(matches))
else:
    print('電話番号やメールアドレスは見つかりませんでした。')