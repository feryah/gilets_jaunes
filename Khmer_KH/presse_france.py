from bs4 import BeautifulSoup
import requests
from lxml import etree

page = etree.Element('xml')
doc = etree.ElementTree(page)
corpus = etree.SubElement(page, 'corpus')
headElt = etree.SubElement(corpus, 'header')
title_head = etree.SubElement(headElt, 'title')
title_head.text = "France dans la Presse Cambodgienne"
lg_head = etree.SubElement(headElt, 'language')
lg_head.text = "Khmer(KH)"
sources = etree.SubElement(headElt, 'sources')
source= etree.SubElement(sources, 'source', id=str('Cambodia'), site=str("https://www.postkhmer.com"))
source.text = "POSTKHMER"
size = etree.SubElement(headElt, 'size')
nb_text = etree.SubElement(size, 'nbText', nb=str())
nb_words = etree.SubElement(size, 'nbWords', nb=str())
editors = etree.SubElement(headElt, 'editors')
editor = etree.SubElement(editors, 'editor',  id=str('ed_1'))
editor.text = "DUHAYON"
bodyElt = etree.SubElement(corpus, 'texts')

req = requests.get('https://www.postkhmer.com/search/node/បារាំង')
soup = BeautifulSoup(req.text, "xml")
req2 = requests.get('https://www.postkhmer.com/search/node/បារាំង?page=1')
soup2 = BeautifulSoup(req2.text, "xml")
req4 = requests.get('http://vovworld.vn/km-KH/tags/បារាំង.vov')
soup4 = BeautifulSoup(req4.text, "xml")

liste_url = []
liste_url2 = []

for sub_heading in soup.find_all('li'):
    if sub_heading.h3 is not None:
        if "អាវកាក់​ពណ៌​លឿង" not in sub_heading.h3:
            liste_url.append(sub_heading.h3.a.attrs.get('href'))

for sub_heading2 in soup2.find_all('li'):
    if sub_heading2.h3 is not None:
        if "អាវកាក់​ពណ៌​លឿង" not in sub_heading2.h3:
            liste_url.append(sub_heading2.h3.a.attrs.get('href'))


for sub_heading3 in soup4.find_all("article", {"class": "story"}):
    if "អាវកាក់​ពណ៌​លឿង" not in sub_heading3.h2:
        ajout = "http://vovworld.vn" + sub_heading3.h2.a.attrs.get('href')

        liste_url2.append(ajout)


contenu = ''
cpt= 1
for link in liste_url:
    lien_crawl = requests.get(link)
    soup3 = BeautifulSoup(lien_crawl.text, "xml")

    article = etree.SubElement(bodyElt, 'article', id=str(cpt))
    title = etree.SubElement(article, 'title')
    title.text = soup3.title.string

    content = etree.SubElement(article, 'content')
    for each_p in soup3.find_all('p'):
        contenu += each_p.text
    content.text = contenu

    cpt +=1

for link in liste_url2:
    lien_crawl = requests.get(link)
    soup5 = BeautifulSoup(lien_crawl.text, "xml")

    article = etree.SubElement(bodyElt, 'article', id=str(cpt))
    title = etree.SubElement(article, 'title')
    title.text = soup3.title.string

    content = etree.SubElement(article, 'content')
    contenu = ''
    for each_p in soup3.find_all('p'):
        contenu += each_p.text
    content.text = contenu

    cpt +=1

outFile = open('presse_contraste.xml', 'wb')


doc.write(outFile, xml_declaration=True, encoding='UTF-8', pretty_print=True)
