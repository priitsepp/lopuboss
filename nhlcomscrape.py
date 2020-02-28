import requests
import os
from bs4 import BeautifulSoup
page = requests.get('https://www.hockey-reference.com/leagues/NHL_2020_games.html')
soup = BeautifulSoup(page.content, 'html.parser')
result = soup.find("div", class_="overthrow table_container")

f = open("results.txt", "w")
f.write(result.text)
f.close
f = open("results.txt", "r")
tuhiList = []
sygavus = 0
for x in f:
    sygavus = sygavus + 1
    if sygavus >= 18:
        tuhiList.append(x.strip('\n'))
print(tuhiList)