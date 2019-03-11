import urllib.request
import re
from bs4 import BeautifulSoup

# ____________________ LE POINT ____________________
articles = []

source = 'https://www.lepoint.fr/recherche/index.php?query=gilets+jaunes&sort=date_asc&date_from=17%2F11%2F2018&date_to=17%2F02%2F2019&type=ARTICLE&page='
i = 1
while i<=100:
	print(i, end='\t')
	adresse = str(source + str(i) )
	page = urllib.request.urlopen(adresse)
	html = BeautifulSoup(page,"html.parser")
	for baliseA in html.find_all('a'):
		articles.append(baliseA.get('href'))
	i += 1
	print(i)

source = 'https://www.lepoint.fr/recherche/index.php?query=gilets+jaunes&sort=date_desc&date_from=17%2F11%2F2018&date_to=17%2F02%2F2019&type=ARTICLE&page='
i = 1
while i<=100:
	print(i, end='\t')
	adresse = str(source + str(i) )
	page = urllib.request.urlopen(adresse)
	html = BeautifulSoup(page,"html.parser")
	for baliseA in html.find_all('a'):
		articles.append(baliseA.get('href'))
	i += 1
	print(i)

source = 'https://www.lepoint.fr/recherche/index.php?query=gilets+jaunes&sort=pertinence&date_from=17%2F11%2F2018&date_to=17%2F02%2F2019&type=ARTICLE&page='
i = 1
while i<=100:
	print(i, end='\t')
	adresse = str(source + str(i) )
	page = urllib.request.urlopen(adresse)
	html = BeautifulSoup(page,"html.parser")
	for baliseA in html.find_all('a'):
		articles.append(baliseA.get('href'))
	i += 1
	print(i)
	
with open('URL_LePoint_GJ.txt', 'w', encoding='UTF-8') as sortieLP:
	for x in sorted(set(articles)):
		sortieLP.write(str(x+'\n'))

	
# sources=[  'https://www.lepoint.fr/societe/'
		 # , 'http://www.lefigaro.fr/actualite-france/'
		 # , 'https://www.lemonde.fr/societe/'
		 # , 'https://www.liberation.fr/france,11'
		 # , 'https://www.humanite.fr/politique'
		# ]

# articles=[]
# sources = ['https://www.lepoint.fr/recherche/index.php?query=gilets+jaunes&sort=date_asc&date_from=17%2F11%2F2018&date_to=17%2F02%2F2019&type=ARTICLE&page='
	# , 'https://www.lepoint.fr/recherche/index.php?query=gilet+jaune&sort=date_asc&date_from=17%2F11%2F2018&date_to=17%2F02%2F2019&type=ARTICLE&page='
	# ]
# for article in sources:
	# i=0
	# while i<100:
		# i+=1
		# page = urllib.request.urlopen(str(article+str(i)))
		# html = BeautifulSoup(page,"html.parser")
		# for balise in html.find_all('a'):
			# liens = re.findall('.* href="([^ "]+)"', str(balise))
			# if len(liens)==1:
				# lien=liens[0]
				# articles.append(lien)			

# 


# articles=[]
# sources = 'https://www.lemonde.fr/recherche/?keywords=gilets+jaunes&page_num='
# suite= '&operator=and&exclude_keywords=&qt=recherche_texte_titre&author=&period=custom_date&start_day=17&start_month=11&start_year=2018&end_day=17&end_month=02&end_year=2019&sort=asc'

# i = 0
# while i<171:
	# i+=1
	# page = urllib.request.urlopen(str(sources+str(i)+suite))
	# html = BeautifulSoup(page,"html.parser")
	# for balise in html.find_all('a'):
		# liens = re.findall('.* href="([^ "]+)"', str(balise))
		# if len(liens)==1:
			# lien=liens[0]
			# articles.append(lien)
	# print(i)
# with open('URL_LeMonde_GJ.txt', 'w', encoding='UTF-8') as sortieLF:
	# for x in sorted(set(articles)):
		# sortieLF.write(str(x+'\n'))
		
		
# articles=[]
# sources = 'https://www.liberation.fr/recherche/?sort=-publication_date_time&period_start_day=17&period_start_month=11&period_end_year=2019&period_start_year=2018&period_end_day=17&editorial_source=&period=custom&q=gilets+jaunes&period_end_month=2&paper_channel=&page='
# suite= '&ajax'

# i = 0
# while i<93:
	# i+=1
	# page = urllib.request.urlopen(str(sources+str(i)+suite))
	# json = page.read().decode('UTF-8')
	# print(i)
	# articles.append(json)
	
# with open('URL_Libe_GJ.txt', 'w', encoding='UTF-8') as sortieLF:
	# for x in sorted(set(articles)):
		# sortieLF.write(str(x+'\n'))
		
# articles=[]
# sources = 'https://www.humanite.fr/search/gilets%20jaunes?page='
# suite = '&f%5B0%5D=type%3Aarticle'
# i = -1
# while i<83:
	# i+=1
	# page = urllib.request.urlopen(str(sources+str(i)+suite))
	# html = BeautifulSoup(page,"html.parser")
	# for balise in html.find_all('a'):
		# liens = re.findall('.* href="([^ "]+)"', str(balise))
		# if len(liens)==1:
			# lien=liens[0]
			# articles.append(lien)
	
# with open('URL_LHuma_GJ.txt', 'w', encoding='UTF-8') as sortieLF:
	# for x in sorted(set(articles)):
		# sortieLF.write(str(x+'\n'))