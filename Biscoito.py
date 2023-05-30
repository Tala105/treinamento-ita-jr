from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

i=0
browser = webdriver.Chrome()
browser.get("https://orteil.dashnet.org/cookieclicker/")
browser.implicitly_wait(5)
lingua=browser.find_element(By.ID,"langSelect-PT-BR")
lingua.click()
browser.implicitly_wait(5)

biscoito = browser.find_element(By.ID,"bigCookie")
produtos = browser.find_element(By.ID,"products")
melhorias = browser.find_element(By.ID,"upgrades")
biscoito.click()

while 1:
    qtd=int(str.split(browser.find_element(By.ID,"cookies").text)[0])
    upgrade = melhorias.find_elements(By.ID,"upgrade0")
    print(upgrade)
    
    autos=produtos.find_elements(By.CLASS_NAME,"product.unlocked.enabled")
    browser.implicitly_wait(0)
    for auto in autos:
        if qtd>int(str.split(auto.text)[1]):
            auto.click()
    biscoito.click()