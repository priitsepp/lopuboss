import requests
import os
import re
from bs4 import BeautifulSoup
page = requests.get('https://www.hockey-reference.com/leagues/NHL_2020_games.html')
soup = BeautifulSoup(page.content, 'html.parser')
result = soup.find("div", class_="overthrow table_container")
tiimideList =["Carolina Hurricanes", "Columbus Blue Jackets", "New Jersey Devils", "New York Islanders", "New York Rangers", "Philadelphia Flyers", "Pittsburgh Penguins", "Washington Capitals", "Boston Bruins", "Buffalo Sabres", "Detroit Red Wings", "Florida Panthers", "Montreal Canadiens", "Ottawa Senators", "Tampa Bay Lightning", "Toronto Maple Leafs", "Chicago Blackhawks", "Colorado Avalanche", "Dallas Stars", "Minnesota Wild", "Nashville Predators", "St. Louis Blues", "Winnipeg Jets", "Anaheim Ducks", "Arizona Coyotes", "Calgary Flames", "Edmonton Oilers", "Los Angeles Kings", "San Jose Sharks", "Vancouver Canucks", "Vegas Golden Knights"]

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
for i in range(0, len(tuhiList)):
   tuhiList[i] = tuhiList[i][10:]
sygavusKaks = 0
skoorid = []
otList = []
htList = []
atList = []
skooriKombod = ""
for x in tuhiList:
    for y in x:
        if y.isdigit():
            sygavusKaks = sygavusKaks+1
            if sygavusKaks==1:
                skooriKombod = y
            if sygavusKaks==2:
                skooriKombod = skooriKombod+"-"+y
                skoorid.append(skooriKombod)
    sygavusKaks=0



for x in tuhiList:
    if "OT" in x:
        otList.append("OT")
    elif "SO" in x:
        otList.append("SO")
    else:
        otList.append("EI")



def remove(tuhiList): 
    pattern = '[0-9]'
    tuhiList = [re.sub(pattern, '', i) for i in tuhiList] 
    return tuhiList

for y in remove(tuhiList):
    for x in tiimideList:
        if x in y[0:22]:
            atList.append(x)
        else:
            if x in y:
                htList.append(x)


for x in range(len(atList)-len(skoorid)):
    skoorid.append("Mängimata")


loplikList = []

loplikList.append(htList[0])
loplikList.append(atList[0])
loplikList.append(skoorid[0])
loplikList.append(otList[0])

for x in range(len(htList)):
    loplikList.append(htList[x])
    loplikList.append(atList[x])
    loplikList.append(skoorid[x])
    loplikList.append(otList[x])
for x in range(len(loplikList)):
    print(loplikList[x])