#! python3
#program     : pw.py
#chapterNo   : 6.3
#description : パスワード管理プログラム（脆弱性あり）
#makeDate    : 2019/06/11

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxuVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('使い方: python pw.py [アカウント名]')
    print('パスワードをクリップボードにコピーします')
    sys.exit()
    
account = sys.argv[1]   # 最初のコマンドライン引数がアカウント名

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(account + 'のパスワードをクリップボードにコピーしました')
else:
    print(account + 'というアカウント名はありません')