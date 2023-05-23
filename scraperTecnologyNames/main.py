import requests
from bs4 import BeautifulSoup

url = "https://www.opservices.com.br/dicionario-da-ti/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
tecnologyNames = (soup.find_all("section", class_="blog-content-single"))[0].find_all("h3")

with open('nomesTecnologia.txt', 'w', encoding = "utf-8") as file:
    for name in tecnologyNames:
        file.write((name.get_text()).replace('e','\n').replace('ou','\n').replace('/','\n').replace('(','\n').replace(')','').replace(' ',''))
        file.write('\n')
        #print((name.get_text()).replace('e','\n').replace('ou','\n').replace('/','\n').replace('(','\n').replace(')',).replace(' ',''))

# test = 'ansi'
# with open('nomesTecnologia.txt', 'r', encoding = "utf-8") as file:
#     for name in file:
#         if name.rstrip() == test.upper():
#             print("true")

