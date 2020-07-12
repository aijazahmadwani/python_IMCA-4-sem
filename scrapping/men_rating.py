import sqlite3
import requests
from bs4 import BeautifulSoup
html=requests.get("https://www.cricbuzz.com/cricket-stats/icc-rankings/men/batting")
page=html.content
soup=BeautifulSoup(page)
data=soup.select(".cb-col.cb-col-100.cb-font-14.cb-lst-itm.text-center")
for item in data[0].text:
    print(item)  

#print(s)
