from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

# temps de chargement
driver.implicitly_wait(10)

try:

    driver.get("https://www.theguardian.com/uk?INTCMP=CE_UK") # garantir version britannique

    # trouver champ de recherche
    depart = driver.find_element_by_css_selector("a.popup__toggle")
    depart.click()

    # trouver champ de saisie
    recherche = driver.find_element_by_id("gsc-i-id1")
    recherche.click()
    recherche.send_keys("gilets jaunes")
    time.sleep(1)

    #envoyer recherche
    recherche.send_keys(Keys.ENTER);
    time.sleep(10)

#     saisie_arrivee.send_keys("New York City")
#
#     # # selection du pays d'arrivee
#     # usa = driver.find_element_by_css_selector(".fsapp-option-city-name")
#     # usa.click()
#     # time.sleep(1)
#
#     # lancer la recherche
#     recherche = driver.find_element_by_css_selector(".gws-flights-form__search-button")
#     recherche.click()
#     time.sleep(5)
#
#     # afficher les resultats
#     resultats = driver.find_elements_by_xpath("//div[contains(@class, 'gws-flights-results__collapsed-itinerary gws-flights-results__itinerary')]")
#     for resultat in resultats:
#         print("##############")
#         print(resultat.text)
#
#
finally:
     driver.quit()

