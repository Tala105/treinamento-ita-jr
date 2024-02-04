from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from time import sleep
import re
import pandas as pd

i=0
options = Options()
options.add_argument("--headless")
lista = []

browser = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe", options = options)
browser.get("https://drive.google.com/drive/folders/1rY6IiuZY18UXLVe66mo7Cu99vi8KXoAh?usp=drive_link")
browser.implicitly_wait(5)
shows = browser.find_elements(By.CLASS_NAME, "uXB7xe")

for show in shows:
    nomes = show.text
    nomes2 = re.split(' e |\+|\.', nomes)
    print(nomes2)
    for nome in nomes2:
        nome = nome.strip()
        nome = nome.lower()
        nome = nome.capitalize()
        if(nome.lower() != "mov" and nome.lower() != "mp4"):
            lista.append([nome])

stocks = pd.DataFrame(lista, columns=['Nome'])
stocks = stocks.sort_values('Nome')
stocks.to_excel('showdobixo.xlsx')