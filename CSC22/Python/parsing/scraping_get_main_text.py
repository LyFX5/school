
import sys
from urllib.request import urlopen
from html.parser import HTMLParser

class FindText_in_HTML(HTMLParser):

    def __init__(self, domain):
        super(FindText_in_HTML, self).__init__()

        self.domain = domain

        self.interesting_tags = ['div', 'ul', 'p', 'table', 'i', 'span', 'h1', 'h2', 'h3', 'h4'] # 'div', 'ul', 'p', 'table', 'i'
        self.data_container = dict.fromkeys(self.interesting_tags)
        self.tag_is_open = dict.fromkeys(self.interesting_tags)

    def handle_starttag(self, tag, attrs):
        # print("START tag:", tag)
        if tag in self.interesting_tags:
            self.tag_is_open[tag] = True

    def handle_endtag(self, tag):
        # print("END tag :", tag)
        if tag in self.interesting_tags:
            self.tag_is_open[tag] = False

    def handle_data(self, data):
        # print("DATA  :", data)
        # print("TYPE of data is  :", type(data))

        for tag in self.interesting_tags:
            if self.tag_is_open[tag]:
                #print(tag)
                if self.data_container.get(tag) != None:
                    self.data_container[tag].append(self.format_string(data))
                else:
                    self.data_container[tag] = []

    def format_string(self, string):
        return string.strip()

    def get_text_from_pieces(self, array):
        text = ''
        for piece in array:
            text += piece
        return text

    def collect_text_by_tags(self):
        data_by_tags = []
        for tag, data in self.data_container.items():
            if data != None:
                text_in_tag = self.get_text_from_pieces(data)
                text_len = len(text_in_tag)
                data_by_tags.append([tag, text_in_tag, text_len])

        return sorted(data_by_tags, key=lambda x: -x[2])

if __name__ == "__main__":
    domain = 'https://habr.com/ru/company/gms/blog/553290/'
    encoding = 'utf-8'

    if len(sys.argv) == 3:
        domain = sys.argv[1]
        encoding = sys.argv[2]
    else:
        print()
        print('Были использованы значения по умолчанию.' + '\n' +
              'Введите интересующий адрес и кодировку.' + '\n' +
              'Например одну пару из следующих : ' + '\n' +
              'https://www.wildberries.ru/catalog/0/search.aspx?search=%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD ' + 'utf-8' + '\n' +
              'https://html5book.ru/html-tags/ ' + 'utf-8 ' + '\n' +
              'https://habr.com/ru/company/gms/blog/553290/ ' + 'utf-8 ' + '\n' +
              'https://www.amalgama-lab.com/songs/e/eminem/lose_yourself.html ' + 'cp1251' + '\n' +
              'http://artculturestudies.sias.ru ' + 'cp1251' + '\n' +
              'https://my.compscicenter.ru/learning/assignments/181613/ ' + 'utf-8')

    data = urlopen(domain).read().decode(encoding)
    # print(data)
    parser = FindText_in_HTML(domain)
    parser.feed(data)

    html_text_len = len(data)

    text_by_tags = parser.collect_text_by_tags()
    largest_text_tag = text_by_tags[0][0]
    largest_text = text_by_tags[0][1]
    largest_text_len = text_by_tags[0][2]
    quotient = largest_text_len / html_text_len

    print()
    print("Основной текст : ")
    print()
    print(largest_text)
    print()
    print(f'Доля основного текста от всего HTML документа равна : {100 * quotient} %')
    print()
    print(f'Текст расположился под тегом {largest_text_tag}')
    print()


# 'https://my.compscicenter.ru/learning/assignments/181613/'
# 'https://www.wildberries.ru/catalog/0/search.aspx?search=%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD'
# 'https://html5book.ru/html-tags/'
# 'https://habr.com/ru/company/gms/blog/553290/'
# 'https://www.amalgama-lab.com/songs/e/eminem/lose_yourself.html'
# "http://artculturestudies.sias.ru"

# utf-8, cp1251



