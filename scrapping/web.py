import requests
from bs4 import BeautifulSoup
response=requests.get('https://www.cricbuzz.com/cricket-team/pakistan/3/stats')
html=response.content
soup = BeautifulSoup(html,'html.parser')
table=soup.find("tbody")
print(table)
#f#  print(row.td)
 #        
