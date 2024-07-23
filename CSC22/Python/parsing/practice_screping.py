
# нормальный обход графа
# сохранять пдф на диск (requests ??)
# обрабатывать кодировки
# правильно пристыковывать url (относительные ссылки) (мы знаем относительный адрес, нужно узнавать абсалютный)
# многопоточность
# настраивать сохраняемый контент (чтобы можно было сохранять не пдф, а, например, картинки (.txt, .jpg))

# находить основной текст обобщенно (независимо от верстки)
# находить списки большие или таблицы внутри сайтов


from urllib.request import urlopen
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def __init__(self, domain):
        super(MyHTMLParser, self).__init__()

        self.domain = domain
        self.links_stack = []

    def is_good_link(self, string):
        return ('.php' not in string) and ('http' not in string) and ('.ru' not in string) and ('#' not in string) and (
                    '//' not in string)

    def get_pdfs(self, links):
        pdfs = []
        for link in links:
            if link.endswith('.pdf'):
                pdfs.append(link)

        return pdfs

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            link = dict(attrs).get('href')
            if self.is_good_link(link):
                self.links_stack.append(self.domain+link)

        #print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        pass

    def handle_data(self, data):
        #print("Encountered some data  :", data)
        pass

domain = "http://artculturestudies.sias.ru"

data = urlopen(domain).read().decode("cp1251")

parser = MyHTMLParser(domain)
parser.feed(data)

for link in parser.links_stack:
    data = urlopen(link).read().decode("cp1251")
    parser = MyHTMLParser(domain) # у меня стояло link
    parser.feed(data)
    all_pdfs = parser.get_pdfs(parser.links_stack)
    print(all_pdfs)

'''
'<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>'
'''


# big_data_recur = ''
# big_data_iter = ''
#
# def DFS_recur(v):
#     global big_data_recur
#     # print(v.name,end=' : ')
#     # print([kid.name for kid in v.kids])
#     big_data_recur += v.name + ' : '
#     # print(v.name, end=' : ')
#     for kid in v.kids:
#         big_data_recur += kid.name + ', '
#     if len(v.kids) == 0:
#         return
#     else:
#         for kid in v.kids:
#             DFS_recur(kid)



