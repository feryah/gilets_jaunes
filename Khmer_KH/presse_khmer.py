from bs4 import BeautifulSoup
import requests
from lxml import etree

page = etree.Element('xml')
doc = etree.ElementTree(page)
bodyElt = etree.SubElement(page, 'body')

req = requests.get('https://www.postkhmer.com/search/node/អាវកាក់​ពណ៌​លឿង')
soup = BeautifulSoup(req.text, "xml")
req2 = requests.get('https://www.postkhmer.com/search/node/អាវកាក់​ពណ៌​លឿង?page=1')
soup2 = BeautifulSoup(req2.text, "xml")

liste_url = []

for sub_heading in soup.find_all('li'):
    if sub_heading.h3 is not None:
        liste_url.append(sub_heading.h3.a.attrs.get('href'))

for sub_heading2 in soup2.find_all('li'):
    if sub_heading2.h3 is not None:
        liste_url.append(sub_heading2.h3.a.attrs.get('href'))

contenu = ''
cpt=1
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

outFile = open('presse_khmer.xml', 'wb')
doc.write(outFile, xml_declaration=True, encoding='UTF-8')
