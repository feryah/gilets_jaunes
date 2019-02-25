"""Parser des pages HTML

    Authors:
        XU Yizhou et JIANG Chunyang

    Update:
        2019-02-10

"""
import urllib.request as rq
from bs4 import BeautifulSoup


def main():
    url = "http://www.xinhuanet.com/world/2018-12/04/c_1123802658.htm"
    print(xinhua_parser(url))

def xinhua_parser(url):
    content = dict()
    article = rq.urlopen(url).read().decode("UTF-8")
    page = BeautifulSoup(article, 'html.parser')

    keywords = page.find(attrs={"name": "keywords"})['content'].strip()
    title = page.find('div', class_="h-title").text.strip()
    date = page.find('span', class_="h-time").text.strip().split()[0]
    text = '\n'.join([p.text.strip() for p in page.find_all('p')])

    content['title'] = title
    content['source'] = url
    content['keywords'] = keywords
    content['date'] = date
    content['text'] = text

    return content

def people_parser(url):
    content = dict()
    article = rq.urlopen(url).read().decode("gbk")
    page = BeautifulSoup(article, 'html.parser')

    keywords = ",".join(
        page.find(attrs={"name": "keywords"})['content'].strip().split()
    )
    title = page.h1.text.strip()
    date = page.find(attrs={"name": "publishdate"})['content'].strip()
    text = '\n'.join(
        [p.text.strip() for p in page.find_all(
            "p", attrs={"style": True}
        )]
    )
    content['title'] = title
    content['source'] = url
    content['keywords'] = keywords
    content['date'] = date
    content['text'] = text

    return content

def huanqiu_parser(url):
    content = dict()
    article = rq.urlopen(url).read().decode("UTF-8")
    page = BeautifulSoup(article, 'html.parser')

    keywords = page.find(attrs={"name": "keywords"})['content'].strip()
    title = page.h1.text.strip()
    date = page.find(attrs={"name": "publishdate"})['content'].strip()
    text = '\n'.join([p.text.strip() for p in page.find_all('p')])

    content['title'] = title
    content['source'] = url
    content['keywords'] = keywords
    content['date'] = date
    content['text'] = text

    return content

def ce_parser(url):
    content = dict()
    article = rq.urlopen(url).read().decode("gbk")
    page = BeautifulSoup(article, 'html.parser')

    keywords = page.find(attrs={"name": "KEYWords"})['content'].strip()
    title = page.h1.text.strip()
    date = page.find(attrs={"name": "publishdate"})['content'].strip()
    text = '\n'.join([p.text.strip() for p in page.find_all('p')])

    content['title'] = title
    content['source'] = url
    content['keywords'] = keywords
    content['date'] = date
    content['text'] = text

    return content

if __name__ == '__main__':
    main()
