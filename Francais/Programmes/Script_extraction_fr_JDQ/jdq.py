import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
from bs4 import BeautifulSoup
import math
import time
import re
import json

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
	
def SearchPage(path):
	counter = 1
	
	with open(path, 'a') as f:
		f.write("<corpus>\n")
	
	while counter < 3:
		searchPage = download('https://recherche-api.quebecormedia.com/sites/jdq/?search=gilet+jaune&count=10&page=' + str(counter) + '&order=0&facet=0&suggest=1')
		j = json.loads(searchPage)
		for i in range(0, 10):
			try:
				url = j['matches'][i]['fields']['url']
				ContentPage(url, path)
				time.sleep(2)
			except:
				break
		counter += 1
		
	with open(path, 'a') as f:
		f.write("</corpus>\n")
		
def ContentPage(url, path):
	with open(path, 'a') as f:
		html = download(url)
		soup = BeautifulSoup(html, "html.parser")
		title = soup.h1.text
		f.write("<doc title=\""+ title +"\" source=\"Journal de Québec\">\n")
		for p in soup.find_all('p'):
			f.write(p.text)
			f.write('\n')
		f.write("</doc>\n")
		
if __name__ == "__main__":
	SearchPage("./JDQ.xml")