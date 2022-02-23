#required module

import requests
from bs4 import BeautifulSoup

#LINK = # https://myanimelist.net/topanime.php?type=bypopularity
url = requests.get("https://myanimelist.net/topanime.php?type=bypopularity").text
soup = BeautifulSoup(url, 'html.parser')



    
#all the needed tags

#name = hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3 h3
#info = information di-ib mt4 div
#rating = text on score-label score-8 span


# process to convert html to list data 

l= [[],[],[],[],[]]

for i in soup.find_all('h3', class_="hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3"):
    l[0].append(i.text)
for  i in soup.findAll('span', class_="text on score-label score-8"):
    l[1].append(i.text)
    
    

l2= [[],[]]

for  i in soup.findAll('div', class_="information di-ib mt4"):
    
    l2[0].append(i.text.split('\n'))
    
for i in l2[0]:
    
    l[2].append(i[1])
    l[3].append(i[2])
    l[4].append(i[3])

print(l)

