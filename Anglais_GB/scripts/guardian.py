from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

urls = []
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
    time.sleep(3)

    # envoyer recherche
    recherche.send_keys(Keys.ENTER)
    time.sleep(1)

    # trouver liens pages suivantes
    pages = driver.find_elements_by_css_selector(".gsc-cursor-page")
    for page in pages:
        urls = driver.find_elements_by_class_name("gs-title")
        for url in urls:
            print(url.get_attribute('href'))

        page.click()
        time.sleep(1)


#
finally:
     driver.quit()
