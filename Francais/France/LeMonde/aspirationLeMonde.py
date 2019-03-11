import urllib.request
import re
from bs4 import BeautifulSoup

##_________________ LE FIGARO_________________
url_pb = []
contenu_pb = []
			
fichier = 'URL_LeMonde_GJ.txt'

sortie = open(str('GJ'+fichier[4:-7]+'URL'), 'w', encoding='UTF-8')
pointeur = open(fichier, 'r')
liens = [ligne.strip() for ligne in pointeur]

#On supprime les doublons
liens = sorted(set(liens))
print(len(liens))

#On vérifie que les liens renvoient un code 200
for url in liens:
	#On extrait la date de l'URL.
	date = re.findall('/(20\d\d)/(\d+)/(\d+)/', url)[0]
	date = '-'.join(date)
	if date<'2019-02-18' and date>'2018-11-16':
		try : 
			#On parse la page
			page = urllib.request.urlopen(url)
			html = BeautifulSoup(page,"html.parser")
		except:
			url_pb.append(url)
			
		else :
			if len(html.find_all("section", class_="paywall"))==0:
				for body in html.find_all("article"):
					if 'gilets jaunes' in body.get_text() or 'Gilets jaunes' in body.get_text():
						sortie.write( str('<ARTICLE url="'+url+'" date="'+date+'">\n') )
						try:
							sortie.write( str( str(body.find_all("div", class_="article__heading")[0].get_text())+'\n') )
						except:
							sortie.write( str( str(body.find_all("h1")[0].get_text())+'\n') )
						for p in body.find_all("p"):
							sortie.write( str( str(p.get_text())+'\n') )
						sortie.write( str('\n</ARTICLE>\n') )
					else:
						contenu_pb.append(url)
	else:
		contenu_pb.append(url)
		
	
print(url_pb)
print(contenu_pb)