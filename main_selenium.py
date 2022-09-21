from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# liste pour page 1
liste_debut = ["20/06/2022", "27/06/2022", "04/07/2022", "08/07/2022", "18/07/2022", "22/07/2022", "29/07/2022", "22/08/2022", "25/08/2022", "29/08/2022", "30/08/2022", "01/09/2022", "07/09/2022", "12/09/2022", "15/09/2022"]
liste_fin = ["24/06/2022", "01/07/2022", "07/07/2022", "13/07/2022", "21/07/2022", "26/07/2022", "16/08/2022", "22/08/2022", "26/08/2022", "29/08/2022", "31/08/2022", "02/09/2022", "09/09/2022", "14/09/2022", "16/09/2022"]
liste_modules_id = ["1416", "1417","1418", "1419", "1420", "1421", "1422", "1423", "1424", "1426", "1427", "1428", "1429", "1431", "1432", "1433"]
liste_formateur_id = ["1450"]

# listes pour page 2
liste_buttons_id = ["#T42_48 > label:nth-child(2)", "#T43_48 > label:nth-child(2)", "#T44_48 > label:nth-child(2)", "#T45_48 > label:nth-child(2)", "#T46_48 > label:nth-child(2)", "#T233_48 > label:nth-child(2)", "#T237_48 > label:nth-child(2)", "#T100_96 > label:nth-child(2)",  "#T103_96 > label:nth-child(2)", "#T227_96 > label:nth-child(2)", "#T101_96 > label:nth-child(2)"]

def remplirpages(i,url,comm):
    try :
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.get(url)
        browser.maximize_window()

        #========================================== PAGE 1 ====================================================
        #browser.find_element(By.ID, "1310Q1308").click()
        #browser.find_element(By.ID, "1309Q1308").click()
        first_name = browser.find_element(By.ID, "Q1312")
        last_name = browser.find_element(By.ID, "Q1311")
        module_suivi = Select(browser.find_element(By.ID, "Q1170"))
        formateur = Select(browser.find_element(By.ID, "Q1171"))
        date_debut = browser.find_element(By.ID, "_Q1167")
        date_fin = browser.find_element(By.ID, "_Q1168")

        module_suivi.select_by_value(str(liste_modules_id[i]))
        formateur.select_by_value("1450")
        date_debut.send_keys(str(liste_debut[i]))
        date_fin.send_keys(str(liste_fin[i]))
        browser.find_element(By.ID, "BtnNext").click()
        #first_name.send_keys("Max")
        #last_name.send_keys("De Quick")

        #========================================= PAGE 2 ======================================================
        #attendre que la checkbox soit clickable
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "Q212"))).click()

        #choisir le taux de satisfaction ("très satisfait")
        taux_satisfaction = Select(browser.find_element(By.ID, "Q212"))
        taux_satisfaction.select_by_value("213")

        #remplir l'espace commentaire
        browser.find_element(By.ID, "Q236").send_keys(str(comm))
        browser.find_element(By.XPATH, value="/html/body/form/table/tbody/tr[3]/td/div/div/div[7]/div[2]/div/div[2]/table/tbody/tr[1]/td/label").click()

        #clicker sur tous les boutons "très bien"
        for x in range(len(liste_buttons_id)):
            browser.find_element(By.CSS_SELECTOR, liste_buttons_id[x]).click()
        
        
        time.sleep(1)
        #cliquer sur le bouton valider
        browser.find_element(By.ID, "BtnNext").click()
        print ("module "+str(i)+" bien rempli !")
        time.sleep(1)
        #closing the browser
        browser.quit()
    except :
        pass
        print("déjà enregistré")


urli = str(input("Quel URL utiliser ?"))
commentaire = str(input("Quel commentaire/appréciation pour les cours de Loup ? "))
for a in range(len(liste_modules_id)):
    remplirpages(a, urli, commentaire)
