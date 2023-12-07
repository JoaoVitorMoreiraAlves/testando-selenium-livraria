from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get('https://books.toscrape.com/')

titleElements = navegador.find_elements(By.TAG_NAME, 'a')[54:94:2]

titleList = [title.get_attribute('title') for title in titleElements]

stockList = []
for title in titleElements:
    title.click()

    qntStock = int(navegador.find_element(By.CLASS_NAME, 'instock').text.replace('In stock (', '').replace(' available)', ''))
    
    stockList.append(qntStock)

    navegador.back()


dictDF = {'title': titleList,
          'stock': stockList}

print(pd.DataFrame(dictDF))

input('Digite Enter para fechar!')