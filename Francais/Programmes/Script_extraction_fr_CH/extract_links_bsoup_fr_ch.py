# Ouverture liste de liens

import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
from bs4 import BeautifulSoup
import math
import time
import re

# Prend en entrée une liste d'URL, renvoie un fichier XML avec pour chaque lien une balise <doc> contenant en métadonnées l'url de la page <doc url="xxx">

path = "fr_CH_links.txt"
out = "out.xml"

# Fonction de téléchargement des liens
def download(url, user_agent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0', num_retries = 1, charset='utf-8'):
	print ('Downloading: ', url)
	request = urllib.request.Request(url)
	request.add_header('User-Agent', user_agent)
	try:
		resp = urllib.request.urlopen(request)
		encoding = resp.headers.get_content_charset()
		if not encoding:
			encoding = chardet.detect(resp.read())['encoding']
		html = resp.read().decode(encoding)
	except (URLError, HTTPError, ContentTooShortError) as e:
		print ('Download error:', e.reason)
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code < 600:
				return download(url, num_retries - 1) 
	return html

# Écriture du fichier XML
def mainPage_1(mainUrl, out):
	main = download(mainUrl)
	mainSoup = BeautifulSoup(main, "html.parser")
	f = open(out, 'a', encoding="utf-8")
	f.write("<doc url="+ mainUrl +">\n")
	
	# récupération des contenus des balises <p>
	chapter = mainSoup.find_all('div', attrs={'id':'mainContent'})[0]
	for paragraph in chapter.find_all('p')[:-1]:
		content = paragraph.get_text()
		content = re.sub('\s+', ' ', content)
		content = re.sub('var badword = [01]; var badwordserch = [01]; ' , '', content)
		if content == " ":
			continue
		content = content + " "
		f.write(content)
		print(mainUrl)
		print(content)

	f.write("\n</doc>\n")
	f.close()

def mainPage_2(mainUrl, out):
	main = download(mainUrl)
	mainSoup = BeautifulSoup(main, "html.parser")
	f = open(out, 'a', encoding="utf-8")
	f.write("<doc url="+ mainUrl +">\n")
	
	# récupération des contenus des balises <p>
	excerpt = mainSoup.find_all('div', attrs={'class':'strong article-header'})[0]
	chapter = mainSoup.find_all('div', attrs={'class':'article-main-content'})[0]
	if excerpt != []:
		for paragraph in excerpt.find_all('p'):
			content = paragraph.get_text()
			content = re.sub('\s+', ' ', content)
			if content == " ":
				continue
			content = content + " "
			f.write(content)
			print(mainUrl)
			print(content)
	if chapter != []:
		for paragraph in chapter.find_all('p'):
			content = paragraph.get_text()
			content = re.sub('\s+', ' ', content)
			if content == " ":
				continue
			content = content + " "
			f.write(content)
			print(mainUrl)
			print(content)

	f.write("\n</doc>\n")
	f.close()

def mainPage_3(mainUrl, out):
	main = download(mainUrl)
	mainSoup = BeautifulSoup(main, "html.parser")
	f = open(out, 'a', encoding="utf-8")
	f.write("<doc url="+ mainUrl +">\n")
	chapter = mainSoup.find_all('div', attrs={'class':'body_content'})[0]
	for paragraph in chapter.find_all('p'):
		content = paragraph.get_text()
		content = re.sub('\s+', ' ', content)
		f.write(content)
		print(mainUrl)
		print(content)
	f.write("\n</doc>\n")
	f.close()

# Parcours de la liste des liens
if __name__ == "__main__":
	with open(path, encoding='utf-8') as f:
		for line in f:
			if "lenouvelliste" in line:
				mainPage_2(line, out)
			elif "lematin" in line:
				mainPage_1(line, out)
			elif "letemps" in line:
				mainPage_3(line, out)
			elif "tdg" in line:
				mainPage_1(line, out)