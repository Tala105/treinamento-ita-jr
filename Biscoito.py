from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

i=0
options = Options()

browser = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
browser.get("https://orteil.dashnet.org/cookieclicker/")
browser.implicitly_wait(5)
lingua=browser.find_element(By.ID,"langSelect-PT-BR")
lingua.click()
browser.implicitly_wait(5)

biscoito = browser.find_element(By.ID,"bigCookie")
produtos = browser.find_element(By.ID,"products")
melhorias = browser.find_element(By.ID,"upgrades")
for i in range (0,15):
    biscoito.click()

while 1:
    qtd=int(str.split(browser.find_element(By.ID,"cookies").text.replace(',', ''))[0])
    upgrades=melhorias.find_elements(By.CLASS_NAME,"crate.upgrade.enabled")
    if len(upgrades):
        upgrades[0].click()
    autos=produtos.find_elements(By.CLASS_NAME,"product.unlocked.enabled")
    autos.reverse()
    browser.implicitly_wait(0)
    for auto in autos:
        if qtd>int(str.split(auto.text.replace(',', ''))[1]):
            auto.click()
    biscoito.click()