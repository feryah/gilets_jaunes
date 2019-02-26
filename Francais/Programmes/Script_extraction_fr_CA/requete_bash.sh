#!/bin/bash

# Extraction des liens pour le français du Canada contenant l'expression "gilets jaunes"

counter=0; while [ $counter -lt 300 ]; do lynx -dump -listonly "https://www.google.fr/search?q=%22gilets+jaunes%22+site:https://www.lesoleil.com/+OR+site:https://www.journaldemontreal.com/+OR+site:https://www.lapresse.ca/+OR+site:https://www.journaldequebec.com/+OR+site:https://www.ledevoir.com/&ei=0wVYXLHjJqOxgwejqYOQBQ&start=$counter&sa=N&ved=0ahUKEwjxmKL34aHgAhWj2OAKHaPUAFIQ8NMDCKEB&biw=1366&bih=624" | egrep -v "OR" | egrep "gilet" | sed -E "s/ [0-9][0-9]\. https:\/\/www\.google\.fr\/(url|search)\?q=(related:)?//g" | sed -E "s/\&.+//g" ; sleep 10s; counter=$((counter+10)); done

# Extraction des liens pour le français du Canada NE contenant PAS l'expression "gilets jaunes"

counter=0; while [ $counter -lt 300 ]; do lynx -dump -listonly "https://www.google.fr/search?q=-%22gilets+jaunes%22+%22france%22+site:https://www.lesoleil.com/actualite/monde+OR+site:https://www.journaldemontreal.com/2018/11+OR+site:https://www.journaldemontreal.com/2018/12+OR+site:https://www.journaldemontreal.com/2019/01+OR+site:https://www.journaldemontreal.com/2019/02+OR+site:https://www.lapresse.ca/international/europe+OR+site:https://www.journaldequebec.com/2018/11+OR+site:https://www.journaldequebec.com/2018/12+OR+site:https://www.journaldequebec.com/2019/01+OR+site:https://www.journaldequebec.com/2019/02+OR+site:https://www.ledevoir.com/monde/europe&ei=qsdzXKiEBYmnUq-SusAL&start=$counter&sa=N&ved=0ahUKEwiogYzL2tbgAhWJkxQKHS-JDrgQ8NMDCH8&biw=1366&bih=624" | egrep -v "OR" | sed -E "s/ [0-9][0-9]\. https:\/\/www\.google\.fr\/(url|search)\?q=(related:)?//g" | egrep -v "google" | sed -E "s/\&.+//g" ; sleep 10s; counter=$((counter+10)); done
