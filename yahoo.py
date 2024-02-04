from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

lista = []

options = Options()
options.add_argument("--headless")

browser = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe",options = options)
action=ActionChains(browser)
browser.get('https://br.financas.yahoo.com/screener/predefined/most_shorted_stocks')

WebDriverWait(browser, 10).until(EC.frame_to_be_available_and_switch_to_it(browser.find_element(By.ID, "guce-inline-consent-iframe")))
WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))).click()
sleep(0.3)

browser.switch_to.default_content()
edit = browser.find_element(By.XPATH, '//*[@id="screener-criteria"]/div[2]/div[1]/div/button[1]')
edit.click()
sleep(0.5)

xbutton = browser.find_elements(By.CLASS_NAME, 'removeFilter')[1]
action.move_to_element(xbutton).perform()
sleep(0.5)
xbutton.click()
sleep(1)
xbutton = browser.find_elements(By.CLASS_NAME, 'removeFilter')[1]
xbutton.click()
sleep(1)
save = browser.find_element(By.XPATH, '//*[@id="screener-criteria"]/div[2]/div[1]/div[3]/button[1]')
save.click()
sleep(0.5)

linesshown=browser.find_element(By.XPATH, '//*[@id="scr-res-table"]/div[2]/span/div')
action.move_to_element(linesshown).perform()
linesshown.click()
line100 = browser.find_element(By.XPATH, '//*[@id="scr-res-table"]/div[2]/span/div[2]/div[3]')
line100.click()
sleep(1)

site = browser.page_source
codigo = BeautifulSoup(site, 'html.parser')

tabela = codigo.find('table', attrs={'class' : 'W(100%)'})
linhas = tabela.findAll('tr')
for linha in linhas:
    nome = linha.find('td', attrs={'aria-label' : 'Nome'})
    sigla = linha.find('td', attrs={'aria-label' : 'Símbolo'})
    porcentagem = linha.find('td', attrs={'aria-label' : '% Alteração'})
    nominal = linha.find('td', attrs={'aria-label' : 'Alterar'})
    volume = linha.find('td', attrs={'aria-label' : 'Volume'})
    valor = linha.find('td', attrs={'aria-label' : 'Capitalização de mercado'})
    if(nome):
        lista.append([nome.text,sigla.text,porcentagem.text, nominal.text,volume.text,valor.text])

stocks = pd.DataFrame(lista, columns=['Nome', 'Sigla', 'Variação em %', 'Variação Nominal', 'Volume', 'Valor de mercado'])
stocks.to_excel('stocks.xlsx')
print("1")