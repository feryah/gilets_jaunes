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
title_head.text ="Gilets Jaunes dans la Presse Algérienne Francophone"
lg_head = etree.SubElement(headElt, 'language')
lg_head.text ="Français(FR)"
sources = etree.SubElement(headElt, 'sources')
source= etree.SubElement(sources, 'source', id=str('Algérie'), site=str("https://www.liberte-algerie.com https://www.elwatan.com/ http://lecourrier-dalgerie.com"))
source.text ="Liberté, El Watan, Le courrier d'Algérie"
size = etree.SubElement(headElt, 'size', nb=str('1.1 Mo'))
nb_text = etree.SubElement(size, 'nbText', nb=str('151'))
nb_words = etree.SubElement(size, 'nbWords', nb=str())
editors = etree.SubElement(headElt, 'editors')
editor = etree.SubElement(editors, 'editor',  id=str('ed_1'))
editor.text ="YAHIAOUI"
bodyElt = etree.SubElement(corpus, 'texts')
req = requests.get('https://www.liberte-algerie.com/search/gilets+jaunes?page=1')
soup = BeautifulSoup(req.text,"xml")
req2 = requests.get('https://www.liberte-algerie.com/search/gilets+jaunes?page=2')
soup2 = BeautifulSoup(req2.text,"xml")
req6 = requests.get('https://www.liberte-algerie.com/search/gilets+jaunes?page=3')
soup6 = BeautifulSoup(req.text,"xml")
req4 = requests.get('https://www.elwatan.com/?s=gilets+jaunes+')
soup4 = BeautifulSoup(req4.text,"xml")

req9 = requests.get('http://lecourrier-dalgerie.com/page/4/?s=gilets+jaunes')
soup9 = BeautifulSoup(req9.text,"xml")
req10 = requests.get('http://lecourrier-dalgerie.com/page/3/?s=gilets+jaunes')
soup10 = BeautifulSoup(req10.text,"xml")
req11 = requests.get('http://lecourrier-dalgerie.com/page/2/?s=gilets+jaunes')
soup11 = BeautifulSoup(req11.text,"xml")
req12 = requests.get('http://lecourrier-dalgerie.com/?s=gilets+jaunes')
soup12 = BeautifulSoup(req12.text,"xml")

liste_url = []
liste_url2 = []
bons_urls9 = []


regexp = re.compile("^.+[0-9]{6}$")

liens = [a['href'] for a in soup.find_all('a', href=True)]
liens2 = [a['href'] for a in soup2.find_all('a', href=True)]
liens6 = [a['href'] for a in soup6.find_all('a', href=True)]


for lien in liens:
    if lien not in liste_url and regexp.search(lien):
        liste_url.append(lien)


for lien in liens2:
    if lien not in liste_url and regexp.search(lien):
        liste_url.append(lien)

for lien in liens6:
    if lien not in liste_url and regexp.search(lien):
        liste_url.append(lien)




liens9 = [lien.find_all("a", href=True) for lien in soup9.find_all('h2', {'class':'post-title'})]
liste_app9 = [val for sousliste in liens9 for val in sousliste]
liens10 = [lien.find_all("a", href=True) for lien in soup10.find_all('h2', {'class':'post-title'})]
liste_app10 = [val for sousliste in liens10 for val in sousliste]
liens11 = [lien.find_all("a", href=True) for lien in soup11.find_all('h2', {'class':'post-title'})]
liste_app11 = [val for sousliste in liens11 for val in sousliste]
liens12 = [lien.find_all("a", href=True) for lien in soup12.find_all('h2', {'class':'post-title'})]
liste_app12 = [val for sousliste in liens12 for val in sousliste]


for lien in liste_app9:
    if lien not in bons_urls9:
        bons_urls9.append(lien.get('href'))

for lien in liste_app10:
    if lien not in bons_urls9:
        bons_urls9.append(lien.get('href'))

for lien in liste_app11:
    if lien not in bons_urls9:
        bons_urls9.append(lien.get('href'))

for lien in liste_app12:
    if lien not in bons_urls9:
        bons_urls9.append(lien.get('href'))


#[<h2 class="post-title"><a href="http://lecourrier-dalgerie.com/france-la-popularite-de-macron-et-dedouard-philippe-en-chute-libre/" rel="bookmark" title="Permalink to France : La popularité de Macron et dEdouard Philippe en chute libre">France : La popularité de Macron et dEdouard Philippe en chute libre</a></h2>]


bons_urls = ["https://www.liberte-algerie.com"+lien for lien in liste_url]

bons_urls8 = ["https://www.elwatan.com/edition/international/un-17-novembre-noir-en-france-17-11-2018","https://www.elwatan.com/pages-hebdo/france-actu/une-deception-dans-la-population-qui-se-sent-flouee-de-son-vote-macron-20-11-2018","https://www.elwatan.com/edition/international/mouvement-des-gilets-jaunes-nouvelle-grande-journee-de-mobilisation-en-france-24-11-2018","https://www.elwatan.com/a-la-une/le-mouvement-des-gilets-jaunes-prend-de-lampleur-en-france-emeutes-au-coeur-de-paris-25-11-2018","https://www.elwatan.com/edition/international/bras-de-fer-entre-le-president-francais-et-le-mouvement-des-gilets-jaunes-macron-promet-un-changement-de-methode-mais-pas-de-cap-28-11-2018","https://www.elwatan.com/edition/international/lurgence-de-reponses-concretes-02-12-2018","https://www.elwatan.com/edition/international/tensions-sociales-en-france-le-mouvement-des-gilets-jaunes-se-radicalise-02-12-2018","https://www.elwatan.com/edition/international/mouvement-des-gilets-jaunes-macron-demande-au-gouvernement-dengager-un-dialogue-03-12-2018","https://www.elwatan.com/edition/international/gouvernement-francais-comment-desamorcer-la-bombe-gilets-jaunes-04-12-2018","https://www.elwatan.com/pages-hebdo/france-actu/suite-a-une-hausse-des-droits-de-scolarite-revolte-en-sourdine-des-etudiants-etrangers-en-france-04-12-2018","https://www.elwatan.com/edition/actualite/on-vous-le-dit-816-05-12-2018","https://www.elwatan.com/edition/international/france-premiere-reculade-du-gouvernement-devant-les-gilets-jaunes-05-12-2018","https://www.elwatan.com/edition/international/un-dispositif-de-securite-exceptionnel-deploye-a-paris-08-12-2018","https://www.elwatan.com/chroniques/point-zero/gilet-jaune-contre-gilet-orange-09-12-2018","https://www.elwatan.com/a-la-une/des-milliers-de-policiers-deployes-pour-stopper-la-manifestation-des-gilets-jaunes-paris-sous-haute-tension-09-12-2018","https://www.elwatan.com/chroniques/analyse-eco/face-a-la-pression-fiscale-des-algeriens-portent-le-gilet-jaune-depuis-plusieurs-decennies-10-12-2018","https://www.elwatan.com/regions/ouest/mascara/mascara-les-eboueurs-et-les-balayeurs-refont-leur-apparition-11-12-2018","https://www.elwatan.com/edition/international/les-les-gilets-jaunes-le-font-flechir-macron-decrete-un-etat-durgence-social-et-economique-12-12-2018","https://www.elwatan.com/edition/international/la-menace-terroriste-plane-a-nouveau-sur-la-france-13-12-2018","https://www.elwatan.com/edition/actualite/sidi-said-mobilise-ses-gilets-jaunes-contre-hmarnia-et-menadi-13-12-2018","https://www.elwatan.com/edition/international/defi-de-survie-pour-le-mouvement-des-gilets-jaunes-14-12-2018","https://www.elwatan.com/edition/contributions/l-ultraliberalisme-se-sustente-de-lintoxication-politique-la-perversion-economique-et-la-depravation-financiere-15-12-2018","https://www.elwatan.com/pages-hebdo/france-actu/france-gilets-jaunes-la-mobilisation-baisse-mais-ne-faiblit-pas-16-12-2018","https://www.elwatan.com/pages-hebdo/france-actu/mouvement-des-gilets-jaunes-en-france-quelles-reponses-a-la-crise-democratique-18-12-2018","https://www.elwatan.com/edition/international/alors-que-le-pays-celebre-la-revolution-du-jasmin-des-gilets-rouges-font-leur-apparition-en-tunisie-18-12-2018","https://www.elwatan.com/edition/international/france-la-loi-gilets-jaunes-au-parlement-21-12-2018","https://www.elwatan.com/edition/contributions/gilets-jaunes-et-regulation-democratique-1re-partie-25-12-2018","https://www.elwatan.com/pages-hebdo/france-actu/rupture-entre-les-decideurs-et-la-france-du-plus-grand-nombre-25-12-2018","https://www.elwatan.com/edition/contributions/gilets-jaunes-et-regulation-democratique-26-12-2018","https://www.elwatan.com/edition/international/le-monde-a-beaucoup-tourne-en-2018-28-12-2018","https://www.elwatan.com/edition/culture/scorsese-houellebecq-madonna-rihanna-lady-gaga-30-12-2018","https://www.elwatan.com/edition/international/les-protestataires-entament-leur-septieme-week-end-30-12-2018","https://www.elwatan.com/edition/contributions/le-mal-dont-le-pays-est-affecte-est-le-manque-de-democratie-31-12-2018","https://www.elwatan.com/chroniques/analyse-eco/pourquoi-2019-nest-plus-ecrite-dans-la-loi-de-finances-pour-lalgerie-31-12-2018","https://www.elwatan.com/archives/actualites/la-marche-de-lunion-a-eu-lieu-a-bejaia-2-21-04-2014","https://www.elwatan.com/pages-hebdo/france-actu/contestation-des-gilets-jaunes-un-samedi-sous-haute-tension-05-01-2019","https://www.elwatan.com/edition/international/france-marches-et-discours-au-menu-de-lacte-viii-des-gilets-jaunes-06-01-2019","https://www.elwatan.com/edition/international/breves-208-08-01-2019","https://www.elwatan.com/pages-hebdo/france-actu/boris-perrin-editeur-le-fait-saillant-cest-la-trahison-des-dirigeants-politiques-08-01-2019","https://www.elwatan.com/archives/magazine-archives/la-revolte-des-resquilleurs-2-16-03-2017","https://www.elwatan.com/edition/culture/france-les-gilets-jaunes-dans-la-rue-pour-un-9e-week-end-de-manifestations-13-01-2019","https://www.elwatan.com/edition/international/neuvieme-semaine-de-contestation-sociale-en-france-les-gilets-jaunes-trouvent-un-nouveau-souffle-13-01-2019","https://www.elwatan.com/edition/contributions/l-ultraliberalisme-se-sustente-de-lintoxication-politique-la-perversion-economique-et-la-depravation-financiere-2-15-01-2019","https://www.elwatan.com/pages-hebdo/france-actu/une-logique-de-tension-qui-consiste-a-employer-la-force-pour-ecraser-et-soumettre-15-01-2019","https://www.elwatan.com/edition/international/mouvement-des-gilets-jaunes-en-france-macron-joue-t-il-sa-derniere-carte-15-01-2019","https://www.elwatan.com/edition/international/manifestations-en-france-acte-x-pour-les-gilets-jaunes-20-01-2019","https://www.elwatan.com/edition/actualite/4-mandats-et-des-departs-par-milliers-harraga-sous-boutef-et-la-part-du-systeme-22-01-2019","https://www.elwatan.com/edition/international/manifestations-en-france-une-foire-dempoigne-26-01-2019","https://www.elwatan.com/edition/international/nuit-jaune-a-paris-rassemblements-et-marches-en-province-27-01-2019","https://www.elwatan.com/edition/international/le-president-nicolas-maduro-sous-la-pression-internationale-27-01-2019","https://www.elwatan.com/pages-hebdo/france-actu/en-bref-1398-29-01-2019","https://www.elwatan.com/pages-hebdo/france-actu/polemique-autour-des-armes-dites-intermediaires-contre-les-casseurs-29-01-2019","https://www.elwatan.com/pages-hebdo/france-actu/apres-les-gilets-jaunes-les-foulards-rouges-29-01-2019","https://www.elwatan.com/pages-hebdo/france-actu/le-point-commun-entre-1968-et-2018-est-la-volonte-de-criminaliser-les-manifestants-29-01-2019","https://www.elwatan.com/edition/economie/indices-92-31-01-2019","https://www.elwatan.com/pages-hebdo/france-actu/crise-sociale-en-france-douzieme-samedi-de-manifestations-02-02-2019","https://www.elwatan.com/edition/international/12e-acte-des-gillets-jaunes-en-france-hommage-aux-victimes-des-lanceurs-de-balles-de-defense-03-02-2019","https://www.elwatan.com/edition/actualite/on-vous-le-dit-3956-04-02-2019","https://www.elwatan.com/pages-hebdo/france-actu/la-mort-de-zineb-redouane-oubliee-par-le-president-macron-05-02-2019","https://www.elwatan.com/edition/international/le-torchon-brule-entre-paris-et-rome-08-02-2019","https://www.elwatan.com/edition/international/union-europeenne-rien-ne-va-plus-entre-paris-et-rome-09-02-2019","https://www.elwatan.com/pages-hebdo/france-actu/13eme-acte-des-gilets-jaunes-une-grenade-arrache-le-bras-a-un-manifestant-10-02-2019","https://www.elwatan.com/edition/contributions/italie-france-la-crise-des-extremes-12-02-2019","https://www.elwatan.com/edition/culture/maghreb-orient-des-livres-est-il-permis-de-rever-15-02-2019","https://www.elwatan.com/edition/actualite/ils-refusent-le-statu-quo-et-le-font-savoir-5e-mandat-ripostes-citoyennes-12-02-2019","https://www.elwatan.com/edition/international/france-plusieurs-manifestations-pour-lacte-14-des-gilets-jaunes-17-02-2019","https://www.elwatan.com/edition/international/france-les-gilets-jaunes-pour-la-quinzieme-fois-consecutive-dans-la-rue-24-02-2019","https://www.elwatan.com/regions/est/constantine/les-employes-de-la-collecte-des-dechets-sans-vaccin-26-02-2019","https://www.elwatan.com/edition/contributions/modernisation-et-modernite-etat-contre-societe-26-02-2019","https://www.elwatan.com/edition/actualite/noureddine-bouderba-ancien-syndicaliste-expert-en-questions-sociales-les-algeriens-reinventent-letat-democratique-et-social-de-novembre-54-03-03-2019","https://www.elwatan.com/pages-hebdo/france-actu/zineb-redouane-victime-dun-tir-de-lacrymogene-05-03-2019","https://www.elwatan.com/edition/actualite/les-reseaux-sociaux-a-lheure-de-la-protestation-facebook-couteau-suisse-politico-mediatique-06-03-2019","https://www.elwatan.com/edition/actualite/une-algerie-debout-et-fiere-06-03-2019","https://www.elwatan.com/archives/supplement-economie/less-est-une-economie-du-reel-et-de-plus-equitable-11-03-2019","https://www.elwatan.com/pages-hebdo/france-actu/loi-anticasseurs-un-arsenal-judiciaire-contraignant-12-03-2019","https://www.elwatan.com/edition/actualite/les-algeriens-de-france-plus-que-jamais-mobilises-pour-degager-bouteflika-et-son-clan-18-03-2019"]


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



for link in bons_urls8:
    lien_crawl = requests.get(link)
    #soup8 = BeautifulSoup(lien_crawl.text, "xml")
    soup8 = BeautifulSoup(lien_crawl.content, 'html.parser')

    article = etree.SubElement(bodyElt, 'article')
    article.set("id", str(cpt))
    title = etree.SubElement(article, 'title') 
    #for t in soup8.find_all('h1', {'class': 'title-21'}):
    for t in soup8.findAll("h1", attrs={"class":"title-21"}):
        #print(t)
        title.text = t.text

    content = etree.SubElement(article, 'content')
    for c in soup8.findAll("h1", attrs={"class":"texte"}): 
    #for c in soup8.find_all('div', {'class': 'texte'}).findChildren('p'):
        #print(c.findChildren("p"))
        #contenu = c.text.replace('<', '&lt;').replace('>', '&gt;').replace('&', '&amp;').replace('&#13;', '')
        contenu = c.text.replace('&#13;', '')
        
    content.text = contenu

    cpt +=1

for link in bons_urls9:
    lien_crawl = requests.get(link)
    #soup8 = BeautifulSoup(lien_crawl.text, "xml")
    soup13 = BeautifulSoup(lien_crawl.content, 'html.parser')

    article = etree.SubElement(bodyElt, 'article')
    article.set("id", str(cpt))
    title = etree.SubElement(article, 'title') 
    #for t in soup8.find_all('h1', {'class': 'title-21'}):
    for t in soup13.findAll("span", attrs={"itemprop":"name"}):
        #print(t)
        title.text = t.text

    content = etree.SubElement(article, 'content')
    for c in soup13.findAll("div", attrs={"class":"entry"}): 
    #for c in soup8.find_all('div', {'class': 'texte'}).findChildren('p'):
        #print(c.findChildren("p"))
        #contenu = c.text.replace('<', '&lt;').replace('>', '&gt;').replace('&', '&amp;').replace('&#13;', '')
        contenu = c.text.replace('&#13;', '')
        
    content.text = contenu

    cpt +=1




outFile = open('gilets.xml', "ab+")
doc.write(outFile, encoding='UTF-8', xml_declaration=True, pretty_print=True)