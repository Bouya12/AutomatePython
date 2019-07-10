#program   : collatz.py
#chapterNo : 3.11
#makeDate  : 2019/05/29

def collatz(number):
    if number % 2 == 0:
        return number / 2
    else:
        return 3 * number + 1
    
print('整数を入力してください：')
try:
    answer = int(input())
except ValueError:
    print('エラー：整数を入力してください')
else:
    while True:
        answer = int(collatz(answer))
        print(answer)
        if answer == 1:
            break
        else:
            continue
