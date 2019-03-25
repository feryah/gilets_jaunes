#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
from lxml import etree
import re
import codecs

page = etree.Element('xml')
doc = etree.ElementTree(page)
corpus = etree.SubElement(page, 'corpus')
headElt = etree.SubElement(corpus, 'header')
title_head = etree.SubElement(headElt, 'title')
title_head.text ="Corpus de contrast dans la Presse Algérienne Francophone"
lg_head = etree.SubElement(headElt, 'language')
lg_head.text ="Français(FR)"
sources = etree.SubElement(headElt, 'sources')
source= etree.SubElement(sources, 'source', id=str('Algérie'), site=str("https://www.liberte-algerie.com"))
source.text ="Liberté"
size = etree.SubElement(headElt, 'size', nb=str())
nb_text = etree.SubElement(size, 'nbText', nb=str())
nb_words = etree.SubElement(size, 'nbWords', nb=str())
editors = etree.SubElement(headElt, 'editors')
editor = etree.SubElement(editors, 'editor',  id=str('ed_1'))
editor.text ="YAHIAOUI"
bodyElt = etree.SubElement(corpus, 'texts')

req = requests.get('https://www.liberte-algerie.com/lalgerie-profonde')
soup = BeautifulSoup(req.text,"xml")
req1 = requests.get('https://www.liberte-algerie.com/lalgerie-profonde/page/2')
soup1 = BeautifulSoup(req1.text,"xml")
req2 = requests.get('https://www.liberte-algerie.com/lalgerie-profonde/page/3')
soup2 = BeautifulSoup(req2.text,"xml")
req3 = requests.get('https://www.liberte-algerie.com/lalgerie-profonde/page/4')
soup3 = BeautifulSoup(req3.text,"xml")
req4 = requests.get('https://www.liberte-algerie.com/lalgerie-profonde/page/5')
soup4 = BeautifulSoup(req4.text,"xml")
req5 = requests.get('https://www.liberte-algerie.com/lalgerie-profonde/page/6')
soup5 = BeautifulSoup(req5.text,"xml")
req6 = requests.get('https://www.liberte-algerie.com/lalgerie-profonde/page/7')
soup6 = BeautifulSoup(req6.text,"xml")
req7 = requests.get('https://www.liberte-algerie.com/lalgerie-profonde/page/8')
soup7 = BeautifulSoup(req7.text,"xml")
req8 = requests.get('https://www.liberte-algerie.com/lalgerie-profonde/page/9')
soup8 = BeautifulSoup(req8.text,"xml")
req9 = requests.get('https://www.liberte-algerie.com/lalgerie-profonde/page/10')
soup9 = BeautifulSoup(req9.text,"xml")
req10 = requests.get('https://www.liberte-algerie.com/lalgerie-profonde/page/11')
soup10 = BeautifulSoup(req10.text,"xml")
req11 = requests.get('https://www.liberte-algerie.com/lalgerie-profonde/page/12')
soup11 = BeautifulSoup(req11.text,"xml")
req12 = requests.get('https://www.liberte-algerie.com/lalgerie-profonde/page/13')
soup12 = BeautifulSoup(req12.text,"xml")
req13 = requests.get('https://www.liberte-algerie.com/lalgerie-profonde/page/14')
soup13 = BeautifulSoup(req13.text,"xml")
req14 = requests.get('https://www.liberte-algerie.com/lalgerie-profonde/page/15')
soup14 = BeautifulSoup(req14.text,"xml")

liste_url = []


regexp = re.compile("^.+[0-9]{6}$")

liens = [a['href'] for a in soup.find_all('a', href=True)]
liens1 = [a['href'] for a in soup1.find_all('a', href=True)]
liens2 = [a['href'] for a in soup2.find_all('a', href=True)]
liens3 = [a['href'] for a in soup3.find_all('a', href=True)]
liens4 = [a['href'] for a in soup4.find_all('a', href=True)]
liens5 = [a['href'] for a in soup5.find_all('a', href=True)]
liens6 = [a['href'] for a in soup6.find_all('a', href=True)]
liens7 = [a['href'] for a in soup7.find_all('a', href=True)]
liens8 = [a['href'] for a in soup8.find_all('a', href=True)]
liens9 = [a['href'] for a in soup9.find_all('a', href=True)]
liens10 = [a['href'] for a in soup10.find_all('a', href=True)]
liens11 = [a['href'] for a in soup11.find_all('a', href=True)]
liens12 = [a['href'] for a in soup12.find_all('a', href=True)]
liens13 = [a['href'] for a in soup13.find_all('a', href=True)]
liens14 = [a['href'] for a in soup14.find_all('a', href=True)]



for lien in liens:
    if lien not in liste_url and regexp.search(lien):
        liste_url.append(lien)


for lien in liens1:
    if lien not in liste_url and regexp.search(lien):
        liste_url.append(lien)

for lien in liens2:
    if lien not in liste_url and regexp.search(lien):
        liste_url.append(lien)

for lien in liens3:
    if lien not in liste_url and regexp.search(lien):
        liste_url.append(lien)

for lien in liens4:
    if lien not in liste_url and regexp.search(lien):
        liste_url.append(lien)

for lien in liens5:
    if lien not in liste_url and regexp.search(lien):
        liste_url.append(lien)

for lien in liens6:
    if lien not in liste_url and regexp.search(lien):
        liste_url.append(lien)

for lien in liens7:
    if lien not in liste_url and regexp.search(lien):
        liste_url.append(lien)

for lien in liens8:
    if lien not in liste_url and regexp.search(lien):
        liste_url.append(lien)

for lien in liens9:
    if lien not in liste_url and regexp.search(lien):
        liste_url.append(lien)

for lien in liens10:
    if lien not in liste_url and regexp.search(lien):
        liste_url.append(lien)

for lien in liens11:
    if lien not in liste_url and regexp.search(lien):
        liste_url.append(lien)

for lien in liens12:
    if lien not in liste_url and regexp.search(lien):
        liste_url.append(lien)

for lien in liens13:
    if lien not in liste_url and regexp.search(lien):
        liste_url.append(lien)

for lien in liens14:
    if lien not in liste_url and regexp.search(lien):
        liste_url.append(lien)



#[<h2 class="post-title"><a href="http://lecourrier-dalgerie.com/france-la-popularite-de-macron-et-dedouard-philippe-en-chute-libre/" rel="bookmark" title="Permalink to France : La popularité de Macron et dEdouard Philippe en chute libre">France : La popularité de Macron et dEdouard Philippe en chute libre</a></h2>]


bons_urls = ["https://www.liberte-algerie.com"+lien for lien in liste_url]


contenu = ''
cpt= 1
for link in bons_urls:
    lien_crawl = requests.get(link)
    #soup3 = BeautifulSoup(lien_crawl.text,"xml")
    soup3 = BeautifulSoup(lien_crawl.content, 'html.parser')
    article = etree.SubElement(bodyElt,"article")
    article.set("id", str(cpt))
    title = etree.SubElement(article, 'title')
    for t in soup3.find_all('h1'):
        title.text = t.text

    content = etree.SubElement(article, 'content')
    for c in soup3.find_all(id="originalText"):
        #contenu = c.text.replace('<', '&lt;').replace('>', '&gt;').replace('&', '&amp;').replace('&#13;', '')
        contenu = c.text.replace('&#13;', '')
    
    content.text = contenu

    cpt +=1



outFile = open('contrast_gilets.xml', "ab+")
doc.write(outFile, encoding='UTF-8', xml_declaration=True, pretty_print=True)