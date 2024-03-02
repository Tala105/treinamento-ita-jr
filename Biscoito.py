#importando as bibli
import requests
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import json
from selenium.webdriver.common.by import By

# tive que ser bronco aqui
urls = ['https://sec.sbfisica.org.br/olimpiadas/obf2019/forms/resultadofinalobf.asp?serie=8', 'https://sec.sbfisica.org.br/olimpiadas/obf2019/forms/resultadofinalobf.asp?serie=9', 'https://sec.sbfisica.org.br/olimpiadas/obf2019/forms/resultadofinalobf.asp?serie=1', 'https://sec.sbfisica.org.br/olimpiadas/obf2019/forms/resultadofinalobf.asp?serie=2', 'https://sec.sbfisica.org.br/olimpiadas/obf2019/forms/resultadofinalobf.asp?serie=3']
"""urls = []
    str = 'https://sec.sbfisica.org.br/olimpiadas/obf2019/forms/resultadofinalobf.asp?serie='
    series = ['8', '9', '1', '2', '3']
    for serie in series:
        urls.append(str + serie)
        
        ou entra faz o webscraping, volta pro """
ind = 7
for url in urls:

    resposta = requests.get(url)

    content = resposta.content

    site = BeautifulSoup(content, 'html.parser')

    tabela = site.find('table', attrs={'width': '760'})
    alunos_info = []
    alunos = tabela.findAll('tr', class_=['trl1', 'trl2'])
    
    for aluno in alunos:
        info = aluno.findAll('td')
        if(info):
            nome = info[0].get_text()
            cidade = info[1].get_text()
            estado = info[2].get_text()
            medalha = info[3].find('img')['title']
            alunos_info.append([nome, cidade, estado, medalha])
  
    tabela_alunos = pd.DataFrame(alunos_info, columns=['Nome', 'Cidade', 'Estado', 'Medalha'])
    ind += 1
    # salvando em excel, nÃ£o salvando com a coluna indicial
    tabela_alunos.to_excel(str(ind) + 'ano_2019.xlsx', index=False)



