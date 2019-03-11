import urllib.request
import re
from bs4 import BeautifulSoup

##_________________ LE FIGARO_________________
contenu_pb = []
			
fichier = 'URL_LeFig_GJ.txt'

sortie = open(str('GJ'+fichier[4:-7]+'URL'), 'w', encoding='UTF-8')
pointeur = open(fichier, 'r')
liens = [ligne.strip() for ligne in pointeur]

#On supprime les doublons
liens = sorted(set(liens))
print(len(liens))

#On vérifie que les liens renvoient un code 200
for url in liens:
	#On extrait la date de l'URL.
	date = '-'.join(re.findall('/(20\d\d)/(\d+)/(\d+)/', url)[0])
	#On vérifie qu'elle correspond à la période étudiée
	if date<'2019-02-18' and date>'2018-11-16':
		#On parse la page
		page = urllib.request.urlopen(url)
		html = BeautifulSoup(page,"html.parser")
		for body in html.find_all("article"):
			#On vérifie la présence du terme recherché:
			if 'gilets jaunes' in body.get_text():
				sortie.write( str('<ARTICLE url="'+url+'" date="'+date+'">\n') )
				#Titre est stocké dans h1 
				sortie.write( str( str(body.find_all("h1")[0].get_text())+'\n') )
				#Texte dans les p 
				for p in body.find_all("p"):
					sortie.write( str(p.get_text()+'\n') )
				sortie.write( str('\n</ARTICLE>\n') )
			else:
				contenu_pb.append(url)

print(contenu_pb)