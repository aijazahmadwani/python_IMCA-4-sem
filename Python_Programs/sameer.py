import requests
from bs4 import BeautifulSoup
import sqlite3
database_name="database.db"
connection=sqlite3.connect(database_name)
connection.execute("create table newzealand_team(name text not null)")
html=requests.get("https://www.cricbuzz.com/cricket-team/new-zealand/13/players")
soup=html.content
page=BeautifulSoup(soup)
players=page.select(".cb-font-16.text-hvr-underline")
print(players)
for player in players.text:
     d=player.text
     connection.execute("insert into newzealand_team (name)values(?)",(d,))
     connection.commit()
#######printing data
#data=connection.execute("select * from newzealand_team")
#for d in data:
#     print(d)
#connection.close()
#print("successfully inserted data")
