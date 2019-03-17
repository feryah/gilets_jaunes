
# coding: utf-8

# In[8]:


from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# In[10]:


lurl=set()
driver = webdriver.Firefox()
    # attendre 10s au maximum avant de récupérer les éléments
driver.implicitly_wait(10)
driver.get("https://www.theguardian.com/uk")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div[3]/button/span[2]").click()
depart = driver.find_element_by_xpath("/html/body/div[1]/header/nav/div[2]/a")
depart.click()
time.sleep(3)# trouver le champ de saisie de l'arrivee
saisie_arrivee = driver.find_element_by_xpath('//*[@id="gsc-i-id1"]')
time.sleep(3)
saisie_arrivee.send_keys("yellow vest")
time.sleep(3)
saisie_arrivee.send_keys(Keys.RETURN)
#driver.find_element_by_xpath("/html/body/div[4]/form/div/button").click()
time.sleep(3)
for e in range(10):
    driver.find_element_by_xpath("/html/body/div[1]/header/nav/div[3]/div/div[2]/div/div/div/div/div[5]/div[2]/div/div/div[2]/div[5]/div/div["+str(e+1)+"]").click()
    time.sleep(3)
    resultats = driver.find_elements_by_css_selector(".gs-title")
    for art in resultats:
        if art.get_attribute('href'):
            lurl.add(art.get_attribute('href'))
time.sleep(1)    
driver.quit()


# In[11]:


with open("Guardian.xml", "w", encoding="utf-8") as g:
    g.write('<?xml version="1.0"?>\n<corpus>\n')
    for lien in lurl:
        driver = webdriver.Firefox()
        driver.implicitly_wait(1)
        driver.get(lien)
        time.sleep(1)
        title = driver.find_element_by_xpath("//h1")
        labels = driver.find_elements_by_xpath("//span[contains(@class, 'label__link-wrapper')]")
        paragraphes = driver.find_elements_by_xpath("//div[contains(@class, 'content__article-body')]/p")
        g.write('''<doc source="Guardian" link=">'''+lien+'''" labels="'''+", ".join([e.text for e in labels])+'''" title="'''+title.text+'''" >\n'''+"\n\n".join([p.text for p in paragraphes]).replace("&","&amp;")+"\n</doc>\n")
        driver.quit()
    g.write('</corpus>')

