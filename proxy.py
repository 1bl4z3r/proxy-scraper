#install requests, bs4(beautifulsoup)
import requests
from bs4 import BeautifulSoup
domain = "https://free-proxy-list.net/"
r = requests.get(domain)
soup = BeautifulSoup(r.content,'html.parser')
table = soup.find('table',{"id" : proxylisttable})
for row in table.find_all('tr'):
  columns = row.find_all('td')
  try:
    print "%s:%s\t%-20s\t%-20s" %(columns[0].get_text(),columns[1].get_text(),columns[3].get_text(),columns[4].get_text())
  except:
    pass
