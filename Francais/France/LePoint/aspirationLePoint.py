import urllib.request
import re
from bs4 import BeautifulSoup

##_________________ LE FIGARO_________________
url_pb = []
contenu_pb = []
			
fichier = 'URL_LePoint_GJ.txt'

sortie = open(str('GJ'+fichier[4:-7]+'URL'), 'w', encoding='UTF-8')
pointeur = open(fichier, 'r')
liens = [ligne.strip() for ligne in pointeur]

#On supprime les doublons
liens = sorted(set(liens))
print(len(liens))

#On vérifie que les liens renvoient un code 200
for url in liens:
	#On extrait la date de l'URL.
	date = re.findall('-(\d+)-(\d+)-(20\d\d)-', url)[0]
	date = str(date[2]+'-'+date[1]+'-'+date[0])
	if date<'2019-02-18' and date>'2018-11-16':
		try : 
			#On parse la page
			page = urllib.request.urlopen(url)
			html = BeautifulSoup(page,"html.parser")
		except:
			url_pb.append(url)
			
		else :
			for b in html.find_all("div", class_="content"):
				if 'gilets jaunes' in b.get_text() or 'Gilets jaunes' in b.get_text():
					#On vérifie la présence du terme recherché:
					for body in b.find_all("article"):
						sortie.write( str('<ARTICLE url="'+url+'" date="'+date+'">\n') )
						try:
							sortie.write( str( str(body.find_all("h1")[0].get_text())+'\n') )
						except:
							pass
						try : 
							sortie.write( str( str(body.find_all("h2")[0].get_text())+'\n') )
						except : 
							pass
						for p in body.find_all("p"):
							sortie.write( str(p.get_text()+'\n') )
						sortie.write( str('\n</ARTICLE>\n') )
				else:
					contenu_pb.append(url)
	else:
		contenu_pb.append(url)
		
	
print(url_pb)
print(contenu_pb)