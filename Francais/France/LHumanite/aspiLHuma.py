import urllib.request
import re
from bs4 import BeautifulSoup
# _________________ L'HUMANITE _________________
# l'huma -> <div class="group-ft-header-node-article field-group-div">
url_pb = []
contenu_pb = []
			
fichier = 'URL_LHuma_GJ.txt'

sortie = open(str('GJ'+fichier[4:-7]+'URL'), 'w', encoding='UTF-8')
pointeur = open(fichier, 'r')
liens = [ligne.strip() for ligne in pointeur]

#On supprime les doublons
liens = sorted(set(liens))
print(len(liens))

#On vérifie que les liens renvoient un code 200
for url in liens:
	print(url)
	try:
		page = urllib.request.urlopen(url)
		html = BeautifulSoup(page,"html.parser")
		for body in html.find_all('div', class_="group-ft-header-node-article field-group-div"):
			texte = str(body.get_text())
			
			#On récupère la date
			date = body.find_all("span", class_="date-display-single")[0].get_text()
			#On la met au format voulu
			jours = ['Lundi, ', 'Mardi, ', 'Mercredi, ', 'Jeudi, ', 'Vendredi, ', 'Samedi, ', 'Dimanche, ']
			mois = ['Janvier, ', 'Février, ', 'Mars, ', 'Avril, ', 'Mai, ', 'Juin, ', 'Juillet, ', 'Août, ', 'Septembre, ', 'Octobre, ', 'Novembre, ', 'Décembre, ']
			for jour in jours:
				date = re.sub(jour, '', date)
			for jour in mois:
				date = re.sub(jour, str(str(mois.index(jour)+1)+'-'), date)
			date = re.sub(' ', '-', date)
				
			#On récupère le titre 
			titre = body.find_all("h1")[0].get_text()
			#Et le texte de l'article
			paragraphes = body.find_all("p")
			
			okay = False
			#On vérifie que l'article parle bien du thème
			if "gilets jaunes" in texte or "gilet jaune" in texte:
				#On vérifie qu'il provient de la bonne période 17-11-2018 17-02-2019
				decomp = date.split('-')
				if decomp[2] == '2018' and decomp[1] in ['11', '12']: 
					if decomp[1] == '12':
						okay = True
					elif decomp[1] == '11' and int(decomp[0])>16:
						okay = True
				elif decomp[2] == '2019' and decomp[1] in ['1', '2']:
					if decomp[1] == '1':
						okay = True
					elif decomp[1] == '2' and int(decomp[0])<18:
						okay = True
				else:
					contenu_pb.append(url)
				if okay == True : 
					sortie.write( str('<ARTICLE url="'+url+'" date="'+date+'">\n') )
					sortie.write( str(titre+'\n') )
					for p in paragraphes:
						sortie.write( str(p.get_text()+'\n') )
					sortie.write( str('\n</ARTICLE>\n') )
			else : 
				contenu_pb.append(url)
	except:
		url_pb.append(url)


print(url_pb)
print(contenu_pb)