import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
from bs4 import BeautifulSoup
import time
import random

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
	
def searchPage(path, url):
	html = download(url)
	soupSearch = BeautifulSoup(html, "html.parser")
	urls = []
	for i in soupSearch.find('div', attrs={'id':'viewResponse'}).findAll('li'):
		urls.append("https://www.dhnet.be" + i.find('a')['href'])
	
	contentPage(path, urls)
	
def contentPage(path, urlList):
	with open(path, 'a') as f:
		
		for i in urlList:
			time.sleep(random.randint(1, 3))
			page = download(i)
			if "gilet" in str(page) or "Gilet" in str(page):
				continue
			contentSoup = BeautifulSoup(page, "html.parser")
			title = contentSoup.find('h1').text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
			f.write("<doc title=\"" + title + "\" source=\"La DH\">\n")
			for j in contentSoup.find('div', attrs={'class':'article-text'}).findAll('p'):
				f.write(j.text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;'))
				f.write('\n')
			f.write('</doc>\n')
		
if __name__ == "__main__":
	
	counter = 0
	
	path = "./DH.xml"
	with open(path, 'a') as f:
		f.write("<corpus>\n")
	
	while counter <= 64:
		counter += 1
		url = "https://www.dhnet.be/recherche?page=" + str(counter) + "&query=France&artefactFilter=article&section=Actu&from=2018-11-17&to=2019-02-23"
		try:
			searchPage(path, url)
		except:
			continue
	
	with open(path, 'a') as f:
		f.write("</corpus>\n")
		
#https://www.dhnet.be/recherche?page=1&query=France&artefactFilter=article&section=Actu&from=2018-11-17&to=2019-02-18