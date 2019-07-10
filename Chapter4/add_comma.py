#program     : add_comma.py
#chapterNo   : 4.10.1
#description : 引数として渡されたリストの内容を連結し、カンマとAndで出力する
#makeDate    : 2019/06/04

def add_comma(lists):
    for i in range(len(lists)):
        if i == 0: 
            string = lists[i]
        elif i == len(lists) - 1:
            string += ' and ' + lists[i]
        else:
            string += ', ' + lists[i]
    
    return string


spam = ['apples', 'bananas', 'tofu', 'cats']
print(add_comma(spam))