import requests
import sqlite3
from bs4 import BeautifulSoup
# html=requests.get("https://www.cricbuzz.com/cricket-team/pakistan/3/stats")
# page=html.content
# soup=BeautifulSoup(page)
# #print(soup.prettify())
# table=soup.find('tbody')
# list_of_rows=[]
connection=sqlite3.connect('pakistamteam.db') #table name ="TEAM"
print("connection established")
# connection.execute('''CREATE TABLE TEAM (PLAYER TEXT,
#                    MATCHES INT,
#                    INS INT,
#                    RUNS INT,
#                    AVG INT,
#                    SR INT,
#                    FOURS INT,
#                    SIXS INT
#                    );''')
# print("team table created")
# for row in table.findAll('tr'):
#     list_of_cells=[]
#     for cell in row.findAll('td'):
#          list_of_cells.append(cell.text)
#     connection.execute("INSERT INTO TEAM VALUES(?,?,?,?,?,?,?,?)",list_of_cells) 
#     connection.commit()
#print (list_of_rows)
#name=list_of_cells[0]
#print(name)

#connection.execute("DELETE FRoM TEAM WHERE PLAYER='Taufeeq Umar'")
#connection.commit()
data=connection.execute("SELECT * FROM TEAM")
for row in data:
    print(row)
connection.close()


