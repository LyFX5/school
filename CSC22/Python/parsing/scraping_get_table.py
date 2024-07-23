
tags_kids_nums = []

def DFS(v):
    # global big_data_iter
    global tags_kids_nums
    stack = [v]
    while len(stack) != 0:
        v = stack.pop()
        stack.extend(reversed(v.kids))

        #print(v.name, end=' : ')
        #print([kid.name for kid in v.kids])
        kids = [kid.name for kid in v.kids]
        unic_names = dict.fromkeys(list(set(kids)), 0)

        for kid in kids:
            unic_names[kid] += 1

        v_kids_freqs = []
        for kid_name, freq in unic_names.items():
            v_kids_freqs.append([kid_name, freq])

        if len(v_kids_freqs) != 0:
            tags_kids_nums.append([v, sorted(v_kids_freqs, key=lambda x: -x[1])])


class Node_html:
    def __init__(self):
        self.kids = []
        self.parent = None

        self.name = 'tag'
        self.attrs = []

        self.data = []
        self.info = []

import sys
from urllib.request import urlopen
from html.parser import HTMLParser

class FindTable_in_HTML(HTMLParser):

    def __init__(self, domain):
        super(FindTable_in_HTML, self).__init__()

        self.domain = domain

        self.root = None

        self.opened_tags_stack = []

    def handle_starttag(self, tag, attrs):
        new_tag_opened = Node_html()
        new_tag_opened.name = tag
        new_tag_opened.attrs = attrs

        if len(self.opened_tags_stack) != 0:
            new_tag_opened.parent = self.opened_tags_stack[-1]
            self.opened_tags_stack[-1].kids.append(new_tag_opened)

        self.opened_tags_stack.append(new_tag_opened)

    def handle_endtag(self, tag):
        self.root = self.opened_tags_stack.pop()

    def handle_data(self, data):
        if len(self.opened_tags_stack) != 0:
            self.opened_tags_stack[-1].data.append(data)
        # else:
        #     print("=================================stack is empty=================================")


if __name__ == "__main__":
    domain = 'https://html5book.ru/html-tags/'
    encoding = 'utf-8'

    if len(sys.argv) == 3:
        domain = sys.argv[1]
        encoding = sys.argv[2]
    else:
        print()
        print('Были использованы значения по умолчанию.' + '\n' +
              'Введите интересующий адрес и кодировку.' + '\n' +
              'Например одну пару из следующих : ')
        print()
        print('https://www.wildberries.ru/catalog/0/search.aspx?search=%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD ' + 'utf-8' + '\n' +
              'https://html5book.ru/html-tags/ ' + 'utf-8 ' + '\n' +
              'https://habr.com/ru/company/gms/blog/553290/ ' + 'utf-8 ' + '\n' +
              'https://www.amalgama-lab.com/songs/e/eminem/lose_yourself.html ' + 'cp1251' + '\n' +
              'http://artculturestudies.sias.ru ' + 'cp1251' + '\n' +
              'https://my.compscicenter.ru/learning/assignments/181613/ ' + 'utf-8')

    data = urlopen(domain).read().decode(encoding)
    #print(data)
    parser = FindTable_in_HTML(domain)
    parser.feed(data)

    DFS(parser.root)

    # for tag_dict in tags_kids_nums:
    #     print(*tag_dict)

    tag_with_many_kids = sorted( tags_kids_nums, key=lambda x: -x[1][0][1] ) [0][0]

    # print(tag_with_many_kids)

    print()
    print("Далее представлено содержимое тега, имеющего самое большое количество одноименных дочерних тегов. Такой тег может быть таблицей.")

    print()
    for kid in tag_with_many_kids.kids:
        for kidkid in kid.kids:
            print(*kidkid.data)




# 'https://my.compscicenter.ru/learning/assignments/181613/'
# 'https://www.wildberries.ru/catalog/0/search.aspx?search=%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD'
# 'https://html5book.ru/html-tags/'
# 'https://habr.com/ru/company/gms/blog/553290/'
# 'https://www.amalgama-lab.com/songs/e/eminem/lose_yourself.html'
# "http://artculturestudies.sias.ru"

# utf-8, cp1251



